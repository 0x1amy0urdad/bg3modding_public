from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

def patch_sharess_caress() -> None:
    ##############################################################################################
    # Dialog: WYR_DapperDrow_SiblingsThreeWay.lsf
    ##############################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/Wyrm/WYR_DapperDrow_SiblingsThreeWay.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/WYR_DapperDrow_SiblingsThreeWay.lsf'), d)

    # speaker slot indexes
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # flags
    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),))
    shadowheart_chosen_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, True, None),))
    tav_partnered_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),))
    tav_partnered_false = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),))
    tav_brokenup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),))
    skinny_dipping_discussion_happened_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),))
    handled_breakup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),))
    really_shadowheart_true = bg3.flag_group('Tag', (bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),))
    shadowheart_goes_to_camp = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_OriginRemoveFromPartyAfterDialog, True, slot_idx_shadowheart),))
    tav_promise_true = bg3.flag_group('Object', (bg3.flag(ORI_State_DontHireDapperDrowPromise.uuid, True, slot_idx_shadowheart),))
    tav_promise_false = bg3.flag_group('Object', (bg3.flag(ORI_State_DontHireDapperDrowPromise.uuid, False, slot_idx_shadowheart),))
    tav_rejected_drow_3some_true = bg3.flag_group('Object', (bg3.flag(ORI_State_RejectedDapperDrow3some.uuid, True, slot_idx_tav),))
    tav_rejected_drow_3some_false = bg3.flag_group('Object', (bg3.flag(ORI_State_RejectedDapperDrow3some.uuid, False, slot_idx_tav),))
    tav_rejected_drow_true = bg3.flag_group('Object', (bg3.flag(ORI_State_RejectedDapperDrow.uuid, True, slot_idx_tav),))
    tav_rejected_drow_false = bg3.flag_group('Object', (bg3.flag(ORI_State_RejectedDapperDrow.uuid, False, slot_idx_tav),))

    # dialog uuids, existing dialogs
    id_like_you_all_to_myself_node_uuid = '42eabadc-bf51-6129-f4f7-e79718020fef'
    theres_an_idea_node_uuid = '4d6c4b25-54b3-d965-9b1d-4240b4d32c09'
    should_i_be_jelous_node_uuid = 'b7f42923-a360-e758-3504-43b90a2354de'
    i_feel_the_same_way_node_uuid = '37e7cf82-ed52-4b7d-b903-38237b6ab604'
    forget_i_said_node_uuid = '0b4912e4-fd26-7785-6e7a-ce1852138fb0'
    id_like_to_hire_both_node_uuid = '650c0d75-3e1a-06f2-63c1-09f4554b4adb'
    id_like_to_hire_my_lady_node_uuid = '49b95aec-c693-2332-1874-9aa1a65d37f4'
    i_want_to_hire_lad_node_uuid = '18138b2a-618f-28dc-7b62-90a7dfb46135'
    id_like_to_spend_time_lady_nym_node_uuid = 'fccddc42-f0a1-e4e0-18d2-4e2c68dbdd0a'

    #dialog uuids, new dialogs
    entry_point_node_uuid = '1248ea3a-a035-4944-80f2-b4d3a3752486'
    partner_reaction_hub_node_uuid = '8c62a0da-1341-e527-91d9-9fe9a960cd47'
    just_like_that_node_uuid = '1f836a58-db44-4b04-8f97-6a9a0361324a'
    deception_node_uuid = '20ae75a9-5abd-4b10-b233-3e867dbaf39d'
    deception_success_node_uuid = '3f1e941d-77e1-4625-9612-dfd81f0403b9'
    deception_failure_node_uuid = 'a1ba021c-571e-43bf-8022-9c3db48c9897'
    persuasion_node_uuid = '2bd1be3b-7b34-4ef1-96e6-58a6813cf153'
    persuasion_success_node_uuid = '44601422-dbc0-4df1-964e-0b32d9c594f4'
    persuasion_failure_node_uuid = '73a44813-57d7-4c86-bc0f-6133ef0ffa93'
    lets_drop_this_node_uuid = '7d411d40-89d2-4e4d-b773-8a6c05a22016'
    cut_you_loose_node_uuid = 'aa037df5-0825-4f52-8cbf-6783c29df1f3'
    dont_do_this_again_node_uuid = '5a598edd-3495-4240-84c7-3e2178f698a0'
    bad_liar_node_uuid = '91265082-8a28-4233-b22b-654c2a7656d6'
    best_leave_me_alone_uuid = 'f2e1df94-dc62-4981-849c-53bf84eed103'
    now_leave_me_alone_uuid = '194e0965-3a7a-4238-b2eb-e5e403e8a4c5'
    your_affections_drifted_uuid = '3258a7bb-a84a-44d9-be22-116089156432'
    i_am_free_uuid = '9fb11096-33d8-4c30-9eef-3fe7b142b46f'
    i_dont_want_to_lose_you_uuid = '56ba2b98-5d0a-4dbe-b5e4-081c85f5bd2c'
    better_if_we_were_friends_node_uuid = '3c5709f2-2586-49c8-b75b-d6cd97572db5'
    your_new_beau_uuid = '35a4a0c9-74c6-4f28-befd-686e3eaec7fb'
    spare_lover_uuid = '1bdb3c57-d180-47d1-8eb0-23c5cf08f0cc'
    way_to_end_things_uuid = '4b9bf0a2-4058-4a7e-8b6b-9649990fc814'
    what_do_you_mean_uuid = '7f30d6cf-1481-4db1-8510-3435005813b9'
    arent_dear_friends_uuid = 'ceacb4b7-6db1-4952-8a00-e4fad3ec0e78'

    # Negative impact to approval rating
    set_zero_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Zero.uuid, True, slot_idx_tav),))
    set_neutral_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Neutral.uuid, True, slot_idx_tav),))
    set_low_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_Low.uuid, True, slot_idx_tav),))
    set_very_low_approval_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_Approval_Set_To_VeryLow.uuid, True, slot_idx_tav),))


    # Camera that looks at Shadowheart
    def create_shadowheart_tl_shot(tl_obj: bg3.timeline_object, start: float, end: float) -> None:
        tl_obj.create_tl_shot(
            '959c765e-cc11-4861-ba1c-ab711f1bffb2',
            start,
            end,
            is_snapped_to_end=True,
            is_logic_enabled=True,
            j_cut_length=1,
            companion_cameras=('81b6ede6-3f4b-4caf-910b-3dd142f0b98b', '26949517-f0f4-4689-ae37-b94fe68dfee9', 'd3e056d9-f660-4ab7-b766-6aaff02b7c78'))


    # Selune Shadowheart always rejects 3some with drows

    # While it's a fascinating prospect, I'd like you all to myself...
    d.set_dialog_flags(id_like_you_all_to_myself_node_uuid, checkflags=(shadowheart_enemy_of_shar_true, tav_partnered_true))
    d.set_tagged_text(id_like_you_all_to_myself_node_uuid, bg3.text_content('h7b905a4fgda7dg4417g9c24g768f4ef486e4', 1))

    # Timeline: re-use the existing one, but change it a bit
    tl_shot = t.find_effect_component('d482b324-2af0-4148-9588-5c0430bce81a')
    end_time = float(bg3.get_required_bg3_attribute(tl_shot, 'EndTime'))
    end_time -= 1.7
    bg3.set_bg3_attribute(tl_shot, 'EndTime', str(end_time))
    tl_shot = t.find_effect_component('92581c30-236e-4cf8-94c0-98a20b45607f')
    bg3.set_bg3_attribute(tl_shot, 'StartTime', str(end_time))
    # Change camera: this camera looks at Nym, attached to Tav
    bg3.set_bg3_attribute(tl_shot.find("./children/node[@id='CameraContainer']"), 'Object', '36b8f8c0-fb65-4088-8c56-aa911e642c5e')
    # Make Tav appear when camera switched back to Nym
    tl_show_visual = t.find_effect_component('b4bab808-d053-4bfc-8b2e-c77b1c46bdba')
    tl_show_visual_keys = tl_show_visual.findall('./children/node[@id="Keys"]/children/node[@id="Key"]')
    bg3.set_bg3_attribute(tl_show_visual_keys[1], 'Time', str(end_time))

    # Block the 3some option after the conversation
    d.set_dialog_flags(i_feel_the_same_way_node_uuid, setflags=(tav_rejected_drow_3some_true,))
    d.set_dialog_flags(forget_i_said_node_uuid, setflags=(tav_rejected_drow_3some_true,))

    # Allow hiring drow twins only if Tav didn't reject this idea
    d.set_dialog_flags(id_like_to_hire_both_node_uuid, checkflags=(tav_rejected_drow_3some_false,))
    d.set_dialog_flags(id_like_to_hire_my_lady_node_uuid, checkflags=(tav_rejected_drow_false,))
    d.set_dialog_flags(i_want_to_hire_lad_node_uuid, checkflags=(tav_rejected_drow_false,))
    d.set_dialog_flags(id_like_to_spend_time_lady_nym_node_uuid, checkflags=(tav_rejected_drow_false,))

    # Shar Shadowheart always agrees to 3some with drows
    d.set_dialog_flags(theres_an_idea_node_uuid, checkflags=(shadowheart_chosen_of_shar_true, tav_partnered_true))

    # Shar Shadowheart doesn't mind Tav hiring drows without her
    d.set_dialog_flags(should_i_be_jelous_node_uuid, checkflags=(shadowheart_chosen_of_shar_true, tav_partnered_true))

    # Partners always react to hiring drow twins
    d.remove_dialog_attribute(partner_reaction_hub_node_uuid, 'transitionmode')
    #d.set_dialog_flags(partner_reaction_hub_node_uuid, checkflags=())

    # Put the entry point node into the conversation
    d.delete_child_dialog_node(partner_reaction_hub_node_uuid, should_i_be_jelous_node_uuid)
    d.add_child_dialog_node(partner_reaction_hub_node_uuid, entry_point_node_uuid, index=0)

    # Entry point: a 3 way fork 
    d.create_standard_dialog_node(
        entry_point_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_like_that_node_uuid, your_affections_drifted_uuid, should_i_be_jelous_node_uuid],
        None,
        checkflags=(tav_partnered_true,))

    # Just like that...? I thought we had something special. Something lasting.
    d.create_standard_dialog_node(
        just_like_that_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [deception_node_uuid, persuasion_node_uuid, lets_drop_this_node_uuid],
        bg3.text_content('h656ea716g6c7fg4810g9a40g7a4faf11bd91', 1),
        checkflags=(shadowheart_enemy_of_shar_true, tav_partnered_true, really_shadowheart_true, tav_promise_false))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        6.75,
        just_like_that_node_uuid,
        (),
        phase_duration=7.05,
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, 1), (2.78, 16, 2), (4.33, 32, None), (5.91, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, None),)
        })
    create_shadowheart_tl_shot(t, 0.0, 6.75)
    t.create_tl_shot('3b786a1e-3d4d-4d02-960f-8dd34901f1ec', 6.75, 7.05, is_snapped_to_end=True)

    # Forget I said anything. Let's drop this.
    d.create_standard_dialog_node(
        lets_drop_this_node_uuid,
        bg3.SPEAKER_PLAYER,
        [cut_you_loose_node_uuid],
        bg3.text_content('hfd18944dg9b68g4093ga62bg4718589a098a', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_rejected_drow_true,))

    # Fine. But understand that I'll cut you loose the moment I have to.
    d.create_standard_dialog_node(
        cut_you_loose_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('ha090154fg5825g4e2bg8e91g6f160fa5e992', 1),
        setflags=(tav_promise_true,),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.97,
        cut_you_loose_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.12, 8, None), (1.5, 64, None), (3.26, 4, None)),
        })
    create_shadowheart_tl_shot(t, 0.0, 3.97)

    # I'm just trying to get you jealous, my love. Of course I wasn't going to hire their services.
    d.create_roll_dialog_node(
        deception_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_WISDOM,
        bg3.dialog_object.SKILL_DECEPTION,
        bg3.DC_Act3_Hard,
        dont_do_this_again_node_uuid,
        bad_liar_node_uuid,
        bg3.text_content('h5def25a4gf970g4dadgbb68gec13e203facc', 1))

    # At least you're honest. Don't do that again.
    d.create_standard_dialog_node(
        dont_do_this_again_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h6f3bfd2agf0d5g4e74g9420g1e59d78b5047', 1),
        setflags=(tav_promise_true,),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.11,
        dont_do_this_again_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (0.65, 4, None), (1.79, 128, 1)),
        })
    create_shadowheart_tl_shot(t, 0.0, 3.11)

    # You're a bad liar... Don't treat me like an idiot, please!
    d.create_standard_dialog_node(
        bad_liar_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [best_leave_me_alone_uuid],
        bg3.text_content('hd86ce9a8g7a59g49ddgad72g6f87d1c370dd', 1),
        setflags=(tav_promise_true, set_zero_approval_true))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.338,
        bad_liar_node_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (3.1, 32, None), (4.2, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 128, None), (4.0, 64, 2))
        },
        phase_duration=6.0)
    create_shadowheart_tl_shot(t, 0.0, 3.538)
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', 3.538, 5.338, is_snapped_to_end=True)

    # Best if you leave me alone, for now.
    d.create_standard_dialog_node(
        best_leave_me_alone_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hb7c3b03bg7d22g41dag989dgae8d9c2223f4', 1),
        setflags=(shadowheart_goes_to_camp,),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.54,
        best_leave_me_alone_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None), (2.2, 128, 1)),
        })
    create_shadowheart_tl_shot(t, 0.0, 3.54)

    # Surely you wouldn't mind if I had a bit of fun? I am my own person, after all.
    d.create_roll_dialog_node(
        persuasion_node_uuid,
        bg3.SPEAKER_PLAYER,
        bg3.SPEAKER_SHADOWHEART,
        bg3.dialog_object.ABILITY_CHARISMA,
        bg3.dialog_object.SKILL_PERSUASION,
        bg3.DC_Act3_Hard,
        spare_lover_uuid,
        way_to_end_things_uuid,
        bg3.text_content('h9a474f8dg36b3g4089gbf4aga01c55224234', 1))

    # In truth, I don't think I'd want to be your spare lover. I'd always want more of you than you'd have to spare. Better perhaps to bow out with dignity.
    d.create_standard_dialog_node(
        spare_lover_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [better_if_we_were_friends_node_uuid, i_dont_want_to_lose_you_uuid],
        bg3.text_content('hd3fd298bgb472g4e8bg8e74gaceeb20de6e1', 3),
        setflags=(handled_breakup_true, tav_partnered_false, tav_brokenup_true, skinny_dipping_discussion_happened_true))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        13.06,
        spare_lover_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.82, 16, None), (3.56, 32, None), (5.29, 64, 1), (8.9, 1024, 2), (11.0, 64, None), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 1),)
        },
        phase_duration=13.56)
    create_shadowheart_tl_shot(t, 0.0, 13.06)
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', 13.06, 13.506, is_snapped_to_end=True)

    # Well that's one way to end things.
    d.create_standard_dialog_node(
        way_to_end_things_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [what_do_you_mean_uuid, i_am_free_uuid],
        bg3.text_content('h80ce62e6g2315g4255g902fg75e92b696ee3', 3),
        setflags=(set_low_approval_true, tav_partnered_false, tav_brokenup_true, skinny_dipping_discussion_happened_true))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        5.29,
        way_to_end_things_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 16, None), (2.14, 4, 2), (3.35, 64, None), (4.01, 128, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 2),)
        },
        phase_duration=5.79)
    create_shadowheart_tl_shot(t, 0.0, 5.29)
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', 5.29, 5.79, is_snapped_to_end=True)

    # Wait, I don't want to lose you... I want to be with you...
    d.create_standard_dialog_node(
        i_dont_want_to_lose_you_uuid,
        bg3.SPEAKER_PLAYER,
        [your_new_beau_uuid],
        bg3.text_content('h4e692070gf12fg40e1g9b36ge64802670e20', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_partnered_false, tav_brokenup_true, skinny_dipping_discussion_happened_true))

    # Perhaps, you're right. It would be better for us if we were friends.
    d.create_standard_dialog_node(
        better_if_we_were_friends_node_uuid,
        bg3.SPEAKER_PLAYER,
        [best_leave_me_alone_uuid],
        bg3.text_content('h5de64a8eg404fg4151ga564g5956eab0a0f4', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_partnered_false, tav_brokenup_true, skinny_dipping_discussion_happened_true))

    # I am free to do whatever I want. Leave, if you have a problem with that.
    d.create_standard_dialog_node(
        i_am_free_uuid,
        bg3.SPEAKER_PLAYER,
        [now_leave_me_alone_uuid],
        bg3.text_content('hf070d2bag8b3cg4918ga17dg7f009caa75dc', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_partnered_false, tav_brokenup_true, skinny_dipping_discussion_happened_true))

    # What do you mean?
    d.create_standard_dialog_node(
        what_do_you_mean_uuid,
        bg3.SPEAKER_PLAYER,
        [arent_dear_friends_uuid],
        bg3.text_content('h6d9862b7g728fg4822ga5f3g658e9bfc16d3', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Oh don't be like that - you've made your bed, now go roll around in it with your new beau.
    d.create_standard_dialog_node(
        your_new_beau_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h45bb0963g86ccg4633gb227gb944064b9b0d', 3),
        setflags=(shadowheart_goes_to_camp,),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        7.0,
        your_new_beau_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 128, 1), (2.5, 16, None), (4.11, 1024, None), (6.2, 64, None))
        })
    create_shadowheart_tl_shot(t, 0.0, 7.0)

    # We aren't dear friends now, if that's what you're asking.
    d.create_standard_dialog_node(
        arent_dear_friends_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [best_leave_me_alone_uuid],
        bg3.text_content('hd08cebbdgc4acg409ag92a9gcaddaec78634', 1))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        3.0,
        arent_dear_friends_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, None), (1.5, 4, None)),
            bg3.SPEAKER_PLAYER: ((3.3, 64, 2),)
        },
        phase_duration=4.2)
    create_shadowheart_tl_shot(t, 0.0, 3.0)
    t.create_tl_shot('b6e5d011-7375-4baf-8c02-942f716ee78c', 3.0, 4.2, is_snapped_to_end=True)

    # Now leave me alone.
    d.create_standard_dialog_node(
        now_leave_me_alone_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('habcc14b2g5065g4b7dg8f22gc39494c34f5e', 1),
        setflags=[shadowheart_goes_to_camp],
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.53,
        now_leave_me_alone_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 8, None),)
        },
        phase_duration=3.0)
    create_shadowheart_tl_shot(t, 0.0, 3.0)

    # So... I gather your affections have drifted elsewhere. Curious.
    d.create_standard_dialog_node(
        your_affections_drifted_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_am_free_uuid, i_dont_want_to_lose_you_uuid],
        bg3.text_content('h888d9f87g4fddg4df6g83c4g9e7307f9c7dc', 3),
        checkflags=(shadowheart_enemy_of_shar_true, tav_partnered_true, really_shadowheart_true, tav_promise_true),
        setflags=(set_low_approval_true, handled_breakup_true))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        6.31,
        your_affections_drifted_uuid,
        (),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (3.35, 16, 1), (5.18, 4, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        },
        phase_duration=7.0)
    create_shadowheart_tl_shot(t, 0.0, 6.31)
    t.create_tl_shot('318bfab8-282a-47ed-abdc-78184e7a6c30', 6.31, 7.0, is_snapped_to_end=True)

    t.update_duration()

add_build_procedure('patch_sharess_caress', patch_sharess_caress)
