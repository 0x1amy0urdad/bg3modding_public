from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

########################################################################################
# Minthara about copmpanions
########################################################################################

def patch_minthara_conversations() -> None:
    ########################################################################################
    # Minthara_InParty.lsf
    ########################################################################################
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minthara_InParty.lsf'))

    # I'm curious to hear your thoughts about our companions.
    d.remove_dialog_attribute('9b0f15eb-4dfd-011a-964f-b9b8c4c596d5', 'ShowOnce')
    d.set_dialog_flags('9b0f15eb-4dfd-011a-964f-b9b8c4c596d5', checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GEN_SoloPlayer, False, None),
        )),
    ))


    ########################################################################################
    # Minthara_InParty_Nested_PartyMemberThoughts.lsf
    ########################################################################################
    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/Minthara_InParty_Nested_PartyMemberThoughts.lsf'))

    # I'm curious to hear what you think of Shadowheart.
    d.remove_dialog_attribute('c390d470-6d3d-4605-bf2b-03a75e72ca1c', 'ShowOnce')
    d.set_dialog_flags('c390d470-6d3d-4605-bf2b-03a75e72ca1c', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Shadowheart, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Shadowheart, True, None),
        )),
    ))

    # How do you and Lae'zel get along?
    d.remove_dialog_attribute('d96b1c54-8903-4eac-9976-b44b8984aad3', 'ShowOnce')
    d.set_dialog_flags('d96b1c54-8903-4eac-9976-b44b8984aad3', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Laezel, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Laezel, True, None),
        )),
    ))

    # What do you make of Astarion?
    d.remove_dialog_attribute('ff494699-3d8a-4333-a709-27f6b3796dfc', 'ShowOnce')
    d.set_dialog_flags('ff494699-3d8a-4333-a709-27f6b3796dfc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Astarion, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Astarion, True, None),
            bg3.flag(bg3.FLAG_ORI_Astarion_State_StayedVampireSpawn, False, None),
            bg3.flag(bg3.FLAG_ORI_Astarion_State_BecameVampireLord, False, None),
        )),
    ))


    # Have you spent much time with Gale?
    d.remove_dialog_attribute('03bdf98e-ab18-4452-b88a-6921f0755ff1', 'ShowOnce')
    d.set_dialog_flags('03bdf98e-ab18-4452-b88a-6921f0755ff1', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Gale, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Gale, True, None),
            bg3.flag(bg3.FLAG_ORI_Gale_Event_BombDisarmed, True, None),
        )),
    ))

    # Any thoughts on Wyll?
    d.remove_dialog_attribute('62ca8389-3502-4c56-8164-4130eafcb737', 'ShowOnce')
    d.set_dialog_flags('62ca8389-3502-4c56-8164-4130eafcb737', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Wyll, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Wyll, True, None),
            bg3.flag(bg3.FLAG_CAMP_MizorasPact_State_WyllReleasedFromPact, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_GrandDuke, False, None),
            bg3.flag(bg3.FLAG_CAMP_MizorasPact_State_WyllEternalPact, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_BladeOfFrontiers, False, None),
            bg3.flag(bg3.FLAG_GLO_Wyll_State_BladeOfAvernus, False, None),
        )),
    ))


    # You and Karlach seem to be friendly.
    d.remove_dialog_attribute('ad478103-114e-4250-8afa-05141b3627fc', 'ShowOnce')
    d.set_dialog_flags('ad478103-114e-4250-8afa-05141b3627fc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_Avatar_Karlach, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Karlach, True, None),
        )),
    ))

    # What do you make of Jaheira?
    d.remove_dialog_attribute('4d323bd3-8403-4246-ae83-0db89ab5689b', 'ShowOnce')
    d.set_dialog_flags('4d323bd3-8403-4246-ae83-0db89ab5689b', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Jaheira_State_PermaDefeated, False, None),
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Jaheira, True, None),
        )),
    ))

    # You and Minsc are unusual allies.
    d.remove_dialog_attribute('3e3e6869-d30a-4bf9-831c-54847a77dfdc', 'ShowOnce')
    d.set_dialog_flags('3e3e6869-d30a-4bf9-831c-54847a77dfdc', setflags = (), checkflags = (
        bg3.flag_group('Global', (
            bg3.flag(bg3.FLAG_GLO_Origin_PartOfTheTeam_Minsc, True, None),
        )),
    ))

    # Leave
    d.remove_dialog_attribute('aad7d24d-8576-40d0-93ac-73d045054069', 'ShowOnce')

add_build_procedure('patch_minthara_conversations', patch_minthara_conversations)
