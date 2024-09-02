from __future__ import annotations

import os
import xml.etree.ElementTree as et

from typing import Optional

def translate_path(in_path: str) -> str:
    parts = in_path.replace('\\', '/').split('/')
    if ':' in parts[0]:
        parts[0] += "\\"
    return os.path.join(*parts)

def to_compact_string(xml_node: et.Element) -> str:
    return et.tostring(xml_node).decode('utf-8').replace('\t', '').replace('\n', '').replace('\r', '')

def to_pretty_string(xml_node: et.Element) -> str:
    s = et.tostring(xml_node).decode('utf-8')

def get_node_attribute(node: et.Element, attribute_name: str) -> Optional[str]:
    for attribute in node.findall('attribute'):
        name = attribute.get('id')
        if name is not None and name == attribute_name:
            t = attribute.get('type')
            if t == 'TranslatedString':
                return attribute.get('handle')
            else:
                return attribute.get('value')
    return None

def get_node_attributes(node: et.Element) -> dict[str, str]:
    result = dict[str, str]()
    for attribute in node.findall('attribute'):
        t = attribute.get('type')
        if t == 'TranslatedString':
            result[attribute.get('id')] = attribute.get('handle')
        else:
            result[attribute.get('id')] = attribute.get('value')
    return result

def remove_node_attribute(node: et.Element, attribute_id: str) -> None:
    existing = node.find(f'attribute[@id="{attribute_id}"]')
    if existing is not None:
        node.remove(existing)
    else:
        raise KeyError(f"Attribute with id '{attribute_id}' doesn't exist.")

def set_node_attribute(node: et.Element, attribute_id: str, attribute_type: str, attribute_value: str, version: Optional[str]=None) -> None:
    existing = node.find(f'attribute[@id="{attribute_id}"]')
    if existing is not None:
        node.remove(existing)
    if attribute_type == 'TranslatedString':
        val_field = 'handle'
    else:
        val_field = 'value'
    if version:
        node.append(et.fromstring(f'<attribute id="{attribute_id}" type="{attribute_type}" {val_field}="{attribute_value}" version="{version}" />'))
    else:
        node.append(et.fromstring(f'<attribute id="{attribute_id}" type="{attribute_type}" {val_field}="{attribute_value}" />'))

def update_node_attribute(node: et.Element, attribute_id: str, attribute_value: str) -> bool:
    existing = node.find(f'attribute[@id="{attribute_id}"]')
    if existing is None:
        return False
    if existing.get('value') is not None:
        existing.set('value', attribute_value)
        return True
    if existing.get('handle') is not None:
        existing.set('handle', attribute_value)
        return True
    return False


def get_node_id(node: et.Element) -> Optional[str]:
    return node.get('id')

def get_node_key(node: et.Element, default_key_name: str=None) -> Optional[str]:
    key_name = node.get('key')
    if key_name is None:
        if default_key_name is None:
            return None
        key_name = default_key_name
    node_attributes = get_node_attributes(node)
    if key_name in node_attributes:
        return node_attributes[key_name]
    return None

def get_node_children(element: et.Element, child_id: str=None, child_key: str=None) -> list[et.Element]:
    result = list[et.Element]()
    children = element.findall('children')
    if len(children) > 1:
        raise ValueError(f"Cannot read children nodes: expected 1 'children' node under the '{element.tag}' tag, got {len(children)}.")
    elif len(children) == 0:
        return result
    for node in children[0].findall('node'):
        if child_id and get_node_id(node) != child_id:
            continue
        if child_key and get_node_key(node) != child_key:
            continue
        result.append(node)
    return result

def get_node_children_as_dict(element: et.Element) -> dict[str, et.Element]:
    children = element.findall('children')
    if len(children) > 1:
        raise ValueError(f"Cannot read children nodes: expected 1 'children' node under the '{element.tag}' tag, got {len(children)}.")
    elif len(children) == 0:
        return list[et.Element]()
    children_nodes = children[0].findall('node')
    return { get_node_id(child_node): child_node for child_node in children_nodes if get_node_id(child_node) is not None }

def read_xml_value_map(map_root: et.Element, default_map_key_name: str="MapKey") -> dict[str, str]:
    result = dict[str, et.Element]()
    children_tier1 = map_root.findall('children')
    if len(children_tier1) == 0:
        return result
    if len(children_tier1) > 1:
        raise RuntimeError(f"Expected 1 'children' node, but got {len(children_tier1)}.")
    nodes_tier1 = children_tier1[0].findall('node')
    if len(nodes_tier1) == 0:
        return result
    if len(nodes_tier1) > 1:
        raise RuntimeError(f"Expected 1 'node' node, but got {len(nodes_tier1)}.")
    children_tier2 = get_node_children(nodes_tier1[0])
    for map_node in children_tier2:
        map_key = get_node_key(map_node, default_map_key_name)
        if not map_key:
            raise RuntimeError(f"Malformed map: an element has no key, {to_compact_string(map_node)}")
        if map_key in result:
            raise KeyError(f"Duplicate key: {map_key}")
        attributes = get_node_attributes(map_node)
        if 'MapValue' not in attributes:
            raise RuntimeError(f"Malformed map: an element's value is not set in attributes, {to_compact_string(map_node)}")
        map_value = attributes['MapValue']
        result[map_key] = map_value
    return result

def read_xml_object_map(map_root: et.Element, default_map_key_name: str="MapKey") -> dict[str, et.Element]:
    result = dict[str, et.Element]()
    children_tier1 = map_root.findall('children')
    if len(children_tier1) == 0:
        return result
    if len(children_tier1) > 1:
        raise RuntimeError(f"Expected 1 'children' node, but got {len(children_tier1)}.")
    nodes_tier1 = children_tier1[0].findall('node')
    if len(nodes_tier1) == 0:
        return result
    if len(nodes_tier1) > 1:
        raise RuntimeError(f"Expected 1 'node' node, but got {len(nodes_tier1)}.")
    children_tier2 = get_node_children(nodes_tier1[0])
    for map_node in children_tier2:
        map_key = get_node_key(map_node, default_map_key_name)
        if not map_key:
            raise RuntimeError(f"Malformed map: an element has no key, {to_compact_string(map_node)}")
        if map_key in result:
            raise KeyError(f"Duplicate key: {map_key}")
        children_tier3 = get_node_children(map_node)
        if len(children_tier3) != 1:
            raise RuntimeError(f"Malformed map: expected 1 child per map node, got {len(children_tier3)}, {to_compact_string(map_node)}")
        map_value = children_tier3[0]
        result[map_key] = map_value
    return result

def find_xml_node(parent: et.Element, path: str) -> Optional[et.Element]:
    t = find_xml_node_and_parent(parent, path)
    if t is None:
        return None
    return t[0]

def add_xml_node(element: et.Element, child_element: et.Element) -> None:
    children_node = element.findall('children')
    if len(children_node) > 1:
        raise ValueError(f"Expected 1 'children' node, but got {len(children_node)}")
    if len(children_node) == 0:
        parent_node = et.fromstring("<children></children>")
        element.append(parent_node)
    else:
        parent_node = children_node[0]
    parent_node.append(child_element)

def remove_xml_node(parent: et.Element, path: str) -> None:
    t = find_xml_node_and_parent(parent, path)
    if t is None:
        raise ValueError(f"Path '{path}' doesn't resolve to a node.")
    children_node = t[1].findall('children')
    if len(children_node) != 1:
        raise ValueError(f"Expected 1 'children' node, got {len(children_node)}")
    children_node[0].remove(t[0])

def replace_xml_node(parent: et.Element, path: str, new_node: et.Element) -> None:
    t = find_xml_node_and_parent(parent, path)
    if t is None:
        raise ValueError(f"Path '{path}' doesn't resolve to a node.")
    children_node = t[1].findall('children')
    if len(children_node) != 1:
        raise ValueError(f"Expected 1 'children' node, got {len(children_node)}")
    children_node[0].remove(t[0])
    children_node[0].append(new_node)

def find_xml_node_and_parent(parent: et.Element, path: str) -> Optional[tuple[et.Element, et.Element]]:
    #print()
    #print(f"find_xml_node_and_parent path {path}")
    n = 0
    elt = parent
    while n < len(path):
        m = path.find('->', n)
        if m == -1:
            m = len(path)
        token = path[n : m].strip()
        if m < len(path):
            m += 2
        k = token.find('@')
        key = ""
        index = -1
        if k != -1:
            key = token[k + 1 : ]
            token = token[ : k]
        else:
            k = token.find('#')
            if k != -1:
                index = int(token[k + 1 : ])
                token = token[ : k]
        children = get_node_children(elt)
        chosen = None
        #print(f"n = {n}, m  = {m}, token = {token}, key = {key}, len(children) = {len(children)}")
        if key:
            #print("by key")
            for child in children:
                child_id = child.get('id')
                #print(f"child_id = {child_id}")
                if token != child_id:
                    continue
                key_attribute = child.get('key')
                #print(f"key_attribute = {key_attribute}")
                if key_attribute is None:
                    continue
                attributes = get_node_attributes(child)
                if key_attribute not in attributes:
                    continue
                key_value = attributes[key_attribute]
                #print(f"key_value = {key_value}")
                if key == key_value:
                    if chosen is None:
                        #print("chosen set")
                        chosen = child
                    else:
                        raise RuntimeError(f"Multiple nodes fit the same key '{key}'")
        elif index >= 0:
            #print("by index")
            if index < len(children):
                chosen = children[index]
        elif len(children) > 1:
            #print("len(children) > 1")
            matching_nodes = list[tuple[et.Element, et.Element]]()
            sub_path = path[m : ]
            #print(f"sub_path = {sub_path}")
            for child in children:
                child_id = child.get('id')
                if token != child_id:
                    continue
                #print(f"child_id = {child_id}")
                if sub_path:
                    maybe_node = find_xml_node_and_parent(child, sub_path)
                    #print(f"maybe_node = {maybe_node}")
                    if maybe_node:
                        #print(f"found a matching child by subpath {sub_path}")
                        matching_nodes.append(maybe_node)
                    #else:
                        #print(f"no matching child by subpath {sub_path}")
                else:
                    #print("sub_path is empty, current child match")
                    matching_nodes.append((child, elt))
            #print(f"got {len(matching_nodes)} matches among children of the node, path {path}")
            if len(matching_nodes) == 1:
                #print(f"returning matched node {matching_nodes[0]}")
                return matching_nodes[0]
            if len(matching_nodes) == 0:
                return None
            raise RuntimeError(f"Multiple nodes match the same path '{path}'")
        elif len(children) == 1:
            #print("len(children) == 1")
            child_id = children[0].get('id')
            #print(f"child_id = {child_id}")
            if token == child_id:
                #print("chosen set")
                chosen = children[0]
        else:
            #print("no children, None")
            return None
        if chosen:
            parent = elt
            elt = chosen
            chosen = None
            n = m
        else:
            return None
    return elt, parent

def require_attributes(message: str, attributes: dict[str, str], *args: str) -> None:
    missing_required_attributes = list[str]()
    for required_attribute in args:
        if required_attribute not in attributes:
            missing_required_attributes.append(required_attribute)
    if missing_required_attributes:
        message += ", ".join(missing_required_attributes)
        raise KeyError(message)

def create_bool_flag_node(flag_uuid: str, value: bool, paramval: Optional[int]=None) -> et.Element:
    param_str = f"""<attribute id="paramval" type="int32" value="{paramval}" />""" if paramval is not None else ""
    flag_str =  f"""<node id="flag" key="UUID"><attribute id="UUID" type="FixedString" value="{flag_uuid}" /><attribute id="value" type="bool" value="{value}" />{param_str}</node>"""
    return et.fromstring(flag_str)

def create_flag_group(group_type: str, flags: tuple[tuple[str, bool, Optional[int]], ...]) -> et.Element:
    result = et.fromstring(f"""<node id="flaggroup" key="type"><attribute id="type" type="FixedString" value="{group_type}" /><children></children></node>""")
    for flag_uuid, flag_value, flag_paramval in flags:
        flag_node = create_bool_flag_node(flag_uuid, flag_value, paramval=flag_paramval)
        add_xml_node(result, flag_node)
    return result

def create_xml_node_with_children(node_id: str, children: tuple[et.Element, ...]) -> None:
    result = et.fromstring(f'<node id="{node_id}"><children></children></node>')
    for child in children:
        add_xml_node(result, child)
    return result

def create_dice_roll_dialog_node(
        node_uuid: str,
        speaker_slot: int,
        ability: str,
        skill: str,
        dc_uuid: str,
        success_node_uuid: str,
        failure_node_uuid: str,
        text_handle: str,
        text_version: str,
        line_id: str,
        tags: list[et.Element]=[],
        setflags: list[et.Element]=[],
        checkflags: list[et.Element]=[],
        roll_type: str='ActiveRoll'
) -> et.Element:
    result = et.fromstring(f"""
<node id="node" key="UUID">
    <attribute id="constructor" type="FixedString" value="{roll_type}" />
    <attribute id="UUID" type="FixedString" value="{node_uuid}" />
    <attribute id="ShowOnce" type="bool" value="True" />
    <attribute id="transitionmode" type="uint8" value="2" />
    <attribute id="speaker" type="int32" value="{speaker_slot}" />
    <attribute id="RollType" type="string" value="SkillCheck" />
    <attribute id="Ability" type="string" value="{ability}" />
    <attribute id="Skill" type="string" value="{skill}" />
    <attribute id="RollTargetSpeaker" type="int32" value="1" />
    <attribute id="Advantage" type="uint8" value="0" />
    <attribute id="ExcludeCompanionsOptionalBonuses" type="bool" value="False" />
    <attribute id="ExcludeSpeakerOptionalBonuses" type="bool" value="False" />
    <attribute id="DifficultyClassID" type="guid" value="{dc_uuid}" />
    <children>
        <node id="children">
            <children>
                <node id="child">
                    <attribute id="UUID" type="FixedString" value="{success_node_uuid}" />
                </node>
                <node id="child">
                    <attribute id="UUID" type="FixedString" value="{failure_node_uuid}" />
                </node>
            </children>
        </node>
        <node id="GameData">
            <children>
                <node id="AiPersonalities" key="AiPersonality" />
                <node id="MusicInstrumentSounds" />
                <node id="OriginSound" />
            </children>
        </node>
        <node id="Tags" />
        <node id="setflags" />
        <node id="checkflags" />
        <node id="TaggedTexts">
            <children>
                <node id="TaggedText">
                    <attribute id="HasTagRule" type="bool" value="True" />
                    <children>
                        <node id="TagTexts">
                            <children>
                                <node id="TagText">
                                    <attribute id="TagText" type="TranslatedString" handle="{text_handle}" version="{text_version}" />
                                    <attribute id="LineId" type="guid" value="{line_id}" />
                                    <attribute id="stub" type="bool" value="True" />
                                </node>
                            </children>
                        </node>
                        <node id="RuleGroup">
                            <attribute id="TagCombineOp" type="uint8" value="0" />
                            <children>
                                <node id="Rules" />
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
        <node id="ValidatedFlags">
            <attribute id="ValidatedHasValue" type="bool" value="False" />
        </node>
    </children>
</node>""")
    tags_node = result.find("children/node[@id='Tags']")
    for tag_node in tags:
        add_xml_node(tags_node, tag_node)
    setflags_node = result.find("children/node[@id='setflags']")
    for flaggroup_node in setflags:
        add_xml_node(setflags_node, flaggroup_node)
    checkflags_node = result.find("children/node[@id='checkflags']")
    for flaggroup_node in checkflags:
        add_xml_node(checkflags_node, flaggroup_node)
    return result

def create_dice_roll_result_node(node_uuid: str, success_node: bool, target_node_uuid: str) -> et.Element:
    return et.fromstring(f"""<node id="node" key="UUID"><attribute id="constructor" type="FixedString" value="RollResult" />
    <attribute id="UUID" type="FixedString" value="{node_uuid}" /><attribute id="Success" type="bool" value="{success_node}" />
    <children><node id="children"><children><node id="child"><attribute id="UUID" type="FixedString" value="{target_node_uuid}" />
    </node></children></node><node id="Tags" /><node id="setflags" /><node id="checkflags" /></children></node>""")

def create_standard_dialog_node(
        node_uuid: str,
        speaker_slot: int,
        children_uuids: list[str],
        text_handle: str,
        text_version: str,
        line_id: str,
        tags: list[et.Element]=[],
        setflags: list[et.Element]=[],
        checkflags: list[et.Element]=[],
        constructor: str="TagAnswer",
        group_id: str="",
        group_index: int=0,
        approval_rating_uuid: str="",
        end_node: bool=False,
        show_once: bool=False
) -> et.Element:
    end_node_str = '<attribute id="endnode" type="bool" value="True" />' if end_node else ""
    show_once_str = '<attribute id="ShowOnce" type="bool" value="True" />' if show_once else ""
    approval_rating_str = f'<attribute id="ApprovalRatingID" type="guid" value="{approval_rating_uuid}" />' if approval_rating_uuid else ""
    if group_id:
        group_id_str = f"""<attribute id="GroupID" type="FixedString" value="{group_id}" />
<attribute id="GroupIndex" type="int32" value="{group_index}" />"""
    else:
        group_id_str = ""
    if text_handle:
        tagged_texts = f"""
        <node id="TaggedTexts">
            <children>
                <node id="TaggedText">
                    <attribute id="HasTagRule" type="bool" value="True" />
                    <children>
                        <node id="TagTexts">
                            <children>
                                <node id="TagText">
                                    <attribute id="TagText" type="TranslatedString" handle="{text_handle}" version="{text_version}" />
                                    <attribute id="LineId" type="guid" value="{line_id}" />
                                    <attribute id="stub" type="bool" value="True" />
                                </node>
                            </children>
                        </node>
                        <node id="RuleGroup">
                            <attribute id="TagCombineOp" type="uint8" value="0" />
                            <children>
                                <node id="Rules" />
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
"""
    else:
        tagged_texts = '<node id="TaggedTexts" />'

    result = et.fromstring(f"""
<node id="node" key="UUID">
    <attribute id="constructor" type="FixedString" value="{constructor}" />
    <attribute id="UUID" type="FixedString" value="{node_uuid}" />
    <attribute id="speaker" type="int32" value="{speaker_slot}" />
    {group_id_str}
    {approval_rating_str}
    {end_node_str}
    {show_once_str}
    <children>
        <node id="children" />
        <node id="GameData">
            <children>
                <node id="AiPersonalities" key="AiPersonality" />
                <node id="MusicInstrumentSounds" />
                <node id="OriginSound" />
            </children>
        </node>
        <node id="Tags" />
        <node id="setflags" />
        <node id="checkflags" />
        {tagged_texts}
        <node id="ValidatedFlags">
            <attribute id="ValidatedHasValue" type="bool" value="False" />
        </node>
    </children>
</node>""")
    children_node = result.find("children/node[@id='children']")
    for child_uuid in children_uuids:
        child_node = et.fromstring(f'<node id="child"><attribute id="UUID" type="FixedString" value="{child_uuid}" /></node>')
        add_xml_node(children_node, child_node)
    tags_node = result.find("children/node[@id='Tags']")
    for tag_node in tags:
        add_xml_node(tags_node, tag_node)
    setflags_node = result.find("children/node[@id='setflags']")
    for flaggroup_node in setflags:
        add_xml_node(setflags_node, flaggroup_node)
    checkflags_node = result.find("children/node[@id='checkflags']")
    for flaggroup_node in checkflags:
        add_xml_node(checkflags_node, flaggroup_node)
    return result

def create_nested_dialog_node(
        node_uuid: str,
        nested_dialog_uuid: str,
        speaker_linking: list[int] = [0, 1, 2, 3, 4, 5, 6],
        end_node: bool = False
) -> et.Element:
    end_node_str = '<attribute id="endnode" type="bool" value="True" />' if end_node else ""
    speaker_linking_entries = list[str]()
    for index in range(0, len(speaker_linking)):
        value = speaker_linking[index]
        speaker_linking_entries.append(f'<node id="SpeakerLinkingEntry"><attribute id="Key" type="int32" value="{index}" /><attribute id="Value" type="int32" value="{value}" /></node>')
    return et.fromstring(f"""
<node id="node" key="UUID">
    <attribute id="constructor" type="FixedString" value="Nested Dialog" />
    <attribute id="UUID" type="FixedString" value="{node_uuid}" />
    <attribute id="NestedDialogNodeUUID" type="guid" value="{nested_dialog_uuid}" />
    {end_node_str}
    <children>
        <node id="children" />
        <node id="Tags" />
        <node id="setflags" />
        <node id="checkflags" />
        <node id="SpeakerLinking">
            <children>{"".join(speaker_linking_entries)}</children>
        </node>
    </children>
</node>""")

def create_jump_dialog_node(
        node_uuid: str,
        target_node_uuid: str,
        target_point: int = 2
) -> et.Element:
    return et.fromstring(f"""
<node id="node" key="UUID">
    <attribute id="constructor" type="FixedString" value="Jump" />
    <attribute id="UUID" type="FixedString" value="{node_uuid}" />
    <attribute id="jumptarget" type="FixedString" value="{target_node_uuid}" />
    <attribute id="jumptargetpoint" type="uint8" value="{target_point}" />
    <children>
        <node id="children" />
        <node id="Tags" />
        <node id="setflags" />
        <node id="checkflags" />
    </children>
</node>""")

def get_time_range_of_effect_components(effect_components: et.Element) -> tuple[float, float]:
    start_time = 1000000000.0
    end_time = 0.0
    for effect_component in effect_components:
        attributes = get_node_attributes(effect_component)
        effect_component_start_time = float(attributes['StartTime']) if 'StartTime' in attributes else 0.0
        effect_component_end_time = float(attributes['EndTime'])
        if effect_component_start_time < start_time:
            start_time = effect_component_start_time
        if effect_component_end_time > end_time:
            end_time = effect_component_end_time
    return start_time, end_time

def create_flag_lsf_lsx(
        mod_path: str,
        flag_uuid: str,
        flag_name: str,
        flag_usage: int,
        flag_description: str,
        lslib_meta: str='v1,bswap_guids,lsf_keys_adjacency'
) -> str:
    xml = f"""<?xml version="1.0" encoding="utf-8"?>
<save>
    <version major="4" minor="0" revision="8" build="3" lslib_meta="{lslib_meta}" />
    <region id="Flags">
        <node id="Flags">
            <attribute id="Description" type="LSString" value="{flag_description}" />
            <attribute id="Name" type="FixedString" value="{flag_name}" />
            <attribute id="UUID" type="guid" value="{flag_uuid}" />
            <attribute id="Usage" type="uint8" value="{flag_usage}" />
        </node>
    </region>
</save>"""
    filename = flag_uuid + '.lsf.lsx'
    dir_path = os.path.join(mod_path, 'Public', 'GustavDev', 'Flags')
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, filename)
    with open(file_path, "wt") as f:
        f.write(xml)
    return file_path

def create_approval_rating(mod_path: str, approval_uuid: str, ratings: dict[str, int], scope: int=1) -> str:
    children = list[str]()
    for key, value in ratings.items():
        children.append(f'<node id="Reaction"><attribute id="id" type="guid" value="{key}"/><attribute id="value" type="int32" value="{value}"/></node>')
    children_nodes = "\n".join(children)
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<save>
    <version major="4" minor="0" revision="9" build="320"/>
    <region id="Reactions">
        <node id="root">
            <children>
                <node id="Reaction">
                    <attribute id="Scope" type="uint8" value="{scope}"/>
                    <attribute id="UUID" type="guid" value="{approval_uuid}"/>
                    <children>
                        <node id="Reactions">
                            <children>
                            {children_nodes}
                            </children>
                        </node>
                    </children>
                </node>
            </children>
        </node>
    </region>
</save>"""
    filename = approval_uuid + '.lsf.lsx'
    dir_path = os.path.join(mod_path, 'Public', 'GustavDev', 'ApprovalRatings', 'Reactions')
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    file_path = os.path.join(dir_path, filename)
    with open(file_path, "wt") as f:
        f.write(xml)
    return file_path
    
