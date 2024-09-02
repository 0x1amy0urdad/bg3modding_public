from __future__ import annotations

import os
import uuid
import xml.etree.ElementTree as et

from typing import Optional

from ._common import (
    get_node_children,
    get_node_attribute,
    get_node_attributes,
    read_xml_object_map,
    read_xml_value_map,
    to_compact_string,
    translate_path
)

class bg3_game_object_dialog_timeline:
    __filename: str
    __xml: et.ElementTree

    # TimelineContent region
    __timeline_content: dict[str, et.Element]
    __phases: dict[str, et.Element]
    __effect_components: dict[str, et.Element]
    __timeline_speakers: dict[str, str]
    __timeline_actor_data: dict[str, et.Element]
    __timeline_phases: dict[str, str]
    __peanut_slots: tuple[str, ...]
    __timeline_settings: Optional[et.Element]

    # EnterPhaseSoundEvents region
    __enter_phase_sound_events: dict[str, et.Element]

    # ExitPhaseSoundEvents region
    __exit_phase_sound_events: dict[str, et.Element]

    # EnterSoundEvents region
    __enter_sound_events: Optional[et.Element]

    # ExitSoundEvents region
    __exit_sound_events: Optional[et.Element]


    def __init__(self, lsx_file_path: str) -> None:
        if not lsx_file_path.endswith(".lsx"):
            raise ValueError(f"Unexpected file: {lsx_file_path}")
        if not os.path.isfile(lsx_file_path):
            raise FileNotFoundError(f"File '{lsx_file_path}' doesn't exist")
        self.__filename = lsx_file_path
        self.__xml = et.parse(lsx_file_path)
        self.__timeline_content = dict[str, et.Element]()
        self.__phases = dict[str, et.Element]()
        self.__effect_components = dict[str, et.Element]()
        self.__timeline_speakers = dict[str, str]()
        self.__timeline_actor_data = dict[str, et.Element]()
        self.__timeline_phases = dict[str, str]()
        self.__peanut_slots = tuple[str, ...]()
        self.__timeline_settings = None
        self.__enter_phase_sound_events = dict[str, et.Element]()
        self.__exit_phase_sound_events = dict[str, et.Element]()
        self.__enter_sound_events = None
        self.__exit_sound_events = None
        self.__init_timeline()

    def get_timeline_content(self, name: str) -> et.Element:
        if name not in self.__timeline_content:
            raise KeyError(f"{name} is not found in the timeline")
        return self.__timeline_content[name]

    @property
    def xml(self) -> et.ElementTree:
        return self.__xml

    @property
    def phases(self) -> tuple[et.Element, ...]:
        return tuple(self.__phases.values())

    @property
    def all_effect_components(self) -> tuple[et.Element, ...]:
        return tuple(self.__effect_components.values())

    def get_phase_by_dialog_node_uuid(self, dialog_node_uuid: str) -> et.Element:
        if dialog_node_uuid in self.__phases:
            return self.__phases[dialog_node_uuid]
        raise KeyError(f"Phase not found for dialog node uuid {dialog_node_uuid}")

    def get_effect_component(self, id: str) -> et.Element:
        if id not in self.__effect_components:
            raise KeyError(f"Effect component '{id}' doesn't exists in the timeline.")
        return self.__effect_components[id]

    def select_effect_components(
            self,
            phase_index: Optional[int]=None,
            dialog_node_uuid: Optional[str]=None,
            type_filter: Optional[list[str]]=None,
            contained_instant: Optional[float]=None,
            time_period_begin: Optional[float]=None,
            time_period_end: Optional[float]=None,
            mandatory_phase_index: bool=True,
            mandatory_dialog_node_uuid: bool=False
    ) -> list[et.Element]:
        result = list[et.Element]()
        start_time = 1000000000.0
        end_time = 0.0
        if type_filter:
            type_filter_set = frozenset(type_filter)
        else:
            type_filter_set = None
        for effect_component in self.__effect_components.values():
            attributes = get_node_attributes(effect_component)
            if phase_index:
                if mandatory_phase_index and 'PhaseIndex' not in attributes:
                    continue
                if 'PhaseIndex' not in attributes and attributes['PhaseIndex'] != phase_index:
                    continue
            if dialog_node_uuid:
                if mandatory_dialog_node_uuid and 'DialogNodeId' not in attributes:
                    continue
                if 'DialogNodeId' in attributes and attributes['DialogNodeId'] != dialog_node_uuid:
                    continue
            if type_filter_set and 'Type' in attributes and attributes['Type'] not in type_filter_set:
                continue
            if contained_instant and 'EndTime' in attributes:
                start_time = float(attributes['StartTime']) if 'StartTime' in attributes else 0.0
                end_time = float(attributes['EndTime'])
                if contained_instant < start_time or contained_instant > end_time:
                    continue
            if time_period_begin and 'StartTime' in attributes:
                start_time = float(attributes['StartTime'])
                if start_time < time_period_begin:
                    continue
            if time_period_end and 'EndTime' in attributes:
                end_time = float(attributes['EndTime'])
                if end_time > time_period_end:
                    continue
            result.append(effect_component)
        return result

    def get_timeline_speaker(self, speaker_index: int) -> str:
        key = str(speaker_index)
        if key not in self.__timeline_speakers:
            raise KeyError(f"Speaker {key} is not found in TimelineSpeakers.")
        return self.__timeline_speakers[key]

    def get_timeline_actor_data(self, node_uuid: str) -> et.Element:
        if node_uuid not in self.__timeline_actor_data:
            raise KeyError(f"Actor data {node_uuid} is not found in TimelineActorData")
        return self.__timeline_actor_data[node_uuid]

    def get_timeline_actors(self, actor_type_id: str) -> dict[str, et.Element]:
        result = dict[str, et.Element]()
        for actor_uuid, actor_data in self.__timeline_actor_data.items():
            attributes = get_node_attributes(actor_data)
            if 'ActorTypeId' in attributes and attributes['ActorTypeId'] == actor_type_id:
                result[actor_uuid] = actor_data
        return result

    def get_timeline_cameras(self) -> dict[str, et.Element]:
        return self.get_timeline_actors('scenecam')

    def get_timeline_characters(self) -> dict[str, et.Element]:
        return self.get_timeline_actors('character')

    def get_timeline_peanuts(self) -> dict[str, et.Element]:
        return self.get_timeline_actors('peanut')

    def get_timeline_phase_index(self, dialog_node_uuid: str) -> int:
        if dialog_node_uuid not in self.__timeline_phases:
            raise KeyError(f"A phase for the dialog node {dialog_node_uuid} is not found in TimelinePhases")
        return int(self.__timeline_phases[dialog_node_uuid])

    def get_peanut_slots(self) -> tuple[str, ...]:
        return self.__peanut_slots

    def get_timeline_duration(self) -> float:
        last_phase_index = 0
        for _, index in self.__timeline_phases.items():
            n = int(index)
            if last_phase_index < n:
                last_phase_index = n
        last_phase_effect_components = self.select_effect_components(phase_index=last_phase_index)
        duration = 0.0
        for effect_component in last_phase_effect_components:
            end_time = get_node_attribute(effect_component, 'EndTime')
            if end_time and float(end_time) > duration:
                duration = float(end_time)
        return duration

    def get_timeline_settings(self) -> et.Element:
        if not self.__timeline_settings:
            raise ValueError("Timeline settings do not exist.")
        return self.__timeline_settings

    def get_enter_phase_sound_event(self, event_id: str) -> et.Element:
        if event_id not in self.__enter_phase_sound_events:
            raise KeyError(f"Sound event {event_id} is not found in EnterPhaseSoundEvents")
        return self.__enter_phase_sound_events[event_id]

    def get_exit_phase_sound_event(self, event_id: str) -> et.Element:
        if event_id not in self.__exit_phase_sound_events:
            raise KeyError(f"Sound event {event_id} is not found in ExitPhaseSoundEvents")
        return self.__exit_phase_sound_events[event_id]

    def get_enter_sound_events(self) -> et.Element:
        if self.__enter_sound_events is None:
            raise ValueError("EnterSoundEvents do not exists")
        return self.__enter_sound_events

    def get_exit_sound_events(self) -> et.Element:
        if self.__exit_sound_events is None:
            raise ValueError("ExitSoundEvents do not exists")
        return self.__exit_sound_events

    def create_peanut_slots_mapping(self, target_timeline: bg3_game_object_dialog_timeline) -> dict[str, str]:
        peanuts_mapping = dict[str, str]()
        p1 = 0
        p2 = 0
        src_peanuts = self.get_peanut_slots()
        dest_peanuts = target_timeline.get_peanut_slots()
        while p1 < len(src_peanuts):
            peanuts_mapping[src_peanuts[p1]] = dest_peanuts[p2]
            p1 += 1
            p2 += 1
            if p2 == len(dest_peanuts):
                p2 = 0
        return peanuts_mapping

    def add_new_phase(self, dialog_node_uuid: str, duration: float, play_count: int, reference_id: str="") -> int:
        new_phase = et.fromstring(f"""<node id="Phase">
            <attribute id="Duration" type="float" value="{duration}" />
            <attribute id="PlayCount" type="int32" value="{play_count}" />
            <attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />
            <children><node id="QuestionHoldAutomation" /></children></node>""")
        xpath = "./region/node[@id='TimelineContent']/children/node[@id='Effect']/children/node[@id='Phases']/children"
        phases_children_node = self.__xml.findall(xpath)
        if len(phases_children_node) == 1:
            phases_children_node[0].append(new_phase)
        else:
            raise RuntimeError(f"Expected 1 node, but got {len(phases_children_node)}, {xpath}")
        phase_index = len(phases_children_node[0]) - 1

        if not reference_id:
            reference_id = dialog_node_uuid
        new_timeline_phase = et.fromstring(f"""<node id="Object" key="MapKey">
            <attribute id="MapKey" type="guid" value="{reference_id}" />
            <attribute id="MapValue" type="uint64" value="{phase_index}" /></node>""")
        xpath = "./region/node[@id='TimelineContent']/children/node[@id='TimelinePhases']/children/node[@id='Object']/children"
        timeline_phases_children_node = self.__xml.findall(xpath)
        if len(timeline_phases_children_node) == 1:
            timeline_phases_children_node[0].append(new_timeline_phase)
        else:
            raise RuntimeError(f"Expected 1 node, but got {len(timeline_phases_children_node)}, {xpath}")
        return phase_index

    def add_new_effect_component(self, effect_component: et.Element) -> None:
        children_node = self.__xml.find("./region/node[@id='TimelineContent']/children/node[@id='Effect']/children/node[@id='EffectComponents']/children")
        children_node.append(effect_component)

    def add_effect_components_from_template(self, template_path, args) -> None:
        lines = list[str]()
        with open(translate_path(template_path), "rt") as f:
            for line in f:
                line = line.strip()
                pos_start = line.find('$')
                add_val = None
                sub_val = None
                if pos_start >= 0:
                    pos_end = line.find('$', pos_start + 1)
                    pos_plus = line.find('+', pos_start + 1)
                    pos_minus = line.find('-', pos_start + 1)
                    if pos_plus == -1 and pos_minus == -1:
                        key = line[pos_start + 1: pos_end]
                    elif pos_plus >= 0:
                        key = line[pos_start + 1: pos_plus]
                        add_val = float(line[pos_plus + 1: pos_end].strip())
                    elif pos_minus >= 0:
                        key = line[pos_start + 1: pos_minus]
                        sub_val = float(line[pos_minus + 1: pos_end].strip())
                    if key == 'uuid':
                        val = str(uuid.uuid4())
                    else:
                        val = args[key]
                    if add_val is not None:
                        val += add_val
                    elif sub_val is not None:
                        val -= sub_val
                    line = line[0: pos_start] + str(val) + line[pos_end + 1:]
                lines.append(line)
        xml = "".join(lines)
        template = et.fromstring(xml)
        append_target = self.__xml.find("./region/node[@id='TimelineContent']/children/node[@id='Effect']/children/node[@id='EffectComponents']/children")
        for node in template:
            append_target.append(node)

    def find_effect_component(self, uuid: str) -> Optional[et.Element]:
        effect_components = self.xml.findall("region[@id='TimelineContent']/node[@id='TimelineContent']/children/node[@id='Effect']/children/node[@id='EffectComponents']/children/node[@id='EffectComponent']")
        for effect_component in effect_components:
            if get_node_attribute(effect_component, "ID") == '98020265-3ead-4cc4-9c99-3ff011567e38':
                return effect_component
        return None


    def update_timeline_duration(self) -> None:
        effect_components = self.__xml.findall("./region/node[@id='TimelineContent']/children/node[@id='Effect']/children/node[@id='EffectComponents']/children/node[@id='EffectComponent']")
        duration = 0.0
        for effect_component in effect_components:
            d = float(get_node_attribute(effect_component, 'EndTime'))
            if d > duration:
                duration = d
        duration_attribute = self.__xml.getroot().find("region/node[@id='TimelineContent']/children/node[@id='Effect']/attribute[@id='Duration']")
        duration_attribute.set('value', str(duration))

    def save_to(self, dest_file_path: str) -> str:
        self.update_timeline_duration()
        dest_file_path = translate_path(dest_file_path)
        dir_path = os.path.dirname(dest_file_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path)
        self.__xml.write(dest_file_path, encoding="utf-8", xml_declaration=True)
        return dest_file_path

    def __init_timeline(self) -> None:
        root = self.__xml.getroot()
        if not isinstance(root, et.Element):
            raise ValueError(f"'{self.__filename}' doesn't contain a timeline: the root node isn't an XML element.")
        if root.tag != 'save':
            raise ValueError(f"'{self.__filename}' doesn't contain a timeline: the root node isn't 'save'.")
        regions = root.findall('region')
        read_regions = set[str]()
        for region in regions:
            region_id = region.get('id')
            if region_id is None:
                continue
            if region_id == 'TimelineContent':
                if region_id in read_regions:
                    raise ValueError("Unexpected: multiple 'TimelineContent' regions")
                self.__read_timeline_content_region(region)
                read_regions.add(region_id)

    def __read_timeline_content_region(self, region: et.Element) -> None:
        nodes = region.findall("node[@id='TimelineContent']")
        if len(nodes) != 1:
            raise RuntimeError(f"Expected 1 'TimelineContent' node, but got {len(nodes)}")
        for child in get_node_children(nodes[0]):
            child_id = child.get('id')
            if child_id is None:
                raise ValueError("Unexpected: a node without id in 'TimelineContent' region.")
            if child_id in self.__timeline_content:
                raise KeyError(f"Unexpected: at least two nodes with duplicate identifiers: {id}")
            self.__timeline_content[child_id] = child
            if child.get('id') == 'Effect':
                for effect_child in get_node_children(child):
                    if effect_child.get('id') == 'Phases':
                        phases = get_node_children(effect_child)
                        for phase in phases:
                            phase_attributes = get_node_attributes(phase)
                            if 'DialogNodeId' in phase_attributes:
                                dialog_node_id = phase_attributes['DialogNodeId']
                                self.__phases[dialog_node_id] = phase
                    elif effect_child.get('id') == 'EffectComponents':
                        effect_components = get_node_children(effect_child)
                        for effect_component in effect_components:
                            attributes = get_node_attributes(effect_component)
                            effect_id = attributes['ID']
                            if effect_id:
                                self.__effect_components[effect_id] = effect_component
            elif child_id == 'TimelineSpeakers':
                try:
                    self.__timeline_speakers = read_xml_value_map(child)
                except:
                    self.__timeline_speakers = dict[str, str]()
            elif child_id == 'TimelineActorData':
                self.__timeline_actor_data = read_xml_object_map(child)
            elif child_id == 'TimelinePhases':
                self.__timeline_phases = read_xml_value_map(child)
            elif child_id == 'PeanutSlotIdMap':
                self.__peanut_slots = self.__read_peanut_slots(child)
            elif child_id == 'TimelineSettings':
                self.__timeline_settings = child

    @staticmethod
    def __read_peanut_slots(node: et.Element) -> tuple[str, ...]:
        child_nodes = node.findall('children/node/children/node')
        if len(child_nodes) == 0:
            return tuple[str, ...]()
        result = ["" for i in range(0, len(child_nodes))]
        for child_node in child_nodes:
            attributes = get_node_attributes(child_node)
            if 'MapKey' not in attributes or 'MapValue' not in attributes:
                raise ValueError("Required attributes are not present in a child node of a peanut slot map: " + to_compact_string(child_node))
            index = int(attributes['MapValue'])
            if index >= len(result):
                raise IndexError(f"Index {index} is equal or greater to the number of peanut slots {len(result)}")
            result[index] = attributes['MapKey']
        return tuple[str, ...](result)

    def __read_enter_phase_sound_events(self, region: et.Element) -> None:
        nodes = region.findall("node[@id='EnterPhaseSoundEvents']")
        if len(nodes) != 1:
            raise RuntimeError(f"Expected 1 'EnterPhaseSoundEvents' node, but got {len(nodes)}")
        for child in get_node_children(nodes[0]):
            child_id = child.get('id')
            if child_id is None:
                raise ValueError("Unexpected: a node without id in 'EnterPhaseSoundEvents' region.")
            if child_id == 'SoundEventMap':
                self.__enter_phase_sound_events = read_xml_value_map(child)

