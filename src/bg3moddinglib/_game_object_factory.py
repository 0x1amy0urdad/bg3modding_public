from __future__ import annotations

import os
import os.path
import xml.etree.ElementTree as et

from typing import Optional

class game_object_factory:

    @staticmethod
    def create_tl_voice(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        dialog_node_uuid: str,
        actor_uuid: str,
        reference_id: Optional[str]=None,
        performance_fade: float=0,
        fade_in: float=0,
        fade_out: float=0,
        head_pitch_correction: Optional[float]=None,
        head_roll_correction: Optional[float]=None,
        is_snapped_to_end: bool=False,
        peanut_override: bool=False,
        hold_mocup: bool=True,
        disable_mocup: bool=False,
        is_mirrored: bool=False
    ) -> et.Element:
        if not reference_id:
            reference_id = dialog_node_uuid
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_is_mirrored = '<attribute id="IsMirrored" type="bool" value="True" />' if is_mirrored else ""
        flag_hold_mocup = '<attribute id="HoldMocap" type="bool" value="False" />' if not hold_mocup else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        flag_disable_mocup = '<attribute id="DisableMocap" type="bool" value="True" />' if disable_mocup else ""
        val_head_pitch_correction = '<attribute id="HeadPitchCorrection" type="double" value="{head_pitch_correction}" />' if head_pitch_correction is not None else ""
        val_head_roll_correction = '<attribute id="HeadRollCorrection" type="double" value="{head_roll_correction}" />' if head_roll_correction is not None else ""
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLVoice" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    <attribute id="DialogNodeId" type="guid" value="{dialog_node_uuid}" />
    <attribute id="ReferenceId" type="guid" value="{reference_id}" />
    <attribute id="PerformanceFade" type="double" value="{performance_fade}" />
    <attribute id="FadeIn" type="double" value="{fade_in}" />
    <attribute id="FadeOut" type="double" value="{fade_out}" />
    {val_head_pitch_correction}
    {val_head_roll_correction}
    {flag_hold_mocup}
    {flag_is_snapped_to_end}
    {flag_is_mirrored}
    {flag_disable_mocup}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
    </children>
</node>"""
        try:
            return et.fromstring(xml)
        except Exception as ex:
            print(xml)
            raise RuntimeError("Failed to create TLVoice") from ex

    @staticmethod
    def create_tl_attitude_event(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        actor_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        is_mimicry: bool=False,
        peanut_override: bool=False,
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_is_mimicry = '<attribute id="IsMimicry" type="bool" value="True" />' if is_mimicry else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLAttitudeEvent" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
    {flag_is_mimicry}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_emotion_event(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        actor_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        is_mimicry: bool=False,
        peanut_override: bool=False
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_is_mimicry = '<attribute id="IsMimicry" type="bool" value="True" />' if is_mimicry else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLEmotionEvent" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
    {flag_is_mimicry}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_look_at_event(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        actor_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        is_mimicry: bool=False,
        peanut_override: bool=False
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_is_mimicry = '<attribute id="IsMimicry" type="bool" value="True" />' if is_mimicry else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLLookAtEvent" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
    {flag_is_mimicry}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_show_visual(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        actor_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        peanut_override: bool=False
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLShowVisual" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_switch_stage_event(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        is_snapped_to_end: bool=False,
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLSwitchStageEvent" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_transform(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        actor_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        peanut_override: bool=False
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLTransform" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {flag_is_snapped_to_end}
    <children>
        <node id="Actor">
            <attribute id="UUID" type="guid" value="{actor_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_shot(
        effect_uuid: str,
        start_time: float,
        end_time: float,
        phase_index: int,
        scenecam_uuid: str,
        keys: tuple[dict[str, tuple[str, str]], ...]=(),
        is_snapped_to_end: bool=False,
        is_looping: bool=True,
        is_logic_enabled: bool=False,
        disable_conditional_staging: bool=False,
        j_cut_length: Optional[int]=None,
        companion_cam_a: Optional[str]=None,
        companion_cam_b: Optional[str]=None,
        companion_cam_c: Optional[str]=None,
        peanut_override: bool=False
    ) -> et.Element:
        flag_is_snapped_to_end = '<attribute id="IsSnappedToEnd" type="bool" value="True" />' if is_snapped_to_end else ""
        flag_disable_conditional_staging = '<attribute id="DisableConditionalStaging" type="bool" value="True" />' if disable_conditional_staging else ""
        flag_is_looping = '<attribute id="IsLooping" type="bool" value="False" />' if not is_looping else ""
        flag_is_logic_enabled = '<attribute id="IsLogicEnabled" type="bool" value="True" />' if is_logic_enabled else ""
        flag_peanut_override = '<attribute id="PeanutOverride" type="bool" value="True" />' if peanut_override else ""
        val_j_cut_length = f'<attribute id="JCutLength" type="float" value="{j_cut_length}" />' if j_cut_length is not None else ""
        val_companion_cam_a = f'<attribute id="CompanionCameraA" type="guid" value="{companion_cam_a}" />' if companion_cam_a is not None else ""
        val_companion_cam_b = f'<attribute id="CompanionCameraB" type="guid" value="{companion_cam_b}" />' if companion_cam_b is not None else ""
        val_companion_cam_c = f'<attribute id="CompanionCameraC" type="guid" value="{companion_cam_c}" />' if companion_cam_c is not None else ""
        keys_node = game_object_factory.create_tl_node_keys(keys)
        xml = f"""<node id="EffectComponent">
    <attribute id="Type" type="LSString" value="TLShot" />
    <attribute id="ID" type="guid" value="{effect_uuid}" />
    <attribute id="StartTime" type="float" value="{start_time}" />
    <attribute id="EndTime" type="float" value="{end_time}" />
    <attribute id="PhaseIndex" type="int64" value="{phase_index}" />
    {val_j_cut_length}
    {flag_is_snapped_to_end}
    {flag_disable_conditional_staging}
    {flag_is_looping}
    {flag_is_logic_enabled}
    {val_companion_cam_a}
    {val_companion_cam_b}
    {val_companion_cam_c}
    <children>
        <node id="CameraContainer">
            <attribute id="Object" type="guid" value="{scenecam_uuid}" />
            {flag_peanut_override}
        </node>
        {keys_node}
    </children>
</node>
"""
        return et.fromstring(xml)

    @staticmethod
    def create_tl_node_keys(keys: tuple[dict[str, tuple[str, str]], ...]) -> str:
        if len(keys) == 0:
            return ""
        nodes = list[str]()
        nodes.append('<node id="Keys"><children>')
        for key in keys:
            nodes.append('<node id="Key">')
            for k, v in key.items():
                t, val = v
                nodes.append(f'<attribute id="{k}" type="{t}" value="{val}" />')
            nodes.append('</node>')
        nodes.append('</children></node>')
        return "".join(nodes)

    @staticmethod
    def create_loca_xml_file(dir_path: str, mod_name: str, content: dict[str, tuple[int, str]]) -> str:
        file_path = os.path.join(dir_path, mod_name)
        file_path += ".loca.xml"
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wt") as fd:
            fd.write('<?xml version="1.0" encoding="utf-8"?>\n')
            fd.write('<contentList>\n')
            for k, v in content.items():
                uuid = k
                version = v[0]
                text = v[1]
                fd.write(f"""    <content contentuid="{uuid}" version="{version}">{text}</content>""")
            fd.write('</contentList>\n')
        return file_path