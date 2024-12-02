from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files

root_victim_killed_node_uuid = '13301f86-8e73-0619-acd3-24402b712d03'
root_victim_saved_node_uuid = '27b8e711-5f07-8986-cf63-6da90796c5d4'
narrator_speaks_node_uuid = 'baa221d3-3fe5-c783-abbe-b92d234b5dca'
victim_killed_node_uuid = '13301f86-8e73-0619-acd3-24402b712d03' # TLShot 6acf4f7e-a637-49e1-83f3-e56745569de4
victim_survived_node_uuid = '27b8e711-5f07-8986-cf63-6da90796c5d4' # TLShot 5292134a-9a7a-4ab9-805a-9b5a749ad236
reaction_fork_node_uuid = '10ce0e11-42ed-4f35-8ea3-a56a6a8e19d3'
partnered_node_uuid = '0aad0986-b2e5-4ff6-92a2-aee41ed99791'
not_partnered_node_uuid = '5cda419c-1b46-4d03-baeb-78aefa7f9c08'
its_difficult_to_speak_node_uuid = '220709ed-2a56-4c9b-918f-23f474bab3cd'
no_it_cant_be_node_uuid = '15b65667-96d0-4b37-a93f-2d46b7c5cb4c'
shadowheart_reaction_fork_node_uuid = '67c8d8d5-7125-8fc9-3fa0-ab777159f9d8'
bypass_reaction_node_uuid = '34e48748-ad74-4efb-bca5-6fbe9a5e1e65' # this node is neede to bypass the standard reaction when Tav is still kneeled
shadowheart_partnered_reaction_fork_node_uuid = '5d572cf4-65bc-4a67-94ca-4e812d64268f'
my_love_node_uuid = '8662a6cd-4aed-4924-96d1-adf8b9fb3310'
just_keep_safe_out_there_node_uuid = '40b80952-aa0c-4b27-8ed5-acd87bb39bc3'
continuation_node_uuid = '28e238b0-2d86-c423-8a7b-d93faa1ad25f'
end_node_uuid = '31c21ce1-1198-4c21-b16d-0f1b95ef341b'
durge_questions_node_uuid = '0860654c-99cf-fbd3-efe8-22f85632d02d'
youre_the_author_node_uuid = '54974771-1fe0-26a1-a86e-a46d4b729628'

body_type_fork_node_uuid = '9f874f70-88d3-45aa-aeab-e8d851439a48'
normal_body_reaction_node_uuid = '64849802-7662-4dfd-be32-d4a71d9c8888'
strong_body_reaction_node_uuid = '7438cdde-c623-4e10-b309-5f789f953aa0'
gith_male_reaction_node_uuid = 'c64398fc-fb5a-4ce3-9cfd-e8fbaf2b6498'
female_reaction_node_uuid = 'fbef6376-4524-4444-97c7-cd77254ea16c'
dragonborn_reaction_node_uuid = 'd7c65e7c-ed64-4964-81cd-0bfe8caefea5'
dwarf_body_reaction_node_uuid = 'ba1b70b0-8b7d-4df4-a3d7-441062101b93'
short_body_reaction_node_uuid = '9ff6809b-4c59-4e54-b050-009f4042b5fd'

#################################################################################################
# Shadowheart cries when Bhaal kills Durge, if she is partnered
#################################################################################################

#################################################################################################
# Dialog: LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf
#################################################################################################

def create_scene_shadowheart_cries_when_durge_dies() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.delete_all_children_dialog_nodes(victim_killed_node_uuid)
    d.delete_all_children_dialog_nodes(victim_survived_node_uuid)
    d.add_child_dialog_node(victim_killed_node_uuid, reaction_fork_node_uuid)
    d.add_child_dialog_node(victim_survived_node_uuid, reaction_fork_node_uuid)

    # Replace TLShot in the opening phase
    # victim_killed_node_uuid
    tl_shot = t.find_effect_component('6acf4f7e-a637-49e1-83f3-e56745569de4')
    bg3.set_bg3_attribute(tl_shot.find('./children/node[@id="CameraContainer"]'), 'Object', 'e94156bf-b946-4a79-b197-d8f092716a21')
    # victim_survived_node_uuid
    tl_shot = t.find_effect_component('5292134a-9a7a-4ab9-805a-9b5a749ad236')
    bg3.set_bg3_attribute(tl_shot.find('./children/node[@id="CameraContainer"]'), 'Object', 'e94156bf-b946-4a79-b197-d8f092716a21')

    # Suppress default Shadowheart's reaction if she is in relationship with Durge
    d.set_dialog_flags(youre_the_author_node_uuid, checkflags = (
        bg3.flag_group('Object', (
            bg3.flag(bg3.FLAG_ORI_Inclusion_PickedAtRandom, True, slot_idx_shadowheart),
            bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_durge),
        )),
        bg3.flag_group('Tag', (
            bg3.flag(bg3.TAG_REALLY_SHADOWHEART, True, slot_idx_shadowheart),
        )),
    ))

    # Reaction fork: partnered or not partnerted with Shadowheart
    d.create_standard_dialog_node(
        reaction_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [partnered_node_uuid, not_partnered_node_uuid],
        None
    )
    d.create_standard_dialog_node(
        partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [no_it_cant_be_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_durge),
            )),
        )
    )
    d.create_standard_dialog_node(
        not_partnered_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [narrator_speaks_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_durge),
            )),
        )
    )

    # No... it can't be true...
    d.create_standard_dialog_node(
        no_it_cant_be_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [narrator_speaks_node_uuid],
        bg3.text_content('hcce3a355g2e43g4231g94fdg0d16de9a5cb8', 1)
    )
    t.create_new_phase(no_it_cant_be_node_uuid, 16.82)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, 0.0, 16.82, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(3.0, 32, variation = 1),
        t.create_emotion_key(6.2, 32, variation = 2),
        t.create_emotion_key(8.5, 32, variation = 24),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            #t.create_value_key(time = 16.82, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, 0.0, 16.82, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 14.1, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)

    # Point the camera at Shadowheart
    # 5fc1d681-14ad-42d8-9cde-ec3eba8393fc
    # d35b098e-8c34-45ee-9dde-21adfd2410a9
    # f1f36ad1-bcb8-4b11-8f0b-e00636ac7510

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.4),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (),
        ()
    ))
    # Point the camera at Shadowheart
    # Euler angles: X = -10, Y = -7, Z = 0
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 9.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.85),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.9),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-7.0, 10.0, 0.0, sequence='yxz')),
        ),
        (),
        ()
    ))

    t.create_tl_shot('e94156bf-b946-4a79-b197-d8f092716a21', 0.0, 3.0)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, (
        t.create_sound_event_key(9.89, sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
        t.create_sound_event_key(11.26, sound_event_id = '8a8136ee-5103-4db4-a2f5-050d2268338a', sound_object_index = 4),
        t.create_sound_event_key(13.06, sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
        t.create_sound_event_key(13.86, sound_event_id = '8428155b-41f4-4618-9bb6-67fe9555954b', sound_object_index = 4),
        t.create_sound_event_key(14.89, sound_event_id = '8a8136ee-5103-4db4-a2f5-050d2268338a', sound_object_index = 4),
        t.create_sound_event_key(16.26, sound_event_id = 'fbb1b315-cb7b-4726-85db-136aaca5b0f9', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, 0.0, 16.82, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = False),
        t.create_value_key(time = 10.7, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 3.0, 14.1)
    t.create_tl_voice(
        bg3.SPEAKER_SHADOWHEART,
        3.0,
        7.0,
        no_it_cant_be_node_uuid,
        is_snapped_to_end = True,
        performance_fade = 0.0,
        fade_in = 1.0,
        fade_out = 1.0)


    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 9.0, 14.82, 'b5822e0c-f5e5-9282-851e-e8f94daf5aef', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6', is_snapped_to_end = True, fade_in = 1.5, fade_out = 1.0)

    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 9.5, 16.82, (
        (
            # -6.8 moves to the right
            t.create_value_key(time = 14.0, interpolation_type = 5, value = -6.2),
        ),
        (
            t.create_value_key(time = 14.0, interpolation_type = 5, value = 1.2),
        ),
        (
            # 1.9 moves forward
            t.create_value_key(time = 14.0, interpolation_type = 5, value = 3.5),
        ),
        (
            #t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.08699, -0.06082, 0.005321, 0.9943)),
            t.create_value_key(time = 14.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-135.0, -12.0, 0.0, sequence='yxz')),
        ),
        (),
        ()
    ))

    t.create_tl_shot('e94156bf-b946-4a79-b197-d8f092716a21', 14.1, 16.82)

    d.create_standard_dialog_node(
        bypass_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [continuation_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_durge),
            )),
        )
    )

    d.add_child_dialog_node(shadowheart_reaction_fork_node_uuid, bypass_reaction_node_uuid, index = 0)

    d.create_standard_dialog_node(
        shadowheart_partnered_reaction_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        #[just_keep_safe_out_there_node_uuid, end_node_uuid],
        [its_difficult_to_speak_node_uuid, end_node_uuid],
        None
    )

    d.create_standard_dialog_node(
        end_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [],
        None,
        end_node = True
    )

    end_nodes = (
        '229059ca-7ca0-55bd-feee-714d3be1ae7e',
        '25545e26-be6a-cb40-9c70-5dedbbdecbf4',
        '476d1ef8-06df-dc56-1d45-ee17c34d16e3',
        '7b262744-577d-1eb2-12b1-0fef9e6bd929')

    for end_node in end_nodes:
        d.remove_dialog_attribute(end_node, 'endnode')
        d.add_child_dialog_node(end_node, shadowheart_partnered_reaction_fork_node_uuid)

    # I... it's difficult for me to talk about...
    d.create_standard_dialog_node(
        its_difficult_to_speak_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [just_keep_safe_out_there_node_uuid],
        bg3.text_content('h79ae6514g939dg49eega50eg86bbf7381a35', 1),
        checkflags = (
            bg3.flag_group('Object', (
                bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_durge),
            )),
        )
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.6,
        its_difficult_to_speak_node_uuid,
        ((None, 'd35b098e-8c34-45ee-9dde-21adfd2410a9'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (2.541, 32, 1)),
            bg3.SPEAKER_DURGE: ((0.0, 1, None),)
        },
        phase_duration = 4.6
    )
    # Smeared make up on Shadowheart's face
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, 0.0, 4.6, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_continuous = True)

    # Place Durge and Shadowheart
    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, 4.6, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (-0.0, 1.0, -0.0, -0.00020365318)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 4.6, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    # Shadowheart looks at Durge
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, 0.0, 4.6, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # Durge looks at Shadowheart
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, 0.0, 4.6, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, 0.0, 4.6, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide everyone
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, 0.0, 4.6, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    # Point the camera at Shadowheart
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 4.6, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -2.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-22.0, 10.0, 0.0, sequence='yxz')),
        ),
        (),
        (),
    ))

    # Just keep safe out there, for me.
    d.create_standard_dialog_node(
        just_keep_safe_out_there_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [body_type_fork_node_uuid],
        bg3.text_content('h4983a16dg6a89g46f6g962fg5dcf9078e466', 2),
        #checkflags = (
        #    bg3.flag_group('Object', (
        #        bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, True, slot_idx_durge),
        #    )),
        #)
    )
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        4.5,
        just_keep_safe_out_there_node_uuid,
        ((None, 'd35b098e-8c34-45ee-9dde-21adfd2410a9'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None),),
            bg3.SPEAKER_DURGE: ((0.0, 1, None),)
        }
    )

    # Smeared make up on Shadowheart's face
    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, 0.0, 4.5, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_continuous = True)

    # Place Durge and Shadowheart
    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, 4.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (-0.0, 1.0, -0.0, -0.00020365318)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 4.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    # Shadowheart looks at Durge
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, 0.0, 4.5, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)
    # Durge looks at Shadowheart
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, 0.0, 4.6, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    # Hide helmet
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, 0.0, 4.5, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            #t.create_value_key(time = 4.5, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    # Hide everyone
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
        t.create_value_key(time = 4.5, interpolation_type = 3, value_name = 'ShowVisual', value = True),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_ASTARION, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_GALE, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_HALSIN, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JAHEIRA, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_KARLACH, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_LAEZEL, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINSC, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_MINTHARA, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_WYLL, 0.0, 4.5, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'ShowVisual', value = False),
    ))

    # Point the camera at Shadowheart
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 4.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.6),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (),
        (),
    ))

    d.create_standard_dialog_node(
        body_type_fork_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [
            dragonborn_reaction_node_uuid,
            strong_body_reaction_node_uuid,
            female_reaction_node_uuid,
            dwarf_body_reaction_node_uuid,
            short_body_reaction_node_uuid,
            gith_male_reaction_node_uuid,
            normal_body_reaction_node_uuid
        ],
        None
    )

    d.create_standard_dialog_node(
        dragonborn_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DRAGONBORN, True, slot_idx_durge),
            )),
        )
    )
    d.create_standard_dialog_node(
        dwarf_body_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_DWARF, True, slot_idx_durge),
            )),
        )
    )
    d.create_standard_dialog_node(
        short_body_reaction_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_node_uuid],
        None,
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_SHORT, True, slot_idx_durge),
            )),
        )
    )


#################################################################################################
# Romanced Shadowheart hugs and kisses Durge after they reject Bhaal
#################################################################################################

#################################################################################################
# Body type 2 except gith (male)
#################################################################################################

def create_scene_shadowheart_kiss_durge_body_type_2() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_cinematic_dialog_node(
        normal_body_reaction_node_uuid,
        [end_node_uuid])

    phase_duration = 27.0
    t.create_new_phase(normal_body_reaction_node_uuid, phase_duration)

    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_attitude_key(12.15, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
        t.create_attitude_key(26.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_attitude_key(0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(6.13, 32, variation = 2),
        t.create_emotion_key(7.34, 32),
        t.create_emotion_key(15.63, 32, variation = 1),
        t.create_emotion_key(20.58, 32),
        t.create_emotion_key(26.0, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 1, variation = 1),
        t.create_emotion_key(3.51, 1),
        t.create_emotion_key(6.08, 1, variation = 1),
        t.create_emotion_key(6.56, 1),
        t.create_emotion_key(8.26, 1, variation = 2),
        t.create_emotion_key(11.26, 1, variation = 1),
        t.create_emotion_key(22.03, 1),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 1, None),
        t.create_emotion_key(25.5, 2, variation = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            4.20,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            9.41,
            turn_mode = 3,
            turn_speed_multiplier = 0.26370612,
            torso_turn_speed_multiplier = 0.26370612,
            head_turn_speed_multiplier = 0.26370612,
            weight = 0.3,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            23.27,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M')
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0.0,
            reset = True,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            1.15,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.21843724,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            4.20,
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            6.56,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3269225,
            torso_turn_speed_multiplier = 0.3269225,
            head_turn_speed_multiplier = 0.10897417,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
        t.create_look_at_key(
            9.4,
            turn_mode = 3,
            turn_speed_multiplier = 0.25471807,
            torso_turn_speed_multiplier = 0.25471807,
            head_turn_speed_multiplier = 0.08490602,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            look_at_mode = 0),
        t.create_look_at_key(
            23.27,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            torso_turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.1,
            weight = 0.0,
            safe_zone_angle = 80.0,
            head_safe_zone_angle = 80.0,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'),
    ), is_snapped_to_end = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, 0.0,  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_sound_event_key(5.52, sound_event_id = 'd0756d07-fd81-4fab-b4af-03d565c7f059', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_sound_event_key(8.74, sound_type = 4, foley_type = 2),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_sound_event_key(12.07, sound_event_id = '50ab7087-b822-455f-9a61-6b10b6e6d968', sound_object_index = 4),
        t.create_sound_event_key(19.2482, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_sound_event_key(5.5, sound_event_id = 'c232329e-2d4e-4f0c-a4d4-ea1585fce27c', sound_object_index = 4),
        t.create_sound_event_key(7.05, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(8.745, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
        t.create_sound_event_key(24.27, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 26.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.PHYSICS, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3, value_name = 'InverseKinematics', value = False),
        t.create_value_key(time = 26.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_DURGE, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.HANDS_IK, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (), is_snapped_to_end = True)

    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 0.0, 25.25, 'a70b0572-f371-49e6-854b-a8347e5db74a', '39e8f7e2-e600-47a8-a5c2-204b1ac9a5a7', fade_in = 2.0, fade_out = 4.0)
    t.create_tl_animation(bg3.SPEAKER_DURGE, 0.0, 25.25, 'a0f79aae-f6c9-4b19-d854-3153658a1da2', '6ef6e0ea-2ae3-46d9-8464-99aa9ba8e427', fade_in = 2.0, fade_out = 4.0)

    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.83),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.38),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1),
        ),
        (),
    ))

    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.0),
            t.create_value_key(time = 16.5, interpolation_type = 5, value = -5.99),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
            t.create_value_key(time = 16.5, interpolation_type = 5, value = 1.79),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.4),
            t.create_value_key(time = 16.5, interpolation_type = 5, value = -0.39),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.6428, 0.0, 0.7660)),
            t.create_value_key(time = 16.5, interpolation_type = 5, value = (0.0, -0.6427, 0.0, 0.7661)),
        ),
        (),
        (),
    ))

    t.create_tl_transform('a6db4283-ef38-4472-827c-fffd0ac04a28', 0.0, phase_duration, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -10.0),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = -9.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.1),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.707071, 0.0, 0.707071)),
            t.create_value_key(time = phase_duration, interpolation_type = 5, value = (0.0, 0.7081, 0.0, 0.7061)),
        ),
        (),
        (),
    ))

    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, phase_duration, disable_conditional_staging = True)
    t.create_tl_shot('a6db4283-ef38-4472-827c-fffd0ac04a28', 16.5, phase_duration, disable_conditional_staging = True)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, 4.58, 8.74,
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)
    t.create_tl_animation(
        bg3.SPEAKER_DURGE, 4.58, 8.74,
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '1913a5ea-cbf7-491b-bf3e-34c829ac69dd',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3.5,
        fade_in = 1.76,
        fade_out = 2.3)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, 9.86, 10.56,
        'a0e37a8e-c619-4d0a-840a-061831fb0523',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_rate = 0.6,
        animation_play_start_offset = 3,
        fade_in = 0.25)

    t.create_tl_animation(
        bg3.SPEAKER_SHADOWHEART, 14.43, 16.97,
        'c26b9b0a-20cc-44a4-a499-18d6d78abec5',
        '16c31857-6247-46a5-9182-28926409bcaf',
        animation_slot = 1,
        animation_play_start_offset = 10.18,
        fade_in = 1,
        fade_out = 0)

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, 0.0, phase_duration, (
        t.create_value_key(time = 25.0, interpolation_type = 3),
    ))

    t.create_tl_shot('4cc77942-a5c2-40cc-89c3-c1187e6bb04e', 25.25, phase_duration, disable_conditional_staging = True)

    t.update_duration()

#################################################################################################
# This creates common nodes of animation timelines such as attitudes, look ats, and emotions
#################################################################################################

def create_common_timeline_nodes(t: bg3.timeline_object, phase_duration: float, smile: float) -> None:
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_attitude_key(0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_0, 0.0, phase_duration, (
        t.create_attitude_key(0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_1, 0.0, phase_duration, (
        t.create_attitude_key(0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.ATTITUDE, bg3.PEANUT_SLOT_2, 0.0, phase_duration, (
        t.create_attitude_key(0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea'),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 32, variation = 2),
        t.create_emotion_key(5.22, 32, variation = 24),
        t.create_emotion_key(19.67, 32, variation = 1),
        t.create_emotion_key(smile, 2)
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_emotion_key(5.99, 32, variation = 1),
        t.create_emotion_key(8.83, 2048, variation = 2),
        t.create_emotion_key(12.08, 32, variation = 1),
        t.create_emotion_key(17.79, 2048, variation = 1),
    ))
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.SPEAKER_JERGAL, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 1),
        t.create_emotion_key(phase_duration - 1.0, 2, variation = 2),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_0, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34, 32, variation = 1),
        t.create_emotion_key(15.79, 32),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_1, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34, 32, variation = 1),
        t.create_emotion_key(15.79, 32),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.EMOTION, bg3.PEANUT_SLOT_2, 0.0, phase_duration, (
        t.create_emotion_key(0.0, 32),
        t.create_emotion_key(1.34, 32, variation = 1),
        t.create_emotion_key(15.79, 32),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_DURGE,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_0, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_1, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)
    t.create_tl_actor_node(bg3.timeline_object.LOOK_AT, bg3.PEANUT_SLOT_2, 0.0, phase_duration, (
        t.create_look_at_key(
            0.0,
            target = bg3.SPEAKER_SHADOWHEART,
            bone = 'Head_M',
            turn_mode = 3,
            turn_speed_multiplier = 0.3,
            head_turn_speed_multiplier = 0.3,
            weight = 0,
            safe_zone_angle = 80,
            head_safe_zone_angle = 80,
            reset = True,
            look_at_mode = 1,
            eye_look_at_bone = 'Head_M'
        ),
    ), is_snapped_to_end = True, is_mimicry = True)

    t.create_tl_material(bg3.SPEAKER_SHADOWHEART, 0.0, phase_duration, '156a2490-d796-402c-b7fc-e00c032042c1', (), (
        t.create_value_key(time = 0.0, value = True),
    ), is_snapped_to_end = True, is_continuous = True)

    # Hide helmets
    t.create_tl_show_armor(bg3.SPEAKER_DURGE, 0.0,  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))
    t.create_tl_show_armor(bg3.SPEAKER_SHADOWHEART, 0.0,  phase_duration, (
        (
            t.create_value_key(time = 0.0, value = False, interpolation_type = 0),
            t.create_value_key(time = phase_duration, interpolation_type = 0)
        ),
        (), (), (), (), (), (), (), (), (), ()
    ))

    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_DURGE, 0.0, phase_duration, (
        t.create_value_key(time = 0.0, interpolation_type = 3),
    ), is_snapped_to_end = True)
    t.create_tl_actor_node(bg3.timeline_object.SHOW_VISUAL, bg3.SPEAKER_JERGAL, 0.0, phase_duration, (
        t.create_value_key(time = 22.5, interpolation_type = 3),
    ))


#################################################################################################
# Body types 3 and 4 (male and female)
#################################################################################################

def create_scene_shadowheart_kiss_durge_body_types_3_4() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_cinematic_dialog_node(
        strong_body_reaction_node_uuid,
        [end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_BODYTYPE_STRONG, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = 34.0
    t.create_new_phase(strong_body_reaction_node_uuid, phase_duration)

    create_common_timeline_nodes(t, phase_duration, 28.5)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.282674465),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.717325535),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))

    # Camera shot #1
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.0),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -5.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = 1.79),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.4),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = 0.6),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-80.0, 0.0, 0.0, sequence="yxz")),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-105.0, 0.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, disable_conditional_staging = True)

    # Hug animation
    t.create_tl_animation(bg3.SPEAKER_DURGE, 0.0, 13.06, 'fb8fbad0-57be-4c54-936b-a58c8fa46876', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.94)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 0.0, 13.06, 'd8684f69-0a63-33dd-3304-87e0128c21ba', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.94)

    t.create_tl_animation(bg3.SPEAKER_DURGE, 12.12, 22.5, 'fb8fbad0-57be-4c54-936b-a58c8fa46876', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 12.12, 22.5, 'd8684f69-0a63-33dd-3304-87e0128c21ba', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)

    # Camera shot #2
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, (
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -6.2),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 10.0, 0.0, sequence="yxz")),
            #t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 12.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, disable_conditional_staging = True)

    # Kiss animation

    # Camera shot #3
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.3),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 0.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, disable_conditional_staging = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_SHADOWHEART, 22.5, phase_duration, (
        t.create_sound_event_key(28.57, sound_event_id = '220abafa-e55f-4124-8cb7-16fca63fda5f', sound_object_index = 4),
    ), is_snapped_to_end = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        t.create_sound_event_key(27.37, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(28.5, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
    ), is_snapped_to_end = True)


    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.625),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.625),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (

            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)

    
    t.create_tl_animation(bg3.SPEAKER_DURGE, 22.5, 32.5, '8cd9dd37-9409-417f-bf1f-011ae3abf79b', '50542eeb-aa9b-4371-aa47-a384ec9fc347',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 5.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, -0.05, -0.625), (0.0, 1.0, 0.0, 0.0)))
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 22.5, 32.5, 'fe1a2452-4ce3-e465-7ae4-50d257f44413', '13ccbef4-3a1f-4c55-988d-b79aa094db1d',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 5.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, 0.05, 0.625), (0.0, 0.0, 0.0, 1.0)))

    t.create_tl_animation(bg3.SPEAKER_DURGE, 24.58, 29.62, 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9a2bcf5c-1d92-4b73-a0a9-f0296bc87239',
                        fade_in = 2.0, fade_out = 1.0, animation_slot = 1, animation_play_start_offset = 4.64, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 24.75, 29.62, 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'da2be73c-6a54-4111-b5e9-c4b23e384bed',
                        fade_in = 1.2, fade_out = 1.5, animation_slot = 1, animation_play_start_offset = 4.89)

    # Camera shot #4
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 32.5, (
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = 2.0),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -0.9),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = bg3.euler_to_quaternion(65.0, 10.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 32.5, disable_conditional_staging = True)

    # Jergal smiles
    t.create_tl_shot('4cc77942-a5c2-40cc-89c3-c1187e6bb04e', 32.5, phase_duration, disable_conditional_staging = True)

    t.update_duration()

#################################################################################################
# Body type 1 (female)
#################################################################################################

def create_scene_shadowheart_kiss_durge_body_type_1() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_cinematic_dialog_node(
        female_reaction_node_uuid,
        [end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_FEMALE, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = 35.47
    t.create_new_phase(female_reaction_node_uuid, phase_duration)

    create_common_timeline_nodes(t, phase_duration, 25.96)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.282674465),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.717325535),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))

    # Camera shot #1
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.0),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -7.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.4),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -0.62),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-80.0, 0.0, 0.0, sequence="yxz")),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-57.0, 0.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, disable_conditional_staging = True)

    # Hug animation
    t.create_tl_animation(bg3.SPEAKER_DURGE, 0.0, 13.06, '882164de-1f6b-4d2a-b336-1f366cb36f14', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.94)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 0.0, 13.06, 'a46f695f-051b-be6d-20cd-32f733524930', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.94)

    t.create_tl_animation(bg3.SPEAKER_DURGE, 12.12, 22.5, '882164de-1f6b-4d2a-b336-1f366cb36f14', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 12.12, 22.5, 'a46f695f-051b-be6d-20cd-32f733524930', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)

    # Camera shot #2
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, (
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -6.2),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 10.0, 0.0, sequence="yxz")),
            #t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 12.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, disable_conditional_staging = True)

    # Kiss animation

    # Camera shot #3
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.3),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 10.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, disable_conditional_staging = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        t.create_sound_event_key(20.85, sound_event_id = 'f728f472-57d5-45ce-be9e-6e2f927bee0d', sound_object_index = 4),
        t.create_sound_event_key(23.92, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(23.92, sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key(24.25, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(25.96, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
        t.create_sound_event_key(29.35, sound_event_id = '7c5a4af8-0d42-48b2-b293-c344c204b919', sound_object_index = 4),
    ), is_snapped_to_end = True)


    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.63),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.63),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)

    t.create_tl_animation(bg3.SPEAKER_DURGE, 22.5, 33.97, '84e8ba51-7b67-4cfd-989d-ecd696545407', '50542eeb-aa9b-4371-aa47-a384ec9fc347',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 7.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, -0.05, -0.63), (0.0, 1.0, 0.0, 0.0)))
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 22.5, 33.97, '95449125-1af2-0744-cb51-1e2b3e8eec67', '13ccbef4-3a1f-4c55-988d-b79aa094db1d',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 7.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, 0.05, 0.63), (0.0, 0.0, 0.0, 1.0)))

    t.create_tl_animation(bg3.SPEAKER_DURGE, 23.13, 26.8, 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9a2bcf5c-1d92-4b73-a0a9-f0296bc87239',
                        fade_in = 1.0, fade_out = 1.0, animation_slot = 1, animation_play_start_offset = 5.18, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 22.75, 27.62, 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'da2be73c-6a54-4111-b5e9-c4b23e384bed',
                        fade_in = 1.2, fade_out = 1.5, animation_slot = 1, animation_play_start_offset = 4.89)

    t.create_tl_animation(bg3.SPEAKER_DURGE, 28.78, 30.84, 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9a2bcf5c-1d92-4b73-a0a9-f0296bc87239',
                        fade_in = 1.0, fade_out = 1.0, animation_slot = 1, animation_play_start_offset = 2.62, offset_type = 5)
    #t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 28.38, 30.8, 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'da2be73c-6a54-4111-b5e9-c4b23e384bed',
    #                    fade_in = 1.2, fade_out = 1.5, animation_slot = 1, animation_play_start_offset = 4.46)

    # Camera shot #4
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 33.97, (
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -1.4),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = bg3.euler_to_quaternion(26.0, 10.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 33.97, disable_conditional_staging = True)

    # Jergal smiles
    t.create_tl_shot('4cc77942-a5c2-40cc-89c3-c1187e6bb04e', 33.97, phase_duration, disable_conditional_staging = True)

    t.update_duration()

#################################################################################################
# Body type 2 (male gith)
#################################################################################################

def create_scene_shadowheart_kiss_durge_body_type_2_gith() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/LowerCity/BhaalTemple/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/LOW_BhaalTemple_PostBattleDarkUrge_Resistance.lsf'), d)

    slot_idx_durge = d.get_speaker_slot_index(bg3.SPEAKER_DURGE)
    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)

    d.create_cinematic_dialog_node(
        gith_male_reaction_node_uuid,
        [end_node_uuid],
        checkflags = (
            bg3.flag_group('Tag', (
                bg3.flag(bg3.TAG_GITH, True, slot_idx_durge),
            )),
        )
    )

    phase_duration = 35.44
    t.create_new_phase(gith_male_reaction_node_uuid, phase_duration)

    create_common_timeline_nodes(t, phase_duration, 27.81)

    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -8.282674465),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, -0.24996054, 0.0, 0.96825606)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 0.0, 22.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -7.717325535),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.5080471000000006),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = (0.0, 0.96666896, 0.0, 0.25602978)),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.0),
        ),
        (),
    ))

    # Camera shot #1
    """
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.0),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -7.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.7),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.4),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -0.62),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-80.0, 0.0, 0.0, sequence="yxz")),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-57.0, 0.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, disable_conditional_staging = True)
    # Camera shot #1
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -6.0),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -5.5),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = 1.79),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -0.4),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = 0.6),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-80.0, 0.0, 0.0, sequence="yxz")),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-105.0, 0.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, disable_conditional_staging = True)
    """

    # Camera shot #1
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, (
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = -5.5),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = -7.0),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = 0.6),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = 1.2),
        ),
        (
            t.create_value_key(time = 0.0, interpolation_type = 5, value = bg3.euler_to_quaternion(-105.0, 4.0, 0.0, sequence="yxz")),
            t.create_value_key(time = 17.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-140.0, 4.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 0.0, 18.5, disable_conditional_staging = True)

    # Hug animation
    t.create_tl_animation(bg3.SPEAKER_DURGE, 0.0, 13.06, '882164de-1f6b-4d2a-b336-1f366cb36f14', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.94)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 0.0, 13.06, 'a46f695f-051b-be6d-20cd-32f733524930', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.94)

    t.create_tl_animation(bg3.SPEAKER_DURGE, 12.12, 22.5, '882164de-1f6b-4d2a-b336-1f366cb36f14', 'a2dae3f2-e3c9-4fc7-b8ac-82abf4a153b0',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 12.12, 22.5, 'a46f695f-051b-be6d-20cd-32f733524930', 'c8dad77b-5b76-44fe-bfeb-61d676ede3f6',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.29)

    # Camera shot #2
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, (
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -6.2),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = -0.5),
        ),
        (
            t.create_value_key(time = 18.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 10.0, 0.0, sequence="yxz")),
            #t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(-70.0, 12.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 18.5, 22.5, disable_conditional_staging = True)

    # Kiss animation

    # Camera shot #3
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -9.2),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.3),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = bg3.euler_to_quaternion(120.0, 10.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 22.5, 27.5, disable_conditional_staging = True)

    t.create_tl_actor_node(bg3.timeline_object.SOUND, bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        t.create_sound_event_key(24.57, sound_event_id = '90a31a12-9f32-47e1-899e-cdced0705f27', sound_object_index = 4),
        t.create_sound_event_key(24.57, sound_event_id = '025fa6be-55ec-43fe-af6a-03b746163d72', sound_object_index = 4),
        t.create_sound_event_key(26.38, sound_event_id = 'ffbbbd57-5c31-444d-bc3a-c3d14df0be53', sound_object_index = 4),
        t.create_sound_event_key(27.81, sound_event_id = 'aa8db628-8c78-4632-ab7a-2ac210393e93', sound_object_index = 4),
    ), is_snapped_to_end = True)


    # Place Shadowheart
    t.create_tl_transform(bg3.SPEAKER_SHADOWHEART, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 0.63),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 0.0, 0.0, 1.0)),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)
    # Place Player
    t.create_tl_transform(bg3.SPEAKER_DURGE, 22.5, phase_duration, (
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -8.0),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.05),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = -0.63),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = (0.0, 1.0, 0.0, 0.0)),
        ),
        (
            t.create_value_key(time = 22.5, interpolation_type = 5, value = 1.0),
        ),
        (),
    ), is_snapped_to_end = True)

    # 18.44
    # 20.91 to 41.82
    t.create_tl_animation(bg3.SPEAKER_DURGE, 22.5, 33.94, 'd885fa92-168a-45a9-acee-824013d85320', '50542eeb-aa9b-4371-aa47-a384ec9fc347',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, -0.05, -0.63), (0.0, 1.0, 0.0, 0.0)))
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 22.5, 33.94, '5db0326e-fb0e-d3dd-a56d-51aa4da6ab00', '13ccbef4-3a1f-4c55-988d-b79aa094db1d',
                        fade_in = 0.0, fade_out = 0.0, animation_play_start_offset = 6.0, animation_play_rate = 1.0,
                        target_transform = t.create_animation_target_transform(1.0, (-8.0, 0.05, 0.63), (0.0, 0.0, 0.0, 1.0)))

    t.create_tl_animation(bg3.SPEAKER_DURGE, 23.58, 29.05, 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9a2bcf5c-1d92-4b73-a0a9-f0296bc87239',
                        fade_in = 1.0, fade_out = 1.0, animation_slot = 1, animation_play_start_offset = 4.64, offset_type = 5)
    t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 23.75, 28.62, 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'da2be73c-6a54-4111-b5e9-c4b23e384bed',
                        fade_in = 1.2, fade_out = 1.5, animation_slot = 1, animation_play_start_offset = 4.89)

    #t.create_tl_animation(bg3.SPEAKER_DURGE, 28.78, 30.84, 'c26b9b0a-20cc-44a4-a499-18d6d78abec5', '9a2bcf5c-1d92-4b73-a0a9-f0296bc87239',
    #                    fade_in = 1.0, fade_out = 1.0, animation_slot = 1, animation_play_start_offset = 2.62, offset_type = 5)
    #t.create_tl_animation(bg3.SPEAKER_SHADOWHEART, 28.38, 30.8, 'a0e37a8e-c619-4d0a-840a-061831fb0523', 'da2be73c-6a54-4111-b5e9-c4b23e384bed',
    #                    fade_in = 1.2, fade_out = 1.5, animation_slot = 1, animation_play_start_offset = 4.46)

    # Camera shot #4
    t.create_tl_transform('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 33.94, (
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -8.5),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = 1.8),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = -1.4),
        ),
        (
            t.create_value_key(time = 27.5, interpolation_type = 5, value = bg3.euler_to_quaternion(26.0, 10.0, 0.0, sequence="yxz")),
        ),
        (),
        (),
    ))
    t.create_tl_shot('d35b098e-8c34-45ee-9dde-21adfd2410a9', 27.5, 33.94, disable_conditional_staging = True)

    # Jergal smiles
    t.create_tl_shot('4cc77942-a5c2-40cc-89c3-c1187e6bb04e', 33.94, phase_duration, disable_conditional_staging = True)

    t.update_duration()


add_build_procedure('create_scene_shadowheart_cries_when_durge_dies', create_scene_shadowheart_cries_when_durge_dies)
add_build_procedure('create_scene_shadowheart_kiss_durge_body_type_1', create_scene_shadowheart_kiss_durge_body_type_1)
add_build_procedure('create_scene_shadowheart_kiss_durge_body_type_2', create_scene_shadowheart_kiss_durge_body_type_2)
add_build_procedure('create_scene_shadowheart_kiss_durge_body_type_2_gith', create_scene_shadowheart_kiss_durge_body_type_2_gith)
add_build_procedure('create_scene_shadowheart_kiss_durge_body_types_3_4', create_scene_shadowheart_kiss_durge_body_types_3_4)
