from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

from typing import Iterable

def patch_relationship_conversations() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # New response to "Admit it - you've never had a relationship quite like this one, have you?"
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    # speaker slot indexes
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),))
    shadowheart_enemy_of_shar_false = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, False, None),))

    admit_it_node_uuid = '1768e8f4-7100-448d-8422-dd41ded1014d'
    even_if_i_could_remember_node_uuid = '067285cc-d3e7-4190-b785-7d4a61bad7d3'
    the_way_i_was_raised_node_uuid = '1921ef97-3e74-4194-88a9-94d4b4c10fb1'
    a_lots_changed_node_uuid = 'cd6593a9-b021-4721-b370-7f68e934ded4'
    i_sougth_to_confide_node_uuid = 'aa276109-e497-4c76-97f7-3b42c43fd47e'

    # The way I was raised, the way I was trained... well, it was positively encouraged, to get to know each other. Even from the memories I can recall, there's stories I could tell you...
    d.create_standard_dialog_node(
        the_way_i_was_raised_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [a_lots_changed_node_uuid],
        bg3.text_content('h58d907fbg3657g4f4egbca2g4542dd67e653', 3, '5b255972-c650-4464-a852-b0be05d4872f'),
        checkflags=(shadowheart_enemy_of_shar_true,)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        15.948,
        the_way_i_was_raised_node_uuid,
        (
            (9.948, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),
            (None,  '0e8837db-4344-48d0-9175-12262c73806b'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.765, 1024, None), (6.046, 1024, 2), (9.948, 1024, 3), (13.3, 1024, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1024, None),)
        }
    )

    # A lot's changed since then. More than I ever thought was possible.
    d.create_standard_dialog_node(
        a_lots_changed_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_sougth_to_confide_node_uuid],
        bg3.text_content('h0d2027f1g386eg45bbg8a6ag7ab77f651a6c', 1, '6727877f-b790-4b32-9896-53e5dd621b28')
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.334,
        a_lots_changed_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.14, 2, None), (3.4, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        }
    )

    # It's difficult to put into words... I can't remember the last time I sought to confide in someone like this - maybe I never have, for all I know. But now it just feels... right.
    d.create_standard_dialog_node(
        i_sougth_to_confide_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h9b00b4fbgd0e0g4bbcgadc0gdbea99682ab5', 1)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        14.938,
        i_sougth_to_confide_node_uuid,
        (
            (2.538, 'b4155335-5e08-4d85-8ccd-ddebf5507447'),
            (None,  '7b067edd-f53f-49e1-95bc-0986e6e2ca2f')
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (4.14, 16, 1), (8.34, 16, 2), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None), (0.5, 1, None), (1.55, 64, None))
        }
    )

    d.set_dialog_flags(even_if_i_could_remember_node_uuid, checkflags=[shadowheart_enemy_of_shar_false])
    d.add_child_dialog_node(admit_it_node_uuid, the_way_i_was_raised_node_uuid, index=0)

    ################################################################################################
    # The following replaces 'Of course' with 'I'm all ears'.
    ################################################################################################

    # '74ebad47-6406-491b-bca9-57811fbe17c3' Shar path 'of course' node
    of_course_node_uuid = '23749c85-4289-4965-a7db-1909f5cb63a2'
    another_swim_lesson_node_uuid = 'ff663060-bb62-48d8-928d-5253b65da04b'
    children_nodes = d.get_children_nodes_uuids(of_course_node_uuid)

    im_all_ears_node_uuid = '3250b885-192c-4feb-93bd-e36be3c1362b'
    d.create_standard_dialog_node(
        im_all_ears_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        children_nodes,
        bg3.text_content('he88e5a7ag2d50g4665gb852gd09d30a20fea', 1),
        constructor = bg3.dialog_object.GREETING,
        root = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag('22c04792-d5fc-4285-b45d-95c7df986e47', True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag('22c04792-d5fc-4285-b45d-95c7df986e47', False, slot_idx_tav),
            )),
        ))
    t.create_new_voice_phase_from_another(
        of_course_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        2.03,
        im_all_ears_node_uuid,
        skip_tl_nodes = ('TLShot',),
        phase_duration = 2.3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None),],
        })
    t.create_tl_shot(
        'd76eaab3-040b-4871-9c1d-4a8624f37cd2',
        0.0,
        2.0)
    t.create_tl_shot(
        'e08db860-1e62-4271-bf4e-d51602468573',
        2.0,
        2.3,
        is_snapped_to_end = True)

    d.delete_dialog_node('da8bcbbb-7d69-4ac0-94f6-dd7b7be3174c')
    d.create_jump_dialog_node('da8bcbbb-7d69-4ac0-94f6-dd7b7be3174c', im_all_ears_node_uuid, 2)

    d.delete_dialog_node('7cf8a483-3d1b-4972-a2d7-cc37f0d217d5')
    d.create_jump_dialog_node('7cf8a483-3d1b-4972-a2d7-cc37f0d217d5', im_all_ears_node_uuid, 2)

    d.remove_root_node(of_course_node_uuid)
    d.add_root_node(im_all_ears_node_uuid, index = 7)

    # This accounts for the more opportunities to make sand castles
    if another_swim_lesson_node_uuid not in children_nodes:
        d.add_child_dialog_node(im_all_ears_node_uuid, another_swim_lesson_node_uuid, index = 0)


    ################################################################################################
    # It'll make for quite a bedtime tale for the children, if you ever get me in a family way.
    # Shadowheart will only say that line if her approval of Tav is >= 60
    ################################################################################################

    d.set_dialog_flags('639cab1b-8130-44b5-8f37-73502e1c33b2', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
        )),
    ))


    ################################################################################################
    # I want to end things between us.
    # This is to prevent accidental break up
    ################################################################################################

    i_want_to_end_things_node_uuid = '8bf568b9-62fa-4c6f-9166-736af8cc150c' # existing node

    just_like_that_node_uuid = 'b7e53d90-9daf-4a5b-8731-60ee57d5942c'
    i_was_mistaken_node_uuid = 'c00bbcb8-d431-47f6-acde-a1c8556c8125'
    oopsie_node_uuid = '02f366cb-d265-49c9-b038-a963d11400e2'
    end_this_now_node_uuid = '9ca5e811-1b05-4877-8c02-8a0091e845ac'
    i_dont_know_what_you_mean_node_uuid = '78d68f1f-b6c8-4622-8633-278f356d8a01'
    gather_your_thoughts_node_uuid = 'bd9f27aa-59e1-477a-a35c-3e877eeeb107'

    reaction_minus_10 = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : -10 }, uuid = 'fc7711e6-e5d6-47bb-ae00-669228590930')

    # Just like that...? I thought we had something special. Something lasting.
    d.create_standard_dialog_node(
        just_like_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [oopsie_node_uuid, end_this_now_node_uuid],
        bg3.text_content('h656ea716g6c7fg4810g9a40g7a4faf11bd91', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        6.75,
        just_like_that_node_uuid,
        ((6.75, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = 6.8,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (2.78, 16, 2), (4.33, 32, None), (5.91, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })

    # Oopsie, my love... I accidentally clicked the wrong option in the dialog.
    d.create_standard_dialog_node(
         oopsie_node_uuid,
         bg3.SPEAKER_PLAYER,
         [i_dont_know_what_you_mean_node_uuid],
         bg3.text_content('h7df66cf3g43c8g4d4dg9581ga29d9779951b', 1),
         constructor = bg3.dialog_object.QUESTION)

    # I realized we are too poor of a match. It'd be better to end this now.
    d.create_standard_dialog_node(
         end_this_now_node_uuid,
         bg3.SPEAKER_PLAYER,
         [i_was_mistaken_node_uuid],
         bg3.text_content('hd6147aa7g76feg48a5g8c11g3f734c02a5a4', 1),
         setflags = (
             bg3.flag_group('Object', (
                 bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
                 bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),
             )),
         ),
         constructor = bg3.dialog_object.QUESTION)

    # # I don't know what you mean.
    # d.create_standard_dialog_node(
    #     i_dont_know_what_you_mean_node_uuid,
    #     bg3.SPEAKER_SHADOWHEART,
    #     [gather_your_thoughts_node_uuid],
    #     bg3.text_content('hefb7aa04g56a6g46edg94f7g4d84e3dcc77e', 1))
    # t.create_simple_dialog_answer_phase(
    #     bg3.SPEAKER_SHADOWHEART,
    #     1.64,
    #     i_dont_know_what_you_mean_node_uuid,
    #     ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
    #     phase_duration = 2.0,
    #     emotions = {
    #         bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),)
    #     })

    # I don't know what you're talking about. I suspect <i>you </i>don't know what you're talking about.
    d.create_standard_dialog_node(
        i_dont_know_what_you_mean_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [gather_your_thoughts_node_uuid],
        bg3.text_content('h7228d91fg9ab8g4854g91b0g54dda6e78438', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.84,
        i_dont_know_what_you_mean_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        phase_duration = 4.9,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.95, 4, None), (3.89, 64, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),),
        })


    # Gather your thoughts. Then perhaps we can talk some more.
    d.create_standard_dialog_node(
        gather_your_thoughts_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h316517e1g18b2g41f3g91deg1900c4cdb48a', 1),
        end_node = True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.21,
        gather_your_thoughts_node_uuid,
        ((4.21, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = 4.3,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),),
        })


    # Clearly I was mistaken. But at least it's a mistake I won't make twice.
    d.create_standard_dialog_node(
        i_was_mistaken_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc4496b0eg4c3eg43e4g8597g1b40e9dd0395', 1),
        end_node = True,
        approval_rating_uuid = reaction_minus_10.uuid)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.29,
        i_was_mistaken_node_uuid,
        ((5.29, '0e8837db-4344-48d0-9175-12262c73806b'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = 5.4,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2048, 1), (0.21, 128, None), (3.12, 128, 1),),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })


    d.set_dialog_flags(i_want_to_end_things_node_uuid, setflags = ())
    d.delete_all_children_dialog_nodes(i_want_to_end_things_node_uuid)
    d.add_child_dialog_node(i_want_to_end_things_node_uuid, just_like_that_node_uuid)

    ################################################################################################
    # How are you faring?
    # Modded answers to this question.
    ################################################################################################

    how_are_you_node_uuid = 'd6882eaf-132e-440e-8416-4b2fa547506a' # existing node
    how_are_you_faring_node_uuid = '0a72a161-8baa-483e-baf2-afa6f93ca8f0' # existing node
    always_good_when_im_with_you_node_uuid = '204d7c3a-fe80-4dd7-a3ff-5b149033a43b' # existing node
    always_good_when_im_with_you_scl_node_uuid = '98004b3e-1268-4450-9a44-a6bd6399a978' # existing node

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act1_node_uuid = '9145fd6e-06b6-42c7-b2b9-4e763b2d5b6c'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act1_node_uuid,
        always_good_when_im_with_you_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            ))
        ),
        end_node = True)

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act2_node_uuid = 'e7da318a-7626-4a71-bdd5-7c7a5d55f321'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act2_node_uuid,
        always_good_when_im_with_you_scl_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, False, None),
                bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
            ))
        ),
        end_node = True)

    # Always good, when I'm with you.
    alias_to_always_good_when_im_with_you_act3_node_uuid = '7707aece-560a-4841-9871-808edef8c087'
    d.create_alias_dialog_node(
        alias_to_always_good_when_im_with_you_act3_node_uuid,
        always_good_when_im_with_you_node_uuid,
        [],
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_VISITEDREGION_INT_Main_A_ACT_3, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
            ))
        ),
        end_node = True)

    fallback_node_uuid = '8747037f-084c-4e25-a039-c798ac3f7864'
    d.create_jump_dialog_node(fallback_node_uuid, how_are_you_node_uuid, 2)

    d.delete_all_children_dialog_nodes(how_are_you_faring_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act1_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act2_node_uuid)
    d.add_child_dialog_node(how_are_you_faring_node_uuid, alias_to_always_good_when_im_with_you_act3_node_uuid)
    

    i_wanted_to_tell_something_node_uuid = '2a96a513-cab2-4cef-992a-77563f54e7de'
    i_wanted_to_tell_something_durge_node_uuid = '633941f0-0e2a-441f-860b-b38a1ec9d458'
    alls_well_i_hope_node_uuid = '7c7211ec-93be-4ae4-9115-aca10e2ba0c4'
    confession_v1_node_uuid = 'b12ca2d7-59b4-4f9d-a03e-189f37f6f1ee'
    confession_v2_node_uuid = 'ce74c73b-d2b6-4b47-9187-92729ac3dd9b'
    confession_durge_node_uuid = 'ec205b47-a89b-43f6-8928-77d824e940df'
    confession_bard_node_uuid = '06acc6da-bf3f-43f0-8637-1ee1f672b593'
    happiest_man_alive_node_uuid = '8f4933c3-a292-4be5-91dd-13b777bd6197'
    happiest_woman_alive_node_uuid = 'b9888f30-2618-46d9-b755-6f86a5cfb1df'
    i_love_you_node_uuid = '5c8b5016-86ae-4a69-af9c-036f091c5a8b'
    my_love_node_uuid = '0d8503d8-9a85-40b2-8211-5882ed1f9bb5'
    first_confession_reaction_node_uuid = '92f6ac2c-5e84-4ea8-8939-e65ff32ed9b5'
    come_here_node_uuid = '0efd0066-4d38-4797-b51c-4fad103cba3d'
    i_know_node_uuid = '4c21339a-95ed-46a6-9f85-21f3edb90d5a'
    i_know_alias_node_uuid = '35939093-8f24-4487-ae25-2d98426182fe'
    nested_confession_kiss_node_uuid = '3192580f-34ca-4a9b-88b3-1e292b2f594e'
    nested_kiss_node_uuid = 'ebae4805-558c-44ce-b24a-186b823f34a4'
    love_you_too_node_uuid = '8ed5d2bf-e8a7-4c33-87d6-4ab4bce9b438'
    say_nothing_node_uuid = '784b3e44-5261-4f9d-baa1-c2a501eaf3f0'
    return_back_node_uuid = 'bb3642b9-5d09-48cf-97ca-fc2bf4f48c31'

    d.add_child_dialog_node(im_all_ears_node_uuid, i_wanted_to_tell_something_node_uuid, index = 1)
    d.add_child_dialog_node(im_all_ears_node_uuid, i_wanted_to_tell_something_durge_node_uuid, index = 1)
    d.add_child_dialog_node(im_all_ears_node_uuid, happiest_man_alive_node_uuid, index = 1)
    d.add_child_dialog_node(im_all_ears_node_uuid, happiest_woman_alive_node_uuid, index = 1)
    d.add_child_dialog_node(im_all_ears_node_uuid, i_love_you_node_uuid, index = 1)

    # There's something I wanted to tell you. Something that was on my mind since I met you.
    d.create_standard_dialog_node(
        i_wanted_to_tell_something_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alls_well_i_hope_node_uuid],
        bg3.text_content('h862a65d3g8f8fg46b7gb8afga7dc2ad11479', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, False, slot_idx_tav),
            )),        
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # There's something I wanted to tell you. Something that was on my mind since I met you.
    d.create_standard_dialog_node(
        i_wanted_to_tell_something_durge_node_uuid,
        bg3.SPEAKER_PLAYER,
        [alls_well_i_hope_node_uuid],
        bg3.text_content('h862a65d3g8f8fg46b7gb8afga7dc2ad11479', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, slot_idx_tav),
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_DarkUrge_State_BhaalResisted, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # All's well I hope...?
    d.create_standard_dialog_node(
        alls_well_i_hope_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [confession_durge_node_uuid, confession_bard_node_uuid, confession_v1_node_uuid, confession_v2_node_uuid],
        bg3.text_content('hd07291d2g217dg47fdg8fd3ga02a235f6b7b', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        1.375,
        alls_well_i_hope_node_uuid,
        ((2.4, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'), (None, 'e08db860-1e62-4271-bf4e-d51602468573')),
        phase_duration = 2.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 0), ),
            bg3.SPEAKER_PLAYER: ((0.0, 32, 1), ),
        })

    confession_approval = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 10 }, uuid = 'bb28ec6c-502a-4fad-902a-7fbe200bf64a')
    love_you_too_approval = bg3.reaction_object.create_new(files, { bg3.SPEAKER_SHADOWHEART : 10 }, uuid = 'd5b42139-675f-4048-b418-54cb7865cf97')

    # Since the time I first saw you in that pod... I changed... no, you changed me. My life has a new meaning: you.
    d.create_standard_dialog_node(
        confession_v1_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h82e6c111g7e35g4b7fgba0egec25bbbe117a', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I was wondering what would have happened if we weren't infected. This was the moment when I realized: the short time we shared was worth more than my entire life.
    d.create_standard_dialog_node(
        confession_v2_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h4d23cd12ga6fdg4485ga129g9ffda516643f', 1),
        constructor = bg3.dialog_object.QUESTION)

    # I can't remember much of myself, and what I remember is like a crimson mist. Until I met you. I am no Bhaal's Chosen anymore. I am yours.
    d.create_standard_dialog_node(
        confession_durge_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('hd386265bgaf96g421bga57eg8d9ffdeeb899', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_REALLY_DARK_URGE, True, slot_idx_tav),
            )),
        ))

    # Sing a long, emotional, and sad love ballad that you wrote for her.
    d.create_standard_dialog_node(
        confession_bard_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, first_confession_reaction_node_uuid],
        bg3.text_content('h2058154fgca15g4c4dg81a9g331986e63a86', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BARD, True, slot_idx_tav),
            )),
        ))
    

    # When I woke up this morning, I listened to your gentle snores for a while. I am the happiest man alive. I love you.
    d.create_standard_dialog_node(
        happiest_man_alive_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('hb23e9145g96dcg4946g85e2ga984fb7ac751', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_MALE, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # When I woke up this morning, I listened to your gentle snores for a while. I am the happiest woman alive. I love you.
    d.create_standard_dialog_node(
        happiest_woman_alive_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('h35801df6g8e05g4eefga058g983fa676324d', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, False, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_tav),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # I love you.
    d.create_standard_dialog_node(
        i_love_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_node_uuid, my_love_node_uuid],
        bg3.text_content('h10588bf1gd0c4g4b91g90cdg7442250d8d4a', 1),
        constructor = bg3.dialog_object.QUESTION,
        show_once = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Cheated_On_Shadowheart.uuid, False, slot_idx_tav),
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Tav_Love_Confession.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Tav_Slept_Together.uuid, True, slot_idx_tav),
                bg3.flag(Cuddles_Love_You.uuid, True, slot_idx_shadowheart),
                bg3.flag(Tav_Said_Love_You.uuid, False, slot_idx_shadowheart),
            )),
        ),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(Tav_Said_Love_You.uuid, True, slot_idx_shadowheart),
            )),
        ))

    # My love...
    d.create_standard_dialog_node(
        my_love_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [come_here_node_uuid],
        bg3.text_content('h8ba27ee6g443bg49cag82eagf508a23378d5', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.765,
        my_love_node_uuid,
        ((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        phase_duration = 1.5,
        fade_in = 0.0,
        fade_out = 0.5,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 32, None), ),
        })

    # Come here...
    d.create_standard_dialog_node(
        first_confession_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_confession_kiss_node_uuid],
        bg3.text_content('h2c35be55g4742g47abgbdccg534dfa831e3e', 1),
        approval_rating_uuid = confession_approval.uuid,
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, True, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.842,
        first_confession_reaction_node_uuid,
        #((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 1.0,
        fade_in = 0.5,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), ),
        })

    # Come here...
    d.create_standard_dialog_node(
        come_here_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [nested_kiss_node_uuid],
        bg3.text_content('h2c35be55g4742g47abgbdccg534dfa831e3e', 1),
        setflags = (
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionA.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionB.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionC.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionD.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionE.uuid, True, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_VersionF.uuid, False, slot_idx_shadowheart),
            )),
            bg3.flag_group('Object', (
                bg3.flag(ORI_ShadowheartKiss_LoveYou.uuid, False, slot_idx_shadowheart),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        0.842,
        come_here_node_uuid,
        #((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 1.0,
        fade_in = 0.5,
        fade_out = 0.0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None),),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None), ),
        })

    # I know. But it's nice to hear you say it.
    d.create_standard_dialog_node(
        i_know_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb3cef858g5973g4601gb5a3gfb6772f115ec', 1),
        end_node = True,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
            )),
        ))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.14,
        i_know_node_uuid,
        #((None, 'e7f21f15-f386-40f4-bb0f-2f9f42249ad1'),),
        ((None, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),),
        phase_duration = 4.15,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.2, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None), ),
        })

    d.create_nested_dialog_node(
        nested_confession_kiss_node_uuid,
        '7d565080-9370-fe5b-9437-89d169096a04',
        [love_you_too_node_uuid, say_nothing_node_uuid],
        speaker_count = 7
    )

    d.create_nested_dialog_node(
        nested_kiss_node_uuid,
        '7d565080-9370-fe5b-9437-89d169096a04',
        [return_back_node_uuid],
        speaker_count = 7
    )

    d.create_jump_dialog_node(return_back_node_uuid, im_all_ears_node_uuid, 2)

    d.create_alias_dialog_node(i_know_alias_node_uuid, i_know_node_uuid, [], end_node = True)

    # Love you too...
    d.create_standard_dialog_node(
        love_you_too_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_know_alias_node_uuid],
        bg3.text_content('h91c7ed29gaec4g4388g8655g77ae1647ebe7', 1),
        approval_rating_uuid = love_you_too_approval.uuid,
        constructor = bg3.dialog_object.QUESTION)

    # Say nothing.
    d.create_standard_dialog_node(
        say_nothing_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('h2b8d754egf05bg4f89g8ae0gacf81a83ad38', 1),
        end_node = True,
        constructor = bg3.dialog_object.QUESTION)

    t.update_duration()


add_build_procedure('patch_relationship_conversations', patch_relationship_conversations)


