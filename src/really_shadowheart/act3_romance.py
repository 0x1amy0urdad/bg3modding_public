from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

from decimal import Decimal


##########################################################################################################
# Skinny dipping cutscene: more opportunities to slip away, fix for the black hair bug, etc
##########################################################################################################

def patch_skinny_dipping_scene() -> None:

    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    # This is a fix for the missed discussion about the night at the beach.
    # Vanilla game checks FLAG_ORI_State_WasPartneredWithShadowheart
    # The correct flag is FLAG_ORI_State_PartneredWithShadowheart
    ##########################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))

    speaker_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    about_our_night_at_the_beach_node_uuid = 'b3bd2cbe-b758-11d7-038f-2966141bf7f9'

    d.set_dialog_flags(
        about_our_night_at_the_beach_node_uuid,
        checkflags = (
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnydipping_Discussed, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable, True, None)
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, speaker_idx_tav),
            )),
        ))


    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    # Adds a new line in Shadowheart's dialog. At night time in camp, if Shadowheart told Tav that
    # she hopes they'll have more opportunities to slip away, Tav can ask Shadowheart to the beach.
    # This replays the skinny dipping cutscene with some options blocked (Tav can't walk away).
    ##########################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    another_swim_lesson_node_uuid = 'ff663060-bb62-48d8-928d-5253b65da04b'
    took_the_words_node_uuid = 'dca8eede-5035-4977-bca7-cf8a08c1efb4'
    wait_until_others_asleep_node_uuid = '738a3386-1a00-4324-afe6-95cb236c127a'
    not_right_now_node_uuid = '62e11af0-bd3b-4f5a-8851-ca91dae393b4'

    # Others seem quite tired, they'll be asleep soon. Don't you think we could seize the opportunity?
    d.create_standard_dialog_node(
        another_swim_lesson_node_uuid,
        bg3.SPEAKER_PLAYER,
        [took_the_words_node_uuid, not_right_now_node_uuid],
        bg3.text_content('h06a5cd66g501bg402bgb1e3g41bd32d9ca18', 1, 'f793f906-dc08-4cac-9ad7-4c97e390e4fc'),
        constructor=bg3.dialog_object.QUESTION,
        checkflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
            )),
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_tav),
                bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Another_Swimming_Lesson_Replied.uuid, False, slot_idx_shadowheart),                     
            )),
        ))

    # You took the words right out of my mouth.
    d.create_standard_dialog_node(
        took_the_words_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [wait_until_others_asleep_node_uuid],
        bg3.text_content('hc89bd245g631dg480ag9218g7d20f8f9422c', 1, '72bb47ca-818d-49ca-b8c6-aed90ed59a6a'),
        checkflags=(
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_Approval_AtLeast_60_For_Sp2, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, False, speaker_idx_tav),
            )),
        )
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        2.71,
        took_the_words_node_uuid,
        ((None, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, 1), (1.0, 2, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        }
    )

    # Wait until the others are asleep, then come with me... Get some rest while you can.
    d.create_standard_dialog_node(
        wait_until_others_asleep_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h40c1c09egd7bcg4575g8a9dgd8ee7a05e75d', 1, '5ca4af10-9855-40f2-8abe-d846c0f4d9b0'),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_AnotherSwimmingLesson.uuid, True, slot_idx_shadowheart),
                bg3.flag(Shadowheart_Another_Swimming_Lesson_Replied.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        6.506,
        wait_until_others_asleep_node_uuid,
        (
            (4.506, 'd76eaab3-040b-4871-9c1d-4a8624f37cd2'),
            (None,  'b4155335-5e08-4d85-8ccd-ddebf5507447'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 2, None), (1.33, 2, 1), (3.1, 2, None), (4.0, 2, 1)),
            bg3.SPEAKER_PLAYER: ((0.0, 2, None),)
        }
    )

    # Perhaps... not right now. As tempting as you make it sound.
    d.create_standard_dialog_node(
        not_right_now_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2df9f309g5badg4c17gb9efgff4360cabd70', 1, '0d7304c8-681a-4b1e-b5e9-5476d52fa095'),
        setflags=(
            bg3.flag_group('Object', (
                bg3.flag(Shadowheart_Another_Swimming_Lesson_Replied.uuid, True, slot_idx_shadowheart),
            )),
        ),
        end_node=True
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.883,
        not_right_now_node_uuid,
        (
            (4.383, '7b067edd-f53f-49e1-95bc-0986e6e2ca2f'),
            (None,  'b4155335-5e08-4d85-8ccd-ddebf5507447'),
        ),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 1024, 1), (0.94, 1024, None), (2.86, 1024, 2)),
            bg3.SPEAKER_PLAYER: ((0.0, 1024, 2),)
        }
    )

    t.update_duration()
    #d.add_child_dialog_node('23749c85-4289-4965-a7db-1909f5cb63a2', another_swim_lesson_node_uuid, index=0)


    ##########################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_Romance.lsf
    # Set the custom flag that enables replays of the skinny dipping cutscene
    # Flags are set in Shadowheart's answers after the first night at the beach
    ##########################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_Romance.lsf'))

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    # But of course they will. I hope we'll have more opportunities to slip away... and make sand castles.
    d.add_dialog_flags('08c8b4f5-79df-4b9b-9e11-2e2c0cf06a3d', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away.uuid, False, slot_idx_shadowheart),
        )),
    ))
    # I suppose it doesn't. I'm glad we have each other. And I hope we'll have more opportunities to slip away.
    d.add_dialog_flags('277288c2-302f-4e53-9e3d-02974e7ac352', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, True, slot_idx_shadowheart),
            bg3.flag(Shadowheart_LongRest_Before_More_Opportunities_To_Slip_Away.uuid, False, slot_idx_shadowheart),
        )),
    ))

    # Oh. I'm sorry you feel that way... I don't.
    d.add_dialog_flags('ce072faa-0aa6-404a-aeaa-27fb3d226b5d', setflags = (
        bg3.flag_group('Object', (
            bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
        )),
    ))

    ##########################################################################################################
    # Dialog: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Removed dialog options that let Tav walk away if this isn't the first time they swim with Shadowheart
    ##########################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Camp/SoloDreams/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    dialog_nodes = [
        # Suppress nodes for the 2nd run of the unsafe cutscene as they don't make sense anymore
        'a36d3365-38ba-8a0a-e249-8491cf394f2c', # What?
        '0403b053-4b6c-9cfb-7b95-007c6024509b', # I never said I was coming in with you.
        '955c8afa-d714-09e6-2541-a409d7919304', # I didn't bring anything to swim in.
        'bbd5a13c-fa69-58c4-e0d8-1b65c3dc908d', # There's easier ways to get me naked, you know.
        'd2205284-8cbe-0cba-be5a-6693eb699a5a', # Forget it. Let's head back.
        'c0230403-b3a9-2203-baff-7102710154c7', # Actually, I've changed my mind. I'm heading back to camp.

        # Suppress nodes for the 2nd run of the safe cutscene as they don't make sense anymore
        'c70dbc9c-5afe-909b-7514-6480a9c2c79c',
        'a00730b5-70c7-13ab-9263-239d28168c29',
        'd53947d8-21fc-df12-a0f0-c43c4d080911',
        '5e5a9953-4814-8853-b8ee-833e25b05af8',
    ]
    for dialog_node in dialog_nodes:
        d.set_dialog_flags(
            dialog_node,
            checkflags = (
                bg3.flag_group('Object', (
                    bg3.flag(Shadowheart_More_Opportunities_To_Slip_Away.uuid, False, slot_idx_shadowheart),
                )),
            ),
        )

    aborted_sd_dialog_nodes = [
        '37f2f70f-2be2-df93-a613-d45b1aa1db31',
        '45b93976-c611-89c0-9546-41fb7996be5a',
        '97859427-f401-6a21-bd0c-e855f36c7d1d'
    ]
    for dialog_node in aborted_sd_dialog_nodes:
        d.set_dialog_flags(
            dialog_node,
            setflags = (
                bg3.flag_group('Global', (
                    bg3.flag(bg3.FLAG_ORI_Shadowheart_State_AbortedSkinnydipping, True, None),
                )),
                bg3.flag_group('Object', (
                    bg3.flag(Shadowheart_Has_Doubts_About_Tav.uuid, True, slot_idx_tav),
                )),
            ))



    ###########################################################################
    # Timeline: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Delay camera transform when Tav & Shadowheart are kissing on the beach
    ###########################################################################

    now_dont_you_dare_stop_node_uuid = '209a6af4-1a79-cbe3-665e-63c03a31db0c'
    phase = t.use_existing_phase(now_dont_you_dare_stop_node_uuid)

    transform_t1 = phase.duration - 4.45
    transform_t2 = phase.duration - 2.25

    transform_channels = (
        (
            t.create_value_key(time=transform_t1, interpolation_type=5, value=-0.9371941),
            t.create_value_key(time=transform_t2, interpolation_type=5, value=-0.9421899),
        ),
        (
            t.create_value_key(time=transform_t1, interpolation_type=5, value=0.2273747),
            t.create_value_key(time=transform_t2, interpolation_type=5, value=0.2277535),
        ),
        (
            t.create_value_key(time=transform_t1, interpolation_type=5, value=-6.752407),
            t.create_value_key(time=transform_t2, interpolation_type=5, value=-6.757811),
        ),
        (
            t.create_value_key(time=transform_t1, interpolation_type=5, value=(0.013664621, 0.3343945, -0.00484906, 0.94232166)),
            t.create_value_key(time=transform_t2, interpolation_type=5, value=(0.22784422, -0.33852422, -0.084851965, -0.90900415)),
        ),
        (),
        ()
    )

    t.edit_tl_transform('98020265-3ead-4cc4-9c99-3ff011567e38', channels=transform_channels)

    ###########################################################################
    # Timeline: CAMP_Shadowheart_SkinnyDipping_SD_ROM.lsf
    # Fix Shadowheart black hair bug: keep her slipper on her feet
    # Fixed in hotfix 28
    ###########################################################################

    # How does this work? Hair color changes to black if she is nude.
    # Weraing camp shoes somehow prevents hair color from turning black.
    # So, all TLShowArmor nodes that control visual state of Shadowheart equipment are patched to keep her slipper on.
    # TLShowArmor's channel 6 (zero-based index) controls camp footwear.
    # The following code sets the 6th channel to True for each TLShowArmor with actor uuid set to Shadowheart.

    # This bug is fixed as of Patch 7 Hotfix 28
    #show_armor_components = t.find_effect_components(effect_component_type=bg3.timeline_object.SHOW_ARMOR, actor=bg3.SPEAKER_SHADOWHEART)
    #for effect_component in show_armor_components:
    #    channels = effect_component.find("./children/node[@id='Channels']/children")
    #    if channels is not None and hasattr(channels, '__len__') and len(channels) == 11:
    #        key = channels[6].find("./children/node[@id='Keys']/children/node[@id='Key']/attribute[@id='Value']")
    #        if key is not None:
    #            key.set('value', 'True')

add_build_procedure('patch_skinny_dipping_scene', patch_skinny_dipping_scene)
