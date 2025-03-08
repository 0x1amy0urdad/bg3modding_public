from __future__ import annotations

import os
import xml.etree.ElementTree as et

from ._common import get_bg3_handle_attribute, get_required_bg3_attribute, new_random_uuid, set_bg3_attribute
from ._files import game_file, game_files
from ._tool import bg3_modding_tool

from typing import Iterable

LOCAL_FLAG = 1
OBJECT_FLAG = 4
GLOBAL_FLAG = 5

class tag_object:
    __file: game_file
    __description: str
    __display_description: tuple[str, int]
    __display_name: tuple[str, int]
    __icon: str
    __name: str
    __uuid: str
    __categories: list[str]

    def __init__(
            self,
            f: game_files | game_file | None,
            /,
            description: str | None = None,
            display_description: tuple[str, int] | None = None,
            display_name: tuple[str, int] | None = None,
            icon: str | None = None,
            name: str | None = None,
            tag_uuid: str | None = None,
            categories: list[str] | None = None,
    ) -> None:
        if isinstance(f, game_files):
            if tag_uuid is None:
                raise RuntimeError("tag_uuid cannot be None")
            if description is None:
                raise RuntimeError("description cannot be None")
            if display_description is None:
                raise RuntimeError("display_description cannot be None")
            if display_name is None:
                raise RuntimeError("display_name cannot be None")
            if name is None:
                raise RuntimeError("name cannot be None")
            if categories is None or len(categories) == 0:
                raise RuntimeError("categories cannot be None or empty")
            self.__description = description
            self.__display_description = display_description
            self.__display_name = display_name
            self.__icon = icon if icon is not None else ""
            self.__name = name
            self.__categories = categories
            self.__file = f.add_new_file(f'Public/Shared/Tags/{tag_uuid}.lsf')
            root_node = self.__file.root_node
            root_node.append(et.fromstring('<version major="4" minor="0" revision="0" build="58" lslib_meta="v1,bswap_guids,lsf_keys_adjacency" />'))
            root_node.append(et.fromstring('<region id="Tags"><node id="Tags"><children><node id="Categories"><children></children></node></children></node></region>'))
            tag_node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]')
            if tag_node is None:
                raise RuntimeError("bad xml object")
            set_bg3_attribute(tag_node, "Description", self.__description[0], attribute_type = "LSString", version = self.__description[1])
            set_bg3_attribute(tag_node, "DisplayDescription", self.__display_description[0], attribute_type = "TranslatedString", version = self.__display_description[1])
            set_bg3_attribute(tag_node, "DisplayName", self.__display_name[0], attribute_type = "TranslatedString", version = self.__display_name[1])
            set_bg3_attribute(tag_node, "Icon", self.__icon, attribute_type = "FixedString")
            set_bg3_attribute(tag_node, "Name", self.__name, attribute_type = "FixedString")
            set_bg3_attribute(tag_node, "UUID", self.__uuid, attribute_type = "guid")
            categories_node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]/children/node[@id="Categories"]/children')
            if categories_node is None:
                raise RuntimeError("bad xml object")
            for category in categories:
                categories_node.append(et.fromstring(f'<node id="Category"><attribute id="Name" type="LSString" value="{category}" /></node>'))
        elif isinstance(f, game_file):
            self.__file = f
            root_node = f.xml.getroot()
            if isinstance(root_node, et.Element):
                node = root_node.find('./region[@id="Tags"]/node[@id="Tags"]')
                if node is None:
                    raise RuntimeError("bad xml object")
                self.__description = get_required_bg3_attribute(node, "Description")
                self.__display_description = get_bg3_handle_attribute(node, "DisplayDescription")
                self.__display_name = get_bg3_handle_attribute(node, "DisplayName")
                self.__icon = get_required_bg3_attribute(node, "Icon")
                self.__name = get_required_bg3_attribute(node, "Name")
                self.__uuid = get_required_bg3_attribute(node, "UUID")
                categories = root_node.findall('./region[@id="Tags"]/node[@id="Tags"]/children/node[@id="Categories"]/children/node[@id="Category"]')
                self.__categories = list[str]()
                for category in categories:
                    self.__categories.append(get_required_bg3_attribute(category, "Name"))
