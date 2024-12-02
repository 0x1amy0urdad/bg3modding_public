from __future__ import annotations

import os
import os.path
import sys
import traceback
import xml.etree.ElementTree as et

from ._common import get_bg3_attribute
from ._files import game_file
from ._dialog import dialog_object
from ._soundbank import soundbank_object
from ._tool import bg3_modding_tool

from typing import Callable, Iterable

class dialog_scanner:
    __tool: bg3_modding_tool

    def __init__(self, tool: bg3_modding_tool) -> None:
        self.__tool = tool

    def scan_dialogs(self, pak_file_name: str, on_dialog_node: Callable[[dialog_object], None], /, early_access: bool = False) -> None:
        if early_access:
            files = [f for f in self.__tool.list(pak_file_name) if f.endswith('.lsj') and 'Dialogs' in f]
        else:
            files = [f for f in self.__tool.list(pak_file_name) if f.endswith('.lsf') and 'DialogsBinary' in f]
        scanner_progress_file_path = os.path.join(os.getcwd(), "__scanner__", "scanner_progress")
        files_count = len(files)
        n = 0
        for file in files:
            try:
                gf = game_file(self.__tool, file, pak_name=pak_file_name)
                dialog = dialog_object(gf)
                on_dialog_node(dialog)
            except BaseException:
                exc = traceback.format_exc()
                print(f"Skipped {file} because processing failed due to exception: \n{exc}")
            n += 1
            if n % 10 == 0:
                with open(scanner_progress_file_path, "wt") as fd:
                    fd.write(f"{pak_file_name}: {n} / {files_count}\n")

    def create_voice_lines_index(self, character_uuids: Iterable[str], /, early_access: bool = False) -> None:
        loca_dict = dict[str, str]()
        loca_file = self.__tool.unpack('Localization/English', 'Localization/English/english.loca')
        xml_file = self.__tool.convert_loca_to_xml(loca_file)
        xml = et.parse(xml_file)
        for element in xml.getroot():
            if isinstance(element, et.Element):
                text_handle = element.attrib['contentuid']
                text_content = element.text
                loca_dict[text_handle] = text_content

        os.makedirs(os.path.join(os.getcwd(), "__scanner__", "dialog_index"), exist_ok=True)
        text_handles = dict[str, frozenset]()
        filepaths = dict[str, str]()
        for character_uuid in character_uuids:
            soundbank_name = character_uuid.replace('-', '')
            if early_access:
                sb = soundbank_object(game_file(self.__tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_name}.lsf', pak_name='Localization/Voice'))
            else:
                sb = soundbank_object(game_file(self.__tool, f'Mods/Gustav/Localization/English/Soundbanks/{soundbank_name}.lsf', pak_name='Localization/VoiceMeta'))
            text_handles[character_uuid] = frozenset(sb.get_all_text_handles())
            sb = None        
            filepath = os.path.join(os.getcwd(), "__scanner__", "dialog_index", character_uuid + ".json")
            if os.path.isfile(filepath):
                os.unlink(filepath)
            with open(filepath, "at") as fd:
                fd.write("[\n")
            filepaths[character_uuid] = filepath
            filepath = None

        def process_dialog(dialog: dialog_object) -> None:
            for character_uuid in character_uuids:
                dialog_tagged_texts = dialog.get_all_tagged_texts()
                ths = text_handles[character_uuid].intersection(dialog_tagged_texts.keys())
                if len(ths) > 0:
                    result = dict[str, str]()
                    result["filename"] = os.path.basename(dialog.filename).replace('\\', '-')
                    for th in ths:
                        version = dialog_tagged_texts[th]
                        if th in loca_dict:
                            text = loca_dict[th]
                            result[th + '#' + str(version)] = text
                    if len(result) > 1:
                        with open(filepaths[character_uuid], "at") as fd:
                            fd.write("{\n")
                            fn = result['filename'] if 'filename' in result else ""
                            fd.write(f'  "filename": "{fn}",\n')
                            for k, v in result.items():
                                if k == 'filename':
                                    continue
                                fd.write(f'  "{k}": "{v}",\n')
                            fd.write("},\n")

        self.scan_dialogs('Gustav', process_dialog, early_access=early_access)
        for character_uuid in character_uuids:
            with open(filepaths[character_uuid], "at") as fd:
                fd.write("]\n")

