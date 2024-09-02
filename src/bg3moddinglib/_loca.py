from __future__ import annotations

import os
import uuid
import xml.etree.ElementTree as et

from ._common import translate_path
from typing import Optional

class bg3_loca_object:
    __filename: str
    __xml: et.ElementTree
    __map: dict[str, et.Element]
    __keys: list[str]

    def __init__(self, loca_xml_file_name: str) -> None:
        if not loca_xml_file_name.endswith(".loca.xml"):
            raise ValueError(f"Unexpected file: {loca_xml_file_name}")
        if not os.path.isfile(loca_xml_file_name):
            raise FileNotFoundError(f"File '{loca_xml_file_name}' doesn't exist")
        self.__filename = loca_xml_file_name
        self.__xml = et.parse(loca_xml_file_name)
        self.__map = dict[str, et.Element]()
        self.__keys = list[str]()
        element_count = 0
        for element in self.__xml.getroot():
            if isinstance(element, et.Element):
                contentuid = element.attrib['contentuid']
                self.__map[contentuid] = element
                self.__keys.append(contentuid)
                element_count += 1
        if len(self.__map) != element_count:
            raise RuntimeError("Non-unique contentuid is detected in loca object")


    def get(self, contentuid: str) -> Optional[str]:
        if contentuid in self.__map:
            return self.__map[contentuid].text
        return None

    def add(self, content: str, version: str) -> str:
        uid = None
        while uid is None or uid in self.__map:
            uid = 'h' + str(uuid.uuid1()).replace('-', 'g')
        new_elt = et.fromstring(f'<content contentuid="{uid}" version="{version}">{content}</content>')
        index = self.__lower_bound(uid)
        self.__xml.getroot().insert(index, new_elt)
        self.__keys.insert(index, uid)
        self.__map[uid] = new_elt
        return uid

    def delete(self, contentuid: str) -> None:
        if contentuid in self.__map:
            self.__xml.getroot().remove(self.__map[contentuid])
            del self.__map[contentuid]
            index = self.__lower_bound(contentuid)
            del self.__keys[index]
        else:
            raise KeyError(f"'{contentuid}' is not found in {self.__filename}")

    def patch(self, contentuid: str, content: str) -> None:
        if contentuid not in self.__map:
            raise KeyError(f"'{contentuid}' is not found in {self.__filename}")
        self.__map[contentuid].text = content

    def save_to(self, dest_file_path: str) -> None:
        dest_file_path = translate_path(dest_file_path)
        os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
        self.__xml.write(dest_file_path, encoding="utf-8", xml_declaration=True)
        return dest_file_path

    def __lower_bound(self, contentuid: str) -> int:
        top = len(self.__keys)
        if top == 1:
            return 0
        pos = top >> 1
        step = pos >> 1
        for n in range(0, top):
            cur = self.__keys[pos]
            next = None if pos + 1 >= top else self.__keys[pos + 1]
            prev = None if pos == 0 else self.__keys[pos - 1]
            if cur < contentuid:
                if next is None or next > contentuid:
                    return pos
                if step > 1:
                    step = step >> 1
                pos += step
            elif cur == contentuid:
                return pos
            else:
                if prev is None or prev < contentuid:
                    return pos
                if step > 1:
                    step = step >> 1
                pos -= step
        raise RuntimeError(f"Failed to find the lower bound for {contentuid}")
