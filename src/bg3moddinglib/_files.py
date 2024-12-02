from __future__ import annotations

import datetime
import hashlib
import json
import os
import os.path
import shutil
import sys
import xml.etree.ElementTree as et

from ._common import translate_path
from ._tool import bg3_modding_tool

class game_file:
    __tool: bg3_modding_tool
    __relative_file_path: str
    __unpacked_file_path: str
    __converted_file_path: str | None
    __file_format: str
    __xml: et.ElementTree | None

    def __init__(
            self,
            tool: bg3_modding_tool,
            file_path: str,
            pak_name: str | None = None,
            source_file_path: str | None = None,
            new_file: bool = False
    ) -> None:
        self.__tool = tool
        if pak_name is not None:
            self.__relative_file_path = file_path
            self.__unpacked_file_path = tool.unpack(pak_name, file_path)
            if self.__unpacked_file_path.endswith(".lsf"):
                self.__converted_file_path = tool.convert_lsf_to_lsx(self.__unpacked_file_path)
                self.__file_format = "lsf"
            elif self.__unpacked_file_path.endswith(".loca"):
                self.__converted_file_path = tool.convert_loca_to_xml(self.__unpacked_file_path)
                self.__file_format = "loca"
            elif self.__unpacked_file_path.endswith(".lsx"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__file_format = "lsx"
            elif self.__unpacked_file_path.endswith(".lsj"):
                self.__converted_file_path = tool.convert_lsj_to_lsx(self.__unpacked_file_path)
                self.__file_format = "lsj"
            else:
                self.__converted_file_path = None
                self.__file_format = "other"
            if self.__converted_file_path is not None:
                self.__xml = et.parse(self.__converted_file_path)
        elif source_file_path is not None:
            self.__unpacked_file_path = source_file_path
            self.__relative_file_path = file_path
            if self.__unpacked_file_path.endswith(".lsf.lsx"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__unpacked_file_path = self.__unpacked_file_path[:-4]
                self.__file_format = "lsf"
            elif self.__unpacked_file_path.endswith(".loca.xml"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__unpacked_file_path = self.__unpacked_file_path[:-4]
                self.__file_format = "loca"
            elif self.__unpacked_file_path.endswith(".lsx"):
                self.__converted_file_path = self.__unpacked_file_path
                self.__unpacked_file_path = self.__unpacked_file_path
                self.__file_format = "lsx"
            else:
                self.__converted_file_path = None
                self.__file_format = "other"
            if self.__converted_file_path is not None:
                self.__xml = et.parse(self.__converted_file_path)
        elif new_file:
            self.__relative_file_path = file_path
            self.__unpacked_file_path = tool.get_file_path(file_path)
            os.makedirs(os.path.dirname(self.__unpacked_file_path), exist_ok=True)
            if self.__unpacked_file_path.endswith(".lsf"):
                self.__file_format = "lsf"
                self.__converted_file_path = None
                self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<save>\n</save>\n'))
            elif self.__unpacked_file_path.endswith(".lsx"):
                self.__file_format = "lsx"
                self.__converted_file_path = None
                self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<save>\n</save>\n'))
            elif self.__unpacked_file_path.endswith(".loca"):
                self.__file_format = "loca"
                self.__converted_file_path = None
                self.__xml = et.ElementTree(et.fromstring('<?xml version="1.0" encoding="utf-8"?>\n<contentList>\n</contentList>\n'))
            else:
                raise RuntimeError(f"unsupported file type: {file_path}")
        else:
            raise FileNotFoundError(f"file {file_path} is not found")

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    @property
    def relative_file_path(self) -> str:
        return self.__relative_file_path

    @property
    def unpacked_file_path(self) -> str:
        return self.__unpacked_file_path

    @property
    def file_format(self) -> str:
        return self.__file_format

    @property
    def xml(self) -> et.ElementTree:
        return self.__xml

    @property
    def root_node(self) -> et.Element:
        return self.__xml.getroot()

class game_files:
    __tool: bg3_modding_tool
    __mod_pretty_name: str
    __mod_name: str
    __mod_uuid: str
    __mod_version: int | None
    __output_dir_path: str
    __preview_dir_path: str
    __files: dict[str, game_file]

    def __init__(self, tool: bg3_modding_tool, mod_name: str, mod_uuid: str) -> None:
        self.__tool = tool
        self.__mod_pretty_name = mod_name
        self.__mod_name = mod_name + "_" + mod_uuid
        self.__mod_uuid = mod_uuid
        self.__mod_version = None
        self.__files = dict[str, game_file]()
        self.__output_dir_path = os.path.join(tool.env.output_path, mod_name)
        os.makedirs(self.__output_dir_path)
        self.__preview_dir_path = os.path.join(tool.env.output_path, mod_name + '_preview')
        os.makedirs(self.__preview_dir_path)

    @property
    def tool(self) -> bg3_modding_tool:
        return self.__tool

    def get_loca_relative_path(self) -> str:
        result = f"Localization/English/{self.__mod_name}.loca"
        os.makedirs(os.path.join(self.__output_dir_path, os.path.dirname(result)), exist_ok=True)
        return result

    def get_file(self, pak_name: str, file_path: str) -> game_file:
        if file_path in self.__files:
            return self.__files[file_path]
        gf = game_file(self.__tool, file_path, pak_name=pak_name)
        self.__files[file_path] = gf
        return gf

    def add_new_file(self, relative_path: str) -> game_file:
        gf = game_file(self.__tool, relative_path, new_file=True)
        self.__files[relative_path] = gf
        return gf

    def add_external_file(self, source_file_path: str, relative_path: str) -> game_file:
        gf = game_file(self.__tool, relative_path, source_file_path=source_file_path)
        self.__files[relative_path] = gf
        return gf

    def copy_external_files(self, source_dir_path: str, relative_path: str) -> None:
        dest_path = os.path.join(self.__output_dir_path, translate_path(relative_path))
        os.makedirs(dest_path, exist_ok=True)
        for dir_entry in os.scandir(source_dir_path):
            if dir_entry.is_dir():
                shutil.copytree(dir_entry.path, os.path.join(dest_path, dir_entry.name), dirs_exist_ok=True)

    def copy_script_extender_lua_files(self, source_path: str) -> None:
        if not os.path.isdir(source_path):
            raise ValueError("not a directory path: " + source_path)
        if os.path.isdir(os.path.join(source_path, "ScriptExtender")):
            scripts_dir_path = os.path.join(self.__output_dir_path, "Mods", self.__mod_name, "ScriptExtender")
            os.makedirs(scripts_dir_path, exist_ok=True)
            shutil.copytree(os.path.join(source_path, "ScriptExtender"), scripts_dir_path, dirs_exist_ok=True)

    def copy_meta_lsx(self, source_path: str) -> None:
        meta_lsx_dir_path = os.path.join(self.__output_dir_path, "Mods", self.__mod_name)
        if os.path.isdir(source_path):
            file_path = os.path.join(source_path, "meta.lsx")
            if os.path.isfile(file_path):
                shutil.copy(file_path, meta_lsx_dir_path)
            else:
                raise FileNotFoundError(f"meta.lsx is not found in provided path {source_path}")
        elif os.path.isfile(source_path):
            shutil.copy(file_path, os.path.join(meta_lsx_dir_path, "meta.lsx"))
        else:
            raise FileNotFoundError(f"meta.lsx is not found in provided path {source_path}")

    def copy_mod_logo(self, source_path: str) -> None:
        mod_dir_path = os.path.join(self.__output_dir_path, "Mods", self.__mod_name)
        if os.path.isdir(source_path):
            file_path = os.path.join(source_path, "mod_publish_logo.png")
            if os.path.isfile(file_path):
                shutil.copy(file_path, mod_dir_path)
            else:
                raise FileNotFoundError(f"meta.lsx is not found in provided path {source_path}")
        elif os.path.isfile(source_path):
            shutil.copy(file_path, os.path.join(mod_dir_path, "mod_publish_logo.png"))
        else:
            raise FileNotFoundError(f"mod_publish_logo.png is not found in provided path {source_path}")

    def create_meta_lsx(
            self,
            version: tuple[int, int, int, int],
            /,
            author: str = "Anonymous",
            display_name: str | None = None,
            description: str | None = None
    ) -> None:
        self.__mod_version = version[3] + (version[2] << 31) + (version[1] << 47) + (version[0] << 55)
        if display_name is None:
            display_name = self.__mod_pretty_name
        if description is None:
            description = self.__mod_pretty_name
        meta_lsx = f"""<?xml version="1.0" encoding="utf-8"?>
<save>
    <version major="4" minor="7" revision="1" build="3" />
    <region id="Config">
        <node id="root">
            <children>
                <node id="Conflicts"/>
                <node id="Dependencies">
                    <children>
                        <node id="ModuleShortDesc">
                            <attribute id="Folder" type="LSString" value="GustavDev"/>
                            <attribute id="MD5" type="LSString" value="96c19798a020e178251944be557fc464"/>
                            <attribute id="Name" type="LSString" value="GustavDev"/>
                            <attribute id="PublishHandle" type="uint64" value="0"/>
                            <attribute id="UUID" type="guid" value="28ac9ce2-2aba-8cda-b3b5-6e922f71b6b8"/>
                            <attribute id="Version64" type="int64" value="145100393449790344"/>
                        </node>
                    </children>
                </node>
                <node id="ModuleInfo">
                    <attribute id="Author" type="LSString" value="{author}" />
                    <attribute id="CharacterCreationLevelName" type="FixedString" value="" />
                    <attribute id="Description" type="LSString" value="{description}" />
                    <attribute id="FileSize" type="uint64" value="0"/>
                    <attribute id="Folder" type="LSString" value="{self.__mod_name}" />
                    <attribute id="LobbyLevelName" type="FixedString" value="" />
                    <attribute id="MD5" type="LSString" value="" />
                    <attribute id="MenuLevelName" type="FixedString" value="" />
                    <attribute id="Name" type="LSString" value="{display_name}" />
                    <attribute id="NumPlayers" type="uint8" value="4" />
                    <attribute id="PhotoBooth" type="FixedString" value="" />
                    <attribute id="StartupLevelName" type="FixedString" value="" />
                    <attribute id="UUID" type="FixedString" value="{self.__mod_uuid}" />
                    <attribute id="Version64" type="int64" value="{self.__mod_version}" />
                    <children>
                        <node id="PublishVersion">
                            <attribute id="Version64" type="int64" value="144255927717549775" />
                        </node>
                        <node id="Scripts">
                            <children>
                                <node id="Script">
                                    <attribute id="UUID" type="FixedString" value="1953f77d-a201-45d7-a194-9b84c34b8461"/>
                                    <children>
                                        <node id="Parameters">
                                            <children>
                                                <node id="Parameter">
                                                    <attribute id="MapKey" type="FixedString" value="HardcoreOnly"/>
                                                    <attribute id="Type" type="int32" value="1"/>
                                                    <attribute id="Value" type="LSString" value="0"/>
                                                </node>
                                            </children>
                                        </node>
                                    </children>
                                </node>
                                <node id="Script">
                                    <attribute id="UUID" type="FixedString" value="0d6510f5-50a3-4ecd-83d8-134c9a640324"/>
                                    <children>
                                        <node id="Parameters">
                                            <children>
                                                <node id="Parameter">
                                                    <attribute id="MapKey" type="FixedString" value="HardcoreOnly"/>
                                                    <attribute id="Type" type="int32" value="1"/>
                                                    <attribute id="Value" type="LSString" value="0"/>
                                                </node>
                                            </children>
                                        </node>
                                    </children>
                                </node>
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>
"""
        meta_lsx_path = os.path.join(self.__output_dir_path, "Mods", self.__mod_name, "meta.lsx")
        os.makedirs(os.path.dirname(meta_lsx_path), exist_ok=True)
        with open(meta_lsx_path, "wt") as f:
            f.write(meta_lsx)

    def create_info_json(self, md5_hash: str) -> None:
        info_json = {
            "Mods": [
                {
                    "Author": "iamy0urdad",
                    "Name": self.__mod_pretty_name,
                    "Folder": self.__mod_name,
                    "Version": str(self.__mod_version),
                    "Description": self.__mod_pretty_name,
                    "UUID": self.__mod_uuid,
                    "Created": datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                    "Dependencies": [],
                    "Group": "9ea70f48-daab-4f0a-8ed8-c6b910ee9c4c"
                }
            ],
            "MD5": md5_hash
        }
        info_json_path = os.path.join(self.__output_dir_path, "info.json")
        with open(info_json_path, "wt") as f:
            json.dump(info_json, f)

    def build(self, preview: bool = True, verbose: bool = False) -> str:
        for gf in self.__files.values():
            relative_file_path = translate_path(gf.relative_file_path)
            if verbose:
                sys.stdout.write(f"Processing {relative_file_path} .")
            match gf.file_format:
                case "lsj":
                    raise RuntimeError(".lsj files are not supported")
                case "lsf":
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(self.__preview_dir_path, relative_file_path) + '.lsx'
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        if verbose:
                            sys.stdout.write('.')
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    lsx_file_path = os.path.join(self.__output_dir_path, relative_file_path) + '.lsx'
                    os.makedirs(os.path.dirname(lsx_file_path), exist_ok=True)
                    gf.xml.write(lsx_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('.')
                    self.__tool.convert_lsx_to_lsf(lsx_file_path)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "lsx":
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(self.__preview_dir_path, relative_file_path)
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        if verbose:
                            sys.stdout.write('.')
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    lsx_file_path = os.path.join(self.__output_dir_path, relative_file_path)
                    os.makedirs(os.path.dirname(lsx_file_path), exist_ok=True)
                    if verbose:
                        sys.stdout.write('.')
                    gf.xml.write(lsx_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "loca":
                    et.indent(gf.xml.getroot())
                    if preview:
                        preview_file_path = os.path.join(self.__preview_dir_path, relative_file_path) + '.xml'
                        os.makedirs(os.path.dirname(preview_file_path), exist_ok=True)
                        gf.xml.write(preview_file_path, encoding="utf-8", xml_declaration=True)
                        if verbose:
                            sys.stdout.write('.')
                    xml_file_path = os.path.join(self.__output_dir_path, relative_file_path) + '.xml'
                    os.makedirs(os.path.dirname(xml_file_path), exist_ok=True)
                    gf.xml.write(xml_file_path, encoding="utf-8", xml_declaration=True)
                    if verbose:
                        sys.stdout.write('.')
                    self.__tool.convert_xml_to_loca(xml_file_path)
                    if verbose:
                        sys.stdout.write('. done\n')
                case "other":
                    file_path = os.path.join(self.__output_dir_path, relative_file_path)
                    os.makedirs(os.path.dirname(file_path), exist_ok=True)
                    src_ext = os.path.splitext(gf.unpacked_file_path)[1]
                    dest_ext = os.path.splitext(file_path)[1]
                    if src_ext == '.lsx' and dest_ext == '.lsf':
                        shutil.copy(gf.unpacked_file_path, file_path + '.lsx')
                        if verbose:
                            sys.stdout.write('.')
                        self.__tool.convert_lsx_to_lsf(file_path + '.lsx')
                    elif src_ext == '.xml' and dest_ext == '.loca':
                        shutil.copy(gf.unpacked_file_path, file_path + '.xml')
                        if verbose:
                            sys.stdout.write('.')
                        self.__tool.convert_xml_to_loca(file_path + '.xml')
                    elif src_ext == dest_ext:
                        shutil.copy(gf.unpacked_file_path, file_path)
                    else:
                        raise RuntimeError(f"failed to process an external file {gf.unpacked_file_path} with target relative path {gf.relative_file_path}")
                    if verbose:
                        sys.stdout.write('. done\n')
                case unknown_format:
                    raise ValueError(F"Unknown file format: {unknown_format}")
        if verbose:
            sys.stdout.write('Generating the .pak file .')
        pak_file = self.__tool.pack(self.__output_dir_path, os.path.join(self.__output_dir_path, self.__mod_name + ".pak"))
        if verbose:
            sys.stdout.write('.')
        md5 = hashlib.new('md5')
        with open(pak_file, 'rb') as f:
            buf = f.read(1024 * 1024)
            while buf:
                md5.update(buf)
                buf = f.read(1024 * 1024)
        md5_hash = md5.hexdigest()
        with open(pak_file + '.md5', 'wt') as f:
            f.write(md5_hash)
        if verbose:
            sys.stdout.write('. done\n')
        self.create_info_json(md5_hash)
