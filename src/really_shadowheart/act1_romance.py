from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *


def patch_waterfall_wine_drinking_scene() -> None:
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Camp/Campfire_Moments/CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/Gustav/Timeline/Generated/CAMP_GoblinHuntCelebration_SD_ROM_NightWithShadowheart.lsf'), d)

    """
    <attribute id="Position" type="fvec3">
        <float3 x="0.81432176" y="0.14" z="0.71399999"/>
    </attribute>
    <attribute id="RotationQuat" type="fvec4">
        <float4 x="-0.000915015" y="0.98133606" z="-0.058707781" w="-0.18311819"/>
    </attribute>
    """

    tav_speaker_slot_idx = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    body_type_fork_node = 'b5ee413f-64a7-4667-b5c7-0870db80d2a1'

    ori_cinematic_node_uuid = 'a3ecdd8e-5976-b241-685a-cd86fafd3bfc'
    ori_visual_state_node_uuid = 'c8aff38c-3717-e3f3-40d8-0c570401c9ba'
    ori_nearly_light_node_uuid = '45e17618-65cb-dd84-65df-fe59eac4d2d6'

    ori_new_memories_node_uuid = '02960967-b62d-cf4b-736c-43999433345c'
    ori_night_ahead_of_us_node_uuid = 'f942b94b-68e2-f898-d647-08d6d2845f59'

    ori_nearly_light_camera_transform = 'af851c13-de4d-41ba-8cf7-a2de3b8920cb'
    ori_nearly_light_camera_fov = 'abc98063-15de-45b8-b00d-f30d2de91f11'
    ori_nearly_light_voice = 'dcb8824d-4484-45d0-9def-dd93a532230b'

    bt1_cinematic_node_uuid = '2d080bc5-a51d-48d3-9644-2509734d9db2'
    bt1_visual_state_node_uuid = 'c4b500da-7fd1-46fd-9c90-ba927205e38a'
    bt1_nearly_light_node_uuid = '17d4b114-1c07-47cc-8154-f595324040de'

    bt2_cinematic_node_uuid = '3ca3c666-1ac5-49fe-93ae-75a92dbc3dae'
    bt2_visual_state_node_uuid = '6ab6b525-e21a-4687-b568-0c83f158ec03'
    bt2_nearly_light_node_uuid = 'ca5df79f-aa4c-453b-b671-1caf3672156f'

    bt3_cinematic_node_uuid = '79d96f69-4a96-4227-8fee-adb76b24873d'
    bt3_visual_state_node_uuid = '94b7b0fc-ae2c-4369-9e47-75a701c2b6d6'
    bt3_nearly_light_node_uuid = 'd702effb-eb65-4a41-a778-e50a13ef4039'

    bt4_cinematic_node_uuid = '5d74b6bc-f898-4476-8d91-f9424d231740'
    bt4_visual_state_node_uuid = '5c61c7c5-2bfb-4ac3-8228-817941155a7d'
    bt4_nearly_light_node_uuid = '607ac158-310d-4a0a-a1f0-6280d638d2c7'

    dwarf_bt1_cinematic_node_uuid = '62a15b7f-7feb-41d8-8177-12698f5f51a9'
    dwarf_bt1_visual_state_node_uuid = 'a8bd4a19-aaf9-4580-952d-4c3745874222'
    dwarf_bt1_nearly_light_node_uuid = '46dc6adf-df4d-4797-b134-f922f204ced2'

    dwarf_bt2_cinematic_node_uuid = '8d25e05b-e972-4ea6-987e-10285569a112'
    dwarf_bt2_visual_state_node_uuid = '177a5222-3e16-4518-83b4-c166d6f24364'
    dwarf_bt2_nearly_light_node_uuid = '262eafbf-fc5d-4278-b486-73fb4c25720c'

    short_bt1_cinematic_node_uuid = 'd2299051-9e2f-40e4-8361-9d68bb9892e5'
    short_bt1_visual_state_node_uuid = 'efeb70ea-f405-4345-ab37-a85d2926b8d2'
    short_bt1_nearly_light_node_uuid = '94e4c35c-cabc-4fbf-af2f-51de5b81c587'

    short_bt2_cinematic_node_uuid = 'c366a5ab-0213-469a-8d62-048d1e1e8e7b'
    short_bt2_visual_state_node_uuid = '70669dfc-feea-46a1-9a62-699c37af1cde'
    short_bt2_nearly_light_node_uuid = 'fd9cb182-0fff-451f-a536-2938b8a674f2'

    children_nodes = d.get_children_nodes_uuids(ori_nearly_light_node_uuid)

    d.create_standard_dialog_node(
        body_type_fork_node,
        bg3.SPEAKER_SHADOWHEART,
        [
            dwarf_bt1_cinematic_node_uuid,
            dwarf_bt2_cinematic_node_uuid,
            short_bt1_cinematic_node_uuid,
            short_bt2_cinematic_node_uuid,
            bt3_cinematic_node_uuid,
            bt1_cinematic_node_uuid,
            bt4_cinematic_node_uuid,
            bt2_cinematic_node_uuid
        ],
        None)
    d.delete_all_children_dialog_nodes(ori_new_memories_node_uuid)
    d.delete_all_children_dialog_nodes(ori_night_ahead_of_us_node_uuid)
    d.add_child_dialog_node(ori_new_memories_node_uuid, body_type_fork_node)
    d.add_child_dialog_node(ori_night_ahead_of_us_node_uuid, body_type_fork_node)

    ################################################
    # Short body type 1
    ################################################
    d.create_cinematic_dialog_node(
        short_bt1_cinematic_node_uuid,
        [short_bt1_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, tav_speaker_slot_idx),
                bg3.flag(bg3.TAG_FEMALE, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = short_bt1_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        short_bt1_visual_state_node_uuid,
        [short_bt1_nearly_light_node_uuid],
        group_id = short_bt1_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        short_bt1_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = short_bt1_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    short_bt1_nearly_light_camera_transform = '98916b3d-f198-41e5-bc94-bb7042b18a50'
    short_bt1_nearly_light_camera_fov = 'b2cccd36-2249-4d37-843f-bbb682772b1e'
    short_bt1_nearly_light_voice = 'f052f298-e261-44ec-8e2f-3ae2e7ffa4f0'
    t.create_new_phase(short_bt1_cinematic_node_uuid, 23.0, additional_nodes = (short_bt1_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: short_bt1_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: short_bt1_nearly_light_camera_fov,
        ori_nearly_light_voice: short_bt1_nearly_light_voice,
    })
    short_bt1_nearly_light_voice_node = t.find_tl_node(short_bt1_nearly_light_voice)
    bg3.set_bg3_attribute(short_bt1_nearly_light_voice_node, 'DialogNodeId', short_bt1_nearly_light_node_uuid)
    bg3.set_bg3_attribute(short_bt1_nearly_light_voice_node, 'ReferenceId', short_bt1_nearly_light_node_uuid)
    
    # Gnome/halfling BT1 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            # move towards Shadowheart
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.93),
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.89),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.17),
        ),
        (
            # move down
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.85),
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.98),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 5, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ), is_snapped_to_end = True)

    t.edit_tl_transform(short_bt1_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(short_bt1_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))


    ################################################
    # Short body type 2
    ################################################
    d.create_cinematic_dialog_node(
        short_bt2_cinematic_node_uuid,
        [short_bt2_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = short_bt2_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        short_bt2_visual_state_node_uuid,
        [short_bt2_nearly_light_node_uuid],
        group_id = short_bt2_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        short_bt2_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = short_bt2_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    short_bt2_nearly_light_camera_transform = '568df27b-cb91-4fc0-ae88-fde87d2cfcf2'
    short_bt2_nearly_light_camera_fov = 'd4d5e89c-fd16-4223-a395-9374a1e7efe5'
    short_bt2_nearly_light_voice = 'a8a09e9b-0539-4615-83fb-e91a0db89e31'
    t.create_new_phase(short_bt2_cinematic_node_uuid, 23.0, additional_nodes = (short_bt2_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: short_bt2_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: short_bt2_nearly_light_camera_fov,
        ori_nearly_light_voice: short_bt2_nearly_light_voice,
    })
    short_bt2_nearly_light_voice_node = t.find_tl_node(short_bt2_nearly_light_voice)
    bg3.set_bg3_attribute(short_bt2_nearly_light_voice_node, 'DialogNodeId', short_bt2_nearly_light_node_uuid)
    bg3.set_bg3_attribute(short_bt2_nearly_light_voice_node, 'ReferenceId', short_bt2_nearly_light_node_uuid)
    
    # Gnome/halfling BT2 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            # move towards Shadowheart
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.91),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.15),
        ),
        (
            # move down
            t.create_value_key(time = 10.43, interpolation_type = 5, value = 0.9),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 5, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ), is_snapped_to_end = True)

    t.edit_tl_transform(short_bt2_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(short_bt2_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))


    ################################################
    # Dwarf body type 1
    ################################################
    d.create_cinematic_dialog_node(
        dwarf_bt1_cinematic_node_uuid,
        [dwarf_bt1_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, tav_speaker_slot_idx),
                bg3.flag(bg3.TAG_FEMALE, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = dwarf_bt1_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        dwarf_bt1_visual_state_node_uuid,
        [dwarf_bt1_nearly_light_node_uuid],
        group_id = dwarf_bt1_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        dwarf_bt1_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = dwarf_bt1_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    dwarf_bt1_nearly_light_camera_transform = '107fd708-1f9e-445e-9085-77d2f39e62ae'
    dwarf_bt1_nearly_light_camera_fov = '1147290d-5a3f-4efb-afed-87aedb629c71'
    dwarf_bt1_nearly_light_voice = '904f5c88-3312-4ea0-afdb-59dbfa4beabb'
    t.create_new_phase(dwarf_bt1_cinematic_node_uuid, 23.0, additional_nodes = (dwarf_bt1_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: dwarf_bt1_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: dwarf_bt1_nearly_light_camera_fov,
        ori_nearly_light_voice: dwarf_bt1_nearly_light_voice,
    })
    dwarf_bt1_nearly_light_voice_node = t.find_tl_node(dwarf_bt1_nearly_light_voice)
    bg3.set_bg3_attribute(dwarf_bt1_nearly_light_voice_node, 'DialogNodeId', dwarf_bt1_nearly_light_node_uuid)
    bg3.set_bg3_attribute(dwarf_bt1_nearly_light_voice_node, 'ReferenceId', dwarf_bt1_nearly_light_node_uuid)
    
    # Dwarf BT1 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            # move towards Shadowheart
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.93),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.17),
        ),
        (
            # move down
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.85),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ), is_snapped_to_end = True)

    t.edit_tl_transform(dwarf_bt1_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(dwarf_bt1_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    ################################################
    # Dwarf body type 2
    ################################################
    d.create_cinematic_dialog_node(
        dwarf_bt2_cinematic_node_uuid,
        [dwarf_bt2_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = dwarf_bt2_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        dwarf_bt2_visual_state_node_uuid,
        [dwarf_bt2_nearly_light_node_uuid],
        group_id = dwarf_bt2_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        dwarf_bt2_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = dwarf_bt2_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    dwarf_bt2_nearly_light_camera_transform = '234c21ae-33f3-4ccc-93c0-2b0f7ee9a9b3'
    dwarf_bt2_nearly_light_camera_fov = '2c1d4933-4435-41a9-9fe2-f19c2df59ba9'
    dwarf_bt2_nearly_light_voice = 'b58461dd-1fef-415a-9eaf-2fdecfcb4cb4'
    t.create_new_phase(dwarf_bt2_cinematic_node_uuid, 23.0, additional_nodes = (dwarf_bt2_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: dwarf_bt2_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: dwarf_bt2_nearly_light_camera_fov,
        ori_nearly_light_voice: dwarf_bt2_nearly_light_voice,
    })
    dwarf_bt2_nearly_light_voice_node = t.find_tl_node(dwarf_bt2_nearly_light_voice)
    bg3.set_bg3_attribute(dwarf_bt2_nearly_light_voice_node, 'DialogNodeId', dwarf_bt2_nearly_light_node_uuid)
    bg3.set_bg3_attribute(dwarf_bt2_nearly_light_voice_node, 'ReferenceId', dwarf_bt2_nearly_light_node_uuid)
    
    # Dwarf BT2 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            # move closer
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.88),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.14),
        ),
        (
            # move down
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.98
                               ),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_transform(dwarf_bt2_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(dwarf_bt2_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    ################################################
    # Body type 1
    ################################################
    d.create_cinematic_dialog_node(
        bt1_cinematic_node_uuid,
        [bt1_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = bt1_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        bt1_visual_state_node_uuid,
        [bt1_nearly_light_node_uuid],
        group_id = bt1_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        bt1_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = bt1_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    bt1_nearly_light_camera_transform = '132269b5-4c8c-4bd3-b2a7-159d73e4e718'
    bt1_nearly_light_camera_fov = 'd671ad54-0daf-4235-ad78-41b90d8b3466'
    bt1_nearly_light_voice = '39446077-8b14-40f0-9022-ed033536e387'
    t.create_new_phase(bt1_cinematic_node_uuid, 23.0, additional_nodes = (bt1_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: bt1_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: bt1_nearly_light_camera_fov,
        ori_nearly_light_voice: bt1_nearly_light_voice,
    })
    bt1_nearly_light_voice_node = t.find_tl_node(bt1_nearly_light_voice)
    bg3.set_bg3_attribute(bt1_nearly_light_voice_node, 'DialogNodeId', bt1_nearly_light_node_uuid)
    bg3.set_bg3_attribute(bt1_nearly_light_voice_node, 'ReferenceId', bt1_nearly_light_node_uuid)
    
    # BT1 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.81432176),
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.96),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.17),
        ),
        (
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.714),
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.80),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_transform(bt1_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(bt1_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    ################################################
    # Body type 2
    ################################################
    d.create_cinematic_dialog_node(
        bt2_cinematic_node_uuid,
        [bt2_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        group_id = bt2_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        bt2_visual_state_node_uuid,
        [bt2_nearly_light_node_uuid],
        group_id = bt2_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        bt2_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = bt2_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    bt2_nearly_light_camera_transform = '43e9d67b-bd47-418f-b781-b5f08d9812ba'
    bt2_nearly_light_camera_fov = '760dd785-c55f-4370-b266-e33be65aefa4'
    bt2_nearly_light_voice = '47e5830d-37d2-49d9-b384-19475571f2f9'
    t.create_new_phase(bt2_cinematic_node_uuid, 23.0, additional_nodes = (bt2_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: bt2_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: bt2_nearly_light_camera_fov,
        ori_nearly_light_voice: bt2_nearly_light_voice,
    })
    bt2_nearly_light_voice_node = t.find_tl_node(bt2_nearly_light_voice)
    bg3.set_bg3_attribute(bt2_nearly_light_voice_node, 'DialogNodeId', bt2_nearly_light_node_uuid)
    bg3.set_bg3_attribute(bt2_nearly_light_voice_node, 'ReferenceId', bt2_nearly_light_node_uuid)
    
    # BT2 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.94),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.14),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.78),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_transform(bt2_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.3308871),
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
            #t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.94),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            #t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 2.06, 0, sequence = 'yxz')),
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
            #t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 28.62, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(bt2_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    ################################################
    # Body type 3
    ################################################
    d.create_cinematic_dialog_node(
        bt3_cinematic_node_uuid,
        [bt3_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, tav_speaker_slot_idx),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = bt3_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        bt3_visual_state_node_uuid,
        [bt3_nearly_light_node_uuid],
        group_id = bt3_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        bt3_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = bt3_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    bt3_nearly_light_camera_transform = 'cb4b2094-075d-462e-bf2a-405e3260429f'
    bt3_nearly_light_camera_fov = '79e357fb-17fc-4f3a-8e30-3d7dc5d5ae38'
    bt3_nearly_light_voice = 'e9c9834f-532b-4a7c-8f35-d8d3c796f438'
    t.create_new_phase(bt3_cinematic_node_uuid, 23.0, additional_nodes = (bt3_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: bt3_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: bt3_nearly_light_camera_fov,
        ori_nearly_light_voice: bt3_nearly_light_voice,
    })
    bt3_nearly_light_voice_node = t.find_tl_node(bt3_nearly_light_voice)
    bg3.set_bg3_attribute(bt3_nearly_light_voice_node, 'DialogNodeId', bt3_nearly_light_node_uuid)
    bg3.set_bg3_attribute(bt3_nearly_light_voice_node, 'ReferenceId', bt3_nearly_light_node_uuid)
    
    # BT3 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.94),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.14),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.78),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_transform(bt3_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(bt3_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    ################################################
    # Body type 4
    ################################################
    d.create_cinematic_dialog_node(
        bt4_cinematic_node_uuid,
        [bt4_visual_state_node_uuid],
        speaker = bg3.SPEAKER_SHADOWHEART,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, tav_speaker_slot_idx),
            )),
        ),
        group_id = bt4_cinematic_node_uuid,
        group_index = 0,
        show_once = True)
    d.create_cinematic_dialog_node(
        bt4_visual_state_node_uuid,
        [bt4_nearly_light_node_uuid],
        group_id = bt4_cinematic_node_uuid,
        group_index = 1,
        visual_state = True,
        show_once = True)
    d.create_standard_dialog_node(
        bt4_nearly_light_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hf11ba7fbg84dfg4f0eg8bdbgddeb015c8334', 1),
        group_id = bt4_cinematic_node_uuid,
        group_index = 2,
        setflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_Camp_Event_SkipSleepCutscene, True, None),
            )),
        ))
    
    bt4_nearly_light_camera_transform = '40c2a9b5-01ff-4142-a570-f46b7c433ffb'
    bt4_nearly_light_camera_fov = '259d4ffb-edb4-40e2-a812-a5b3c32c5c59'
    bt4_nearly_light_voice = 'f612289e-b040-4410-a9ae-0709387a8e3c'
    t.create_new_phase(bt4_cinematic_node_uuid, 23.0, additional_nodes = (bt4_nearly_light_node_uuid,))
    t.copy_tl_nodes_to_current_phase(ori_cinematic_node_uuid, node_id_map = {
        ori_nearly_light_camera_transform: bt4_nearly_light_camera_transform,
        ori_nearly_light_camera_fov: bt4_nearly_light_camera_fov,
        ori_nearly_light_voice: bt4_nearly_light_voice,
    })
    bt4_nearly_light_voice_node = t.find_tl_node(bt4_nearly_light_voice)
    bg3.set_bg3_attribute(bt4_nearly_light_voice_node, 'DialogNodeId', bt4_nearly_light_node_uuid)
    bg3.set_bg3_attribute(bt4_nearly_light_voice_node, 'ReferenceId', bt4_nearly_light_node_uuid)
    
    # BT4 player position
    t.create_tl_transform(bg3.SPEAKER_PLAYER, 10.43, 23.0, (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.81432176),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.14),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.714),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-158.79434, 6.63588, 1.13671, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_transform(bt4_nearly_light_camera_transform, channels = (
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 1.768583),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.768583),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.76),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = 0.04885589),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = 0.04885589),
        ),
        (
            t.create_value_key(time = 10.43, interpolation_type = 0, value = bg3.euler_to_quaternion(-81.8184, 21.03, 0, sequence = 'yxz')),
            t.create_value_key(time = 23.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-81.8184, 40.0, 0, sequence = 'yxz')),
        ),
        (),
        ()
    ))

    t.edit_tl_camera_fov(bt4_nearly_light_camera_fov, keys = (
        t.create_value_key(time = 10.43, value_name = 'FoV', value = 32.0),
    ))

    t.update_duration()

add_build_procedure('patch_waterfall_wine_drinking_scene', patch_waterfall_wine_drinking_scene)

