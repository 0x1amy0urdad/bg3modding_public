from __future__ import annotations

import bg3moddinglib as bg3

from .build import add_build_procedure
from .context import files
from .flags import *

#################################################################################################
# Encounter with Gandrel in the putrid bog, this adds protected/betrayed flags to dialog nodes
#################################################################################################

#################################################################################################
# Dialog: HAG_GurHunter_OM_Astarion_COM.lsf
#################################################################################################

def create_conversation_gur_monster_hunter_putrid_bog() -> None:

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Companions/Origin_Moments/HAG_GurHunter_OM_Astarion_COM.lsf'))

    protected_nodes_uuids = [
        '6a62689b-808c-9857-d533-3ea53adb9d58',
        '6836ff29-ee6c-2ae2-c776-8f1cf51445e8',
        'dfa4762d-2100-ae80-5ac3-629e4464f365',
        '0e357a0b-bb60-c257-4d6a-b6257f891d6f'
    ]

    betrayed_nodes_uuids = [
        'f762abd3-350f-8f5a-bde0-96902de0ea47',
        '17f20ee8-b8ef-9a4e-dcf2-92783bf3914f',
        'd40fe431-d761-c1f4-1f51-ba31c3bbab35',
    ]

    for node_uuid in protected_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, True, None),
                bg3.flag(Tav_Betrayed_Astarion.uuid, False, None),
            )),
        ))

    for node_uuid in betrayed_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, False, None),
                bg3.flag(Tav_Betrayed_Astarion.uuid, True, None),
            )),
        ))


    #################################################################################################
    # Dialog: HAG_GurHunter.lsf
    #################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/Gustav/Story/DialogsBinary/Act1/Swamp/HAG_GurHunter.lsf'))

    protected_nodes_uuids = [
        '75c501e8-f14e-50fe-345a-5215a96b41f9',
        '67f1947a-1ab7-c258-0154-c281e044dce6',
        'd5038649-4a25-e499-a298-40880a5fb433',
        'fe4cdf90-da1a-fbd9-d4df-f3b0df3f4925'
    ]

    betrayed_nodes_uuids = [
        '6433cf07-496a-e117-b4bb-64c28f2d26cb'
    ]

    for node_uuid in protected_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, True, None),
                bg3.flag(Tav_Betrayed_Astarion.uuid, False, None),
            )),
        ))

    for node_uuid in betrayed_nodes_uuids:
        d.set_dialog_flags(node_uuid, setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Tav_Protected_Astarion.uuid, False, None),
                bg3.flag(Tav_Betrayed_Astarion.uuid, True, None),
            )),
        ))


    #################################################################################################
    # Dialog: ShadowHeart_InParty2_Nested_DefaultChapter.lsf
    #################################################################################################

    d = bg3.dialog_object(files.get_file('Gustav', 'Mods/GustavDev/Story/DialogsBinary/Companions/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'))
    t = bg3.timeline_object(files.get_file('Gustav', 'Public/GustavDev/Timeline/Generated/ShadowHeart_InParty2_Nested_DefaultChapter.lsf'), d)

    #################################################################################################
    # Shadowheart reaction to Tav protecting Astarion from the Gut Hunter
    #################################################################################################


    #entry_template_node_uuid = '5027aa91-9c7b-4e32-8ca9-7b0e511c1496'
    template_node_uuid = 'bbc05a29-e779-486e-86a0-ae796c2893b3'

    d.add_child_dialog_node('9f7d4510-e658-4b23-b066-4fe117fbba7b', '4654bc7c-ac9a-4351-aa74-9370075aac6a', index = 0)

    # What do you make of our encounter with the Gur monster hunter?
    d.create_standard_dialog_node(
        '4654bc7c-ac9a-4351-aa74-9370075aac6a',
        bg3.SPEAKER_PLAYER,
        ['79071ea4-3722-4a1d-9856-07e8487524bb'],
        bg3.text_content('h8b4751f2g4391g412dg8f63gc05bf8c67056', 1),
        constructor = bg3.dialog_object.QUESTION,
        checkflags = (
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(bg3.FLAG_GLO_CAMP_State_NightMode, True, None),
                bg3.flag(Tav_Protected_Astarion.uuid, True, None),
                bg3.flag(Shadowheart_Reacted_Astarion_Protected.uuid, False, None),
            )),
        ))

    # Speaking truthfully, I'm a little surprised you chose to shield Astarion.
    d.create_standard_dialog_node(
        '79071ea4-3722-4a1d-9856-07e8487524bb',
        bg3.SPEAKER_SHADOWHEART,
        ['8540671a-9877-4e44-8370-e8e82aeb1796', 'b6c92aa7-6b07-7a52-a553-9a283b30bc32', '4aead3ff-33fb-484a-bbf5-0d9fea92d42c'],
        #[],
        bg3.text_content('hb3033ad0gf4d6g41d7gba68gab137658a56a', 1),
        constructor=bg3.dialog_object.ANSWER,
        #end_node=True,
        setflags=(
            bg3.flag_group(bg3.flag_group.GLOBAL, (
                bg3.flag(Shadowheart_Reacted_Astarion_Protected.uuid, True, None),
            )),
        ))

    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        4.461,
        '79071ea4-3722-4a1d-9856-07e8487524bb',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 4.7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, 4, None), (1.89, 4, 1), (3.19, 4, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', None),),
            bg3.SPEAKER_PLAYER: ((0.0, '7f6ccd67-aa7d-4803-ad7f-629c7783e83f', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', None),),
        })
    t.create_tl_shot('7b067edd-f53f-49e1-95bc-0986e6e2ca2f', 0.0, 4.5)
    t.create_tl_shot('e08db860-1e62-4271-bf4e-d51602468573', 4.5, 4.7)

    # He's one of us. I wasn't about to just betray him.
    d.create_standard_dialog_node(
        '8540671a-9877-4e44-8370-e8e82aeb1796',
        bg3.SPEAKER_PLAYER,
        ['568c8ed8-939a-443c-8548-f22e7034e709'],
        bg3.text_content('hfc1897b2g015ag4589gbe29gff4cf74aff01', 1),
        constructor=bg3.dialog_object.QUESTION)

    # How adorable. Such camaraderie at such a bargain rate.
    d.create_standard_dialog_node(
        '568c8ed8-939a-443c-8548-f22e7034e709',
        bg3.SPEAKER_SHADOWHEART,
        ['b5672ea7-9093-e82d-5b87-bee7b48bbdf6'],
        bg3.text_content('h56359b73gb29ag4f19gbcd0gcd15a66d30f6', 1),
        constructor=bg3.dialog_object.ANSWER)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        4.368,
        '568c8ed8-939a-443c-8548-f22e7034e709',
        skip_tl_nodes = ('TLShot',),
        phase_duration=4.7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.5, 16, None), (1.77, 16, 1), (2.83, 32, None), (3.79, 2048, None))
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 4.4)
    t.create_tl_shot('e7f21f15-f386-40f4-bb0f-2f9f42249ad1', 4.4, 4.7)

    # You're as loyal as a pup and twice as handsome.
    # You're as loyal as a pup and twice as pretty.
    # You're as loyal as a pup and twice as charming.
    d.create_standard_dialog_node(
        'b5672ea7-9093-e82d-5b87-bee7b48bbdf6',
        bg3.SPEAKER_SHADOWHEART,
        [],
        (
            bg3.text_content('h18a8a0c7g2147g42beg8a5fgdedc6b33b731', 1, '2ca3a5d6-7af6-48d8-8b97-f1b2eb1702a3', custom_sequence_id='2ca3a5d6-7af6-48d8-8b97-f1b2eb1702a3'),
            bg3.text_content('haab6ee84g0a04g403dga445g5d9e7088377b', 1, '57e2aae4-fbd1-46f2-8f67-167e9b6a57db', custom_sequence_id='57e2aae4-fbd1-46f2-8f67-167e9b6a57db'),
            bg3.text_content('h3ce42409g98f5g4c9bgaf28ge161d5015c0a', 1, '74290c11-8cff-4c82-b1d1-5dc565cd0794', custom_sequence_id='74290c11-8cff-4c82-b1d1-5dc565cd0794'),
        ),
        constructor=bg3.dialog_object.ANSWER,
        end_node=True)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        3.224,
        'b5672ea7-9093-e82d-5b87-bee7b48bbdf6',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 3.8,
        line_index = 0,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None))
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 3.224)
    t.create_tl_shot('0e8837db-4344-48d0-9175-12262c73806b', 3.224, 3.8)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        3.379,
        'b5672ea7-9093-e82d-5b87-bee7b48bbdf6',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 3.8,
        line_index = 1,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None))
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 3.379)
    t.create_tl_shot('0e8837db-4344-48d0-9175-12262c73806b', 3.379, 3.8)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        3.306,
        'b5672ea7-9093-e82d-5b87-bee7b48bbdf6',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 3.8,
        line_index = 2,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.61, 16, None), (1.2, 4, None), (2.06, 16, None), (2.95, 64, None))
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 3.306)
    t.create_tl_shot('0e8837db-4344-48d0-9175-12262c73806b', 3.306, 3.8)

    # He knows too much - safer to keep him with us than risk him exposing our condition.
    d.create_standard_dialog_node(
        'b6c92aa7-6b07-7a52-a553-9a283b30bc32',
        bg3.SPEAKER_PLAYER,
        ['95445707-07c8-af8b-7d3b-3980eb4ffcce'],
        bg3.text_content('hc1913f71g45e1g4388g9a08gbbef9784d018', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Very strategic of you, actually. Hopefully keeping him in our midst proves to be the lesser risk.
    d.create_standard_dialog_node(
        '95445707-07c8-af8b-7d3b-3980eb4ffcce',
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('hf78f63ffg0e44g4359ga02cg205cb18ab600', 1),
        constructor=bg3.dialog_object.ANSWER,
        end_node=True)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        6.510,
        '95445707-07c8-af8b-7d3b-3980eb4ffcce',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.4, 16, None), (1.51, 4, None), (2.8, 4, 1), (4.66, 16, None))
        },
        attitudes = {
            bg3.SPEAKER_SHADOWHEART: ((0.0, '88f49c59-3a8c-49d7-b3e8-ed731abaafeb', '375d49d9-707a-42fb-a7f5-7bccba35a6ea', None),)
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 6.510)
    t.create_tl_shot('e7f21f15-f386-40f4-bb0f-2f9f42249ad1', 6.510, 7)

    # I just hope I don't come to regret standing by him.
    d.create_standard_dialog_node(
        '4aead3ff-33fb-484a-bbf5-0d9fea92d42c',
        bg3.SPEAKER_PLAYER,
        ['7b189788-4a3c-44dd-8b2f-225bf9088127'],
        bg3.text_content('hbe191947g233fg4ef7gb172g415bdd40ba49', 1),
        constructor=bg3.dialog_object.QUESTION)

    # Well you can always rid yourself of that regret with a well-place thrust of a dagger... if it comes to that, of course.
    d.create_standard_dialog_node(
        '7b189788-4a3c-44dd-8b2f-225bf9088127',
        bg3.SPEAKER_SHADOWHEART,
        [],
        bg3.text_content('h2351244eg25b9g4136ga0e4gec799138c580', 1),
        constructor=bg3.dialog_object.ANSWER,
        end_node=True)
    t.create_new_voice_phase_from_another(
        template_node_uuid,
        bg3.SPEAKER_SHADOWHEART,
        6.789,
        '7b189788-4a3c-44dd-8b2f-225bf9088127',
        skip_tl_nodes = ('TLShot',),
        phase_duration = 7,
        emotions = {
            bg3.SPEAKER_SHADOWHEART: ((0.89, 16, None), (2.03, 16, 1), (2.93, 16, None), (3.65, 4, None), (4.94, 16, None), (6.15, 4, None))
        })
    t.create_tl_shot('b4155335-5e08-4d85-8ccd-ddebf5507447', 0.0, 6.789)
    t.create_tl_shot('7b067edd-f53f-49e1-95bc-0986e6e2ca2f', 6.789, 7)

    t.update_duration()

add_build_procedure('create_conversation_gur_monster_hunter_putrid_bog', create_conversation_gur_monster_hunter_putrid_bog)
