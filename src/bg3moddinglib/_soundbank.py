from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, lower_bound_by_bg3_attribute, set_bg3_attribute
from ._files import game_file

from typing import Iterable

class soundbank_asset:
    __wem_path: str
    __ffxanim_path: str
    __gr2_path: str

    def __init__(self, wem_path: str, ffxanim_path: str, gr2_path: str) -> None:
        self.__wem_path = wem_path
        self.__ffxanim_path = ffxanim_path
        self.__gr2_path = gr2_path

    @property
    def wem_path(self) -> str:
        return self.__wem_path
    
    @property
    def ffxanim_path(self) -> str:
        return self.__ffxanim_path

    @property
    def gr2_path(self) -> str:
        return self.__gr2_path


class soundbank_object:
    __file: game_file
    __index: dict[str, str]

    def __init__(self, gamefile: game_file) -> None:
        self.__file = gamefile
        self.__index = dict[str, str]()

    @property
    def file(self) -> game_file:
        return self.__file

    def add_voice_metadata(self, text_handle: str, duration: float, audio_file_name: str) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        if parent_node is None:
            raise ValueError(f"cannot parse {self.__file.relative_file_path} as a soundbank file")
        nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
        index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
        new_node = et.fromstring(f"""\n<node id="VoiceTextMetaData">
            <attribute id="MapKey" type="FixedString" value="{text_handle}" />
            <children>
                <node id="MapValue">
                    <attribute id="Codec" type="FixedString" value="VORBIS" />
                    <attribute id="Length" type="float" value="{duration}" />
                    <attribute id="Priority" type="FixedString" value="P1_StoryDialog" />
                    <attribute id="Source" type="FixedString" value="{audio_file_name}" />
                </node>
            </children>
        </node>\n""")
        parent_node.insert(index, new_node)

    def delete_voice_metadata(self, text_handle: str) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
        index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
        if get_required_bg3_attribute(nodes[index], "MapKey") == text_handle:
            parent_node.remove(nodes[index])
        else:
            raise KeyError(f"node {text_handle} doesn't exist in soundbank {self.__file.relative_file_path}")

    def update_voice_metadata(self, text_handle: str, duration: float, audio_file_name: str) -> None:
        root_node = self.__file.root_node
        parent_node = root_node.find('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children')
        nodes = parent_node.findall('./node[@id="VoiceTextMetaData"]')
        index = lower_bound_by_bg3_attribute(nodes, "MapKey", text_handle)
        node = nodes[index]
        if get_required_bg3_attribute(node, "MapKey") == text_handle:
            node = node.find('./children/node[@id="MapValue"]')
            if node is None:
                raise ValueError(f"bad node {text_handle} in soundbank {self.__file.relative_file_path}, update failed")
            set_bg3_attribute(node, "Length", str(duration))
            set_bg3_attribute(node, "Source", audio_file_name)
        else:
            raise KeyError(f"node {text_handle} doesn't exist in soundbank {self.__file.relative_file_path}")

    def get_wem_file_name(self, text_handle: str) -> str:
        if len(self.__index) == 0:
            self.__build_index()
        if text_handle in self.__index:
            return self.__index[text_handle]
        raise KeyError(f'text not found for the given handle {text_handle}')

    def unpack_sound_assets(self, text_handle: str) -> soundbank_asset:
        wem_file_name = self.get_wem_file_name(text_handle)
        base_file_name = wem_file_name.split('.')[0]
        gf_wem = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Soundbanks/' + wem_file_name,
            pak_name='Localization/Voice')
        gf_ffxanim = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Animation/' + f'FX_{base_file_name}.ffxanim',
            pak_name='Localization/English_Animations')
        gf_gr2 = game_file(
            self.__file.tool,
            'Mods/Gustav/Localization/English/Animation/' + f'MC_{base_file_name}.gr2',
            pak_name='Localization/English_Animations')
        return soundbank_asset(gf_wem.unpacked_file_path, gf_ffxanim.unpacked_file_path, gf_gr2.unpacked_file_path)

    def get_all_text_handles(self) -> tuple[str]:
        if len(self.__index) == 0:
            self.__build_index()
        return tuple(self.__index.keys())

    def __build_index(self) -> None:
        nodes = self.__file.root_node.findall('./region[@id="VoiceMetaData"]/node[@id="VoiceMetaData"]/children/node[@id="VoiceSpeakerMetaData"]/children/node[@id="MapValue"]/children/node[@id="VoiceTextMetaData"]')
        if len(nodes) == 0:
            raise RuntimeError(f'not a soundbank or an empty soundbank: {self.__file.relative_file_path}')
        for node in nodes:
            handle = get_required_bg3_attribute(node, 'MapKey')
            value = node.find('./children/node[@id="MapValue"]')
            if value is None:
                raise ValueError(f'malformed entry with handle {handle}')
            source = get_required_bg3_attribute(value, 'Source')
            self.__index[handle] = source
        
