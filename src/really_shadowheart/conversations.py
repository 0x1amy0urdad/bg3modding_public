from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

################################################################################################
# Conversations with Shadowheart
################################################################################################

def create_recurrent_conversations() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    speaker_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    conversations_root_node_uuid = '5f864b1a-65af-45de-ac29-d27242ab07b7'
    topic_list_node_uuid = 'f654c44d-f6e6-4518-b2ff-1701028d13f7'
    ask_you_about_mentioned_earlier_node_uuid = 'ee19b863-c409-4ac5-ad05-b2cb3f44e792'
    talk_about_something_else_node_uuid = 'a6664aa7-c29c-421a-8e78-712540d7b21e'
    jump_back_node_uuid = '11bf5079-6bf4-49ce-9a3e-4ebc7f909955'
    fine_if_you_insist_node_uuid = 'b8f1ba30-7bd6-4666-832f-76d8beb97773'
    of_course_node_uuid = '34b08a0b-1622-4f85-a4bf-d4a704dd0664'
    gladly_node_uuid = 'd7718188-e909-436b-967d-4bf9433272de'
    ofcourse_node_uuid = '3fbea392-fee9-48a4-a332-d9b748697340'


    """
    cameras
    d76eaab3-040b-4871-9c1d-4a8624f37cd2 SH  -> SH
    0e8837db-4344-48d0-9175-12262c73806b SH  -> SH
    8942c483-83c9-4974-9f47-87cd1dd10828 Tav -> SH
    2b1dd4ed-5f01-46a2-a244-ac074d0feff0 Tav -> Tav
    95a53513-08ce-4d80-ae74-e306b51db565 Tav -> Tav
    cde43894-62c3-4f23-8ea7-b772f9357697 Tav -> Tav
    fd96b957-6a74-4f97-a035-eb9641c48242 SH  -> Tav
    b188e5c9-4ec1-456f-8408-b4a5da405cc5 Tav -> SH
    """

    d.create_jump_dialog_node(jump_back_node_uuid, conversations_root_node_uuid, 2)

    alias_tell_me_about_fear_node_uuid = '4f2910ee-e2b0-4695-80ec-cf87c23c5481'
    alias_whats_the_story_odd_artifact_node_uuid = '62024cb7-b670-4d96-a872-07e04a555f20'
    alias_know_each_other_node_uuid = '2c3b320e-c2b3-41c3-b301-56c32811422e'
    alias_i_want_to_get_to_know_you_more_node_uuid = '1b466975-78be-4def-94a8-91262a139dd1'
    alias_you_worship_shar_selune_node_uuid = '04d4ff74-4fb6-4345-8267-fda9f96b328e'
    alias_why_were_you_in_pain_node_uuid = '94118018-3efc-499a-b237-3f053ee0baf8'
    alias_flareups_im_concerned_low_trust_node_uuid = 'da2f5067-7292-4f2e-b2e2-5e9842030339'
    alias_help_me_understand_wound_node_uuid = '9e555b1b-f11f-4919-9c1d-99bb551ae8b7'
    alias_tell_me_more_about_mother_superior_node_uuid = 'a53a364c-ab4f-42bb-9d11-89d2050c05f3'
    alias_must_be_a_way_to_heal_it_node_uuid = 'b7a6e096-e835-44e4-b594-43c21196e363'
    alias_the_curse_isnt_affecting_you_node_uuid = 'f00e50a4-56a8-46ef-8934-27d284b9651d'
    alias_that_grave_did_it_mean_something_node_uuid = 'ab140c80-aca4-4808-ad65-557d6656f972'
    alias_that_graffiti_we_saw_node_uuid = '6c5a09ac-17e4-4d06-8eea-89369675b216'
    alias_so_you_had_hideout_node_uuid = '7a398d00-59b4-4f9b-be83-1a8150098d71'
    alias_memories_discussion_selune_parents_saved_node_uuid = 'c0a99345-f89e-403b-b8bc-9dcf2a059746'
    alias_memories_discussion_selune_parents_killed_node_uuid = '5077e27c-c047-4a79-97e4-b17c9bb17142'
    alias_memories_discussion_shar_parents_saved_node_uuid = 'f6891dde-db2d-4faa-aef4-511d47bbecf9'

    i_want_to_pray_with_you_node_uuid = '35f7eb91-d690-4137-a0f4-876937a31a99'

    topics = [
        alias_tell_me_about_fear_node_uuid,
        alias_whats_the_story_odd_artifact_node_uuid,
        alias_know_each_other_node_uuid,
        alias_i_want_to_get_to_know_you_more_node_uuid,
        alias_you_worship_shar_selune_node_uuid,
        alias_why_were_you_in_pain_node_uuid,
        alias_flareups_im_concerned_low_trust_node_uuid,
        alias_help_me_understand_wound_node_uuid,
        alias_tell_me_more_about_mother_superior_node_uuid,
        alias_must_be_a_way_to_heal_it_node_uuid,
        alias_the_curse_isnt_affecting_you_node_uuid,
        alias_that_grave_did_it_mean_something_node_uuid,
        alias_that_graffiti_we_saw_node_uuid,
        alias_so_you_had_hideout_node_uuid,
        alias_memories_discussion_selune_parents_saved_node_uuid,
        alias_memories_discussion_selune_parents_killed_node_uuid,
        alias_memories_discussion_shar_parents_saved_node_uuid,
        talk_about_something_else_node_uuid,
    ]

    d.create_standard_dialog_node(
        topic_list_node_uuid,
        bg3.SPEAKER_PLAYER,
        topics,
        None)

    condition_dating_node_uuid = 'fe042ad4-6071-4c65-9b68-adf905098ec5'
    condition_high_approval_node_uuid = 'f5e85e62-952a-4021-b384-b1b62df94b70'
    condition_knows_shar_worship_node_uuid = '2a38a339-180d-4e2d-bdc1-b24c67660cbc'

    # I want to pray with you to your goddess.
    d.create_standard_dialog_node(
        i_want_to_pray_with_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        ['472e19a0-94c5-4f93-92bc-074da3d3fede'],
        bg3.text_content('h92e55267ga65ag4dfdgadcfgebb601a079ee', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Prayer_Event.uuid, True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Prayed_With_Her.uuid, True, speaker_idx_tav),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.create_nested_dialog_node(
        '472e19a0-94c5-4f93-92bc-074da3d3fede',
        'd71b23ba-6d5a-b71b-a1f9-bca2944c6a62',
        [jump_back_node_uuid],
        speaker_count = 7)

    # I want to ask you about something you mentioned earlier.
    d.create_standard_dialog_node(
        ask_you_about_mentioned_earlier_node_uuid,
        bg3.SPEAKER_PLAYER,
        [condition_dating_node_uuid, condition_high_approval_node_uuid, condition_knows_shar_worship_node_uuid, fine_if_you_insist_node_uuid],
        bg3.text_content('he3a0d778g05c4g4a26gaffcg576978f906a7', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    d.create_standard_dialog_node(
        condition_dating_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [of_course_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_shadowheart),
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, speaker_idx_tav)
            )),
        ))
    d.create_standard_dialog_node(
        condition_high_approval_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [of_course_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    d.create_standard_dialog_node(
        condition_knows_shar_worship_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [of_course_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_20_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))


    # Fine, if you insist.
    # Fine. Just keep out matters that don't concern you.
    d.create_standard_dialog_node(
        fine_if_you_insist_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [topic_list_node_uuid],
        [
            bg3.text_content('h8ca3accfgefdag4f15gaf74ge5d672fef3af', 1, '2db0bfef-16c3-4e1d-b47a-f1cbefb43fd0', custom_sequence_id = '2db0bfef-16c3-4e1d-b47a-f1cbefb43fd0'),
            bg3.text_content('hccdbd99bg8066g41d3ga622g9b3ad197abbc', 1, 'bb1630e0-925c-48a0-b196-cd55ebc3de49', custom_sequence_id = 'bb1630e0-925c-48a0-b196-cd55ebc3de49'),
        ])
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.05,
        fine_if_you_insist_node_uuid,
        ((3.2, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 3.3,
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None), (1.1, 2048, None),)
        })
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.631,
        fine_if_you_insist_node_uuid,
        ((3.8, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 4.0,
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None), (1.2, 2048, None),)
        })

    # By all means.
    # Of course.
    d.create_standard_dialog_node(
        of_course_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [topic_list_node_uuid],
        [
            bg3.text_content('h5d734366g7655g42ebgb239g6ccf3752cb62', 1, 'aa9dde75-f73a-4326-b25b-84669a4d4a7f', custom_sequence_id = 'aa9dde75-f73a-4326-b25b-84669a4d4a7f'),
            bg3.text_content('h5da02478g29e4g4cdega14cg92a8f3b7cb7f', 1, 'fcd44c01-6a5f-4e00-8411-b19f817f144b', custom_sequence_id = 'fcd44c01-6a5f-4e00-8411-b19f817f144b'),
        ])
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.9,
        of_course_node_uuid,
        ((1.1, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 1.4,
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),)
        })
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.9,
        of_course_node_uuid,
        ((1.1, '8942c483-83c9-4974-9f47-87cd1dd10828'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 1.4,
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1),)
        })


    # Let's talk about something else.
    d.create_standard_dialog_node(
        talk_about_something_else_node_uuid,
        bg3.SPEAKER_PLAYER,
        [gladly_node_uuid, ofcourse_node_uuid],
        bg3.text_content('h203c71e0g0992g46b8g939eg52adc1d0d7c7', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Gladly.
    d.create_standard_dialog_node(
        gladly_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('hfa539d78g5f25g4c8fg999agf1056b000d5f', 2),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, speaker_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.95,
        gladly_node_uuid,
        ((1.2, '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 1.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),)
        })

    # Of course
    d.create_standard_dialog_node(
        ofcourse_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [jump_back_node_uuid],
        bg3.text_content('he581660cg380dg496eg98ecg07d934167a8b', 1)) 
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.95,
        ofcourse_node_uuid,
        ((1.2, '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'fd96b957-6a74-4f97-a035-eb9641c48242')),
        phase_duration = 1.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, None),)
        })

    d.add_child_dialog_node(conversations_root_node_uuid, i_want_to_pray_with_you_node_uuid, index = 1)
    d.add_child_dialog_node(conversations_root_node_uuid, ask_you_about_mentioned_earlier_node_uuid, index = 1)

    tell_me_about_fear_node_uuid = 'f7807efd-4aa0-1b73-6586-49ac60fc6334' # existing node
    wolf_fear_greeting_node_uuid = '535f019b-e243-87f4-dc12-f7ef8127a40d'  # existing node
    whats_the_story_odd_artifact_node_uuid = 'fd3f1005-8cd6-4260-993e-183012f41e0e' # existing node
    know_each_other_node_uuid = '89eea7bd-ca95-4e6e-892f-fd1498aa99f0' # existing node
    i_want_to_get_know_you_more = '71cc008d-0e4a-4a29-83ea-f2a0d4d42f11' # existing node
    you_worship_shar_selune_node_uuid = '7e5f2c8d-b6a1-f21b-14ac-8e3c6a6c1659' # existing node
    why_were_you_in_pain_1_node_uuid = 'ef330806-f5d9-7af5-2c45-53608eddc799' # existing node
    why_were_you_in_pain_2_node_uuid = 'c77a9451-7a9b-2eb0-4ab8-e83ed9d5b88c' # existing node
    why_were_you_in_pain_3_node_uuid = 'cced6497-5b88-0de2-6c81-e488224b26da' # existing node
    why_were_you_in_pain_4_node_uuid = '46d214e0-87b7-3cf5-c750-61ada5811204' # existing node
    flareups_im_concerned_low_trust_node_uuid = '272c6c10-3a5d-e779-19f0-754ca5ab907b' # existing node
    help_me_understand_wound_node_uuid = '555dd7ea-56d0-04b9-eae1-01f5ea578c59' # existing node
    must_be_a_way_to_heal_it_node_uuid = '613074ad-0257-616b-b7ab-76d467706e91' # existing node
    the_curse_isnt_affecting_you_greet_node_uuid = '6438618d-2f44-bdf8-d493-7417dd8adb32' # existing node
    the_curse_isnt_affecting_you_node_uuid = 'fd4dad5a-9cbf-2b81-f98f-270f9fb88538' # existing node
    tell_me_more_about_mother_superior_node_uuid = '4e8b0236-d03c-bd9c-5267-f3b786253468' # existing node
    that_grave_did_it_mean_something_greet_node_uuid = 'e984cbd9-8e17-2f75-2ae2-d231c560e20d'
    that_grave_did_it_mean_something_node_uuid = '51f00d93-d908-53f1-307d-79ec1189ff10'
    that_graffiti_we_saw_greet_node_uuid = '6c4a525c-7217-8a37-5bc8-b8ea46bd6d64'
    that_graffiti_we_saw_node_uuid = '89c73887-81c8-3289-232c-efc44dad93c8'
    so_you_had_hideout_greet_node_uuid = 'da318c55-dadc-d887-59d4-418b59ea708a'
    so_you_had_hideout_node_uuid = '317802f1-4297-ce3c-5166-d9d7c2cb1eac'

    # Tell me about your fear of wolves.
    d.create_standard_dialog_node(
        alias_tell_me_about_fear_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(tell_me_about_fear_node_uuid),
        bg3.text_content("h2ec9e310g8c3eg4efeg9e52ga930c366a9b2", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('2a7514a0-e41e-49f6-a5c9-18cd3b4187b2', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_WolfFear, True, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Tell_Me_About_Fear.uuid, True, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(tell_me_about_fear_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Tell_Me_About_Fear.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(wolf_fear_greeting_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Tell_Me_About_Fear.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # What's the story with that odd little artefact you have?
    d.create_standard_dialog_node(
        alias_whats_the_story_odd_artifact_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(whats_the_story_odd_artifact_node_uuid),
        bg3.text_content("hf5c3d51egadc4g46eag90d7gb8df75c770cb", 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('a97cfd0e-ab96-4c28-84a0-4d086fc2889b', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_SeenWithBox, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Whats_The_Story_Odd_Artifact.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(whats_the_story_odd_artifact_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Whats_The_Story_Odd_Artifact.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # We should get to know each other a little more.
    d.create_standard_dialog_node(
        alias_know_each_other_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(know_each_other_node_uuid),
        bg3.text_content("h7439a0f7gb385g44bbg938age86c8df0605a", 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('b4fe5970-e8fd-4de1-b2a1-d5cd0eca633d', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(Alias_Know_Each_Other.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(know_each_other_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Know_Each_Other.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # I want to get to know you more, Shadowheart.
    d.create_standard_dialog_node(
        alias_i_want_to_get_to_know_you_more_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(i_want_to_get_know_you_more),
        bg3.text_content("h4de317fcg152cg45c9gb381g89f82af8db9e", 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('7d559817-f55b-4b22-ad1c-02a5a6087fd9', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, False, speaker_idx_tav),
                bg3.flag(Alias_I_Want_To_Get_To_Know_You_More.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(i_want_to_get_know_you_more, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_I_Want_To_Get_To_Know_You_More.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # So - you worship Shar, and I serve Selûne... dare I ask how you feel about that?
    d.create_standard_dialog_node(
        alias_you_worship_shar_selune_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(you_worship_shar_selune_node_uuid),
        bg3.text_content("h6038f6c0g553bg410egb5e8g4e879b0ccab0", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('237ae6c8-663f-41a1-a4ef-d4f46e44b948', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Alias_You_Worship_Shar_Selune.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Selune, True, speaker_idx_tav),
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(you_worship_shar_selune_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_You_Worship_Shar_Selune.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # Why were you in pain before?
    d.create_standard_dialog_node(
        alias_why_were_you_in_pain_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(why_were_you_in_pain_1_node_uuid),
        bg3.text_content("h3c747b6fg14f7g4dc8gbdb7g406c5c1639f8", 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('cb6e5de7-a8df-49e1-900c-db757ac46942', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Alias_Why_Were_You_In_Pain.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(why_were_you_in_pain_1_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Why_Were_You_In_Pain.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(why_were_you_in_pain_2_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Why_Were_You_In_Pain.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(why_were_you_in_pain_3_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Why_Were_You_In_Pain.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(why_were_you_in_pain_4_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Why_Were_You_In_Pain.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # These... flare-ups you're experiencing. I'm concerned.
    d.create_standard_dialog_node(
        alias_flareups_im_concerned_low_trust_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(flareups_im_concerned_low_trust_node_uuid),
        bg3.text_content("h83eda4b9g2611g464bga373gb76161fe2193", 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('6e4a7449-b91d-4f7f-be26-1ab6cc149f3c', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Alias_Flareups_Iam_Concerned_Low_Trust.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(flareups_im_concerned_low_trust_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Flareups_Iam_Concerned_Low_Trust.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # Help me understand this wound of yours, Shadowheart.
    d.create_standard_dialog_node(
        alias_help_me_understand_wound_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(help_me_understand_wound_node_uuid),
        bg3.text_content("h4e824742g70bbg4660g8b71gc4f6c6b0f7e2", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('6382fb99-7d4e-4562-83b6-587829d2a06d', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Help_Me_Understand_Wound.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(help_me_understand_wound_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Help_Me_Understand_Wound.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # Your wound is causing you too much pain, Shadowheart. There must be a way to heal it.
    d.create_standard_dialog_node(
        alias_must_be_a_way_to_heal_it_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(must_be_a_way_to_heal_it_node_uuid),
        bg3.text_content("hbd2866b8gf83cg48cag97cfg2e05acac709e", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('908f6c67-423f-4446-ad19-933e9694c070', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Must_Be_Way_To_Heal_It.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(must_be_a_way_to_heal_it_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Must_Be_Way_To_Heal_It.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # Is it true, what you said? The curse isn't affecting you?
    d.create_standard_dialog_node(
        alias_the_curse_isnt_affecting_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(the_curse_isnt_affecting_you_node_uuid),
        bg3.text_content("h99268c58gd6b0g4797g9fccgc8035bf51043", 2),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('31b85210-0f85-421c-b9f1-b0db0d9b8e89', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(The_Curse_Isnt_Affecting_You.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(the_curse_isnt_affecting_you_greet_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(The_Curse_Isnt_Affecting_You.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(the_curse_isnt_affecting_you_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(The_Curse_Isnt_Affecting_You.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # Tell me more about the Mother Superior.
    d.create_standard_dialog_node(
        alias_tell_me_more_about_mother_superior_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(tell_me_more_about_mother_superior_node_uuid),
        bg3.text_content("h7f40572ag7799g4a39gbcdcgd6418d02dc31", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('36700081-4f52-4974-9c2f-09a7da0add2f', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tell_Me_More_About_Mother_Superior.uuid, True, speaker_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, speaker_idx_shadowheart),
                bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, speaker_idx_shadowheart),
            ))
        ))
    d.add_dialog_flags(tell_me_more_about_mother_superior_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Tell_Me_More_About_Mother_Superior.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # That grave you lingered at before - did it mean something to you?
    d.create_standard_dialog_node(
        alias_that_grave_did_it_mean_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(that_grave_did_it_mean_something_node_uuid),
        bg3.text_content("hd5d5228fg079bg4547gb193g60d7a1e6368f", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('ea8ace0b-3130-4381-a639-c007e65e8741', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(That_Grave_Did_It_Mean_Something.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_dialog_flags(that_grave_did_it_mean_something_greet_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(That_Grave_Did_It_Mean_Something.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(that_grave_did_it_mean_something_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(That_Grave_Did_It_Mean_Something.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # That graffiti we saw - you remember it?
    d.create_standard_dialog_node(
        alias_that_graffiti_we_saw_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(that_graffiti_we_saw_node_uuid),
        bg3.text_content("h436a7977g1186g469bga9eega848cf839e83", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('4a29e000-eb00-42ff-881f-a7ab13ce6880', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(That_Graffiti_We_Saw.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_dialog_flags(that_graffiti_we_saw_greet_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(That_Graffiti_We_Saw.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(that_graffiti_we_saw_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(That_Graffiti_We_Saw.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # So you had your own little hiding place in the Sharran Cloister? Why?
    d.create_standard_dialog_node(
        alias_so_you_had_hideout_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(so_you_had_hideout_node_uuid),
        bg3.text_content("h9cf872eag8dbeg47dbg859bg0947e1719a49", 3),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('754f3390-b9aa-46d1-b919-3ec77989ac86', True, speaker_idx_tav),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(So_You_Had_Hideout.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_dialog_flags(so_you_had_hideout_greet_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(So_You_Had_Hideout.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))
    d.add_dialog_flags(so_you_had_hideout_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(So_You_Had_Hideout.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    ########################################################################################
    # Bugfix: after saving parents when on enemy of shar path, the discussion about her
    #         memories was under Shadowheart_InParty_Event_SavedParentsMemoriesEnemy flag
    #         which is the Shar path flag. Obviously, the conversation never popped up.
    #         Also, this fix makes that conversation a recurring one.
    ########################################################################################

    memories_discussion_selune_parents_saved_node_uuid = 'db424664-9086-bb2a-2f73-62b9ab38c641' # existing node
    memories_discussion_selune_parents_killed_node_uuid = 'ac4359eb-ae3a-87c3-4405-2c0ee04bd934' # existing node
    memories_discussion_shar_parents_saved_node_uuid = '287b8eb3-4501-97af-f5a8-4fb7c9928257' # existing node

    # Selune path, saved parents
    d.set_dialog_flags(
        memories_discussion_selune_parents_saved_node_uuid,
        checkflags=(
            bg3.flag_group('Dialog', (
                bg3.flag('df37eece-b396-4243-a9ad-1d3a25441553', True, speaker_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Memories_Discussion_Selune_Parents_Saved.uuid, True, speaker_idx_shadowheart),
                bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
            ))
        ))

    # What about the memories that were taken from you?
    d.create_standard_dialog_node(
        alias_memories_discussion_selune_parents_saved_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(memories_discussion_selune_parents_saved_node_uuid),
        bg3.text_content("h39ccea34g324cg4ff5gb04egbe1c8e74ff80", 2),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('2eb239a8-f3f6-474f-a2a7-636ff19407f0', True, speaker_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Memories_Discussion_Selune_Parents_Saved.uuid, True, speaker_idx_shadowheart),
            )),
        ))

    # What about the memories that were taken from you?
    d.create_standard_dialog_node(
        alias_memories_discussion_selune_parents_killed_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(memories_discussion_selune_parents_killed_node_uuid),
        bg3.text_content("h757f113ag8bbag40a7g978dg9cc4ba68941e", 2),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('2825740b-0dc2-4e82-8ce4-ef6b87ea810b', True, speaker_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Memories_Discussion_Selune_Parents_Killed.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_dialog_flags(memories_discussion_selune_parents_killed_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Memories_Discussion_Selune_Parents_Killed.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))

    # What about the memories that were taken from you?
    d.create_standard_dialog_node(
        alias_memories_discussion_shar_parents_saved_node_uuid,
        bg3.SPEAKER_PLAYER,
        d.get_children_nodes_uuids(memories_discussion_shar_parents_saved_node_uuid),
        bg3.text_content("hcf0725c0g7210g410dg9db4gb0864a19811c", 2),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('ad4382a9-a10c-4c2f-981c-6da40ac4682b', True, speaker_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(Alias_Memories_Discussion_Shar_Parents_Saved.uuid, True, speaker_idx_shadowheart),
            )),
        ))
    d.add_dialog_flags(memories_discussion_shar_parents_saved_node_uuid, setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Alias_Memories_Discussion_Shar_Parents_Saved.uuid, True, speaker_idx_shadowheart),
            bg3.flag(Enable_Recurring_Convos.uuid, True, speaker_idx_shadowheart),
        )),
    ))


def patch_conversations() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Make "What do you think of all that's happened to us so far?" a permanent dialog option
    what_do_you_think_node_uuid = '438627c9-bcd0-43c7-86db-f3193873fb38'
    d.set_dialog_flags(what_do_you_think_node_uuid, checkflags=(), setflags=(
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_HappenedThought, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_attribute(what_do_you_think_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    ################################################################################################
    # Dialog: ShadowHeart_Recruitment_Beach.lsf
    # Shadowheart on the beach is less appreciative when Tav saves her
    # Approval increase reduced to 3 instead of 10
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Companions/ShadowHeart_Recruitment_Beach.lsf'))

    # replace +10 with +3
    reaction_plus_3 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 3 }, uuid = 'cfbfcb19-0881-438d-8f60-5258b910920f')
    ill_remember_that_node_uuid = 'b24c2a6c-9a76-30c2-8a78-5263283b7ff9'
    d.set_dialog_attribute(ill_remember_that_node_uuid, 'ApprovalRatingID', reaction_plus_3.uuid)

    ################################################################################################
    # The following makes a few more conversations accessible for longer
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    #
    # This will prevent lines under "I want to get to know you more, Shadowheart." from disappearing
    #
    what_drew_you_to_shar_worship = '4b2787dc-b2b5-4a58-afb1-fbffec2b218c'
    d.set_dialog_flags(what_drew_you_to_shar_worship, setflags=(), checkflags=())

    tell_me_something_about_yourself = '453889f3-47a2-4a0e-9ece-571effb963de'
    d.set_dialog_flags(tell_me_something_about_yourself, setflags=(), checkflags=())

    there_has_to_be_more = '3a5a50de-18f7-40e8-a83b-6f1296eba165'
    d.set_dialog_flags(there_has_to_be_more, setflags=(), checkflags=())


    # Make "You must have thoughts about our little stowaways." available until act 3
    thoughts_about_stowaways_node_uuid = '1735f36f-79b2-404f-a028-eea5511f1d4d'
    d.set_dialog_flags(thoughts_about_stowaways_node_uuid, setflags=(), checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_COL_PartyProgress_EnteredColony, False, None),
        )),
    ))
    d.set_dialog_attribute(thoughts_about_stowaways_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "What will you do, if we actually manage to remove the tadpoles?" available until it is known Shadowheart worships Shar
    what_will_you_do_node_uuid = '49292b6b-5bde-41a6-bd27-48b8aabab092'
    d.set_dialog_flags(what_will_you_do_node_uuid, setflags=(), checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, False, None),
        )),
    ))
    d.set_dialog_attribute(what_will_you_do_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "What do you think about what happened to the druid grove?" available until act 2
    grove_victory_node_uuid = '66aa48ae-781d-46a2-89e3-4b959be6694c'
    grove_victory_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, True, None),
        bg3.flag(bg3.DEN_GoblinHunt_Event_LeaderMetPlayer, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, True, None),
    ))
    d.set_dialog_flags(grove_victory_node_uuid, setflags=(), checkflags=[grove_victory_flag_group])
    d.set_dialog_attribute(grove_victory_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    grove_victory_spared_minthara_node_uuid = 'b742835b-8214-4740-a23f-b3671aea9e4c'
    druid_victory_spared_minthara_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, False, None),
        bg3.flag(bg3.DEN_GoblinHunt_Event_LeaderMetPlayer, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, True, None),
    ))
    d.set_dialog_flags(grove_victory_spared_minthara_node_uuid, setflags=(), checkflags=[druid_victory_spared_minthara_flag_group])
    d.set_dialog_attribute(grove_victory_spared_minthara_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    goblin_leaders_dead_node_uuid = '47540c55-bd07-4374-af09-547f504d0e74'
    goblin_leaders_dead_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
    ))
    d.set_dialog_flags(goblin_leaders_dead_node_uuid, setflags=(), checkflags=[goblin_leaders_dead_flag_group])
    d.set_dialog_attribute(goblin_leaders_dead_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    goblin_victory_node_uuid = 'eb5992d7-3341-4e39-8647-1185ddf9f82c'
    goblin_victory_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, True, None),
    ))
    d.set_dialog_flags(goblin_victory_node_uuid, setflags=(), checkflags=[goblin_victory_flag_group])
    d.set_dialog_attribute(goblin_victory_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    rite_of_thorns_node_uuid = '85b8756a-e231-4f28-817d-06312cc95cdb'
    rite_of_thorns_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.FLAG_DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.DEN_Lockdown_State_Active, True, None),
    ))
    d.set_dialog_flags(rite_of_thorns_node_uuid, setflags=(), checkflags=[rite_of_thorns_flag_group])
    d.set_dialog_attribute(rite_of_thorns_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    ################################################################################################
    # Put "Your goddess surely can't approve of what you and I share." under the correct flag
    ################################################################################################

    # Bug: it is possible to ask Shadowheart about how Shar would look at their romance before learning that she worships Shar.
    # This is because the dialog node is under ORI_Shadowheart_State_Shar_SavedParents_8a0fad17-1615-4a0d-a045-21661d9a2aa0  flag.
    # The correct flag should be ShadowHeart_InParty_Knows_SharWorshipper_634f858d-9b54-0711-e31f-075d304422ab
    d.set_dialog_flags('495bfcc6-f16a-4c1d-8eb9-459ef4e86c1d', checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, True, None),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.GOD_Selune, True, slot_idx_tav),
            bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, slot_idx_shadowheart)
        ))
    ))

    # Do not show "Everyone's got their own fears. I won't judge yours." when Shadowheart rejects Shar because of refernce to mother superior.
    everyones_got_their_own_fears_node_uuid = 'dbc225b9-17b9-45bf-83eb-f4143c48d8a7'
    d.set_dialog_flags(everyones_got_their_own_fears_node_uuid, checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, False, None),
        )),
    ))


def create_faith_conversation_entry_point() -> None:
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    conversations_root_node_uuid = '5f864b1a-65af-45de-ac29-d27242ab07b7' # existing node

    shar_worship_node_uuid = '95d8899d-6da5-4f66-abae-bfa28ab97132'
    shar_worship_nested_dialog_node_uuid = '718f1dec-cdbf-463f-9c0a-02f2580e35a9'
    jump_back_node_uuid = '51576606-32fe-4244-8a75-94fb8ecde3ff'

    # I thought Lady Shar blessed you, yet the shadows hurt you. Do you want to talk about that?
    d.create_standard_dialog_node(
        shar_worship_node_uuid,
        bg3.SPEAKER_PLAYER,
        [shar_worship_nested_dialog_node_uuid],
        bg3.text_content('heab327e2gc976g4342ga0bfg894d952f25b5', 1),
        constructor = bg3.dialog_object.QUESTION,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Shadow_Cursed_Event.uuid, True, slot_idx_tav),
                bg3.flag(Shadowheart_Shadow_Cursed.uuid, False, slot_idx_shadowheart),
            )),
        ),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, True, slot_idx_tav),
                bg3.flag(Shadowheart_Shadow_Cursed.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, False, None)
            )),
        ))
    d.create_nested_dialog_node(
        shar_worship_nested_dialog_node_uuid,
        'd71b23ba-6d5a-b71b-a1f9-bca2944c6a62',
        [jump_back_node_uuid],
        speaker_count = 7)
    d.create_jump_dialog_node(jump_back_node_uuid, conversations_root_node_uuid, 2)
    d.add_child_dialog_node(conversations_root_node_uuid, shar_worship_node_uuid, index = 0)

    create_faith_conversation_nested()

def create_faith_conversation_nested() -> None:
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_SharranChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_SharranChapter.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # The following tweaks approval flags for her response to 'Our goddesses are twins - part of a whole. We complement each other.'

    youre_good_company_node_uuid = '189efb9f-502d-444c-911a-01e968d86922' # existing node
    youre_better_company_node_uuid = 'dac409fb-3e6d-484e-82e0-f484836b9ab8' # existing node
    oil_and_fire_node_uuid = '6172bc60-9e98-44a0-8e04-acc0eb8a131f' # existing node

    d.set_dialog_flags(youre_good_company_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart)
        )),
    ))

    d.set_dialog_flags(youre_better_company_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart)
        )),
    ))

    # This adds a new conversation about her faith

    entry_point_node_uuid = '6ebe4401-511b-4669-9478-814f563a5687'


    all_we_can_do_is_try_node_uuid = '192829c4-4794-4583-ab5a-8a6706346b05' # existing node
    not_this_again_node_uuid = '17f3aedb-8ea9-4d0a-89d7-92f0cab42763' # existing node
    not_something_talk_about_freely_node_uuid = 'd534c0a2-3543-48bb-acd9-75de0ecab1c3' # existing node
    #iam_not_sure_id_agree_node_uuid = 'f8e34af5-39ed-4b28-809d-50ecd8e898d6' # existing node

    alias_all_we_can_do_is_try_node_uuid = 'e8a2a5b2-3cd8-4113-a0c7-49add03cb9f4'
    alias_not_this_again_node_uuid = '9c72261a-bf2c-478b-9121-acad4c9faaf9'
    alias_not_something_talk_about_freely_node_uuid = 'cee7b5a5-4994-449e-a7ff-cf6f96e4d47a'

    iam_not_sure_id_agree_node_uuid = '03053706-7a3a-45e2-996a-169d4e71065e'
    told_you_already_forget_it_node_uuid = 'b1b8ea62-e06b-4c62-bfb3-de6e9e9e67fa'

    # remove 'show once' from 'turn to other matters'
    d.remove_dialog_attribute('dc4d4be3-f443-bc8f-0223-05e7067db617', 'ShowOnce')

    pray_together_node_uuid = '2cd0ceb9-41f9-4d84-853e-e75a54170fe3'
    losing_your_blessing_node_uuid = 'd10af8c7-72a1-4d3a-b7ea-3eab2f65d273'
    values_you_this_much_node_uuid = '34900def-bb3c-4e6c-b2fb-fc1a42c1adf8'
    very_well_node_uuid = '74840f69-5ef5-4283-b506-463d326b6371'
    selunite_trick_node_uuid = 'ad68ec0b-c6d5-4f2c-9b46-be6d959d7296'
    goad_me_node_uuid = '1ce42ccc-a8cd-4245-ba17-f9241451f97b'
    iam_honoured_blessing_node_uuid = 'c2035aa7-a3e0-4ebf-8213-661eead2a3cd'
    give_it_time_node_uuid = 'cd5f0b49-b6c2-43ce-ae10-b8fc921a3b2d'

    reaction_plus_3 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 3 }, uuid = 'c802b369-229a-495f-b1b3-2d5d9945d6b9')
    reaction_minus_10 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -10 }, uuid = '7b2e084a-e220-41e7-a688-596b4a76f73d')
    reaction_minus_5 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -5 }, uuid = '7d41539d-eaa4-4330-95aa-ac961c54104b')

    d.create_alias_dialog_node(
        alias_not_something_talk_about_freely_node_uuid,
        not_something_talk_about_freely_node_uuid,
        [],
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
            )),
        ))

    # Entry point for the new conversation
    d.create_standard_dialog_node(
        entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [iam_not_sure_id_agree_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Shadow_Cursed_Event.uuid, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Shadow_Cursed_Event.uuid, False, slot_idx_tav),
            )),
        ))
    d.add_root_node(entry_point_node_uuid, index = 0)

    # I'm not sure I'd agree, but ... very well.
    d.create_standard_dialog_node(
        iam_not_sure_id_agree_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [values_you_this_much_node_uuid, losing_your_blessing_node_uuid, pray_together_node_uuid],
        bg3.text_content('h5e78e8b3ga141g4fdegaf94gb6848de17210', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.942,
        iam_not_sure_id_agree_node_uuid,
        ((3.4, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (3.5, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 4.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (2.85, 8, None)),
        })

    # I want to pray with you. Perhaps, the Nightsinger would be pleased and the shadows would spare you next time.
    d.create_standard_dialog_node(
        pray_together_node_uuid,
        bg3.SPEAKER_PLAYER,
        [told_you_already_forget_it_node_uuid, alias_not_something_talk_about_freely_node_uuid, alias_all_we_can_do_is_try_node_uuid],
        bg3.text_content('hc5db671eg0534g4598g948age7537f10f15d', 1),
        show_once = True,
        constructor = bg3.dialog_object.QUESTION)

    # You don't seem to worry about the shadows even now. What if you're losing your blessing?
    d.create_standard_dialog_node(
        losing_your_blessing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [selunite_trick_node_uuid],
        bg3.text_content('h568ddb44g1bd5g4869g92aagf46a058edead', 1),
        show_once = True,
        constructor = bg3.dialog_object.QUESTION)

    # Apparently, the Nightsinger only values you this much. It's good to know where the limit is, don't you agree?
    d.create_standard_dialog_node(
        values_you_this_much_node_uuid,
        bg3.SPEAKER_PLAYER,
        [goad_me_node_uuid],
        bg3.text_content('h8d40543bg23c0g45b7g924ag253d16e26545', 1),
        show_once = True,
        constructor = bg3.dialog_object.QUESTION)

    # I don't know. Maybe it's a Selunite trick, or another way for Lady Shar to test my faith.
    d.create_standard_dialog_node(
        selunite_trick_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf0d1f77fga701g42f9g813fgb02b83a5352f', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        9.187,
        selunite_trick_node_uuid,
        ((10.0, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 10.18,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, None), (3.36, 2048, 1), (5.6, 16, 1)),
        })

    # If you're attempting to goad me, don't bother. I'm more than familiar with those sort of tricks.
    d.create_standard_dialog_node(
        goad_me_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h04299789g481fg4cb0g8b10gb21bb0f74b13', 1),
        approval_rating_uuid = reaction_minus_10.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Mocked_Sharran_Prayer.uuid, True, slot_idx_tav),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.85,
        goad_me_node_uuid,
        ((6.1, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 6.2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.2, 4, 1)),
        })

    prayer_1_node_uuid = 'e408db8e-0d22-4df6-953b-a40321b3df09'
    prayer_1_repeat_node_uuid = 'd39c52aa-52ae-4917-82cd-a6581a0c214e'
    prayer_1_repeat_shar_node_uuid = 'f6c15f0a-69db-4234-a2e5-477170ced5a0'
    prayer_1_dont_repeat_node_uuid = '17982bef-559c-4b6b-b259-98c474de972b'

    prayer_2_node_uuid = 'a5bf60d1-cecd-4b74-8c77-2d95c671041e'
    prayer_2_repeat_node_uuid = '11f733da-da06-4be6-bf79-6be81080eb76'
    prayer_2_repeat_shar_node_uuid = 'e10f0249-66c8-4abb-81c2-832ecb9b0d04'
    prayer_2_dont_repeat_node_uuid = 'dfa2be04-fab1-4cad-8ef7-3ba175286583'

    prayer_3_node_uuid = 'c6261117-ffbf-4cac-95ac-60b38170e80f'
    prayer_3_repeat_node_uuid = 'c2a23e65-f00a-4ab5-a8d2-2c5d13faf538'
    prayer_3_repeat_shar_node_uuid = '4c4dcd59-0da3-4c6a-b1d3-ba5ba22edc4b'
    prayer_3_dont_repeat_node_uuid = 'bb1b8df8-a5a9-4876-bab7-0c09092f611c'

    prayer_4_node_uuid = '2dddd84e-1d25-4e7b-ab93-9e71d4c88d72'
    prayer_4_repeat_node_uuid = 'd1729be8-ae5a-4918-bd1b-96a8a862148f'
    prayer_4_dont_repeat_node_uuid = '08af1a13-4c93-4088-956d-b86b087a5e75'

    youve_habit_saying_right_things_node_uuid = '55777e22-79bb-4f99-9933-c9e37896b198'

    # Alias to "All we can do is try, I suppose..."
    d.create_alias_dialog_node(
        alias_all_we_can_do_is_try_node_uuid,
        all_we_can_do_is_try_node_uuid,
        [prayer_1_node_uuid])

    # Very well...
    d.create_standard_dialog_node(
        very_well_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [prayer_1_node_uuid],
        bg3.text_content('h93eaf8e9g2808g47cdgbd6egc9add28a87c0', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.92,
        very_well_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = 1.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1, 2),),
        })

    # Blessed Nightsinger, witness our adoration. See how we serve you, only you.
    d.create_standard_dialog_node(
        prayer_1_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [prayer_1_dont_repeat_node_uuid, prayer_1_repeat_shar_node_uuid, prayer_1_repeat_node_uuid],
        bg3.text_content('he4e82517gbb5eg4488g9007gaaef072bd008', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Already_Prayed_With_Her_Today.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.61,
        prayer_1_node_uuid,
        ((7.7, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 7.8,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 256, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 256, None),),
        })

    # Ugh, this is embarrasing. I am not saying that. I don't serve Shar.
    d.create_standard_dialog_node(
        prayer_1_dont_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [goad_me_node_uuid],
        bg3.text_content('h662f6ae0g3786g473dgbfa8g3671968c6418', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, False, slot_idx_tav),
            )),
        ))
    # See our actions, Lady Shar. Hear our words of faith.
    d.create_standard_dialog_node(
        prayer_1_repeat_shar_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_2_node_uuid],
        bg3.text_content('h72bfa66dg9e41g4110ga2f3g8f7193f10092', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, True, slot_idx_tav),
            )),
        ))
    # Carefully repeat every word.
    d.create_standard_dialog_node(
        prayer_1_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_2_node_uuid],
        bg3.text_content('h8d184815g3f6bg4475ga4e4g3677cafbd52b', 1),
        constructor = bg3.dialog_object.QUESTION)

    # We have emptied our hearts of falsehoods. We have vanquished your foes. In the darkness, we see your truth.
    d.create_standard_dialog_node(
        prayer_2_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [prayer_2_dont_repeat_node_uuid, prayer_2_repeat_shar_node_uuid, prayer_2_repeat_node_uuid],
        bg3.text_content('h191e7da0g13a1g4a7dg8ce0g8e8b710f1670', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        8.27,
        prayer_2_node_uuid,
        ((9.0, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 9.2,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 256, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 256, None),),
        })

    # I don't see a thing in the darkness.
    d.create_standard_dialog_node(
        prayer_2_dont_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [goad_me_node_uuid],
        bg3.text_content('h0472ed53gbcf9g41e6g9d2agf231e8aca0e9', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, False, slot_idx_tav),
            )),
        ))
    # Guide us to your perfect, eternal darkness.
    d.create_standard_dialog_node(
        prayer_2_repeat_shar_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_3_node_uuid],
        bg3.text_content('hb4d4bfeag236eg4cd4g93dfgb2bfa840649b', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, True, slot_idx_tav),
            )),
        ))
    # Suppress your feelings and focus on repeating what she said.
    d.create_standard_dialog_node(
        prayer_2_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_3_node_uuid],
        bg3.text_content('he2c5ddc7gca8cg4416g80e2gd093b49f75ce', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Embrace us, your loyal warriors. Cloak us in your shadow. Guide us to your victory.
    d.create_standard_dialog_node(
        prayer_3_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [prayer_3_dont_repeat_node_uuid, prayer_3_repeat_shar_node_uuid, prayer_3_repeat_node_uuid],
        bg3.text_content('hac7d7dd7g4137g4a77gbb62g67a8b27012b4', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.59,
        prayer_3_node_uuid,
        ((7.7, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 8.0,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 256, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 256, None),),
        })

    # Day-night cycles seem to be a better alternative to eternal darkness.
    d.create_standard_dialog_node(
        prayer_3_dont_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [goad_me_node_uuid],
        bg3.text_content('hd3ca3c69g6507g497cg9193g23ea94a8f784', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, False, slot_idx_tav),
            )),
        ))
    # Empower us to slaughter the heretics.
    d.create_standard_dialog_node(
        prayer_3_repeat_shar_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_4_node_uuid],
        bg3.text_content('ha33826a2g3260g412bga68fg161e7f5a694b', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, True, slot_idx_tav),
            )),
        ))
    # Snuff your inner protest and repeat after her.
    d.create_standard_dialog_node(
        prayer_3_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [prayer_4_node_uuid],
        bg3.text_content('hc39de06egc1a2g4e15gab05ga64464313bfa', 1),
        constructor = bg3.dialog_object.QUESTION)

    # Shar's will shall be done. As sure as night will fall.
    d.create_standard_dialog_node(
        prayer_4_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [prayer_4_dont_repeat_node_uuid, prayer_4_repeat_node_uuid],
        bg3.text_content('h47153ba4gb683g4720g89b4g7025c9be3871', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.71,
        prayer_4_node_uuid,
        ((4.0, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 4.5,
        performance_fade = 2.0,
        fade_in = 2.0,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.3, 8, None),),
            bg3.SPEAKER_PLAYER: ((0.5, 8, None),),
        })
    t.create_tl_actor_node(
        bg3.timeline_object.LOOK_AT,
        bg3.SPEAKER_SHADOWHEART, 0.0, 4.5,
        (
            t.create_look_at_key(
                0.0,
                target = bg3.SPEAKER_PLAYER,
                bone = 'Head_M',
                turn_mode = 3,
                turn_speed_multiplier = 0.3,
                head_turn_speed_multiplier = 0.1,
                weight = 0.3,
                safe_zone_angle = 15,
                look_at_interp_mode = 2,
                is_eye_look_at_enabled = True,
                eye_look_at_target_id = bg3.SPEAKER_PLAYER,
                eye_look_at_bone = 'Head_M'
            ),
        ))

    # Her will could only be done over my dead body.
    d.create_standard_dialog_node(
        prayer_4_dont_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [goad_me_node_uuid],
        bg3.text_content('hc2b9bd3cg7c82g4e90gb0e5g144b6c8a8d26', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.GOD_Shar, False, slot_idx_tav),
            )),
        ))

    #iam_honoured_blessing_node_uuid = '9ff0f00d-d217-40e1-88b5-b3e3214ddd1f' # existing node

    # You pray with such conviction. The presence of your goddess must fill your whole being.
    d.create_standard_dialog_node(
        prayer_4_repeat_node_uuid,
        bg3.SPEAKER_PLAYER,
        [iam_honoured_blessing_node_uuid],
        bg3.text_content('hdd92e16dg7fb5g4806ga0fdgc3d464d89dad', 1),
        constructor = bg3.dialog_object.QUESTION)

    # ... yes. I am honoured with her blessing.
    d.create_standard_dialog_node(
        iam_honoured_blessing_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [youve_habit_saying_right_things_node_uuid],
        bg3.text_content('h4e10ad41g06dfg4346g8adbge162db863f4f', 1),
        approval_rating_uuid = reaction_plus_3.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Prayed_With_Her.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.84,
        iam_honoured_blessing_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = 4.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1),),
        })
    
    # You've a habit of saying all the right things. Either you're very glib or we're kindred spirits.
    d.create_standard_dialog_node(
        youve_habit_saying_right_things_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h899595fag722eg4730g9b17g7d3bf72eacee', 1),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.29,
        youve_habit_saying_right_things_node_uuid,
        ((6.2, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 6.3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, 1), (2.5, 4, None)),
        })

    # Recurring prayer, once per long rest

    # Disapproval for "Not this again. I told you already - forget it."
    d.create_standard_dialog_node(
        told_you_already_forget_it_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [alias_not_this_again_node_uuid],
        None,
        approval_rating_uuid = reaction_minus_5.uuid,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Mocked_Sharran_Prayer.uuid, True, slot_idx_tav),
            )),
        ))

    # Alias to "Not this again. I told you already - forget it."
    d.create_alias_dialog_node(
        alias_not_this_again_node_uuid,
        not_this_again_node_uuid,
        [],
        end_node = True)

    # Give it time - and thought.
    d.create_standard_dialog_node(
        give_it_time_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('he5101a9ag5cd9g468cgb5cdg00418327d0df', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Already_Prayed_With_Her_Today.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node = True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.49,
        give_it_time_node_uuid,
        ((2.6, 'f07cff8f-87f5-4617-aa1f-6fa5e28a3293'), (None, '500073a6-bd12-451e-8076-cda6e2d7d8ad')),
        phase_duration = 3.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None),),
        })

    prayer_entry_point_node_uuid = '180856c7-94f7-49cd-ac7a-0c555fb6fe9c'
    d.create_standard_dialog_node(
        prayer_entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [told_you_already_forget_it_node_uuid, alias_not_something_talk_about_freely_node_uuid, give_it_time_node_uuid, very_well_node_uuid],
        None,
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Prayer_Event.uuid, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Prayer_Event.uuid, False, slot_idx_tav),
            )),
        ))
    d.add_root_node(prayer_entry_point_node_uuid, index = 0)

    t.update_duration()

add_build_procedure('patch_conversations', patch_conversations)
add_build_procedure('create_recurrent_conversations', create_recurrent_conversations)
add_build_procedure('create_faith_conversation', create_faith_conversation_entry_point)