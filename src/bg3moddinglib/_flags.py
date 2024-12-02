from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import get_required_bg3_attribute, new_random_uuid
from ._files import game_file, game_files
from ._tool import bg3_modding_tool

from typing import Iterable

LOCAL_FLAG = 1
OBJECT_FLAG = 4
GLOBAL_FLAG = 5

class flag_object:
    __file: game_file
    __uuid: str
    __name: str
    __description: str
    __usage: int

    def __init__(
            self,
            f: game_files | game_file | None,
            name: str | None = None,
            usage: int | None = None,
            flag_uuid: str | None = None,
            description: str | None = None
    ) -> None:
        if flag_uuid is None:
            flag_uuid = new_random_uuid()
        if description is None:
            description = name
        if isinstance(f, game_files):
            self.__uuid = flag_uuid
            self.__name = name
            self.__description = description
            self.__usage = usage
            self.__file = f.add_new_file(f'Public/GustavDev/Flags/{flag_uuid}.lsf')
            root_node = self.__file.root_node
            root_node.append(et.fromstring('<version major="4" minor="3" revision="0" build="0" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
            root_node.append(et.fromstring('<region id="Flags"><node id="Flags">' +
                f'<attribute id="UUID" type="guid" value="{flag_uuid}" />'
                f'<attribute id="Name" type="FixedString" value="{name}" />'
                f'<attribute id="Description" type="LSString" value="{description}" />'
                f'<attribute id="Usage" type="uint8" value="{usage}" /></node></region>'))
        elif isinstance(f, game_file):
            self.__file = f
            root_node = f.xml.getroot()
            if isinstance(root_node, et.Element):
                node = root_node.find('./region[@id="Flags"]/node[@id="Flags"]')
                if node is None:
                    raise ValueError(f"bad flag {flag_uuid}")
                self.__uuid = get_required_bg3_attribute(node, 'UUID')
                self.__name = get_required_bg3_attribute(node, 'Name')
                self.__description = get_required_bg3_attribute(node, 'Description')
                self.__usage = int(get_required_bg3_attribute(node, 'Usage'))
        else:
            self.__file = None
            if flag_uuid is None or name is None or description is None or usage is None:
                raise ValueError('expected all flag oarameters')
            self.__uuid = flag_uuid
            self.__name = name
            self.__description = description
            self.__usage = usage

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def name(self) -> str:
        return self.__name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def usage(self) -> str:
        return self.__usage

class flag:
    __uuid: str
    __value: bool
    __speaker_index: int | None

    def __init__(self, flag_uuid: str, value: bool, speaker_index: int | None = None) -> None:
        self.__uuid = flag_uuid
        self.__value = value
        self.__speaker_index = speaker_index

    @property
    def uuid(self) -> str:
        return self.__uuid

    @property
    def value(self) -> str:
        return self.__value

    @property
    def speaker_index(self) -> str:
        return self.__speaker_index

    def to_xml(self) -> et.Element:
        if self.__speaker_index is not None:
            return et.fromstring('<node id="flag" key="UUID">' +
                f'<attribute id="UUID" type="FixedString" value="{self.__uuid}" />' +
                f'<attribute id="value" type="bool" value="{self.__value}" />' +
                f'<attribute id="paramval" type="int32" value="{self.__speaker_index}" /></node>')
        else:
            return et.fromstring('<node id="flag" key="UUID">' +
                f'<attribute id="UUID" type="FixedString" value="{self.__uuid}" />' +
                f'<attribute id="value" type="bool" value="{self.__value}" /></node>')


class flag_group:
    OBJECT = 'Object'
    GLOBAL = 'Global'
    DIALOG = 'Dialog'
    LOCAL = 'Local'

    __scope: str
    __flags: tuple[flag]

    def __init__(self, scope: str, flags: Iterable[flag]) -> None:
        self.__scope = scope
        self.__flags = tuple[flag](flags)

    def scope(self) -> str:
        return self.__scope

    def flags(self) -> tuple[flag]:
        return self.__flags

    def to_xml(self) -> et.Element:
        result = et.fromstring(f'<node id="flaggroup" key="type"><attribute id="type" type="FixedString" value="{self.__scope}" /><children></children></node>')
        children_nodes = result.find('./children')
        for flag in self.__flags:
            children_nodes.append(flag.to_xml())
        return result

class flag_registry:
    __tool: bg3_modding_tool
    __registry: dict[str, str]

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__tool = tool
        self.__registry = dict[str, str]()
        flag_files = [f for f in self.__tool.list('Gustav') if "/Flags/" in f]
        for flag_file in flag_files:
            flag_uuid = os.path.basename(flag_file)[:-4]
            self.__registry[flag_uuid] = flag_file
        

    def get_flag(self, flag_uuid: str) -> flag_object:
        if flag_uuid not in self.__registry:
            raise KeyError(f'flag {flag_uuid} is not found')
        return flag_object(game_file(self.__tool, self.__registry[flag_uuid], pak_name='Gustav'))
