from __future__ import annotations

import os
import os.path
import traceback
import xml.etree.ElementTree as et

from ._common import get_node_attributes
from ._loca import bg3_loca_object
from ._lsf_dialog import bg3_game_object_dialog
from ._tool import bg3_modding_tool

from typing import Callable

class bg3_object_scanner:
    __tool: bg3_modding_tool

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__tool = tool

    def scan_dialogs(self, pak_file_name: str, on_dialog_node: Callable[[bg3_game_object_dialog], None]) -> None:
        files = [f for f in self.__tool.list(pak_file_name) if 'DialogsBinary' in f]
        scanner_progress_file_path = os.path.join(os.getcwd(), "__scanner__", "scanner_progress")
        files_count = len(files)
        n = 0
        for file in files:
            try:
                lsf = self.__tool.unpack(pak_file_name, file)
                lsx = self.__tool.convert_lsf_to_lsx(lsf)
                dialog = bg3_game_object_dialog(lsx)
                on_dialog_node(dialog)
            except BaseException:
                exc = traceback.format_exc()
                print(f"Failed to load {file} due to exception: \n{exc}")
            n += 1
            if n % 10 == 0:
                with open(scanner_progress_file_path, "wt") as fd:
                    fd.write(f"{pak_file_name}: {n} / {files_count}\n")

    def create_voice_lines_index(self, character_uuid: str) -> None:
        loca_dict = dict[str, str]()
        loca_file = self.__tool.unpack('Localization/English', 'Localization/English/english.loca')
        xml_file = self.__tool.convert_loca_to_xml(loca_file)
        xml = et.parse(xml_file)
        for element in xml.getroot():
            if isinstance(element, et.Element):
                text_handle = element.attrib['contentuid']
                text_content = element.text
                loca_dict[text_handle] = text_content

        filepath = os.path.join(os.getcwd(), "__scanner__", "dialog_index", character_uuid + ".json")
        if os.path.isfile(filepath):
            os.unlink(filepath)
        os.makedirs(os.path.join(os.getcwd(), "__scanner__", "dialog_index"), exist_ok=True)

        def process_dialog(dialog: bg3_game_object_dialog) -> None:
            speaker_slot_index = dialog.get_speaker_slot_index(character_uuid)
            if speaker_slot_index is None:
                return
            result = dict[str, str]()
            result["filename"] = os.path.basename(dialog.filename).replace('\\', '-')
            for dialog_node in dialog.get_dialog_nodes():
                dialog_attributes = get_node_attributes(dialog_node)
                if 'speaker' in dialog_attributes and int(dialog_attributes['speaker']) == speaker_slot_index:
                    tag_text_node = dialog_node.find("./children/node[@id='TaggedTexts']/children/node[@id='TaggedText']/children/node[@id='TagTexts']/children/node[@id='TagText']")
                    if tag_text_node is not None:
                        tag_text_attributes = get_node_attributes(tag_text_node)
                        if 'TagText' in tag_text_attributes and 'LineId' in tag_text_attributes:
                            text_handle = tag_text_attributes['TagText']
                            line_id = tag_text_attributes['LineId']
                            if text_handle in loca_dict:
                                text = loca_dict[text_handle]
                                result[text_handle + '#' + line_id] = text
            if len(result) > 1:
                with open(filepath, "at") as fd:
                    fd.write("{\n")
                    fn = result['filename'] if 'filename' in result else ""
                    fd.write(f'  "filename": "{fn}",\n')
                    for k, v in result.items():
                        if k == 'filename':
                            continue
                        fd.write(f'  "{k}": "{v}",\n')
                    fd.write("}\n")

        self.scan_dialogs('Gustav', process_dialog)

