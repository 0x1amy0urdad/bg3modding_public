from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

########################################################
# If parents are saved, Tav proposes to Shadowheart
# in the romance fate cutscene
########################################################

########################################################
# Dialog: END_GameFinale_RomanceFates_Shadowheart.lsf
########################################################

def create_scene_marriage_proposal() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Act3/EndGame/END_GameFinale_RomanceFates_Shadowheart.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/END_GameFinale_RomanceFates_Shadowheart.lsf'), d)

    # 91a8325d-1459-2217-ee8a-c172f8e5adee - mind flayer entry point
    # 4ad0bd1e-5cc1-1d9b-cc27-84c466ddc49d - Shar path, killed parents
    # f87f78dd-6113-7dd3-0a25-30dc1b4e45c7 - Shar path, saved parents
    # 78380d5b-cdb0-b39f-e230-e4c604c0c215 - Selune path, saved parents
    # e566423f-90fd-8b94-5be0-4acdaed3979d - Selune path, killed parents
    # ab53db8d-015d-fce5-c444-f9ce225eea6c - didn't go to the cloister

    """
    d.remove_root_node('e566423f-90fd-8b94-5be0-4acdaed3979d')
    d.add_root_node('e566423f-90fd-8b94-5be0-4acdaed3979d', index = 0)
    d.set_dialog_flags(
        'e566423f-90fd-8b94-5be0-4acdaed3979d',
        setflags=(
            bg3.flag_group('Global', (
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_SavedParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_Shar_KilledParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_SavedParents, False, None),
                bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RejectShar_KilledParents, True, None),
            )),
        ),
        checkflags=())
    """

    its_not_an_exciting_life_selune_path_node_uuid = 'cc85bbdb-0b50-276b-f638-064e23ca9844'
    its_not_an_exciting_life_shar_redemption_path_node_uuid = '61b7b9ca-9867-f3c7-fcff-e950fd556383'
    marry_me_selune_path_node_uuid = 'cd1b875b-88b5-4d2f-9a18-ac10859fb794'
    marry_me_selune_dead_parents_path_node_uuid = 'db110fb9-7071-4088-b6b5-d7940dc43bb9'
    marry_me_shar_redemption_path_node_uuid = '9521b783-8d6b-4315-985d-c81448ef86b1'
    yes_node_uuid = '468a5596-9336-4257-8729-fbc514d5c0c5'
    time_to_find_myself_node_uuid = '80f78526-0763-45a1-8155-0d512222776e'
    end_cinematic_node_uuid = 'd3c4e608-8352-6aff-ebad-d4ab8ffe72d3' # alias to efbdf0bf-738d-35da-eff4-346ff2c1b950
    ive_got_to_move_on = '8ebf7ba3-ae8c-712a-74bc-62c4e563e0a0' # existing node
    i_can_choose_my_own_path_node_uuid = '6046cd40-1cab-99fb-2065-2ff0ace182f2' # existing node

    shadowheart_tav_married_true = bg3.flag_group(bg3.flag_group.GLOBAL, (
        bg3.flag(ORI_Shadowheart_Tav_State_Married.uuid, True),
        bg3.flag(bg3.FLAG_ORI_Shadowheart_State_RetiredToFarmWithAvatar, True)
    ))

    # I want to spend my life with you. Would you marry me?
    d.create_standard_dialog_node(
        marry_me_selune_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=[shadowheart_tav_married_true])

    # I want to spend my life with you. Would you marry me?
    d.create_standard_dialog_node(
        marry_me_selune_dead_parents_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [time_to_find_myself_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        constructor=bg3.dialog_object.QUESTION)

    # I want to spend my life with you. Would you marry me?
    d.create_standard_dialog_node(
        marry_me_shar_redemption_path_node_uuid,
        bg3.SPEAKER_PLAYER,
        [yes_node_uuid],
        bg3.text_content('h2155d8e8g3584g48fbg95fdg5651ebed00ee', 1),
        constructor=bg3.dialog_object.QUESTION,
        setflags=[shadowheart_tav_married_true])

    # What more could I need? If I had all that, and I had you... Yes. I want to share everything that lies ahead of me with you.
    d.create_standard_dialog_node(
        yes_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [end_cinematic_node_uuid],
        bg3.text_content('h0a14be70g6828g4ed5g8202g288788d68b6e', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        12.0,
        yes_node_uuid,
        ((5.7, '3206da4a-d3c6-46aa-ba8f-d6f1a8cdef72'), (None, '4ba153f7-42ff-401a-88c3-2620964e041b')),
        emotions={
            bg3.SPEAKER_SHADOWHEART: [(0.0, 2, None), (9.2, 2, 2)],
            bg3.SPEAKER_PLAYER: [(0.0, 64, None), (3.3, 64, 1), (4.7, 2, None)]
        }
    )

    # I can't... at least not right now. I'm sorry. After everything that happened with my parents, with Shar, I need time to myself. Time to find myself.
    d.create_standard_dialog_node(
        time_to_find_myself_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [i_can_choose_my_own_path_node_uuid],
        bg3.text_content('h70a5193egc2c9g4b82g9752g7545e7c73658', 1),
        constructor=bg3.dialog_object.ANSWER)

    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        19.0,
        time_to_find_myself_node_uuid,
        ((None, 'f3318a30-48f3-4e93-b87b-b272d92ee652'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: [(0.0, 32, None), (1.7, 2048, 1), (8.44, 16, None), (11.72, 32, None)],
            bg3.SPEAKER_PLAYER: [(0.0, 32, None),]
        }
    )

    d.add_child_dialog_node(its_not_an_exciting_life_selune_path_node_uuid, marry_me_selune_path_node_uuid, index = 0)
    d.add_child_dialog_node(its_not_an_exciting_life_shar_redemption_path_node_uuid, marry_me_selune_path_node_uuid, index = 0)
    d.add_child_dialog_node(ive_got_to_move_on, marry_me_selune_dead_parents_path_node_uuid, index = 0)

    t.update_duration()

add_build_procedure('create_scene_marriage_proposal', create_scene_marriage_proposal)
