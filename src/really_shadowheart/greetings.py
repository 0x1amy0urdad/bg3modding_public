from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

################################################################################################
# Shadowheart's greetings
################################################################################################

def create_greetings() -> None:
    ################################################################################################
    # Dialog: CAMP_Shadowheart_CRD_SharedFuture.lsf
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/Camp_Relationship_Dialogs/CAMP_Shadowheart_CRD_SharedFuture.lsf'))

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Then sounds like I have everything I need - more of life than I'd ever imagined possible, without Shar.
    d.set_dialog_flags('0ae96d3a-27b0-2fa4-42cd-5a987b18836b', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shared_Future_With_Shadowheart.uuid, True, slot_idx_tav),
        )),
    ))

    # What more could I need? If I had all that, and I had you... that's more of a life that I ever dared to dream of.
    d.set_dialog_flags('26d82675-85f4-6600-5bd1-0f4b01565e53', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shared_Future_With_Shadowheart.uuid, True, slot_idx_tav),
        )),
    ))

    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    approval_80_greetings_node_uuid = '80fc8153-9363-4c6f-a3bc-ec5e81cbc08a'
    approval_40_greetings_node_uuid = '4c2f28c3-4a1b-370a-73f8-d2bfcea53e9d'


    d.create_standard_dialog_node(
        approval_80_greetings_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        d.get_children_nodes_uuids(approval_40_greetings_node_uuid),
        [
            bg3.text_content('hd0509e5dgee24g4e38g9e53gd72e5795cba6', 1, 'e4b1d9bf-135b-45e6-847a-8463012c6866', custom_sequence_id = 'e4b1d9bf-135b-45e6-847a-8463012c6866'),
            bg3.text_content('h58a61da8g7b5ag4f8agbac5g354f62512e77', 3, 'a577d549-8937-4e3a-b988-d8ccaaebb569', custom_sequence_id = 'a577d549-8937-4e3a-b988-d8ccaaebb569'),
            bg3.text_content('ha2c23788g2acdg4d58gabe0g0caffdc54064', 3, 'd208eefa-aad3-47af-ab98-ea9a42441a71', custom_sequence_id = 'd208eefa-aad3-47af-ab98-ea9a42441a71'),
            bg3.text_content('h089930fdg3555g4822gae62g09abc9d6fee2', 3, '59aa4791-0680-46f4-9950-a3f89e632a48', custom_sequence_id = '59aa4791-0680-46f4-9950-a3f89e632a48'),
            bg3.text_content('h0633cd9bg74dfg4126g9e4fg65ca5667b814', 2, '62719932-ea92-4880-a0c0-92b1e4d7cdb4', custom_sequence_id = '62719932-ea92-4880-a0c0-92b1e4d7cdb4'),
        ],
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartMoreOpportunitiesToSlipAway.uuid, True, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_80_For_Sp2, True, slot_idx_shadowheart)
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MALE, True, slot_idx_tav),
            ))
        )
    )

    # Checking in on me? I'm right where I'm supposed to be - with the man I love.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.696,
        approval_80_greetings_node_uuid,
        ((5.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 6.2,
        line_index = 0,
        emotions = {
            #bg3.SPEAKER_SHADOWHEART: ((0.0, 64, 1), (2.61, 64, 1), (5.0, 2, 1)),
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
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        6.2,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Aren't you a sight for sore eyes.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.01,
        approval_80_greetings_node_uuid,
        ((2.23, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 2.6,
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
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        2.6,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Did you want something? If not, I'm perfectly happy to just gaze upon you a while.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.5,
        approval_80_greetings_node_uuid,
        ((7.5, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.0,
        line_index = 2,
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
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.0,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Why hello, lover... that sounded more debonaire in my head, I'll admit. Do you need something?<br>
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.72,
        approval_80_greetings_node_uuid,
        ((7.8, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 8.1,
        line_index = 3,
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
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        8.1,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    # Good. I was just starting to miss the sound of your voice.
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.96,
        approval_80_greetings_node_uuid,
        ((5, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '95a53513-08ce-4d80-ae74-e306b51db565')),
        phase_duration = 5.36,
        line_index = 4,
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
        bg3.SPEAKER_SHADOWHEART,
        0.0,
        5.36,
        (t.create_look_at_key(0.0, target = bg3.SPEAKER_PLAYER, bone = 'Head_M', turn_mode = 2, reset = True),),
        is_snapped_to_end = True
    )

    t.update_duration()

    node_index = d.get_root_node_index(approval_40_greetings_node_uuid)
    d.add_root_node(approval_80_greetings_node_uuid, index = node_index)

add_build_procedure('create_greetings', create_greetings)