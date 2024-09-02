from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import (
    get_node_attribute,
    get_node_children,
    read_xml_object_map,
    translate_path
)

class bg3_game_object_soundbank:
    __filename: str
    __xml: et.ElementTree
    __speaker_uuid: str
    __speaker_root_node: et.Element
    __voice_text_metadata: dict[str, et.Element]

    @property
    def xml(self) -> et.ElementTree:
        return self.__xml

    @property
    def speaker_uuid(self) -> str:
        return self.__speaker_uuid

    def __init__(self, lsx_file_path: str) -> None:
        if not lsx_file_path.endswith(".lsx"):
            raise ValueError(f"Unexpected file: {lsx_file_path}")
        if not os.path.isfile(lsx_file_path):
            raise FileNotFoundError(f"File '{lsx_file_path}' doesn't exist")
        self.__filename = lsx_file_path
        self.__xml = et.parse(lsx_file_path)
        self.__voice_text_metadata = dict[str, et.Element]()
        self.__init_soundbank()

    def get_voice_metadata(self, voice_id: str) -> et.Element:
        if voice_id not in self.__voice_text_metadata:
            raise KeyError(f"Voice metadata '{voice_id}' doesn't exist in this soundbank.")
        return self.__voice_text_metadata[voice_id]

    def add_voice_metadata(self, node: et.Element) -> None:
        if node.get('id') != 'VoiceTextMetaData':
            raise ValueError("Expected a 'VoiceTextMetaData' element.")
        key = get_node_attribute(node, 'MapKey')
        if not isinstance(key, str):
            raise ValueError("A 'VoiceTextMetaData' element doesn't have a MapKey.")
        self.__voice_text_metadata[key] = node
        self.__speaker_root_node.append(node)

    def save_to(self, dest_file_path: str) -> str:
        dest_file_path = translate_path(dest_file_path)
        dir_path = os.path.dirname(dest_file_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        self.__xml.write(dest_file_path, encoding="utf-8", xml_declaration=True)
        return dest_file_path

    def __init_soundbank(self) -> None:
        root = self.__xml.getroot()
        speaker_nodes = root.findall("region[@id='VoiceMetaData']/node[@id='VoiceMetaData']/children/node[@id='VoiceSpeakerMetaData']")
        if len(speaker_nodes) != 1:
            raise ValueError(f"Expected 1 speaker in the soundbank '{self.__filename}', got {len(speaker_nodes)}")
        self.__speaker_uuid = get_node_attribute(speaker_nodes[0], "MapKey")
        self.__speaker_root_node = speaker_nodes[0].find('children/node/children')
        if not isinstance(self.__speaker_root_node, et.Element):
            raise ValueError(f"Expected an XML element as a speaker root node in the soundbank '{self.__filename}'")
        for node in self.__speaker_root_node:
            key = get_node_attribute(node, "MapKey")
            self.__voice_text_metadata[key] = node
