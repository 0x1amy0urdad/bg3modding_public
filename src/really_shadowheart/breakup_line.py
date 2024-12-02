from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

########################################################################################
# When Shadowheart breaks up with Tav/Durge because of Mizora, Halsin, or drow twins,
# there is no specific line for any of those;
# this is a replacement that works for all non-origin break-ups.
########################################################################################

def create_breakup_line() -> None:
    ########################################################################################
    # Dialog: ShadowHeart_InParty2.lsf
    ########################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2.lsf'), d)

    slot_idx_shadowheart = d.get_speaker_slot_index(bg3.SPEAKER_SHADOWHEART)
    slot_idx_tav = d.get_speaker_slot_index(bg3.SPEAKER_PLAYER)

    shadowheart_break_up_finish_true = bg3.flag_group('Object', (bg3.flag(Shadowheart_BreakUp_Notification_Finish.uuid, True, slot_idx_tav),))
    shadowheart_skinnydipping_false = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_NIGHT_Shadowheart_Skinnydipping, False, None),))
    shadowheart_enemy_of_shar_true = bg3.flag_group('Global', (bg3.flag(bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath, True, None),))
    tav_partnered_false = bg3.flag_group('Object', (bg3.flag(bg3.FLAG_ORI_State_PartneredWithShadowheart, False, slot_idx_tav),))

    greeting_node_uuid = '8e227955-8a68-42da-98b6-3fcff2c2af5f'
    new_answer_node_uuid = '5f23932d-fe2c-4ea6-8a84-8483f63259dc'
    dialog_continuation_node_uuid = '0251a191-20a0-4ca5-b8c1-d4c1dd386190'

    d.create_standard_dialog_node(
        new_answer_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        [dialog_continuation_node_uuid],
        bg3.text_content('h03a13c89ge885g4ebcgbc71gb2d502c80f3a', 1),
        setflags=(shadowheart_break_up_finish_true, shadowheart_skinnydipping_false),
        checkflags=(shadowheart_enemy_of_shar_true, tav_partnered_false))
    t.create_simple_dialog_answer_phase(
        bg3.SPEAKER_SHADOWHEART,
        11.2,
        new_answer_node_uuid,
        ((11.2, '0e8837db-4344-48d0-9175-12262c73806b'),),
        emotions={
            bg3.SPEAKER_SHADOWHEART: ((0.0, 32, None), (4.76, 16, None), (9.05, 2048, None))
        })

    d.add_child_dialog_node(greeting_node_uuid, new_answer_node_uuid)
    t.update_duration()

add_build_procedure('create_breakup_line', create_breakup_line)
