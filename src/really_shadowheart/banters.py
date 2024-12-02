from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

#############################################################################################################
# Lae'zel/Wyll/Shadowheart banter bugfix: both Shar and Selune banters didn't have their respective flags.
# This causes both banters to play one after another, which is very odd.
#############################################################################################################


def fix_banters() -> None:
    #############################################################################################################
    # Public/GustavDev/Gossips/Gossips.lsx
    #############################################################################################################
    g = bg3.gossips_object(files.get_file("Gustav", "Public/GustavDev/Gossips/Gossips.lsx"))

    # PB_Laezel_Shadowheart_ROM_Act3_001
    g.add_condition_flag('864be4b4-5180-00c6-71eb-2154cd643362', 'Flag', bg3.FLAG_ORI_Shadowheart_Event_PostNightfall_DiscussionAvailable)

    # PB_Laezel_Shadowheart_ROM_Act3_002
    g.add_condition_flag('145920b8-d582-5cd3-03c0-65557663fad9', 'Flag', bg3.FLAG_ORI_Shadowheart_State_PostSkinnyDipping_DiscussionAvailable)

    # PB_Wyll_Shadowheart_ROM_Act3_001
    g.add_condition_flag('78ee3f89-256f-0dba-f14c-4fcbb1a731a1', 'Flag', bg3.FLAG_ORI_Shadowheart_State_SharPath)
    g.add_condition_flag('78ee3f89-256f-0dba-f14c-4fcbb1a731a1', 'Flag', bg3.FLAG_ORI_State_ShadowheartIsDating)

    # PB_Wyll_Shadowheart_ROM_Act3_002
    g.add_condition_flag('a5be03a8-7ecd-5d0e-b1d5-283f58806581', 'Flag', bg3.FLAG_ORI_Shadowheart_State_EnemyOfSharPath)
    g.add_condition_flag('a5be03a8-7ecd-5d0e-b1d5-283f58806581', 'Flag', bg3.FLAG_ORI_State_ShadowheartIsDating)

add_build_procedure('fix_banters', fix_banters)
