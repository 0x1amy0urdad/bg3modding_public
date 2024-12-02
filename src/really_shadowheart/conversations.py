from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

################################################################################################
# Conversations with Shadowheart
################################################################################################

def patch_conversations() -> None:
    ################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # This flag group evaluates to true on Shadowheart up to Shadowfell
    tag_group_before_shadowfell = bg3.flag_group('Tag', (
        bg3.flag(bg3.TAG_SHADOWHEART_ENEMYOFSHARPATH, False, slot_idx_shadowheart),
        bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, False, slot_idx_shadowheart)))

    # Make "What do you think of all that's happened to us so far?" a permanent dialog option
    what_do_you_think_node_uuid = '438627c9-bcd0-43c7-86db-f3193873fb38'
    d.set_dialog_flags(what_do_you_think_node_uuid, checkflags=(), setflags=(
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Shadowheart_InParty_Event_HappenedThought, True, slot_idx_tav),
        )),
    ))
    d.set_dialog_attribute(what_do_you_think_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "Tell me about your fear of wolves." a permanent dialog option as long as Shadowheart is not on Shar path
    tell_me_about_fear_node_uuid = 'f7807efd-4aa0-1b73-6586-49ac60fc6334'
    d.set_dialog_flags(tell_me_about_fear_node_uuid, checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_Knows_WolfFear, True, None),
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, False, None),
        )),
    ))

    d.set_dialog_attribute(tell_me_about_fear_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "What's the story with that odd little artefact you have?" available until the voice of absolute event on the bridge
    whats_the_story_odd_artifact_node_uuid = 'fd3f1005-8cd6-4260-993e-183012f41e0e'
    before_voice_of_absolute_seen_the_artifact = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_GOB_Orpheus_State_HadVoiceOfAbsoluteEvent, False, None),
        bg3.flag(bg3.FLAG_ORI_Shadowheart_SeenWithBox, True, None)
    ))
    d.set_dialog_flags(whats_the_story_odd_artifact_node_uuid, checkflags=[before_voice_of_absolute_seen_the_artifact, tag_group_before_shadowfell])
    d.set_dialog_attribute(whats_the_story_odd_artifact_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "We should get to know each other a little more." available until revealing Shar worship or asking Shadowheart to the first date
    know_each_other_node_uuid = '89eea7bd-ca95-4e6e-892f-fd1498aa99f0'
    glob_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, False, None),
        bg3.flag(bg3.FLAG_ORI_Shadowheart_Romance1_AfterCelebration_State_QueueInvitation, False, None),
    ))
    tav_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_ORI_State_DatingShadowheart, False, slot_idx_tav),
        bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),
        bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, False, slot_idx_tav),
    ))
    d.set_dialog_flags(know_each_other_node_uuid, checkflags=[glob_flag_group, tav_flag_group, tag_group_before_shadowfell])
    d.set_dialog_attribute(know_each_other_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    # Make "I want to get to know you more, Shadowheart." available until Nightsong story fork.
    i_want_to_get_know_you_more = '71cc008d-0e4a-4a29-83ea-f2a0d4d42f11'
    flag_knows_shar_worship_true = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_ShadowHeart_InParty_Knows_SharWorshipper, True, None),
    ))
    d.set_dialog_flags(i_want_to_get_know_you_more, checkflags=[flag_knows_shar_worship_true, tag_group_before_shadowfell])
    d.set_dialog_attribute(i_want_to_get_know_you_more, 'ShowOnce', 'True', attribute_type='bool')


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
        d.add_child_dialog_node(im_all_ears_node_uuid, another_swim_lesson_node_uuid, index=0)

    ################################################################################################
    # It'll make for quite a bedtime tale for the children, if you ever get me in a family way.
    # Shadowheart will only say that line if her approval of Tav is >= 40
    ################################################################################################

    d.set_dialog_flags('639cab1b-8130-44b5-8f37-73502e1c33b2', checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
            bg3.flag(bg3.FLAG_Approval_AtLeast_40_For_Sp2, True, slot_idx_shadowheart),
        )),
    ))

    t.update_duration()


    ################################################################################################
    # The following makes a few more conversations accessible for longer
    ################################################################################################

    #
    # This will prevent lines under "I want to get to know you more, Shadowheart." from disappearing
    #
    what_drew_you_to_shar_worship = '4b2787dc-b2b5-4a58-afb1-fbffec2b218c'
    d.set_dialog_flags(what_drew_you_to_shar_worship, setflags=(), checkflags=())

    tell_me_something_about_yourself = '453889f3-47a2-4a0e-9ece-571effb963de'
    d.set_dialog_flags(tell_me_something_about_yourself, setflags=(), checkflags=())

    there_has_to_be_more = '3a5a50de-18f7-40e8-a83b-6f1296eba165'
    d.set_dialog_flags(there_has_to_be_more, setflags=(), checkflags=())


    # Make "You must have thoughts about our little stowaways." available until until act 3
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
        bg3.flag(bg3.DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, True, None),
        bg3.flag(bg3.DEN_GoblinHunt_Event_LeaderMetPlayer, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, True, None),
    ))
    d.set_dialog_flags(grove_victory_node_uuid, setflags=(), checkflags=[grove_victory_flag_group])
    d.set_dialog_attribute(grove_victory_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    grove_victory_spared_minthara_node_uuid = 'b742835b-8214-4740-a23f-b3671aea9e4c'
    druid_victory_spared_minthara_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, False, None),
        bg3.flag(bg3.DEN_GoblinHunt_Event_LeaderMetPlayer, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, True, None),
    ))
    d.set_dialog_flags(grove_victory_spared_minthara_node_uuid, setflags=(), checkflags=[druid_victory_spared_minthara_flag_group])
    d.set_dialog_attribute(grove_victory_spared_minthara_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    goblin_leaders_dead_node_uuid = '47540c55-bd07-4374-af09-547f504d0e74'
    goblin_leaders_dead_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.GOB_State_LeadersAreDead, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_DenVictory, False, None),
    ))
    d.set_dialog_flags(goblin_leaders_dead_node_uuid, setflags=(), checkflags=[goblin_leaders_dead_flag_group])
    d.set_dialog_attribute(goblin_leaders_dead_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    goblin_victory_node_uuid = 'eb5992d7-3341-4e39-8647-1185ddf9f82c'
    goblin_victory_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.DEN_PartyProgress_EnteredGrove, True, None),
        bg3.flag(bg3.DEN_AttackOnDen_State_RaiderVictory, True, None),
    ))
    d.set_dialog_flags(goblin_victory_node_uuid, setflags=(), checkflags=[goblin_victory_flag_group])
    d.set_dialog_attribute(goblin_victory_node_uuid, 'ShowOnce', 'True', attribute_type='bool')

    rite_of_thorns_node_uuid = '85b8756a-e231-4f28-817d-06312cc95cdb'
    rite_of_thorns_flag_group = bg3.flag_group('Global', (
        bg3.flag(bg3.FLAG_VISITEDREGION_SCL_Main_A_ACT_2, False, None),
        bg3.flag(bg3.DEN_PartyProgress_EnteredGrove, True, None),
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

add_build_procedure('patch_conversations', patch_conversations)
