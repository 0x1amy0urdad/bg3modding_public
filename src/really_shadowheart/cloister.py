from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

########################################################################################
# Cloister of Sombre Embrace
########################################################################################

def patch_cloister_events() -> None:
    ########################################################################################
    # LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM.lsf
    ########################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/LOW_SharGrotto_ViconiaDefeated_OM_Shadowheart_COM.lsf'))

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # flags
    loot_viconias_stuff_true = bg3.flag_group('Object', (bg3.flag(Loot_Viconias_Stuff.uuid, True, slot_idx_tav),))
    loot_viconias_stuff_false = bg3.flag_group('Object', (bg3.flag(Loot_Viconias_Stuff.uuid, False, slot_idx_tav),))
    tag_shadowheart_shar_path_true = bg3.flag_group('Tag', (bg3.flag(bg3.TAG_SHADOWHEART_SHARPATH, True, slot_idx_shadowheart),))

    # dialog nodes
    viconia_node_uuid = '075925ee-5b83-f8ea-d00d-720c57ca6844'
    tav_decision_node_uuid = '2db696a0-5f5a-480a-b968-99c8f066ba64'
    shadowheart_decision_node_uuid = '135d73e9-bb85-5b14-cb28-41c8773237d3'
    kill_her_node_uuid = '300a5cf6-4f96-a4e7-5a1e-58f7b87a5a8f'
    kill_viconia_roll_node_uuid = 'cab06c2b-c320-4d0c-ab66-5e57cd6dc5ba'
    loot_viconias_stuff_node_uuid = '43e67fa4-d42a-412b-a550-924c98829384'
    shadowheart_kills_viconia_node_uuid = 'fbc03324-7fa3-b039-6392-d4ac255c1253'
    shadowheart_spares_viconia_node_uuid = 'ae0948ab-4134-9f9b-b93d-9147090354d3'

    # This dialog node adds an option to loot Viconia's stuff without killing her; it works for both Selune and Shar paths
    d.create_standard_dialog_node(
        loot_viconias_stuff_node_uuid,
        bg3.SPEAKER_PLAYER,
        [],
        bg3.text_content('ha0b56eb6gbc0bg4535g97efga2b7c2671c58', 1),
        constructor=bg3.dialog_object.QUESTION,
        checkflags=(loot_viconias_stuff_false,),
        setflags=(loot_viconias_stuff_true,))

    d.add_child_dialog_node(viconia_node_uuid, loot_viconias_stuff_node_uuid, index=0)
    d.add_child_dialog_node(tav_decision_node_uuid, loot_viconias_stuff_node_uuid, index=0)
    d.add_child_dialog_node(shadowheart_decision_node_uuid, loot_viconias_stuff_node_uuid, index=0)

    # When on Selune path, Shadowheart doesn't want to follow what Viconia taught her;
    # it will require a skill check to make her kill Viconia.
    d.create_roll_dialog_node(
        kill_viconia_roll_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Hard,
        shadowheart_kills_viconia_node_uuid,
        shadowheart_spares_viconia_node_uuid,
        bg3.text_content("h78558948gae13g4d46g936dgf47d53d9fbaf", 2))

    d.delete_child_dialog_node(shadowheart_decision_node_uuid, kill_her_node_uuid)
    d.add_child_dialog_node(shadowheart_decision_node_uuid, kill_viconia_roll_node_uuid)

    ########################################################################################
    # Selunite Shadowheart saves parents
    ########################################################################################

    ########################################################################################
    # LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM.lsf
    ########################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Origin_Moments/LOW_SharGrotto_ParentsFate_OM_Shadowheart_COM.lsf'))

    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    tag_god_selune_true = bg3.flag_group("Tag", (
        bg3.flag(bg3.GOD_Selune, True, slot_idx_tav),
    ))
    tag_god_selune_false = bg3.flag_group("Tag", (
        bg3.flag(bg3.GOD_Selune, False, slot_idx_tav),
    ))

    last_hurdle_node_uuid = '4aabcb2b-a3d6-2cb4-1cdf-0eb99e2463ca'
    but_the_curse_node_uuid = '5b7dc260-a93a-e231-efc9-a37f73c60089'
    you_have_great_faith_node_uuid = '34ae1c3e-8cdc-0eb0-00fa-773859e5645d'
    you_have_great_faith_adv_node_uuid = 'd61a9f9c-c241-4e6f-880a-077f01659262'
    you_can_endure_it_node_uuid = '1db6f59d-8002-109b-f915-d89a73c2de37'
    you_can_endure_it_adv_node_uuid = '90e91f1f-c526-40a1-baa8-536e48e20c2b'
    remain_silent_node_uuid = 'c3a6e897-7565-25d4-ef70-24a968e9785b'
    is_this_truly_what_you_want_node_uuid = '13a9c749-b989-b71d-760c-c2a55796e202'
    you_should_end_their_suffering_node_uuid = '502739a5-ba58-d164-f793-d18c14dd8bf6'
    and_replace_it_with_another_node_uuid = '0001265e-7823-7e88-d1d3-bb16e735ac67'
    your_father_is_right_node_uuid = 'cba612bc-d577-8782-683e-d7797679320d'
    you_will_be_free_node_uuid = '6b7c30e5-d0c6-be55-c927-f1d62fc602be'
    dont_ask_me_to_kill_my_parents_node_uuid = '0686e3dc-23d6-4920-df64-2f3bbb9707fd'
    passive_check_node_uuid = '7b93af0a-5690-44d6-873d-c370ee4d544b'
    i_need_to_obey_my_parents_wishes = '4f4ac30c-45c4-283d-c696-b2bee39d1c2b'

    d.set_dialog_flags(last_hurdle_node_uuid, checkflags=(
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),
        )),
    ))

    #do_not_lose_your_parents_node_uuid = '6d67773e-2681-77f0-9dcd-0f206794e6ff'
    #d.delete_all_children_dialog_nodes(do_not_lose_your_parents_node_uuid)
    #d.add_child_dialog_node(do_not_lose_your_parents_node_uuid, last_hurdle_node_uuid)

    bg3.set_bg3_attribute(d.find_dialog_node(you_have_great_faith_node_uuid), 'DifficultyClassID', bg3.DC_Act3_Medium)
    bg3.set_bg3_attribute(d.find_dialog_node(you_can_endure_it_node_uuid), 'DifficultyClassID', bg3.DC_Act3_Medium)

    d.set_dialog_flags(you_have_great_faith_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
        )),
    ))
    d.set_dialog_flags(you_can_endure_it_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, False, slot_idx_shadowheart),
        )),
    ))

    # You can endure it together, as a family. This is what you've been looking for - don't deny yourself.
    d.create_roll_dialog_node(
        you_can_endure_it_adv_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Medium,
        last_hurdle_node_uuid,
        i_need_to_obey_my_parents_wishes,
        bg3.text_content("h36917627gd2e7g45fdgab50g2271e3c33799", 2),
        advantage = 1,
        advantage_reason = ('he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
            )),
        ))

    # You have great faith and great resolve - all of you. Trust in that. You need not say goodbye here.
    d.create_roll_dialog_node(
        you_have_great_faith_adv_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Medium,
        last_hurdle_node_uuid,
        i_need_to_obey_my_parents_wishes,
        bg3.text_content("h37813951g6489g4e4fg90ecge3150692b4c3", 1),
        advantage = 1,
        advantage_reason = ('he7d56031g63c2g4a69gacdcg1151b2bfc3b1', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
            )),
        ))

    d.add_child_dialog_node(but_the_curse_node_uuid, you_have_great_faith_adv_node_uuid)
    d.add_child_dialog_node(but_the_curse_node_uuid, you_can_endure_it_adv_node_uuid)

    d.delete_all_children_dialog_nodes(remain_silent_node_uuid)
    d.add_child_dialog_node(remain_silent_node_uuid, passive_check_node_uuid)

    # You should end their suffering, and yours.
    # DC 20 Charisma/Persuasion check to kill parents.
    d.delete_dialog_node(you_should_end_their_suffering_node_uuid)
    d.create_roll_dialog_node(
        you_should_end_their_suffering_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Hard,
        is_this_truly_what_you_want_node_uuid,
        last_hurdle_node_uuid,
        bg3.text_content("hf7ab97f1g9c21g467bg9feag961801ba37b9", 2))


    # Your father is right. This is the only way to free your family from Shar's curse and stop the pain.
    d.delete_dialog_node(your_father_is_right_node_uuid)
    d.create_standard_dialog_node(
        your_father_is_right_node_uuid,
        bg3.SPEAKER_PLAYER,
        [and_replace_it_with_another_node_uuid],
        bg3.text_content('hc0077229g09edg4ed4gb446g6e6f48cf2363', 1),
        constructor=bg3.dialog_object.QUESTION)

    d.delete_all_children_dialog_nodes(and_replace_it_with_another_node_uuid)
    d.add_child_dialog_node(and_replace_it_with_another_node_uuid, passive_check_node_uuid)

    # Let your parents die with honour. They will become Selûne's martyrs, and you will be free.
    d.delete_dialog_node(you_will_be_free_node_uuid)
    d.create_standard_dialog_node(
        you_will_be_free_node_uuid,
        bg3.SPEAKER_PLAYER,
        [dont_ask_me_to_kill_my_parents_node_uuid],
        bg3.text_content('h13ebab14g1a05g4971ga118g27bfe03dd22e', 1),
        constructor=bg3.dialog_object.QUESTION)

    d.delete_all_children_dialog_nodes(dont_ask_me_to_kill_my_parents_node_uuid)
    d.add_child_dialog_node(dont_ask_me_to_kill_my_parents_node_uuid, passive_check_node_uuid)

    # DC 7 Wisdom/Religion passive check to save parents.
    d.create_roll_dialog_node(
        passive_check_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        bg3.SPEAKER_PLAYER,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_RELIGION,
        bg3.DC_Act3_Easy,
        last_hurdle_node_uuid,
        is_this_truly_what_you_want_node_uuid,
        None,
        checkflags=(tag_god_selune_true,),
        passive=True,
        transition_mode=True,
        advantage=0,
        exclude_companion_bonus=True,
        exclude_speaker_bonus=True)

    ########################################################################################
    # ShadowHeart_InParty2.lsf
    ########################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)


    ########################################################################################
    # Bugfix: after saving parents when on enemy of shar path, the discussion about her
    #         memories was under Shadowheart_InParty_Event_SavedParentsMemoriesEnemy flag
    #         which is the Shar path flag. Obviously, the conversation never popped up.
    #         Also, this fix makes that conversation a recurring one.
    ########################################################################################

    memories_discussion_selune_parents_saved_node_uuid = 'db424664-9086-bb2a-2f73-62b9ab38c641'
    memories_discussion_selune_parents_killed_node_uuid = 'ac4359eb-ae3a-87c3-4405-2c0ee04bd934'
    memories_discussion_shar_parents_saved_node_uuid = '287b8eb3-4501-97af-f5a8-4fb7c9928257'

    # Selund path, saved parents
    d.set_dialog_flags(
        memories_discussion_selune_parents_saved_node_uuid,
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag('2eb239a8-f3f6-474f-a2a7-636ff19407f0', True, slot_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, True, None),
            )),
        ))

    # Selune path, killed parents
    d.set_dialog_flags(
        memories_discussion_selune_parents_killed_node_uuid,
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag('2825740b-0dc2-4e82-8ce4-ef6b87ea810b', True, slot_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, True, None),
            )),
        ))

    # Shar path, saved parents
    d.set_dialog_flags(
        memories_discussion_shar_parents_saved_node_uuid,
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag('ad4382a9-a10c-4c2f-981c-6da40ac4682b', True, slot_idx_tav),
            )),
        ),
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, True, None),
            )),
        ))

    #######################################################################################
    # After the events in the Chamber of Loss, Shadowheart stays in camp until long rest
    #######################################################################################

    # Shadowheart will keep saying this until long rest

    # Give me a night, to try and get my head together.
    give_me_a_night_node_uuid = 'bcfdf718-6d56-45fa-ab0a-967b0f11abfa'
    d.create_standard_dialog_node(
        give_me_a_night_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h11c7cf31ga874g4f1bgb4e6gf6d126ea12da', 2),
        constructor=bg3.dialog_object.GREETING,
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(ORI_Shadowheart_AfterParents.uuid, True, slot_idx_shadowheart),
                bg3.flag(ORI_Shadowheart_CriedAfterParents.uuid, False, slot_idx_shadowheart),
            )),
        ),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.47,
        give_me_a_night_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, 1), (2.06, 2048, 1))
        })

    # This new node has the top priority.
    d.add_root_node(give_me_a_night_node_uuid, index=0)

    t.update_duration()

    #######################################################################################
    # The following sets the flag for the line above to trigger
    #######################################################################################

    #######################################################################################
    # ShadowHeart_InParty2_Nested_CityChapter.lsf
    #######################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_CityChapter.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # Enemy of Shar path, killed parents
    d.set_dialog_flags(
        'daa105c0-10cc-4334-a550-9a0103674cc4',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(ORI_Shadowheart_AfterParents.uuid, True, slot_idx_shadowheart),
                bg3.flag(ORI_Shadowheart_CriedAfterParents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('d59fe46f-cce5-4a2c-ac44-65cfda9073f2', False, slot_idx_tav) # Shadowheart_InParty_Event_KilledParentsEnemyStart
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_IrregularBehaviour, True, None),
            ))
        ))

    # Enemy of Shar path, saved parents
    d.set_dialog_flags(
        '48f77fda-8492-4b65-8a7f-a533388250f6',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(ORI_Shadowheart_AfterParents.uuid, True, slot_idx_shadowheart),
                bg3.flag(ORI_Shadowheart_CriedAfterParents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('e3c97bf9-c58c-4dfb-ba8e-27cba587d77d', False, slot_idx_tav) # Shadowheart_InParty_Event_SavedParentsEnemyStart
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_IrregularBehaviour, True, None),
            ))
        ))

    # Shar path, saved parents
    d.set_dialog_flags(
        'a11549ed-8ffe-417d-a0f4-1ebbe313661d',
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(ORI_Shadowheart_AfterParents.uuid, True, slot_idx_shadowheart),
                bg3.flag(ORI_Shadowheart_CriedAfterParents.uuid, False, slot_idx_shadowheart),
                bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),
                bg3.flag('1e379d40-cd40-4b49-a45f-d9b28c2d0437', False, slot_idx_tav) # Shadowheart_InParty_Event_SavedParentsSharStart
            )),
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_IrregularBehaviour, True, None),
            ))
        ))

    # fix for for Shadowheart's hideout dialog
    my_parents_stil_captive_node_uuid = '24048b6b-b998-42cd-8154-85f03c91d0fe'
    hideout_conversation_node_uuid = 'ba4c1693-2117-42ae-85f8-6b34e7036610'
    idx = d.get_root_node_index(my_parents_stil_captive_node_uuid)
    d.remove_root_node(hideout_conversation_node_uuid)
    d.add_root_node(hideout_conversation_node_uuid, idx)


add_build_procedure('patch_cloister_events', patch_cloister_events)
