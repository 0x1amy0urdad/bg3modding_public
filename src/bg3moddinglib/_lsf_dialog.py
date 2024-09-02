from __future__ import annotations

import os
import uuid
import xml.etree.ElementTree as et

from typing import Optional, Union

from ._common import get_node_children, get_node_attribute, get_node_attributes, require_attributes, set_node_attribute, translate_path

class bg3_game_object_dialog:
    __filename: str
    __xml: et.ElementTree
    __xml_dialog_nodes: Optional[et.Element]
    __dialog_uid: str
    __timeline_id: str
    __speakers: list[tuple[str, str]]
    __root_nodes: list[str]
    __nodes: dict[str, et.Element]

    def __init__(self, lsx_file_path: str) -> None:
        if not lsx_file_path.endswith(".lsx"):
            raise ValueError(f"Unexpected file: {lsx_file_path}")
        if not os.path.isfile(lsx_file_path):
            raise FileNotFoundError(f"File '{lsx_file_path}' doesn't exist")
        self.__filename = lsx_file_path
        self.__xml = et.parse(lsx_file_path)
        self.__xml_dialog_nodes = None
        self.__dialog_uid = ""
        self.__timeline_id = ""
        self.__speakers = list[tuple[str, str]]()
        self.__root_nodes = list[str]()
        self.__nodes = dict[str, et.Element]()
        self.__init_dialog()

    @property
    def filename(self) -> str:
        return self.__filename

    @property
    def uid(self) -> str:
        return self.__dialog_uid

    @property
    def timeline_id(self) -> str:
        return self.__timeline_id

    @property
    def speakers(self) -> dict[str, str]:
        return { speaker[0]: speaker[1] for speaker in self.__speakers }

    @property
    def root_nodes(self) -> tuple[str, ...]:
        return tuple(self.__root_nodes)

    @property
    def xml(self) -> et.ElementTree:
        return self.__xml

    def create_uuid(self) -> str:
        while True:
            result = str(uuid.uuid4())
            if result not in self.__nodes:
                return result

    def get_children_uuids(self, node_uuid: str) -> list[str]:
        result = list[str]()
        if node_uuid not in self.__nodes:
            raise KeyError(f"Node '{node_uuid}' doesn't exists in the dialog.")
        d = self.__nodes[node_uuid]
        for child_node in d.findall("children/node[@id='children']/children/node"):
            attributes = get_node_attributes(child_node)
            if 'UUID' in attributes:
                result.append(attributes['UUID'])
        return result

    def get_dialog_node(self, node_uuid: str) -> et.Element:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        return self.__nodes[node_uuid]

    def get_dialog_children_count(self, node_uuid: str) -> int:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        td = self.__nodes[node_uuid]
        children = td.find("children/node[@id='children']/children")
        if children is et.Element:
            return len(children)
        return 0

    def get_child_dialog_node(self, node_uuid: str, child_id: Union[str, int]) -> et.Element:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        td = self.__nodes[node_uuid]
        children = td.find("children/node[@id='children']/children")
        if isinstance(child_id, int):
            if child_id >= len(children):
                raise IndexError(f"Index {child_id} >= number of elements {len(children)} in dialog node {node_uuid}")
            return children[child_id]
        if isinstance(child_id, str):
            for child in children:
                if get_node_attribute(child, 'UUID') == child_id:
                    return child
        return None

    def delete_child_dialog_node(self, node_uuid: str, child_id: Union[str, int]) -> et.Element:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        td = self.__nodes[node_uuid]
        children = td.find("children/node[@id='children']/children")
        if not isinstance(children, et.Element):
            return None
        if isinstance(child_id, int):
            if child_id >= len(children):
                raise IndexError(f"Index {child_id} >= number of elements {len(children)} in dialog node {node_uuid}")
            result = children[child_id]
            children.remove(children[child_id])
            return result
        if isinstance(child_id, str):
            for child in children:
                if get_node_attribute(child, 'UUID') == child_id:
                    children.remove(child)
                    return child
        return None

    def append_child_dialog_node(self, node_uuid: str, child_uuid: str) -> None:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        td = self.__nodes[node_uuid]
        children = td.find("children/node[@id='children']/children")
        if not isinstance(children, et.Element):
            children = et.fromstring("<children></children>")
            td.find("children/node[@id='children']").insert(0, children)
        children.append(et.fromstring(f"""<node id="child"><attribute id="UUID" type="FixedString" value="{child_uuid}" /></node>"""))

    def insert_child_dialog_node(self, node_uuid: str, index: int, child_uuid: str) -> None:
        if node_uuid not in self.__nodes:
            raise KeyError(f"Dialog node '{node_uuid}' doesn't exists in the dialog.")
        td = self.__nodes[node_uuid]
        children = td.find("children/node[@id='children']/children")
        if not isinstance(children, et.Element):
            children = et.fromstring("<children></children>")
            td.find("children/node[@id='children']").insert(0, children)
        child = et.fromstring(f"""<node id="child"><attribute id="UUID" type="FixedString" value="{child_uuid}" /></node>""")
        if index >= len(children):
            children.append(child)
        else:
            children.insert(index, child)

    def get_dialog_nodes(self) -> tuple[et.Element, ...]:
        return tuple(self.__nodes.values())

    def create_speakers_mapping(self, target_dialog: bg3_game_object_dialog) -> dict[str, str]:
        speakers_mapping = dict[str, str]()
        target_dialog_speakers = target_dialog.speakers
        for src_speaker_uuid, src_actor_uuid in self.__speakers:
            if src_speaker_uuid in target_dialog_speakers:
                speakers_mapping[src_actor_uuid] = target_dialog_speakers[src_speaker_uuid]
        return speakers_mapping

    def get_speaker_slot_index(self, speaker_uuid: str) -> Optional[int]:
        for index in range(0, len(self.__speakers)):
            if self.__speakers[index][0] == speaker_uuid:
                return index
        return None

    def add_dialog_node(self, new_node: et.Element) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot add a new node to an empty or invalid dialog object")
        attributes = get_node_attributes(new_node)
        require_attributes("The new node doesn't contain a required attribute: ", attributes, "UUID")
        new_node_uuid = attributes["UUID"]
        if new_node_uuid in self.__nodes:
            raise KeyError(f"Cannot add a new node: another node with UUID '{new_node_uuid}' already exists.")
        self.__xml_dialog_nodes.append(new_node)
        self.__nodes[new_node_uuid] = new_node

    def patch_dialog_node(self, node_uuid: str, children_nodes: tuple[et.Element, ...]) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        new_children = { n.get('id'): n for n in children_nodes if n.get('id') is not None }
        existing_children = get_node_children(target_node)
        children_node = target_node.find('children')
        if children_node is None:
            raise ValueError("Unexpected: children node is None.")
        for existing_child in existing_children:
            if existing_child.get('id') in new_children:
                children_node.remove(existing_child)
        for new_child in new_children.values():
            children_node.append(new_child)

    def patch_dialog_node_attributes(self, node_uuid: str, add_attrs: list[tuple[str, str, str]]=[], remove_attrs: list[str]=[]) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        existing_attrs = { elt.get("id"): elt for elt in target_node.findall("attribute") }
        for remove_attr_id in remove_attrs:
            if remove_attr_id in existing_attrs:
                target_node.remove(existing_attrs[remove_attr_id])
            else:
                raise KeyError(f"Cannot remove attribute {remove_attr_id} from node {node_uuid}")
        for attr_id, attr_type, attr_value in add_attrs:
            if attr_id in existing_attrs:
                target_node.remove(existing_attrs[attr_id])
            target_node.insert(0, et.fromstring(f'<attribute id="{attr_id}" type="{attr_type}" value="{attr_value}" />'))

    def patch_dialog_node_flags(self, node_uuid: str, checkflags: Optional[list[et.Element]]=None, setflags: Optional[list[et.Element]]=None) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        node_children = target_node.find("children")
        if not isinstance(node_children, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        if checkflags is not None:
            if len(checkflags) > 0:
                checkflags_node = et.fromstring("""<node id="checkflags"><children></children></node>""")
                checkflags_children_node = checkflags_node.find("children")
                for node in checkflags:
                    checkflags_children_node.append(node)
            else:
                checkflags_node = et.fromstring("""<node id="checkflags"></node>""")
            existing_checkflags = target_node.find("children/node[@id='checkflags']")
            if isinstance(existing_checkflags, et.Element):
                node_children.remove(existing_checkflags)
            node_children.append(checkflags_node)
        if setflags is not None:
            if len(setflags) > 0:
                setflags_node = et.fromstring("""<node id="setflags"><children></children></node>""")
                setflags_children_node = setflags_node.find("children")
                for node in setflags:
                    setflags_children_node.append(node)
            else:
                setflags_node = et.fromstring("""<node id="setflags"></node>""")
            existing_setflags = target_node.find("children/node[@id='setflags']")
            if isinstance(existing_setflags, et.Element):
                node_children.remove(existing_setflags)
            node_children.append(setflags_node)

    def patch_dialog_tagged_text(self, node_uuid: str, handle: str, version: str) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        tag_text = target_node.find("children/node[@id='TaggedTexts']/children/node[@id='TaggedText']/children/node[@id='TagTexts']/children/node[@id='TagText']")
        set_node_attribute(tag_text, "TagText", "TranslatedString", handle, version=version)

    def patch_dialog_set_tagged_texts(self, node_uuid: str, new_tagged_texts: tuple[tuple[str, str, str, bool], ...]) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        tag_texts = target_node.find("children/node[@id='TaggedTexts']/children/node[@id='TaggedText']/children/node[@id='TagTexts']/children")
        children_nodes = tag_texts.findall("node")
        for child_node in children_nodes:
            tag_texts.remove(child_node)
        for new_tagged_text in new_tagged_texts:
            handle = new_tagged_text[0]
            version = new_tagged_text[1]
            line_id = new_tagged_text[2]
            has_custom_sequence_id = new_tagged_text[3]
            if has_custom_sequence_id:
                tag_texts.append(et.fromstring(f"""<node id="TagText">
<attribute id="TagText" type="TranslatedString" handle="{handle}" version="{version}" />
<attribute id="LineId" type="guid" value="{line_id}" />
<attribute id="CustomSequenceId" type="guid" value="{line_id}" />
<attribute id="stub" type="bool" value="True" /></node>"""))
            else:
                tag_texts.append(et.fromstring(f"""<node id="TagText">
<attribute id="TagText" type="TranslatedString" handle="{handle}" version="{version}" />
<attribute id="LineId" type="guid" value="{line_id}" />
<attribute id="stub" type="bool" value="True" /></node>"""))
        

    def patch_dialog_remove_child(self, node_uuid: str, child_node_uuid: str) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        children_node = target_node.find("children/node[@id='children']/children")
        if not isinstance(children_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        children = children_node.findall('node')
        for child_node in children:
            if get_node_attribute(child_node, "UUID") == child_node_uuid:
                children_node.remove(child_node)
                return
        raise ValueError(f"Child node with id {child_node_uuid} doesn't exist in dialog {node_uuid}")

    def patch_dialog_append_child(self, node_uuid: str, child_node_uuid: str, index: int=-1) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot patch an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot patch: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        if not isinstance(target_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        children_node = target_node.find("children/node[@id='children']/children")
        if children_node is None:
            children_node = target_node.find("children/node[@id='children']")
            child_node = et.fromstring(f"""<children><node id="child"><attribute id="UUID" type="FixedString" value="{child_node_uuid}" /></node></children>""")
            children_node.append(child_node)
        elif not isinstance(children_node, et.Element):
            raise ValueError("Cannot patch a malformed dialog object")
        else:
            child_node = et.fromstring(f"""<node id="child"><attribute id="UUID" type="FixedString" value="{child_node_uuid}" /></node>""")
            if index == -1:
                children_node.append(child_node)
            else:
                children_node.insert(index, child_node)

    def delete_dialog_node(self, node_uuid: str) -> None:
        if self.__xml_dialog_nodes is None:
            raise ValueError("Cannot delete from an empty or invalid dialog object")
        if node_uuid not in self.__nodes:
            raise KeyError(f"Cannot delete: a node with UUID '{node_uuid}' doesn't exist.")
        target_node = self.__nodes[node_uuid]
        self.__xml_dialog_nodes.remove(target_node)
        del self.__nodes[node_uuid]

    def add_root_node(self, node_uuid: str, index: int=-1) -> None:
        nodes = self.__xml.find("region[@id='dialog']/node[@id='dialog']/children/node[@id='nodes']/children")
        new_root_node = et.fromstring(f'<node id="RootNodes"><attribute id="RootNodes" type="FixedString" value="{node_uuid}" /></node>')
        if index == -1:
            nodes.append(new_root_node)
            return
        n = len(nodes)
        idx = index
        for i in range(0, n):
            if nodes[i].get("id") == 'RootNodes':
                if idx == 0:
                    nodes.insert(i, new_root_node)
                    return
                else:
                    idx -= 1
        raise RuntimeError(f"Cannot add root node '{node_uuid}' at index {index}")       

    def save_to(self, dest_file_path: str) -> str:
        dest_file_path = translate_path(dest_file_path)
        dir_path = os.path.dirname(dest_file_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        self.__xml.write(dest_file_path, encoding="utf-8", xml_declaration=True)
        return dest_file_path

    def __init_dialog(self) -> None:
        root = self.__xml.getroot()
        if not isinstance(root, et.Element):
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: the root node isn't an XML element.")
        if root.tag != 'save':
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: the root node isn't 'save'.")
        region = root.findall('region')
        if len(region) != 1:
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: expected 1 'region' node, got {len(region)}.")
        if region[0].get('id') != 'dialog':
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: region's id is not 'dialog'.")
        dialog = region[0].findall('node')
        if len(dialog) != 1:
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: expected 1 'dialog' node, got {len(dialog)}.")
        if dialog[0].get('id') != 'dialog':
            raise ValueError(f"'{self.__filename}' doesn't contain a dialog: dialog's id is not 'dialog'.")

        dialog_attributes = get_node_attributes(dialog[0])
        require_attributes("Required attributes are not found in a dialog object: ", dialog_attributes, "UUID")
        self.__dialog_uid = dialog_attributes['UUID']
        if 'TimelineId' in dialog_attributes:
            self.__timeline_id = dialog_attributes['TimelineId']
        else:
            self.__timeline_id = ""

        children = get_node_children(dialog[0])
        if not children:
            raise ValueError(f"'{self.__filename}' dialog doesn't have children.")
        for child_node in children:
            if child_node.get('id') == 'speakerlist':
                self.__read_speakers(get_node_children(child_node))
            if child_node.get('id') == 'nodes':
                self.__read_dialog_nodes(get_node_children(child_node))
                self.__xml_dialog_nodes = child_node.find('children')

    def __read_speakers(self, speaker_nodes: list[et.Element]) -> None:
        self.__speakers = [(None, None) for i in range(0, len(speaker_nodes))]
        for speaker_node in speaker_nodes:
            if speaker_node.get('id') != 'speaker':
                raise ValueError(f"Expected a 'speaker' node, got {speaker_node.get('id')}")
            speaker_attributes = get_node_attributes(speaker_node)
            require_attributes("Required attributes are not found in a speaker object: ", speaker_attributes, "index", "SpeakerMappingId")
            index = int(speaker_attributes["index"])
            if "list" in speaker_attributes:
                self.__speakers[index] = (speaker_attributes["list"], speaker_attributes["SpeakerMappingId"])
            else:
                self.__speakers[index] = ("", speaker_attributes["SpeakerMappingId"])

    def __read_dialog_nodes(self, dialog_nodes: list[et.Element]) -> None:
        for node in dialog_nodes:
            node_id = node.get("id")
            attributes = get_node_attributes(node)
            if node_id == "node":
                require_attributes("Required attributes are not found in a dialog node object: ", attributes, "UUID")
                self.__nodes[attributes["UUID"]] = node
            elif node_id == "RootNodes":
                require_attributes("Required attributes are not found in a dialog RootNodes object: ", attributes, "RootNodes")
                self.__root_nodes.append(attributes["RootNodes"])
