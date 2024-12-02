from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import lower_bound_by_node_attribute
from ._files import game_file


class loca_object:
    __file: game_file

    def __init__(self, gamefile: game_file) -> None:
        self.__file = gamefile

    @property
    def file(self) -> game_file:
        return self.__file

    def add_lines(self, content: dict[str, tuple[int, str]]) -> None:
        root_node = self.__file.root_node
        handles = [h for h in content.keys()]
        handles.sort()
        for handle in handles:
            value = content[handle]
            version = value[0]
            text = value[1]
            root_node.append(et.fromstring(f'    <content contentuid="{handle}" version="{version}">{text}</content>\n'))

    def add_line(self, handle: str, version: int, text: str) -> None:
        root_node = self.__file.root_node
        nodes = root_node.findall(f'./content')
        if isinstance(nodes, list) and len(nodes) > 0:
            index = lower_bound_by_node_attribute(nodes, "contentuid", handle)
            root_node.insert(index, et.fromstring(f'    <content contentuid="{handle}" version="{version}">{text}</content>\n'))
        else:
            root_node.append(et.fromstring(f'    <content contentuid="{handle}" version="{version}">{text}</content>\n'))

    def update_line(self, handle: str, version: int, text: str) -> None:
        root_node = self.__file.root_node
        node = root_node.find(f'./content[@contentuid="{handle}"]')
        if node is None:
            raise KeyError(f"text content with handle {handle} doesn't exist")
        node.set("version", str(version))
        node.text = text

    def delete_line(self, handle: str) -> None:
        root_node = self.__file.root_node
        node = root_node.find(f'./content[@contentuid="{handle}"]')
        if node is None:
            raise KeyError(f"text content with handle {handle} doesn't exist")
        root_node.remove(node)
