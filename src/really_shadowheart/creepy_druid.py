from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

############################################################################
# This fixes all the shoehorned Halsin-related nonsense, including banter
############################################################################

def patch_creepy_druid() -> None:
    ############################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # If Shadowheart rejected Shar, she breaks up with Tav
    # if they are determined to sleep with Halsin.
    ############################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    # speaker slots
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    # flags
    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),))
    shadowheart_chosen_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, True, None),))
    skinny_dipping_discussion_happened_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, True, None),))
    tav_partnered_false = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),))
    tav_brokenup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_WasPartneredWithShadowheart, True, slot_idx_tav),))
    handled_breakup_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_HandledBreakupWithShadowheart, True, slot_idx_tav),))
    halsin_sharing_ok_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerAllowsHalsin, True, slot_idx_tav),))
    halsin_sharing_not_ok_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_CAMP_Halsin_CRD_Romance_PartnerDoesNotAllowHalsin, True, slot_idx_tav),))

    # dialog uuids
    # these will work for Sharran path only
    ori_willing_to_share_node_uuid = 'd068cdda-889c-48e4-862b-3f7582a2178a'        # ha4ef192dg5572g46a4g8650g392d3e528c46 "He's open-minded, and willing to share... as long as you are."
    ori_space_for_you_and_i_node_uuid = '6c42318e-a9f1-447b-bf53-0395e02ce610'     # hd659b6abge7f2g4246gbdfag871ce01df511 "He wants me. And I want him. I'm not sure if there's space for you and I."
    ori_forget_it_wandering_eye_node_uuid = '1a331bb1-d9e2-4ad8-a625-6bc349eb9430' # hdddd3031g1a88g4096g97e7gc4c0527b20c8 "Forget it. Just my wandering eye. I'll tell him I'm not interested."

    # replacement nodes for Selune path
    new_willing_to_share_node_uuid = 'd8739c08-8abd-4d6c-80d0-af66e42d966f'
    new_space_for_you_and_i_node_uuid = 'd7f46d8d-e432-4599-99f2-9ae107b7b90a'
    new_forget_it_wandering_eye_node_uuid = '7f98e7dd-5724-4508-a57a-70e7023d74ae'

    # reactions to the new nodes
    breakup_reaction_node_uuid = '522b8845-5f52-4b19-b4fa-ffe92eeeff5d' # existing node, reposnse to new_space_for_you_and_i_node_uuid
    spare_lover_node_uuid = '2c250206-77c2-4feb-a73e-c80a6fe285b4' # response to new_willing_to_share_node_uuid
    want_be_with_you_node_uuid = 'cdbf6ef1-f01a-455e-ad95-016ce20741d4'
    thank_you_understanding_node_uuid = 'b3558b5e-8e65-467e-ba57-fd72b4050c7d'
    almost_flattered_node_uuid = 'fac231c8-8200-445f-9b5f-5f43281017bc'
    fleeting_relationship_node_uuid = '7d7e27c7-87c4-4074-b9a7-d8f43b146aa0'
    i_suppose_it_was_node_uuid = 'b80794d3-eb9c-4cbd-b593-1efb50153d84'
    not_meant_to_be_node_uuid = 'd0bff72f-3e42-4adc-bec2-0ccabe6ac20b'

    # the parent node for all new nodes
    youre_talking_about_halsin_uuid = '3da75e80-d9eb-4ca1-9c0e-6cf8bd0938ac'

    # preserve the existing behavior if Shadowhart remained loyal to Shar
    d.set_dialog_flags(ori_willing_to_share_node_uuid, checkflags=(shadowheart_chosen_of_shar_true,))
    d.set_dialog_flags(ori_space_for_you_and_i_node_uuid, checkflags=(shadowheart_chosen_of_shar_true,))
    d.set_dialog_flags(ori_forget_it_wandering_eye_node_uuid, checkflags=(shadowheart_chosen_of_shar_true,))

    # add new behavior if Shadowheart defied Shar
    d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_willing_to_share_node_uuid)
    d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_space_for_you_and_i_node_uuid)
    d.add_child_dialog_node(youre_talking_about_halsin_uuid, new_forget_it_wandering_eye_node_uuid)

    # He wants me. And I want him. I'm not sure if there's space for you and I.
    d.create_standard_dialog_node(
        new_space_for_you_and_i_node_uuid,
        bg3.SPEAKER_PLAYER,
        [breakup_reaction_node_uuid],
        bg3.text_content('hd659b6abge7f2g4246gbdfag871ce01df511', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_partnered_false, tav_brokenup_true, halsin_sharing_ok_true, skinny_dipping_discussion_happened_true, handled_breakup_true),
        checkflags=(shadowheart_enemy_of_shar_true,))

    # He's open-minded, and willing to share... as long as you are.
    d.create_standard_dialog_node(
        new_willing_to_share_node_uuid,
        bg3.SPEAKER_PLAYER,
        [spare_lover_node_uuid],
        bg3.text_content('ha4ef192dg5572g46a4g8650g392d3e528c46', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(),
        checkflags=(shadowheart_enemy_of_shar_true,))

    # Forget it. Just my wandering eye. I'll tell him I'm not interested.
    d.create_standard_dialog_node(
        new_forget_it_wandering_eye_node_uuid,
        bg3.SPEAKER_PLAYER,
        [almost_flattered_node_uuid],
        bg3.text_content('hdddd3031g1a88g4096g97e7gc4c0527b20c8', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(halsin_sharing_not_ok_true,),
        checkflags=(shadowheart_enemy_of_shar_true,))

    # In truth, I don't think I'd want to be your spare lover. I'd always want more of you than you'd have to spare. Better perhaps to bow out with dignity.
    d.create_standard_dialog_node(
        spare_lover_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [fleeting_relationship_node_uuid, want_be_with_you_node_uuid],
        bg3.text_content('hd3fd298bgb472g4e8bg8e74gaceeb20de6e1', 1),
        setflags=(halsin_sharing_not_ok_true,))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        13.06,
        spare_lover_node_uuid,
        ((13.06, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'), (None, 'b4155335-5e08-4d85-8ccd-ddebf5507447')),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.82, 16, None), (3.56, 32, None), (5.29, 64, 1), (8.9, 1024, 2), (11.0, 64, None), (11.8, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 64, 1),)
        },
        phase_duration=13.56)

    # Our relationship was... fleeting. I want to move on.
    d.create_standard_dialog_node(
        fleeting_relationship_node_uuid,
        bg3.SPEAKER_PLAYER,
        [i_suppose_it_was_node_uuid],
        bg3.text_content('hf278c5d2g81beg46abgaa45g649a20dfeb09', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=(tav_partnered_false, tav_brokenup_true, halsin_sharing_ok_true, skinny_dipping_discussion_happened_true, handled_breakup_true))

    # I suppose it was. And don't worry - I'm not going to toss your belongings into the campfire or anything.
    d.create_standard_dialog_node(
        i_suppose_it_was_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [not_meant_to_be_node_uuid],
        bg3.text_content('h11cbe8fcg20cdg498bgb7cbg47060b5530a6', 3))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        8.31,
        i_suppose_it_was_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (2.98, 64, None), (4.73, 64, 1), (6.26, 4, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 4, None),)
        })

    # Maybe you and I are not meant to be, I don't know. I sense I'll have little time for distractions, moving forward. Especially ones that don't bear fruit.
    d.create_standard_dialog_node(
        not_meant_to_be_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h03a13c89ge885g4ebcgbc71gb2d502c80f3a', 1),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        11.2,
        not_meant_to_be_node_uuid,
        ((None, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (4.76, 16, None), (9.05, 2048, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 16, None),)
        })

    # I didn't realize your feel this way. I want to be with you... Forget I ever said anything.
    d.create_standard_dialog_node(
        want_be_with_you_node_uuid,
        bg3.SPEAKER_PLAYER,
        [thank_you_understanding_node_uuid],
        bg3.text_content('h9635e41bge285g4f12gb61bg13692d55fba6', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Thank you. I had a feeling you'd be understanding.
    d.create_standard_dialog_node(
        thank_you_understanding_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hc6d2bb77g1250g40e2gac71g74c4d0c686ff', 1),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.53,
        thank_you_understanding_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (2.48, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        })

    # I'm almost flattered. Almost.
    d.create_standard_dialog_node(
        almost_flattered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('he817ea29gb437g4509gaa6egf9f4acf255a0', 1),
        end_node=True)
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.45,
        almost_flattered_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 64, None), (1.84, 2, None)),
            bg3.SPEAKER_PLAYER: ((0.0, 1, None),)
        })

    t.update_duration()

    #########################################################################
    # Dialog: Halsin_InParty_Nested_Polyamory.lsf
    #########################################################################

    #########################################################################
    # Selune Shadowheart doesn't want Tav to sleep with Halsin.
    # If Tav ignores her and does that, Shadowheart ends their relatinship
    #########################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Halsin_InParty_Nested_Polyamory.lsf'))

    # speaker slots
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)
    slot_idx_halsin = d.get_speaker_slot_index(bg3.SPEAKER_HALSIN)

    shadowheart_breakup_start_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_BreakUp_Notification_Start.uuid, True, slot_idx_tav),))
    shadowheart_chosen_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_SharPath, True, None),))
    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),))
    tav_partnered_true = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),))
    tav_partnered_false = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),))

    existing_making_my_own_node_uuid = 'b73b4b91-7c1f-4b0a-975d-68a4e2ee3017'
    existing_answer_node_uuid = 'e86250d2-036a-4a13-9d4b-dae85d7193e6'
    new_selune_path_node_uuid = '389d34ce-0297-4f86-b6b5-12a2811e0f06'
    new_shar_path_node_uuid = 'bd6ee90c-8e29-48e4-a9a9-a045f6ea97e8'
    new_not_partnered_node_uuid = '5b616a0c-bedb-4b04-b858-5345c2438dee'

    d.create_standard_dialog_node(
        new_selune_path_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        setflags=(tav_partnered_false, skinny_dipping_discussion_happened_true, tav_brokenup_true, shadowheart_breakup_start_true),
        checkflags=(shadowheart_enemy_of_shar_true, tav_partnered_true))

    d.create_standard_dialog_node(
        new_shar_path_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        checkflags=(shadowheart_chosen_of_shar_true, tav_partnered_true))

    d.create_standard_dialog_node(
        new_not_partnered_node_uuid,
        bg3.SPEAKER_HALSIN,
        [existing_answer_node_uuid],
        None,
        checkflags=(tav_partnered_false,))


    d.delete_child_dialog_node(existing_making_my_own_node_uuid, existing_answer_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_selune_path_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_shar_path_node_uuid)
    d.add_child_dialog_node(existing_making_my_own_node_uuid, new_not_partnered_node_uuid)


    ##################################################################
    # Banter: PB_Halsin_Shadowheart_ROM_Act3_Selune.lsf
    ##################################################################

    ##################################################################
    # Shadowheart & Halsin act 3 banter, Shadowheart's new response
    ##################################################################
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Party_Banter/PB_Halsin_Shadowheart_ROM_Act3_Selune.lsf'))

    d.set_tagged_text('c271277b-9408-4c66-bf2f-c5b76fac64f4', bg3.text_content("hbf7a4276g3c6bg49c0gab09g790c7dcb6428", 2))

add_build_procedure('patch_creepy_druid', patch_creepy_druid)
