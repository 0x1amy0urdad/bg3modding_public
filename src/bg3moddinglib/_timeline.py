from __future__ import annotations

import xml.etree.ElementTree as et

from ._common import get_bg3_attribute, get_required_bg3_attribute, new_random_uuid, set_bg3_attribute, to_compact_string
from ._constants import PEANUT_SLOT_0, PEANUT_SLOT_1, PEANUT_SLOT_2, PEANUTS
from ._dialog import dialog_object
from ._files import game_file

from typing import Iterable

class timeline_phase:
    __index: int
    __dialog_node_uuid: str
    __reference_id: str
    __start: float
    __end: float

    def __init__(self, index: int, dialog_node_uuid: str, reference_id: str, start: float, end: float) -> None:
        self.__index = index
        self.__dialog_node_uuid = dialog_node_uuid
        self.__reference_id = reference_id
        self.__start = start
        self.__end = end

    @property
    def index(self) -> int:
        return self.__index

    @property
    def dialog_node_uuid(self) -> str:
        return self.__dialog_node_uuid

    @property
    def reference_id(self) -> str:
        return self.__reference_id

    @property
    def start(self) -> float:
        return self.__start

    @property
    def end(self) -> float:
        return self.__end

    @property
    def duration(self) -> float:
        return self.__end - self.__start

class timeline_object:
    TIMELINE_PRECISION = 4

    ACTOR_CHARACTER = 'character'
    ACTOR_PEANUT = 'peanut'
    ACTOR_NARRATOR = 'narrator'
    ACTOR_CAMERA = 'scenecam'
    ACTOR_LIGHT = 'scenelight'
    ACTOR_EFFECT = 'effect'

    ATTITUDE = 'TLAttitudeEvent'
    EMOTION = 'TLEmotionEvent'
    LOOK_AT = 'TLLookAtEvent'
    SOUND = 'TLSoundEvent'
    SHOW_VISUAL = 'TLShowVisual'
    SHOW_WEAPON = 'TLShowWeapon'
    HANDS_IK = 'TLHandsIK'
    PHYSICS = 'TLPhysics'

    VALID_ACTOR_NODES = frozenset([ATTITUDE, EMOTION, LOOK_AT, SOUND, SHOW_VISUAL, SHOW_WEAPON, HANDS_IK, PHYSICS])

    SWITCH_STAGE = 'TLSwitchStageEvent'
    SWITCH_LOCATION = 'TLSwitchLocationEvent'
    SHOW_PEANUTS = 'TLShowPeanuts'

    VALID_NON_ACTOR_NODES = frozenset([SWITCH_STAGE, SWITCH_LOCATION, SHOW_PEANUTS])

    SHOW_ARMOR = 'TLShowArmor'

    __file: game_file
    __dialog: dialog_object
    __effect_components_parent_node: et.Element
    __duration: float
    __phases_start_times: list[float]
    __phases_durations: list[float]
    __current_phase_start_time: float | None
    __current_phase_index: int | None
    __peanuts_uuids: list[str]

    def __init__(self, gamefile: game_file, dialog: dialog_object) -> None:
        self.__file = gamefile
        self.__dialog = dialog
        node = gamefile.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="EffectComponents"]/children')
        if node is None:
            raise RuntimeError(f"file {gamefile.relative_file_path} doesn't contain a timeline object")
        self.__effect_components_parent_node = node
        self.__phases_start_times = list[float]()
        self.__phases_durations = list[float]()
        self.update_duration()
        self.__current_phase_start_time = None
        self.__current_phase_index = None
        self.__peanuts_uuids = list[str]()
        peanuts = gamefile.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="PeanutSlotIdMap"]/children/node[@id="Object"]/children/node[@id="Object"][@key="MapKey"]')
        for peanut in peanuts:
            peanut_uuid = get_required_bg3_attribute(peanut, 'MapKey')
            self.__peanuts_uuids.append(peanut_uuid)

    @property
    def duration(self) -> int:
        return self.__duration

    @property
    def all_effect_components(self) -> tuple[et.Element, ...]:
        return tuple(self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]'))

    @property
    def xml(self) -> et.Element:
        return self.__file.root_node

    def update_duration(self) -> float:
        self.__duration = 0.0
        effect_node = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]')
        if effect_node is None:
            raise RuntimeError(f"cannot determine duration of timeline {self.__file.relative_file_path}")
        phases = effect_node.findall('./children/node[@id="Phases"]/children/node[@id="Phase"]')
        self.__phases_start_times = list[float]()
        for phase in phases:
            phase_duration = timeline_object.__round(float(get_required_bg3_attribute(phase, 'Duration')))
            self.__phases_start_times.append(self.__duration)
            self.__phases_durations.append(phase_duration)
            self.__duration = timeline_object.__round(self.__duration + phase_duration)
        set_bg3_attribute(effect_node, "Duration", str(self.__duration))
        return self.__duration

    def get_timeline_actors(self, actor_type_id: str | Iterable[str] = None) -> dict[str, et.Element]:
        result = dict[str, et.Element]()
        actors = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineActorData"]/children/node[@id="TimelineActorData"]/children/node[@id="Object"][@key="MapKey"]')
        if isinstance(actor_type_id, str):
            actor_type_ids = frozenset([actor_type_id])
        elif isinstance(actor_type_id, Iterable):
            actor_type_ids = frozenset(actor_type_id)
        else:
            actor_type_ids = None
        for actor in actors:
            actor_uuid = get_required_bg3_attribute(actor, 'MapKey')
            value = actor.find('./children/node[@id="Value"]')
            type_id = get_bg3_attribute(value, 'ActorTypeId')
            if actor_type_ids is None or type_id in actor_type_ids:
                result[actor_uuid] = value
        return result

    def get_timeline_actors_uuids(self, actor_type_id: str | Iterable[str] = None) -> Iterable[str]:
        return list[str](self.get_timeline_actors(actor_type_id).keys())

    def get_timeline_peanuts_uuids(self) -> tuple[str, ...]:
        return tuple(self.__peanuts_uuids)

    def get_phase_start_time(self, phase_index: int) -> float:
        if phase_index >= len(self.__phases_start_times):
            raise KeyError(f"phase index {phase_index} is out of bounds [0; {len(self.__phases_start_times)})")
        return self.__phases_start_times[phase_index]

    def get_phase_duration(self, phase_index: int) -> float:
        if phase_index >= len(self.__phases_durations):
            raise KeyError(f"phase index {phase_index} is out of bounds [0; {len(self.__phases_durations)})")
        return self.__phases_durations[phase_index]

    def create_new_phase(self, dialog_node_uuid: str, phase_duration: float, line_index: int | None = None) -> int:
        phases_children = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="Phases"]/children')
        if phases_children is None:
            raise RuntimeError(f"cannot find 'Phases' in timeline {self.__file.relative_file_path}")
        phase_index = len(phases_children)
        timeline_phases_children = self.__file.root_node.find('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children')
        if timeline_phases_children is None:
            raise RuntimeError(f"cannot find 'TimelinePhases' in timeline {self.__file.relative_file_path}")
        phase_xml = '<node id="Phase">' + \
                f'<attribute id="Duration" type="float" value="{phase_duration}" />' + \
                '<attribute id="PlayCount" type="int32" value="1" />' + \
                f'<attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />' + \
				'<children><node id="QuestionHoldAutomation" /></children></node>'
        if line_index is None:
            reference_id = dialog_node_uuid
        else:
            tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
            if line_index >= len(tag_texts) or line_index < 0:
                raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
            reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
        timeline_phase_xml = f'<node id="Object" key="MapKey"><attribute id="MapKey" type="guid" value="{reference_id}" /><attribute id="MapValue" type="uint64" value="{phase_index}" /></node>'
        phases_children.append(et.fromstring(phase_xml))
        timeline_phases_children.append(et.fromstring(timeline_phase_xml))
        self.__current_phase_start_time = timeline_object.__round(self.__duration)
        self.__current_phase_index = phase_index
        self.__duration = timeline_object.__round(self.__duration + phase_duration)
        self.__phases_start_times.append(self.__current_phase_start_time)
        self.__phases_durations.append(phase_duration)
        return phase_index

    def use_existing_phase(self, phase_id: str | int) -> timeline_phase:
        phase = self.get_timeline_phase(phase_id)
        self.__current_phase_index = phase.index
        self.__current_phase_start_time = phase.start
        return phase

    def find_tl_node(self, node_uuid: str) -> et.Element:
        for node in self.all_effect_components:
            if get_bg3_attribute(node, 'ID') == node_uuid:
                return node
        raise KeyError(f"node {node_uuid} doesn't exist in timeline {self.__file.relative_file_path}")

    @staticmethod
    def __recurse_update_node_times(current_node: et.Element, time_delta: float) -> None:
        time_value = get_bg3_attribute(current_node, 'Time')
        if time_value is not None:
            time_value = timeline_object.__round(float(time_value) + time_delta)
            set_bg3_attribute(current_node, 'Time', str(time_value))
        children = current_node.findall("./children/node")
        for child in children:
            timeline_object.__recurse_update_node_times(child, time_delta)

    @staticmethod
    def __round(value: float) -> float:
        return round(value, ndigits = timeline_object.TIMELINE_PRECISION)

    def get_effective_actor(self, actor_uuid: str) -> tuple[str, bool]:
        if actor_uuid in PEANUTS:
            peanut_override = False
            if actor_uuid == PEANUT_SLOT_0:
                effective_actor = self.__peanuts_uuids[0]
            elif actor_uuid == PEANUT_SLOT_1:
                effective_actor = self.__peanuts_uuids[1]
            elif actor_uuid == PEANUT_SLOT_2:
                effective_actor = self.__peanuts_uuids[2]
            else:
                raise RuntimeError(f'unexpected peanut: {actor_uuid}')
        else:
            try:
                effective_actor = self.__dialog.get_speaker_actor_uuid(actor_uuid)
                peanut_override = self.__dialog.is_peanut_speaker(actor_uuid)
            except:
                effective_actor = actor_uuid
                peanut_override = False
        return effective_actor, peanut_override

    def get_tl_node_speaker_uuid(self, tl_node: et.Element) -> str | None:
        actor_node = tl_node.find('./children/node[@id="Actor"]')
        if actor_node is None:
            raise RuntimeError("cannot determine actor: actor node doesn't exist")
        actor_uuid = get_required_bg3_attribute(actor_node, 'UUID')
        speakers = self.__file.xml.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelineSpeakers"]/children/node[@id="TimelineSpeaker"]/children/node[@id="Object"][@key="MapKey"]')
        for speaker in speakers:
            map_val = get_required_bg3_attribute(speaker, 'MapValue')
            if map_val == actor_uuid:
                speaker_index = get_required_bg3_attribute(speaker, 'MapKey')
                return self.__dialog.get_speaker_by_index(int(speaker_index))
        return None

    def clone_tl_node(
            self,
            source_node: str | et.Element,
            /,
            new_node_uuid: str | None = None,
            new_node_duration: float | None = None,
            new_actor: str | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("cannot clone a node without creating a new phase first")
        if isinstance(source_node, str):
            source_node = self.find_tl_node(source_node)
        elif not isinstance(source_node, et.Element):
            raise TypeError(f"unexpected type of 'source_node' argument: {type(source_node)}")
        new_node = et.fromstring(et.tostring(source_node))
        phase_index = get_bg3_attribute(source_node, 'PhaseIndex')
        source_node_start = float(get_required_bg3_attribute(source_node, 'StartTime'))
        source_node_end = float(get_required_bg3_attribute(source_node, 'EndTime'))
        if phase_index is None:
            phase_index = 0
        else:
            phase_index = int(phase_index)
        source_phase_start = timeline_object.__round(self.__phases_start_times[phase_index])
        current_phase_duration = timeline_object.__round(self.__phases_durations[self.__current_phase_index])
        current_phase_end_time = timeline_object.__round(self.__current_phase_start_time + current_phase_duration)

        if new_node_uuid is None:
            new_node_uuid = new_random_uuid()
        time_delta = timeline_object.__round(source_node_start - source_phase_start)
        if time_delta < 0.0001:
            time_delta = 0.0
        new_node_start = timeline_object.__round(self.__current_phase_start_time + time_delta)
        if new_node_duration is None:
            new_node_end = timeline_object.__round(self.__current_phase_start_time + current_phase_duration)
        elif new_node_duration < 0.0001:
            new_node_end = timeline_object.__round(new_node_start + (source_node_end - source_node_start))
            if new_node_end > current_phase_end_time:
                raise RuntimeError(f'node end time {new_node_end} exceeds phase end time {current_phase_end_time}')
        else:
            new_node_end = new_node_start + new_node_duration
        set_bg3_attribute(new_node, 'ID', new_node_uuid, attribute_type = 'guid')
        set_bg3_attribute(new_node, 'PhaseIndex', str(self.__current_phase_index), attribute_type = 'int64')
        set_bg3_attribute(new_node, 'StartTime', str(new_node_start), attribute_type = 'float')
        set_bg3_attribute(new_node, 'EndTime', str(new_node_end), attribute_type = 'float')
        timeline_object.__recurse_update_node_times(new_node, timeline_object.__round(new_node_start - source_node_start))
        if new_actor is not None:
            actor_node = new_node.find('./children/node[@id="Actor"]')
            if actor_node is None:
                raise RuntimeError(f'effect component cloning failed: the source node has no actor node')
            peanut_override = False
            try:
                effective_actor, peanut_override = self.get_effective_actor(new_actor)
            except:
                effective_actor = new_actor
            set_bg3_attribute(actor_node, 'UUID', effective_actor, attribute_type='guid')
        return new_node

    def create_new_voice_phase_from_another(
            self,
            template_dialog_node_uuid: str,
            speaker: str,
            voice_duration: float,
            dialog_node_uuid: str,
            /,
            skip_tl_nodes: Iterable[str] | None = None,
            phase_duration: float | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[float, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[float, str, str, int | None]]] | None = None
    ) -> None:
        tl_phase = self.get_timeline_phase(template_dialog_node_uuid)
        phase_components = list[et.Element]()
        for effect_component in self.all_effect_components:
            phase_index = get_bg3_attribute(effect_component, 'PhaseIndex')
            phase_index = 0 if phase_index is None else int(phase_index)
            if phase_index == tl_phase.index:
                phase_components.append(effect_component)
        if phase_duration is None:
            phase_duration = voice_duration
        self.create_new_phase(dialog_node_uuid, phase_duration, line_index=line_index)
        skip_set = frozenset(skip_tl_nodes) if skip_tl_nodes is not None else frozenset()
        tl_voice_cloned = False
        emotions_added = list[str]()
        attitudes_added = list[str]()
        for effect_component in phase_components:
            tl_node_type = get_required_bg3_attribute(effect_component, 'Type')
            if tl_node_type in skip_set:
                continue
            if tl_node_type == 'TLVoice':
                if tl_voice_cloned:
                    continue
                tl_voice_cloned = True
                new_effect_component = self.clone_tl_node(effect_component, new_node_duration=voice_duration, new_actor=speaker)
                if line_index is None:
                    reference_id = dialog_node_uuid
                else:
                    tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
                    if line_index >= len(tag_texts) or line_index < 0:
                        raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
                    reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
                set_bg3_attribute(new_effect_component, 'DialogNodeId', dialog_node_uuid, attribute_type='guid')
                set_bg3_attribute(new_effect_component, 'ReferenceId', reference_id, attribute_type='guid')
            elif tl_node_type == 'TLEmotionEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if emotions is not None and speaker_uuid is not None and speaker_uuid in emotions:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError("this should never happen: children node doesn't exist")
                    for emotion in emotions[speaker_uuid]:
                        children.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    emotions_added.append(speaker_uuid)
            elif tl_node_type == 'TLAttitudeEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if attitudes is not None and speaker_uuid is not None and speaker_uuid in attitudes:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))                            
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError(f"this should never happen: children node doesn't exist: {to_compact_string(new_effect_component)}")
                    for attitude in attitudes[speaker_uuid]:
                        interpolation_type = 3 if attitude[3] is None else attitude[3]
                        children.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2], interpolation_type = interpolation_type))
                    attitudes_added.append(speaker_uuid)
            else:
                new_effect_component = self.clone_tl_node(effect_component)
            self.__effect_components_parent_node.append(new_effect_component)
        phase_duration = self.__phases_durations[self.__current_phase_index]
        if emotions is not None:
            for speaker_uuid in emotions:
                if speaker_uuid not in emotions_added:
                    emotion_keys = list[et.Element]()
                    for emotion in emotions[speaker_uuid]:
                        emotion_keys.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    self.create_tl_actor_node(timeline_object.EMOTION, speaker_uuid, 0.0, phase_duration, emotion_keys)
        if attitudes is not None:
            for speaker_uuid in attitudes:
                if speaker_uuid not in attitudes_added:
                    attitude_keys = list[et.Element]()
                    for attitude in attitudes[speaker_uuid]:
                        attitude_keys.append(self.create_attitude_key(emotion[0], emotion[1], emotion[2]))
                    self.create_tl_actor_node(timeline_object.ATTITUDE, speaker_uuid, 0.0, phase_duration, attitude_keys)

    def create_new_cinematic_phase_from_another(
            self,
            template_dialog_node_uuid: str,
            dialog_node_uuid: str,
            /,
            skip_tl_nodes: Iterable[str] | None = None,
            phase_duration: float | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[float, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[float, str, str, int | None]]] | None = None
    ) -> None:
        tl_phase = self.get_timeline_phase(template_dialog_node_uuid)
        phase_components = list[et.Element]()
        for effect_component in self.all_effect_components:
            phase_index = get_bg3_attribute(effect_component, 'PhaseIndex')
            phase_index = 0 if phase_index is None else int(phase_index)
            if phase_index == tl_phase.index:
                phase_components.append(effect_component)
        if phase_duration is None:
            phase_duration = tl_phase.duration
        self.create_new_phase(dialog_node_uuid, phase_duration, line_index=line_index)
        skip_set = frozenset(skip_tl_nodes) if skip_tl_nodes is not None else frozenset()
        emotions_added = list[str]()
        attitudes_added = list[str]()
        for effect_component in phase_components:
            tl_node_type = get_required_bg3_attribute(effect_component, 'Type')
            if tl_node_type in skip_set:
                continue
            if tl_node_type == 'TLEmotionEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if emotions is not None and speaker_uuid is not None and speaker_uuid in emotions:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError("this should never happen: children node doesn't exist")
                    for emotion in emotions[speaker_uuid]:
                        children.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    emotions_added.append(speaker_uuid)
            elif tl_node_type == 'TLAttitudeEvent':
                new_effect_component = self.clone_tl_node(effect_component)
                speaker_uuid = self.get_tl_node_speaker_uuid(effect_component)
                if attitudes is not None and speaker_uuid is not None and speaker_uuid in attitudes:
                    children = new_effect_component.find('./children')
                    if children is None:
                        new_effect_component.append(et.fromstring('<children><node id="Keys"><children></children></node></children>'))
                    else:
                        emotion_keys = children.find('./node[@id="Keys"]')
                        if emotion_keys is not None:
                            children.remove(emotion_keys)
                        children.append(et.fromstring('<node id="Keys"><children></children></node>'))                            
                    children = new_effect_component.find('./children/node[@id="Keys"]/children')
                    if children is None:
                        raise RuntimeError(f"this should never happen: children node doesn't exist: {to_compact_string(new_effect_component)}")
                    for attitude in attitudes[speaker_uuid]:
                        children.append(self.create_attitude_key(attitude[0], attitude[1], attitude[2]))
                    attitudes_added.append(speaker_uuid)
            else:
                new_effect_component = self.clone_tl_node(effect_component)
            self.__effect_components_parent_node.append(new_effect_component)
        phase_duration = self.__phases_durations[self.__current_phase_index]
        if emotions is not None:
            for speaker_uuid in emotions:
                if speaker_uuid not in emotions_added:
                    emotion_keys = list[et.Element]()
                    for emotion in emotions[speaker_uuid]:
                        emotion_keys.append(self.create_emotion_key(emotion[0], emotion[1], variation = emotion[2]))
                    self.create_tl_actor_node(timeline_object.EMOTION, speaker_uuid, 0.0, phase_duration, emotion_keys)
        if attitudes is not None:
            for speaker_uuid in attitudes:
                if speaker_uuid not in attitudes_added:
                    attitude_keys = list[et.Element]()
                    for attitude in attitudes[speaker_uuid]:
                        attitude_keys.append(self.create_attitude_key(emotion[0], emotion[1], emotion[2]))
                    self.create_tl_actor_node(timeline_object.ATTITUDE, speaker_uuid, 0.0, phase_duration, attitude_keys)

    def create_tl_actor_node(
            self,
            node_type: str,
            speaker_actor: str,
            start: float,
            end: float,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            is_mimicry: bool = False,
            peanut_override: bool | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        
        effective_actor, effective_peanut = self.get_effective_actor(speaker_actor)
        if peanut_override is None:
            peanut_override = effective_peanut

        if node_type in timeline_object.VALID_ACTOR_NODES:
            xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="{node_type}" />']
        else:
            raise ValueError(f"unsupported timeline event {node_type}")
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_mimicry:
            xml.append('<attribute id="IsMimicry" type="bool" value="True" />')
        if peanut_override:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /><attribute id="PeanutOverride" type="bool" value="True" /></node>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        if len(keys) > 0:
            xml.append('<node id="Keys"><children></children></node>')
        xml.append('</children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if len(keys) > 0:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if keys_children is None:
                raise RuntimeError(f'cannot add keys to the node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_actor_nodes(
            self,
            node_type: str,
            actors: list[str],
            start: float,
            end: float,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            is_mimicry: bool = False,
            peanut_override: bool | None = None
    ) -> list[et.Element]:
        return [self.create_tl_actor_node(
            node_type,
            actor,
            start,
            end,
            keys,
            is_snapped_to_end=is_snapped_to_end,
            is_mimicry=is_mimicry,
            peanut_override=peanut_override) for actor in actors]

    def create_tl_non_actor_node(
            self,
            node_type: str,
            start: float,
            end: float,
            keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        if node_type in timeline_object.VALID_NON_ACTOR_NODES:
            xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="{node_type}" />']
        else:
            raise ValueError(f"unsupported timeline event {node_type}")
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if len(keys) > 0:
            xml.append('<children><node id="Keys"><children></children></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if keys:
            keys_children = tl_node.find('./children/node[@id="Keys"]/children')
            if keys_children is None:
                raise RuntimeError(f'cannot add keys to the node: {to_compact_string(tl_node)}')
            for key in keys:
                keys_children.append(key)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_voice(
            self,
            speaker: str,
            start: float,
            end: float,
            dialog_node_uuid: str,
            /,
            line_index: int | None = None,
            node_uuid: str | None = None,
            performance_fade: float | None = None,
            fade_in: float | None = None,
            fade_out: float | None = None,
            head_pitch_correction: float | None = None,
            head_roll_correction: float | None = None,
            hold_mocap: bool = True,
            disable_mocap: bool = False,
            is_snapped_to_end: bool = False,
            peanut_override: bool | None = None,
            is_mirrored: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()

        xml = ['<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLVoice" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        xml.append(f'<attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if line_index is None:
            reference_id = dialog_node_uuid
        else:
            tag_texts = self.__dialog.get_tagged_texts(dialog_node_uuid)
            if line_index >= len(tag_texts) or line_index < 0:
                raise IndexError(f"line index {line_index} is out of bounds [0; {len(tag_texts)})")
            reference_id = get_required_bg3_attribute(tag_texts[line_index], "CustomSequenceId")
        xml.append(f'<attribute id="ReferenceId" type="guid" value="{reference_id}" />')        
        if performance_fade is not None:
            xml.append(f'<attribute id="PerformanceFade" type="double" value="{performance_fade}" />')
        if fade_in is not None:
            xml.append(f'<attribute id="FadeIn" type="double" value="{fade_in}" />')
        if fade_out is not None:
            xml.append(f'<attribute id="FadeOut" type="double" value="{fade_out}" />')
        if head_pitch_correction is not None:
            xml.append(f'<attribute id="HeadPitchCorrection" type="double" value="{head_pitch_correction}" />')
        if head_roll_correction is not None:
            xml.append(f'<attribute id="HeadRollCorrection" type="double" value="{head_roll_correction}" />')
        if not hold_mocap:
            xml.append('<attribute id="HoldMocap" type="bool" value="False" />')
        if disable_mocap:
            xml.append('<attribute id="DisableMocap" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_mirrored:
            xml.append('<attribute id="IsMirrored" type="bool" value="True" />')

        effective_actor, effective_peanut_override = self.get_effective_actor(speaker)
        if peanut_override is None:
            peanut_override = effective_peanut_override
        if peanut_override:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /><attribute id="PeanutOverride" type="bool" value="True" /></node></children>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_show_armor(
            self,
            target_speaker: str,
            start: float,
            end: float,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            peanut_override: bool | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if len(channels) != 11:
            raise ValueError(f"TLShowArmor requires 11 channels, {len(channels)} were provided")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLShowArmor" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        
        effective_actor, effective_peanut_override = self.get_effective_actor(target_speaker)
        if peanut_override is None:
            peanut_override = effective_peanut_override        
        if peanut_override:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" />' +
                       '<attribute id="PeanutOverride" type="bool" value="True" /></node>' +
                       '<node id="Channels"><children></children></node></children>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>' +
                       '<node id="Channels"><children></children></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        channels_children = tl_node.find('./children/node[@id="Channels"]/children')
        if channels_children is None:
            raise RuntimeError(f'cannot add channels to the node: {to_compact_string(tl_node)}')
        for channel in channels:
            if len(channel) == 0:
                channels_children.append(et.fromstring('<node id="" />'))
            else:
                channel_node = et.fromstring('<node id=""><children><node id="Keys"><children></children></node></children></node>')
                keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                for key in channel:
                    keys_children.append(key)
                channels_children.append(channel_node)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_transform(
            self,
            actor: str,
            start: float,
            end: float,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            continuous: bool = False,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if len(channels) > 0 and len(channels) != 6:
            raise ValueError(f"expected 6 channels, got {len(channels)}")
        effective_actor, _ = self.get_effective_actor(actor)
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLTransform" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if continuous:
            xml.append('<attribute id="Continuous" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if len(channels) == 0:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children></node>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>' +
                       '<node id="TransformChannels"><children></children></node></children></node>')
        tl_node = et.fromstring("".join(xml))
        if len(channels) == 6:
            transform_channels_children = tl_node.find('./children/node[@id="TransformChannels"]/children')
            for channel in channels:
                if len(channel) == 0:
                    transform_channels_children.append(et.fromstring('<node id="TransformChannel" />'))
                else:
                    channel_node = et.fromstring('<node id="TransformChannel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    for key in channel:
                        channel_node_keys_children.append(key)
                    transform_channels_children.append(channel_node)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_shot(
            self,
            camera: int | str,
            start: float,
            end: float,
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False,
            is_looping: bool = True,
            is_logic_enabled: bool = False,
            disable_conditional_staging: bool = False,
            j_cut_length: int | None = None,
            companion_cameras: tuple[object, object, object] | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if isinstance(camera, int):
            if camera < 0 or camera >= len(self.__cameras_uuids):
                raise ValueError(f"camera index is out of bounds [0, {len(self.__cameras_uuids)})")
            effective_camera_uuid = self.__cameras_uuids[camera]
        elif isinstance(camera, str):
            effective_camera_uuid = camera
        else:
            raise TypeError(f"camera could be either an integer index or a string uuid, got {type(camera)}")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLShot" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if not is_looping:
            xml.append('<attribute id="IsLooping" type="bool" value="False" />')
        if is_logic_enabled:
            xml.append('<attribute id="IsLogicEnabled" type="bool" value="True" />')
        if disable_conditional_staging:
            xml.append('<attribute id="DisableConditionalStaging" type="bool" value="True" />')
        if companion_cameras is not None:
            for i in range(0, 3):
                c = "ABC"[i]
                if isinstance(companion_cameras[i], int):
                    xml.append(f'<attribute id="CompanionCamera{c}" type="guid" value="{self.__cameras_uuids[companion_cameras[i]]}" />')
                elif isinstance(companion_cameras[i], str):
                    xml.append(f'<attribute id="CompanionCamera{c}" type="guid" value="{companion_cameras[i]}" />')
                else:
                    raise TypeError(f'companion camera should be either int or str, got {type(companion_cameras[i])}')
        if j_cut_length is not None:
            xml.append(f'<attribute id="JCutLength" type="float" value="{j_cut_length}" />')
        xml.append(f'<children><node id="CameraContainer"><attribute id="Object" type="guid" value="{effective_camera_uuid}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_camera_dof(
            self,
            camera: int | str,
            start: float,
            end: float,
            channels: Iterable[Iterable[et.Element]],
            /,
            node_uuid: str | None = None,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if len(channels) > 0 and len(channels) != 7:
            raise ValueError(f"expected 7 channels, got {len(channels)}")
        if isinstance(camera, str):
            effective_camera_uuid = camera
        elif isinstance(camera, int):
            if camera < 0 or camera >= len(self.__cameras_uuids):
                raise ValueError(f"camera index is out of bounds [0, {len(self.__cameras_uuids)})")
            effective_camera_uuid = self.__cameras_uuids[camera]
        else:
            raise TypeError(f"camera could be either an integer index or a string uuid, got {type(camera)}")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLCameraDoF" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if len(channels) == 0:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_camera_uuid}" /></node></children>')
        else:
            xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_camera_uuid}" /></node>' +
                       '<node id="Channels"><children></children></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if len(channels) == 7:
            channels_children = tl_node.find('./children/node[@id="Channels"]/children')
            for channel in channels:
                if len(channel) == 0:
                    channels_children.append(et.fromstring('<node id="Channel" />'))
                else:
                    channel_node = et.fromstring('<node id="Channel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    for key in channel:
                        channel_node_keys_children.append(key)
                    channels_children.append(channel_node)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_material(
            self,
            actor: str,
            start: float,
            end: float,
            group_id: str,
            material_parameters: Iterable[et.Element],
            visibility_channel_keys: Iterable[et.Element],
            /,
            node_uuid: str | None = None,
            is_continuous: bool = False,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLMaterial" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if is_continuous:
            xml.append('<attribute id="IsContinuous" type="bool" value="True" />')
        xml.append(f'<attribute id="GroupId" type="guid" value="{group_id}" />')
        effective_actor, _ = self.get_effective_actor(actor)
        xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node>')
        if len(material_parameters) > 0:
            xml.append(f'<node id="MaterialParameter"><children></children></node>')
        else:
            xml.append(f'<node id="MaterialParameter" />')
        if len(visibility_channel_keys) > 0:
            xml.append(f'<node id="VisibilityChannel"><children><node id="Keys"><children></children></node></children></node>')
        else:
            xml.append(f'<node id="VisibilityChannel" />')
        xml.append('</children></node>')
        tl_node = et.fromstring("".join(xml))
        if len(material_parameters) > 0:
            material_parameters_children = tl_node.find('./children/node[@id="MaterialParameter"]/children')
            if material_parameters_children is None:
                raise RuntimeError(f"bad TLMaterial node: {to_compact_string(tl_node)}")
            for material_parameter in material_parameters:
                material_parameters_children.append(material_parameter)
        if len(visibility_channel_keys) > 0:
            visibility_channel_keys_children = tl_node.find('./children/node[@id="VisibilityChannel"]/children/node[@id="Keys"]/children')
            if visibility_channel_keys_children is None:
                raise RuntimeError(f"bad TLMaterial node: {to_compact_string(tl_node)}")
            for key in visibility_channel_keys:
                visibility_channel_keys_children.append(key)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node

    def create_tl_animation(
            self,
            actor: str,
            start: float,
            end: float,
            animation_id: str,
            animation_group: str,
            /,
            node_uuid: str | None = None,
            animation_slot: int | None = None,
            animation_play_rate: float | None = None,
            animation_play_start_offset: float | None = None,
            offset_type: int | None = None,
            fade_in: float | None = None,
            fade_out: float | None = None,
            continuous: bool = False,
            is_mirrored: bool = False,
            is_snapped_to_end: bool = False,
            enable_root_motion: bool = False,
            target_transform: et.Element | None = None
    ) -> et.Element:
        if self.__current_phase_index is None or self.__current_phase_start_time is None:
            raise RuntimeError("a new phase hasn't been created")
        if node_uuid is None:
            node_uuid = new_random_uuid()
        xml = [f'<node id="EffectComponent"><attribute id="Type" type="LSString" value="TLAnimation" />']
        xml.append(f'<attribute id="ID" type="guid" value="{node_uuid}" />')
        xml.append(f'<attribute id="StartTime" type="float" value="{self.__current_phase_start_time + start}" />')
        xml.append(f'<attribute id="EndTime" type="float" value="{self.__current_phase_start_time + end}" />')
        if self.__current_phase_index > 0:
            xml.append(f'<attribute id="PhaseIndex" type="int64" value="{self.__current_phase_index}" />')
        xml.append(f'<attribute id="AnimationSourceId" type="guid" value="{animation_id}" />')
        xml.append(f'<attribute id="AnimationGroup" type="guid" value="{animation_group}" />')
        if animation_slot is not None:
            xml.append(f'<attribute id="AnimationSlot" type="FixedString" value="{animation_slot}" />')
        if animation_play_rate is not None:
            xml.append(f'<attribute id="AnimationPlayRate" type="double" value="{animation_play_rate}" />')
        if animation_play_start_offset is not None:
            xml.append(f'<attribute id="AnimationPlayStartOffset" type="double" value="{animation_play_start_offset}" />')
        if offset_type is not None:
            xml.append(f'<attribute id="OffsetType" type="uint8" value="{offset_type}" />')
        if fade_in is not None:
            xml.append(f'<attribute id="FadeIn" type="double" value="{fade_in}" />')
        if fade_out is not None:
            xml.append(f'<attribute id="FadeOut" type="double" value="{fade_out}" />')
        if continuous:
            xml.append('<attribute id="Continuous" type="bool" value="True" />')
        if is_mirrored:
            xml.append('<attribute id="IsMirrored" type="bool" value="True" />')
        if is_snapped_to_end:
            xml.append('<attribute id="IsSnappedToEnd" type="bool" value="True" />')
        if enable_root_motion:
            xml.append('<attribute id="EnableRootMotion" type="bool" value="True" />')
        effective_actor, _ = self.get_effective_actor(actor)
        xml.append(f'<children><node id="Actor"><attribute id="UUID" type="guid" value="{effective_actor}" /></node></children>')
        xml.append('</node>')
        tl_node = et.fromstring("".join(xml))
        if target_transform is not None:
            children = tl_node.find('./children')
            if children is None:
                raise RuntimeError(f'bad TLAnimation node: {to_compact_string(tl_node)}')
            children.append(target_transform)
        self.__effect_components_parent_node.append(tl_node)
        return tl_node


    def create_animation_target_transform(
            self,
            scale: float,
            position: tuple[float, float, float],
            rotation: tuple[float, float, float, float]
    ) -> et.Element:
        return et.fromstring(f'<node id="TargetTransform"><attribute id="Scale" type="float" value="{scale}" />' +
                             f'<attribute id="Position" type="fvec3" value="{position[0]} {position[1]} {position[2]}" />' +
                             f'<attribute id="RotationQuat" type="fvec4" value="{rotation[0]} {rotation[1]} {rotation[2]} {rotation[3]}" /></node>')

    def create_attitude_key(
            self,
            time: float,
            pose: str,
            transition: str,
            /,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + time
        return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                                f'<attribute id="Pose" type="FixedString" value="{pose}" />' +
                                f'<attribute id="Transition" type="FixedString" value="{transition}" /></node>')

    def create_emotion_key(
            self,
            time: float,
            emotion: int,
            /,
            variation: int | None = None,
            interpolation_type: int = 3,
            is_sustained: bool = True
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + time
        strings = [
            f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />',
            f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />',
            f'<attribute id="Emotion" type="int32" value="{emotion}" />'
        ]
        if variation is not None:
            strings.append(f'<attribute id="Variation" type="int32" value="{variation}" />')
        if is_sustained == False:
            strings.append('<attribute id="IsSustainedEmotion" type="bool" value="False" />')
        strings.append('</node>')
        return et.fromstring(''.join(strings))

    def create_look_at_key(
            self,
            time: float,
            /,
            target: str | None = None,
            bone: str | None = None,
            turn_mode: int | None = None,
            tracking_mode: int | None = None,
            turn_speed_multiplier: float | None = None,
            torso_turn_speed_multiplier: float | None = None,
            head_turn_speed_multiplier: float | None = None,
            weight: float | None = None,
            look_at_mode: int | None = None,
            eye_look_at_bone: str | None = None,
            eye_look_at_offset: tuple[float, float, float] | None = None,
            offset: tuple[float, float, float] | None = None,
            safe_zone_angle: float | None = None,
            head_safe_zone_angle: float | None = None,
            reset: bool = False,
            is_eye_look_at_enabled: bool = False,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        if target is not None:
            effective_target, _ = self.get_effective_actor(target)
        else:
            effective_target = None
        xml = ['<node id="Key">']
        abs_time = self.__current_phase_start_time + time
        xml.append(f'<attribute id="Time" type="float" value="{abs_time}" />')
        xml.append(f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />')
        if effective_target is not None:
            xml.append(f'<attribute id="Target" type="guid" value="{effective_target}" />')
        if bone is not None:
            xml.append(f'<attribute id="Bone" type="FixedString" value="{bone}" />')
        if turn_mode is not None:
            xml.append(f'<attribute id="TurnMode" type="uint8" value="{turn_mode}" />')
        if tracking_mode is not None:
            xml.append(f'<attribute id="TurnMode" type="uint8" value="{tracking_mode}" />')
        if turn_speed_multiplier is not None:
            xml.append(f'<attribute id="TurnSpeedMultiplier" type="float" value="{turn_speed_multiplier}" />')
        if torso_turn_speed_multiplier is not None:
            xml.append(f'<attribute id="TorsoTurnSpeedMultiplier" type="float" value="{torso_turn_speed_multiplier}" />')
        if head_turn_speed_multiplier is not None:
            xml.append(f'<attribute id="HeadTurnSpeedMultiplier" type="float" value="{head_turn_speed_multiplier}" />')
        if weight is not None:
            xml.append(f'<attribute id="Weight" type="double" value="{weight}" />')
        if look_at_mode is not None:
            xml.append(f'<attribute id="LookAtMode" type="uint8" value="{look_at_mode}" />')
        if eye_look_at_bone is not None:
            xml.append(f'<attribute id="EyeLookAtBone" type="FixedString" value="{eye_look_at_bone}" />')
        if eye_look_at_offset is not None:
            xml.append(f'<attribute id="EyeLookAtOffset" type="fvec3" value="{eye_look_at_offset[0]} {eye_look_at_offset[1]} {eye_look_at_offset[2]}" />')
        if offset is not None:
            xml.append(f'<attribute id="Offset" type="fvec3" value="{offset[0]} {offset[1]} {offset[2]}" />')
        if safe_zone_angle is not None:
            xml.append(f'<attribute id="SafeZoneAngle" type="double" value="{safe_zone_angle}" />')
        if head_safe_zone_angle is not None:
            xml.append(f'<attribute id="HeadSafeZoneAngle" type="double" value="{head_safe_zone_angle}" />')
        if reset:
            xml.append(f'<attribute id="Reset" type="bool" value="True" />')
        if is_eye_look_at_enabled:
            xml.append(f'<attribute id="IsEyeLookAtEnabled" type="bool" value="True" />')
        xml.append("</node>")
        return et.fromstring("".join(xml))

    def create_sound_event_key(
            self,
            time: float,
            /,
            sound_event_id: str | None = None,
            sound_object_index: int | None = None,
            sound_type: int | None = None,
            foley_type: int | None = None,
            interpolation_type: int = 3
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")        
        strings = [
            f'<node id="Key"><attribute id="Time" type="float" value="{self.__current_phase_start_time + time}" />',
            f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />'
        ]
        if sound_event_id is not None:
            strings.append(f'<attribute id="SoundEventID" type="guid" value="{sound_event_id}" />')
        if sound_object_index is not None:
            strings.append(f'<attribute id="SoundObjectIndex" type="uint8" value="{sound_object_index}" />')
        if sound_type is not None:
            strings.append(f'<attribute id="SoundType" type="uint8" value="{sound_type}" />')
        if foley_type is not None:
            strings.append(f'<attribute id="FoleyType" type="uint8" value="{foley_type}" />')
        strings.append('</node>')
        return et.fromstring(''.join(strings))

    def create_value_key(
            self,
            /,
            value: bool | float | Iterable | None = None,
            value_name: str | None = None,
            value_type: str | None = None,
            time: float | None = None,
            interpolation_type: int | None = None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        xml = ['<node id="Key">']
        if value_name is None:
            value_name = "Value"
        if isinstance(value_type, str):
            xml.append(f'<attribute id="{value_name}" type="{value_type}" value="{value}" />')
        elif isinstance(value, bool):
            xml.append(f'<attribute id="{value_name}" type="bool" value="{value}" />')
        elif isinstance(value, float):
            xml.append(f'<attribute id="{value_name}" type="float" value="{value}" />')
        elif isinstance(value, Iterable) and len(value) == 3:
            xml.append(f'<attribute id="{value_name}" type="fvec3" value="{value[0]} {value[1]} {value[2]}" />')
        elif isinstance(value, Iterable) and len(value) == 4:
            xml.append(f'<attribute id="{value_name}" type="fvec4" value="{value[0]} {value[1]} {value[2]} {value[3]}" />')
        if time is not None:
            abs_time = self.__current_phase_start_time + time
            xml.append(f'<attribute id="Time" type="float" value="{abs_time}" />')
        if interpolation_type is not None:
            xml.append(f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />')
        xml.append('</node>')
        return et.fromstring("".join(xml))

    def create_frame_of_reference_key(
            self,
            time: float,
            interpolation_type: int,
            target_uuid: str,
            target_bone: str,
            one_frame_only: bool,
            keep_scale: bool
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + time
        return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                             f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                             '<children><node id="Value"><children><node id="frameOfReference">' +
                             f'<attribute id="targetId" type="guid" value="{target_uuid}" />' +
                             f'<attribute id="targetBone" type="FixedString" value="{target_bone}" />' +
                             f'<attribute id="OneFrameOnly" type="bool" value="{one_frame_only}" />' +
                             f'<attribute id="KeepScale" type="bool" value="{keep_scale}" />' +
                             '</node></children></node></children></node>')

    def create_switch_stage_event_key(
            self,
            time: float,
            interpolation_type: int,
            event_uuid: str | None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + time
        if event_uuid is None:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" /></node>')
        else:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                                 f'<attribute id="SwitchStageEventID" type="guid" value="{event_uuid}" /></node>')
        
    def create_switch_location_event_key(
            self,
            time: float,
            interpolation_type: int,
            event_uuid: str | None
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        abs_time = self.__current_phase_start_time + time
        if event_uuid is None:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" /></node>')
        else:
            return et.fromstring(f'<node id="Key"><attribute id="Time" type="float" value="{abs_time}" />' +
                                 f'<attribute id="InterpolationType" type="uint8" value="{interpolation_type}" />' +
                                 f'<attribute id="SwitchLocationEventID" type="guid" value="{event_uuid}" /></node>')

    def create_material_parameter(
            self,
            parameter_name: str,
            keys: Iterable[et.Element]
    ) -> et.Element:
        if self.__current_phase_start_time is None:
            raise RuntimeError("new phase should be created before effect components")
        elt = et.fromstring(f'<node id="Node"><attribute id="MaterialParameterName" type="FixedString" value="{parameter_name}" /><children>' +
                            '<node id="MaterialParameter"><children><node id="Keys"><children></children></node></children></node></children></node>')
        keys_children = elt.find('./children/node[@id="MaterialParameter"]/children/node[@id="Keys"]/children')
        if keys_children is None:
            raise RuntimeError(f'bad material parameter: {to_compact_string(elt)}')
        for key in keys:
            keys_children.append(key)
        return elt

    def create_simple_dialog_answer_phase(
            self,
            speaker: str,
            voice_duration: float,
            dialog_node_uuid: str,
            shots: Iterable[tuple[float | None, int | str]],
            /,
            phase_duration: float | None = None,
            line_index: int | None = None,
            emotions: dict[str, Iterable[tuple[float, int, int | None]]] | None = None,
            attitudes: dict[str, Iterable[tuple[float, str, str, int | None]]] | None = None,
            is_snapped_to_end: bool = False,
            peanut_override: bool = False,
            fade_in: float = 0.0,
            fade_out: float = 0.0,
            performance_fade: float = 0.0
    ) -> None:
        if phase_duration is None:
            phase_duration = voice_duration
        start = 0.0
        end = phase_duration
        self.create_new_phase(dialog_node_uuid, phase_duration, line_index=line_index)
        self.create_tl_voice(
            speaker,
            start,
            voice_duration,
            dialog_node_uuid,
            line_index=line_index,
            is_snapped_to_end=is_snapped_to_end,
            peanut_override=peanut_override,
            fade_in=fade_in,
            fade_out=fade_out,
            performance_fade=performance_fade)
        if emotions is not None:
            for target, emotion_records in emotions.items():
                emotion_keys = list[et.Element]()
                for emotion_record in emotion_records:
                    emotion_keys.append(self.create_emotion_key(emotion_record[0], emotion_record[1], variation = emotion_record[2]))
                self.create_tl_actor_node(timeline_object.EMOTION, target, start, end, emotion_keys, is_snapped_to_end=True)
        if attitudes is not None:
            for target, attitude_records in attitudes.items():
                attitude_keys = list[et.Element]()
                for attitude_record in attitude_records:
                    interpolation_type = 3 if attitude_record[3] is None else attitude_record[3]
                    attitude_keys.append(
                        self.create_attitude_key(
                            attitude_record[0],
                            attitude_record[1],
                            attitude_record[2],
                            interpolation_type = interpolation_type))
            self.create_tl_actor_node(timeline_object.ATTITUDE, target, start, end, attitude_keys)
        shot_start = start
        for shot in shots:
            if shot_start >= phase_duration:
                raise RuntimeError(f"duration of TLShot exceeds phase duration: {shot_start} >= {phase_duration}")
            shot_end = shot[0]
            if shot_end is None:
                shot_end = phase_duration
            camera = shot[1]
            self.create_tl_shot(camera, shot_start, shot_end)
            shot_start = shot_end

    def remove_effect_component(self, effect_component: et.Element) -> None:
        self.__effect_components_parent_node.remove(effect_component)

    def get_timeline_phase(self, phase_id: str | int) -> timeline_phase:
        phases = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="Effect"]/children/node[@id="Phases"]/children/node[@id="Phase"]')
        timeline_phases = self.__file.root_node.findall('./region[@id="TimelineContent"]/node[@id="TimelineContent"]/children/node[@id="TimelinePhases"]/children/node[@id="Object"]/children/node[@id="Object"]')
        for tl_phase in timeline_phases:
            map_key = get_required_bg3_attribute(tl_phase, "MapKey")
            map_value = int(get_required_bg3_attribute(tl_phase, "MapValue"))
            if (isinstance(phase_id, str) and phase_id == map_key) or (isinstance(phase_id, int) and phase_id == map_value):
                phase_start = 0.0
                for idx in range(0, map_value):
                    phase_start += float(get_required_bg3_attribute(phases[idx], "Duration"))
                phase_end = phase_start + float(get_required_bg3_attribute(phases[map_value], "Duration"))
                dialog_uuid = get_required_bg3_attribute(phases[map_value], "DialogNodeId")
                return timeline_phase(map_value, dialog_uuid, map_key, phase_start, phase_end)
        raise KeyError(f"failed to find a phase with id {phase_id} in timeline {self.__file.relative_file_path}")

    def find_effect_component(self, effect_component_uuid: str) -> et.Element:
        effect_components = self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]')
        for effect_component in effect_components:
            if get_required_bg3_attribute(effect_component, "ID") == effect_component_uuid:
                return effect_component
        raise KeyError(f"effect component {effect_component_uuid} is not found in {self.__file.relative_file_path}")

    def find_effect_components(self, /, effect_component_type: str | None = None, actor: str | None = None) -> et.Element:
        result = list[et.Element]()
        effect_components = self.__effect_components_parent_node.findall('./node[@id="EffectComponent"]')
        effective_actor, _ = self.get_effective_actor(actor)
        for effect_component in effect_components:
            if effect_component_type is not None and get_required_bg3_attribute(effect_component, "Type") != effect_component_type:
                continue
            if actor is not None:
                actor_node = effect_component.find('./children/node[@id="Actor"]')
                if actor_node is None or get_bg3_attribute(actor_node, "UUID") != effective_actor:
                    continue
            result.append(effect_component)
        return result

    def edit_tl_transform(
            self,
            node_uuid: str,
            /,
            actor: str | None = None,
            start: float | None = None,
            end: float | None = None,
            channels: Iterable[Iterable[et.Element]] | None = None,
            continuous: bool = False,
            is_snapped_to_end: bool = False
    ) -> et.Element:
        tl_node = self.find_effect_component(node_uuid)
        if actor is not None:
            actor_node = tl_node.find('./children/node[@id="Actor"]')
            if actor_node is None:
                raise RuntimeError(f"bad timeline object {node_uuid}, cannot find the Actor node")
            effective_actor, _ = self.get_effective_actor(actor)
            set_bg3_attribute(actor_node, "UUID", effective_actor)
        if start is not None:
            set_bg3_attribute(tl_node, "StartTime", start, attribute_type="float")
        if end is not None:
            set_bg3_attribute(tl_node, "EndTime", start, attribute_type="float")
        if continuous:
            set_bg3_attribute(tl_node, "Continuous", "True", attribute_type="bool")
        if is_snapped_to_end:
            set_bg3_attribute(tl_node, "IsSnappedToEnd", "True", attribute_type="bool")
        if channels is not None:
            transform_channels = et.fromstring('<node id="TransformChannels"><children></children></node>')
            transform_channels_children = transform_channels.find('./children')
            if transform_channels_children is None:
                raise RuntimeError('impossible: children node not found')
            for channel in channels:
                if len(channel) == 0:
                    transform_channels_children.append(et.fromstring('<node id="TransformChannel" />'))
                else:
                    channel_node = et.fromstring('<node id="TransformChannel"><children><node id="Keys"><children></children></node></children></node>')
                    channel_node_keys_children = channel_node.find('./children/node[@id="Keys"]/children')
                    for key in channel:
                        channel_node_keys_children.append(key)
                    transform_channels_children.append(channel_node)
            tl_node_children = tl_node.find('./children')
            if tl_node_children is None:
                raise RuntimeError('unexpected: children node not found')
            old_transform_channels = tl_node_children.find('./node[@id="TransformChannels"]')
            if old_transform_channels is not None:
                tl_node_children.remove(old_transform_channels)
            tl_node_children.append(transform_channels)
        return tl_node
