from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

################################################################################################
# Shadowheart's greetings
################################################################################################
something_the_matter_node_uuid = '5f864b1a-65af-45de-ac29-d27242ab07b7'

def create_greetings() -> None:
    ############################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ############################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    tav_cheated_greeting_node_uuid = '3d54008c-057f-47ed-8bde-6c236d7da47e'
    i_need_to_think_node_uuid = 'ac9ea285-9901-4fae-b7f6-785fafb82814'
    i_digress_node_uuid = 'c95f06c1-3b2d-4f3a-89a0-47e90c1761db'
    approval_80_greetings_male_node_uuid = '80fc8153-9363-4c6f-a3bc-ec5e81cbc08a'
    approval_80_greetings_female_node_uuid = '8d8076e7-1bf1-4a91-95f2-469986a6a5bb'
    approval_40_greetings_node_uuid = '4c2f28c3-4a1b-370a-73f8-d2bfcea53e9d'

    sleep_together_entry_point_node_uuid = '80ad286d-cf0a-4737-9261-3b4a8e6ee797'
    shadowheart_hesitates_to_ask_node_uuid = 'e0fbf080-1b83-4de8-9ddd-717b4c56b011'
    dialog_flow_node_uuid = '313eed6b-ac15-4ebe-894d-4844163fb36c'
    please_tell_me_node_uuid = 'fb1fae6d-386f-4a2f-be91-12f3b61658ca'
    very_well_node_uuid = '28faa883-7814-4786-91bc-6b3a4f269a93'
    wine_more_often_node_uuid = '9e750a0a-3de3-47d7-bf64-724f2bf4d3b9'
    awfully_cold_node_uuid = '730c51a2-aa91-43c9-8b0d-27b56260268b'
    you_dont_need_wine_node_uuid = '8d5b9ad9-7186-48d3-98c9-892640b532ec'
    id_gladly_kill_a_bottle_node_uuid = 'c6774d31-9526-4f5d-8209-5d2abc4b9bb6'
    i_feel_the_same_way_node_uuid = '64aab437-c9b0-4e61-948b-4e285a25bd37'
    more_than_one_way_keep_me_warm_node_uuid = '9dc01dba-c3ff-4f10-8d35-6d247a76783e'
    room_for_you_and_the_bottle_node_uuid = '6552fdfa-a30b-4f2d-b5aa-5715a689efc6'
    good_enough_for_me_node_uuid = 'd9248dcf-2289-43f2-a180-3e9837ab18c4'
    jump_back_node_uuid = 'f09c2d44-ef52-43ae-ae80-254fc05c9db1'

    children_nodes = d.get_children_nodes_uuids(approval_40_greetings_node_uuid)
    d.delete_all_children_dialog_nodes(approval_40_greetings_node_uuid)
    d.add_child_dialog_node(approval_40_greetings_node_uuid, sleep_together_entry_point_node_uuid)

    d.create_jump_dialog_node(jump_back_node_uuid, something_the_matter_node_uuid, 2)

    # Shadowheart hesitates to ask Tav about sleeping together at night
    d.create_standard_dialog_node(
        sleep_together_entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [shadowheart_hesitates_to_ask_node_uuid, dialog_flow_node_uuid],
        None)
    d.create_cinematic_dialog_node(
        shadowheart_hesitates_to_ask_node_uuid,
        [dialog_flow_node_uuid],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav),
                bg3.flag(Shadowheart_Hesitated_To_Ask.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Noticed_Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        dialog_flow_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        None)

    phase_duration = 4.5
    t.create_new_phase(shadowheart_hesitates_to_ask_node_uuid, phase_duration)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_PLAYER, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 64),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0, phase_duration,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0, phase_duration,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_shot('95a53513-08ce-4d80-ae74-e306b51db565', 0.0, 2.0)
    t.create_tl_shot('8942c483-83c9-4974-9f47-87cd1dd10828', 2.0, phase_duration - 0.1)
    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART,
        2.0, phase_duration,
        '5db0326e-fb0e-d3dd-a56d-51aa4da6ab00',
        '13ccbef4-3a1f-4c55-988d-b79aa094db1d',
        animation_play_rate = 0.8,
        fade_in = 0.0,
        fade_out = 0.0,
        is_snapped_to_end = 0.0)
    t.create_tl_shot('cde43894-62c3-4f23-8ea7-b772f9357697', phase_duration - 0.1, phase_duration, is_snapped_to_end = True)

    # You were looking at me like you wanted to say something. Don't be shy, tell me.
    d.create_standard_dialog_node(
        please_tell_me_node_uuid,
        bg3.SPEAKER_PLAYER,
        [very_well_node_uuid],
        bg3.text_content('h35eecf11g59ceg496bg9d60g37fe40337891', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_BGO_Main_A, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
                bg3.flag(Tav_Noticed_Shadowheart_Hesitated_To_Ask.uuid, True, slot_idx_shadowheart),
            )),
        ))
    d.add_child_dialog_node(something_the_matter_node_uuid, please_tell_me_node_uuid, index = 0)

    # Very well...
    d.create_standard_dialog_node(
        very_well_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [wine_more_often_node_uuid],
        bg3.text_content('h93eaf8e9g2808g47cdgbd6egc9add28a87c0', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.9135,
        very_well_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        phase_duration = 1.1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        1.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        1.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # We should've had wine more often. More warming than the fire.
    d.create_standard_dialog_node(
        wine_more_often_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [awfully_cold_node_uuid],
        bg3.text_content('h1717338fga82bg4f20ga158g6dbca07e41f3', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.97,
        wine_more_often_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = 4.1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 2), (2.9, 1024, 0)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        4.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        4.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # After all, it can get awfully cold at night out here in this wilderness...
    d.create_standard_dialog_node(
        awfully_cold_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [id_gladly_kill_a_bottle_node_uuid, you_dont_need_wine_node_uuid],
        bg3.text_content('h592daa08g31f9g418eg9be7g0ed58daf3b49', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.71,
        awfully_cold_node_uuid,
        ((5.7, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 5.8,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.16, 32, None), (4.7, 1024, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        5.8,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        5.8,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You don't need wine if you have me. I can keep you warm all night. There's room for you in my bedroll.
    d.create_standard_dialog_node(
        you_dont_need_wine_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_feel_the_same_way_node_uuid],
        bg3.text_content('h0d248adbg6d7cg4e55gb525gd439c5d526d9', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, True, slot_idx_tav),
            )),
        ))

    # I'm glad. I feel the same way.
    reaction_plus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 5 }, uuid = '9f79f483-4cc1-4aef-9402-83ec7502ed25')
    d.create_standard_dialog_node(
        i_feel_the_same_way_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h5fb51729g09b2g4e2dgbdceg2d86d3c32275', 1),
        approval_rating_uuid=reaction_plus_5.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.1,
        i_feel_the_same_way_node_uuid,
        ((4.1, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2')),
        phase_duration = 4.2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        4.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        4.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you manage to save one of those liberated vintages? I'd gladly kill a bottle or two.
    d.create_standard_dialog_node(
        id_gladly_kill_a_bottle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [more_than_one_way_keep_me_warm_node_uuid],
        bg3.text_content('h1cde79d9g165bg4f6fg9025g57881c3491f6', 1),
        constructor = bg3.dialog_object.QUESTION)

    # There's more than one way to keep me warm.
    d.create_standard_dialog_node(
        more_than_one_way_keep_me_warm_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [you_dont_need_wine_node_uuid, room_for_you_and_the_bottle_node_uuid],
        bg3.text_content('hc792b085g2c19g430fgb461g700fd3588775', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.7,
        more_than_one_way_keep_me_warm_node_uuid,
        ((2.7, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 3.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.0, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        })
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        3.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        3.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)

    # There's room for you in my bedroll. And the bottle.
    d.create_standard_dialog_node(
        room_for_you_and_the_bottle_node_uuid,
        bg3.SPEAKER_PLAYER,
        [good_enough_for_me_node_uuid],
        bg3.text_content('hc875bd6cgdffag4bc1gb668g133a1cf06ba5', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, True, slot_idx_tav),
            )),
        ))

    # That's good enough for me.
    d.create_standard_dialog_node(
        good_enough_for_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('h08ccc8afgb1dag4ea7g907eg5760821bdca7', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        1.95,
        good_enough_for_me_node_uuid,
        ((1.95, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2')),
        phase_duration = 2.1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        })
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True)


    # I can't help but notice you seem happier of late. There's a spring in your step that wasn't there before.
    d.create_standard_dialog_node(
        tav_cheated_greeting_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_need_to_think_node_uuid],
        bg3.text_content('h9a16a3c8g8292g4e7ag93f0g2b5e721d602e', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Cheated_On_Shadowheart.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Reacted_To_Cheating.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Reacted_To_Cheating.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.7,
        tav_cheated_greeting_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        phase_duration = 8.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.54, 1024, 2), (4.46, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None), (4.0, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # I'm not sure I want to know...
    d.create_standard_dialog_node(
        i_need_to_think_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_digress_node_uuid],
        bg3.text_content('h9f205acbg8e31g462bgbfbbg956e9f1fb647', 1),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.477,
        i_need_to_think_node_uuid,
        #((None, 'b188e5c9-4ec1-456f-8408-b4a5da405cc5'),),
        #((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        #((4.0, '95a53513-08ce-4d80-ae74-e306b51db565'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        # cde43894-62c3-4f23-8ea7-b772f9357697
        # fd96b957-6a74-4f97-a035-eb9641c48242
        ((4.0, 'cde43894-62c3-4f23-8ea7-b772f9357697'), (None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 5.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((4.0, 64, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((1.0, '8128cb03-b18f-46c9-aca9-1c93991cf4ef', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        5.5,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        5.5,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # But I digress. Did you want something?
    d.create_standard_dialog_node(
        i_digress_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('hdcd786d5gf823g4367g8227gc8254d5ac7e8', 2),
        constructor = bg3.dialog_object.ANSWER)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.96,
        i_digress_node_uuid,
        ((4.0, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 4.1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (2.2, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        4.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        4.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )


    d.create_standard_dialog_node(
        approval_80_greetings_male_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        [
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, 'e4b1d9bf-135b-45e6-847a-8463012c6866', custom_sequence_id = 'e4b1d9bf-135b-45e6-847a-8463012c6866'),
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, 'fd040b4f-2f98-4a14-8637-871e005f3f4a', custom_sequence_id = 'fd040b4f-2f98-4a14-8637-871e005f3f4a'),
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, '2a0925e2-918f-454a-b959-1088b620adf5', custom_sequence_id = '2a0925e2-918f-454a-b959-1088b620adf5'),
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, '93e2cc80-a6d8-44d2-8199-28d9acb49966', custom_sequence_id = '93e2cc80-a6d8-44d2-8199-28d9acb49966'),
            bg3.text_content('h58a61da8g7b5ag4f8agbac5g354f62512e77', 3, 'a577d549-8937-4e3a-b988-d8ccaaebb569', custom_sequence_id = 'a577d549-8937-4e3a-b988-d8ccaaebb569'),
            bg3.text_content('ha2c23788g2acdg4d58gabe0g0caffdc54064', 3, 'd208eefa-aad3-47af-ab98-ea9a42441a71', custom_sequence_id = 'd208eefa-aad3-47af-ab98-ea9a42441a71'),
            bg3.text_content('h089930fdg3555g4822gae62g09abc9d6fee2', 3, '59aa4791-0680-46f4-9950-a3f89e632a48', custom_sequence_id = '59aa4791-0680-46f4-9950-a3f89e632a48'),
            bg3.text_content('h0633cd9bg74dfg4126g9e4fg65ca5667b814', 2, '62719932-ea92-4880-a0c0-92b1e4d7cdb4', custom_sequence_id = '62719932-ea92-4880-a0c0-92b1e4d7cdb4'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MALE, True, slot_idx_tav),
            ))
        ))

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.696,
        approval_80_greetings_male_node_uuid,
        ((5.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.2,
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.696,
        approval_80_greetings_male_node_uuid,
        ((5.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.2,
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.696,
        approval_80_greetings_male_node_uuid,
        ((5.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.2,
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.696,
        approval_80_greetings_male_node_uuid,
        ((5.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.2,
        line_index = 3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.29, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Aren't you a sight for sore eyes.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.01,
        approval_80_greetings_male_node_uuid,
        ((2.23, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.6,
        line_index = 4,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you want something? If not, I'm perfectly happy to just gaze upon you a while.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.5,
        approval_80_greetings_male_node_uuid,
        ((7.5, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.0,
        line_index = 5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.23, 4, None), (4.02, 1024, 1), (5.83, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Why hello, lover... that sounded more debonaire in my head, I'll admit. Do you need something?<br>
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.72,
        approval_80_greetings_male_node_uuid,
        ((7.8, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.1,
        line_index = 6,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.91, 2, 23), (2.79, 2, 1), (6.48, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        8.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Good. I was just starting to miss the sound of your voice.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.96,
        approval_80_greetings_male_node_uuid,
        ((5, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 5.36,
        line_index = 7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.6, 64, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        5.36,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        5.36,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You may be what's been missing from my life.
    d.create_standard_dialog_node(
        approval_80_greetings_female_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [sleep_together_entry_point_node_uuid],
        [
            bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, '6d564eb5-06d4-485a-807d-41520b49a54f', custom_sequence_id = '6d564eb5-06d4-485a-807d-41520b49a54f'),
            bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, '1216b29f-d790-4f92-aa27-335ef85b9090', custom_sequence_id = '1216b29f-d790-4f92-aa27-335ef85b9090'),
            bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, 'd1cb10d5-b80c-47a0-a720-fa4e21e3328c', custom_sequence_id = 'd1cb10d5-b80c-47a0-a720-fa4e21e3328c'),
            bg3.text_content('h8d6dc67fg9d25g4231g9188g177f1c53b322', 2, 'baa40e34-2d0c-4a9a-8e96-dc9eac53955f', custom_sequence_id = 'baa40e34-2d0c-4a9a-8e96-dc9eac53955f'),
            bg3.text_content('h58a61da8g7b5ag4f8agbac5g354f62512e77', 3, '8a7f1a61-c327-48ea-932b-90709cf7a9e8', custom_sequence_id = '8a7f1a61-c327-48ea-932b-90709cf7a9e8'),
            bg3.text_content('ha2c23788g2acdg4d58gabe0g0caffdc54064', 3, 'd2f5a568-b211-4e55-ab6e-ed8fc04c4761', custom_sequence_id = 'd2f5a568-b211-4e55-ab6e-ed8fc04c4761'),
            bg3.text_content('h089930fdg3555g4822gae62g09abc9d6fee2', 3, 'e7878c05-d73e-469a-9f83-a687e45a2c1f', custom_sequence_id = 'e7878c05-d73e-469a-9f83-a687e45a2c1f'),
            bg3.text_content('h0633cd9bg74dfg4126g9e4fg65ca5667b814', 2, '55bc1c66-c6f1-477c-b710-877e8ec19e44', custom_sequence_id = '55bc1c66-c6f1-477c-b710-877e8ec19e44'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, slot_idx_tav)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            ))
        ))

    # You may be what's been missing from my life.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.604,
        approval_80_greetings_female_node_uuid,
        ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.7,
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You may be what's been missing from my life.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.604,
        approval_80_greetings_female_node_uuid,
        ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.7,
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You may be what's been missing from my life.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.604,
        approval_80_greetings_female_node_uuid,
        ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.7,
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # You may be what's been missing from my life.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.604,
        approval_80_greetings_female_node_uuid,
        ((2.604, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.7,
        line_index = 3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.7,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Aren't you a sight for sore eyes.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.01,
        approval_80_greetings_female_node_uuid,
        ((2.23, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.6,
        line_index = 4,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you want something? If not, I'm perfectly happy to just gaze upon you a while.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.5,
        approval_80_greetings_female_node_uuid,
        ((7.5, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.0,
        line_index = 5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.23, 4, None), (4.02, 1024, 1), (5.83, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Why hello, lover... that sounded more debonaire in my head, I'll admit. Do you need something?<br>
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.72,
        approval_80_greetings_female_node_uuid,
        ((7.8, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.1,
        line_index = 6,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.91, 2, 23), (2.79, 2, 1), (6.48, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        8.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Good. I was just starting to miss the sound of your voice.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.96,
        approval_80_greetings_female_node_uuid,
        ((5, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 5.36,
        line_index = 7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.6, 64, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),)
        }
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        5.36,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_PLAYER,
        0.0,
        5.36,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_SHADOWHEART, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )


    ###############################################################################
    # Tav did something that will cause Shadowheart to reject marriage proposal
    ###############################################################################
    in_need_of_attention_node_uuid = '5da1bb39-0494-4787-80f9-26413183c498'
    few_occasions_given_me_doubts_node_uuid = '12bde6cd-12ee-4219-aedc-a17ff830483d'
    were_just_too_different_node_uuid = '6d2d7f03-7e0e-4ebc-9989-53354790028a'
    we_cant_pretend_node_uuid = '92fe1f40-15b9-456a-b724-ba2e7b117d47'
    take_things_as_they_come_node_uuid = 'faeeef9a-65a1-4938-b648-92972ccd0413'
    nothing_more_to_be_said_node_uuid = 'ab9de392-4084-4067-9e8f-28baec7b4784'

    jump_back_node_uuid = '3b6eeb56-3db2-42b8-96a6-9a1b73357b85'

    were_doing_great_together_node_uuid = '2c228652-4ad5-42c9-ba84-748349b68f2d'
    had_i_done_something_node_uuid = '24ed394b-e426-42a4-8a8d-5473d5a1a12c'
    i_didnt_expect_you_like_that_node_uuid = '750f3121-55ed-4c02-8bf8-630f126b063b'
    its_the_opposite_node_uuid = 'f1102cb6-4ff2-47a1-b79c-932b85bdfb9d'

    # In need of attention, I take it?
    d.create_standard_dialog_node(
        in_need_of_attention_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            were_doing_great_together_node_uuid,
            i_didnt_expect_you_like_that_node_uuid,
            had_i_done_something_node_uuid,
            its_the_opposite_node_uuid
        ],
        bg3.text_content('hdcf8e090g9bbeg4352ga4b7g955471d143c4', 3),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, False, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                #bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            ))
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Rejects_Proposal.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Tav_Sleep_Together.uuid, False, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.49,
        in_need_of_attention_node_uuid,
        ((2.49, '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.8,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.01, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })

    # Am I? I thought we were doing great together, but now I am not sure.
    d.create_standard_dialog_node(
        were_doing_great_together_node_uuid,
        bg3.SPEAKER_PLAYER,
        [few_occasions_given_me_doubts_node_uuid],
        bg3.text_content('h208de7e1g4c8bg4828ga771g0d5ae624e63d', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Had I done something? Something that upset you? Tell me, I could do better next time.
    d.create_standard_dialog_node(
        had_i_done_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        [we_cant_pretend_node_uuid],
        bg3.text_content('hc70f7dfdg98e7g4e41g9ee4g88a6502124c8', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Why, I didn't expect to hear you speaking like that.
    d.create_standard_dialog_node(
        i_didnt_expect_you_like_that_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nothing_more_to_be_said_node_uuid],
        bg3.text_content('h2756a7e4g929eg4533g9b0cgf5232e323f14', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # But it's the opposite, isn't it? You were trying to get my attention lately.
    d.create_standard_dialog_node(
        its_the_opposite_node_uuid,
        bg3.SPEAKER_PLAYER,
        [nothing_more_to_be_said_node_uuid],
        bg3.text_content('h132e0bdege62fg43d1ga95fg11c17111e614', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True)

    # Well... since then, there's been a few occasions where you've given me doubts. Said things, or done things...
    d.create_standard_dialog_node(
        few_occasions_given_me_doubts_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [were_just_too_different_node_uuid],
        bg3.text_content('h0fb40b24gb09dg4c37gade4gd03b7e79d750', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        11.56,
        few_occasions_given_me_doubts_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 11.7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (1.4, 4, None), (3.12, 64, None), (5.62, 4, None), (8.98, 32, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })

    # Made me wonder if perhaps we're just too different. If we should just let things lie.
    d.create_standard_dialog_node(
        were_just_too_different_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('he3fb77aag6e0ag4cc4gb1cfgc7d96426324f', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        6.19,
        were_just_too_different_node_uuid,
        ((6.19, '0e8837db-4344-48d0-9175-12262c73806b'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (3.68, 4, None), (5.55, 16, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })

    d.create_jump_dialog_node(jump_back_node_uuid, in_need_of_attention_node_uuid, 2)

    # Don't. We can't pretend to be someone we're not - either of us. It'll just end badly.
    d.create_standard_dialog_node(
        we_cant_pretend_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [take_things_as_they_come_node_uuid],
        bg3.text_content('h6d8757ccgc91eg4d61gb239g5399f29ff092', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        8.52,
        we_cant_pretend_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 8.6,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, None), (1.61, 32, None), (5.69, 2048, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })

    # Let's just... take things in as they come.
    d.create_standard_dialog_node(
        take_things_as_they_come_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h4148e233g5535g4c07ga75cg34aea80fea52', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.85,
        take_things_as_they_come_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = 4.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })


    # Oh... I see. Well in that case, I suppose there's nothing more to be said on the matter.
    d.create_standard_dialog_node(
        nothing_more_to_be_said_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h51e0aa30g444dg42fbga21fgd6339b3ad12c', 1),
        end_node = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Approval_Set_To_35.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.27,
        nothing_more_to_be_said_node_uuid,
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 7.3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (3.68, 4, None), (5.55, 16, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })


    t.update_duration()

    node_index = d.get_root_node_index(approval_40_greetings_node_uuid)
    d.add_root_node(approval_80_greetings_male_node_uuid, index = node_index)
    d.add_root_node(approval_80_greetings_female_node_uuid, index = node_index)
    d.add_root_node(in_need_of_attention_node_uuid, index = node_index)
    d.add_root_node(tav_cheated_greeting_node_uuid, index = node_index)

    # This replaces
    # "I wanted to talk about our relationship."
    # with
    # "I want to talk about us."
    d.set_tagged_text('5fd62d4b-a8b1-23bc-8582-fc20d5e5f04e', bg3.text_content('h1e8574a0gb5d2g48abg95a9gbe6264723760', 1))

def create_health_check() -> None:
    ############################################################################################
    # Mod health check
    ############################################################################################

    """
        "h5692a0a3gb7a1g4bb5g92d4gd2f9c470fea8": (1, "&lt;i&gt;ReallyShadowheart: health check.&lt;/i&gt;"),
        "h85351a0fg6554g433fg85d5gf789e019bef8": (1, "&lt;i&gt;ReallyShadowheart: health check passed.&lt;/i&gt;"),
        "h2b6aae90g166ag462eg9448g46ee4c649ed9": (1, "&lt;i&gt;ReallyShadowheart: Osiris health check failed.&lt;/i&gt;"),
        "h981348a1g38a0g45dbg869fgf0c747341ab4": (1, "&lt;i&gt;ReallyShadowheart: ScriptExtender health check failed.&lt;/i&gt;"),
        "h2fa20812g9b85g4bcfg8cf0g0feacd08bfad": (1, "&lt;i&gt;ReallyShadowheart: both Osiris and ScriptExtender health checks failed.&lt;/i&gt;"),
    """

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    health_check_entry_node_uuid = 'ece12fef-66f7-42a8-bb01-928daaa01d13'
    health_check_step1_node_uuid = '24f5282a-cae0-4244-b17b-63808180818f'
    health_check_step2_node_uuid = '6a7a4a3b-43d6-4b33-b1af-d8f811ae89ed'
    health_check_step3_node_uuid = '5b482d6d-b2b6-418b-993f-72ec5f9dbae7'
    health_check_passed_node_uuid = 'da7a78ef-2d45-4228-954f-d856e9e54c55'
    health_check_osi_failed_node_uuid = '7401a4bf-9b2f-4c91-bffa-14d326230b5c'
    health_check_se_failed_node_uuid = '89d2a2b6-3303-497b-bc99-5b06f616565f'
    health_check_osi_se_failed_node_uuid = 'ad29bdb7-0eb6-4bae-a19a-c7929ed2e116'
    exit_node_uuid = '24dc92cc-bf7d-4475-8cdd-cf122fc99221'

    d.add_child_dialog_node(something_the_matter_node_uuid, health_check_entry_node_uuid)

    d.create_standard_dialog_node(
        health_check_entry_node_uuid,
        bg3.SPEAKER_PLAYER,
        [health_check_step1_node_uuid],
        bg3.text_content('h5692a0a3gb7a1g4bb5g92d4gd2f9c470fea8', 1),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        health_check_step1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [health_check_step2_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check.uuid, False, slot_idx_tav),
                bg3.flag(Osiris_Health_Check_Passed.uuid, False, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check.uuid, False, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check_Passed.uuid, False, slot_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        health_check_step2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [health_check_step3_node_uuid],
        None,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check.uuid, True, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check.uuid, True, slot_idx_tav),
            )),
        ))
    d.create_standard_dialog_node(
        health_check_step3_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            health_check_passed_node_uuid,
            health_check_osi_failed_node_uuid,
            health_check_se_failed_node_uuid,
            health_check_osi_se_failed_node_uuid,
        ],
        None)

    d.create_standard_dialog_node(
        health_check_passed_node_uuid,
        bg3.SPEAKER_PLAYER,
        [exit_node_uuid],
        bg3.text_content('h5692a0a3gb7a1g4bb5g92d4gd2f9c470fea8', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check_Passed.uuid, True, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check_Passed.uuid, True, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        health_check_osi_failed_node_uuid,
        bg3.SPEAKER_PLAYER,
        [exit_node_uuid],
        bg3.text_content('h2b6aae90g166ag462eg9448g46ee4c649ed9', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check_Passed.uuid, False, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check_Passed.uuid, True, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        health_check_se_failed_node_uuid,
        bg3.SPEAKER_PLAYER,
        [exit_node_uuid],
        bg3.text_content('h981348a1g38a0g45dbg869fgf0c747341ab4', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check_Passed.uuid, True, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check_Passed.uuid, False, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        health_check_osi_se_failed_node_uuid,
        bg3.SPEAKER_PLAYER,
        [exit_node_uuid],
        bg3.text_content('h2fa20812g9b85g4bcfg8cf0g0feacd08bfad', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Osiris_Health_Check_Passed.uuid, False, slot_idx_tav),
                bg3.flag(ScriptExtender_Health_Check_Passed.uuid, False, slot_idx_tav),
            )),
        ),
        constructor = bg3.dialog_object.QUESTION)

    d.create_standard_dialog_node(
        exit_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True)

def create_rehearsal_node() -> None:

    """
        "h25ae89f3g08c4g47fegb737gb796065444b0": (1, "Could you &lt;i&gt;please&lt;/i&gt; stop reading that bloody reddit, get your ass out from the house, and help me out in the garden?"),
    """

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)


    test_question_node_uuid = 'e54bbb16-882c-45d4-9f04-8d0466ee93a9'
    test_answer_node_uuid = 'd33294d8-698d-4d19-b474-ce94e264aeee'
    d.create_standard_dialog_node(
        test_question_node_uuid,
        bg3.SPEAKER_PLAYER,
        [test_answer_node_uuid],
        bg3.text_content('h42d1b00bg51a3g4375gb34dge423a6fe72e8', 1),
        constructor = bg3.dialog_object.QUESTION)

    # And watch out for Raphael. He's better at getting into people's heads than you are, you ass.
    d.create_standard_dialog_node(
        test_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h25ae89f3g08c4g47fegb737gb796065444b0', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.69,
        test_answer_node_uuid,
        ((None, '8942c483-83c9-4974-9f47-87cd1dd10828'),),
        phase_duration = 6.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (0.93, 4, None), (2.79, 4, 2), (4.76, 128, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),),
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', 3),),
        })
    d.add_child_dialog_node(something_the_matter_node_uuid, test_question_node_uuid)
    t.update_duration()

add_build_procedure('create_greetings', create_greetings)
