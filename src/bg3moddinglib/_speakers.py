from ._tool import bg3_modding_tool

# Origins and Companions: speaker uuids; these are global templates UUIDs and used in dialogs to refer to speakers
SPEAKER_MINSC       = '0de603c5-42e2-4811-9dad-f652de080eba'
SPEAKER_MINTHARA    = '25721313-0c15-4935-8176-9f134385451b'
SPEAKER_KARLACH     = '2c76687d-93a2-477b-8b18-8a14b549304c'
SPEAKER_SHADOWHEART = '3ed74f06-3c60-42dc-83f6-f034cb47c679'
SPEAKER_LAEZEL      = '58a69333-40bf-8358-1d17-fff240d7fb12'
SPEAKER_HALSIN      = '7628bc0e-52b8-42a7-856a-13a6fd413323'
SPEAKER_JAHEIRA     = '91b6b200-7d00-4d62-8dc9-99e8339dfa1a'
SPEAKER_GALE        = 'ad9af97d-75da-406a-ae13-7071c563f604'
SPEAKER_WYLL        = 'c774d764-4a17-48dc-b470-32ace9ce447d'
SPEAKER_ASTARION    = 'c7c13742-bacd-460a-8f65-f864fe41f255'
SPEAKER_DURGE       = 'e6b3c2c4-e88d-e9e6-ffa1-d49cdfadd411'
SPEAKER_BOO         = 'd49e3b49-a089-4465-b453-28dc79e82bb3'
SPEAKER_MIZORA      = '491a7686-3081-405b-983c-289ec8781e0a'
SPEAKER_VICONIA     = 'b1ea974d-96fb-47ca-b6d9-9c85fcb69313'
SPEAKER_ARNELL      = 'c12d561f-beae-4ef6-917e-0bec2f829449'
SPEAKER_NYM_ORLYTH  = '7574fc5a-3645-4370-a778-0b38d0ef162a'
SPEAKER_SORN_ORLYTH = 'f25b5f9a-bfde-4d81-a3fb-74fc39dad95b'
SPEAKER_GANDREL     = '0e47fcb9-c0c4-4b0c-902b-2d13d209e760'
SPEAKER_JERGAL      = '0133f2ad-e121-4590-b5f0-a79413919805'

SPEAKER_NAME = {
    SPEAKER_MINSC       : 'Minsc',
    SPEAKER_MINTHARA    : 'Minthara',
    SPEAKER_KARLACH     : 'Karlach',
    SPEAKER_SHADOWHEART : 'Shadowheart',
    SPEAKER_LAEZEL      : 'Lae\'zel',
    SPEAKER_HALSIN      : 'Creepy druid',
    SPEAKER_JAHEIRA     : 'Jaheira',
    SPEAKER_GALE        : 'Gale',
    SPEAKER_WYLL        : 'Wyll',
    SPEAKER_ASTARION    : 'Astarion',
    SPEAKER_DURGE       : 'Durge',
    SPEAKER_BOO         : 'Boo',
    SPEAKER_MIZORA      : 'Mizora',
    SPEAKER_VICONIA     : 'Viconia DeVir',
    SPEAKER_ARNELL      : 'Arnell Hallowleaf',
    SPEAKER_NYM_ORLYTH  : 'Nym Orlyth',
    SPEAKER_SORN_ORLYTH : 'Sorn Orlyth',
    SPEAKER_GANDREL     : 'Gandrel',
    SPEAKER_JERGAL      : 'Jergal'
}


def get_all_speakers_uuids(t: bg3_modding_tool) -> list[str]:
    return [f'{v[44:52]}-{v[52:56]}-{v[56:60]}-{v[60:64]}-{v[64:76]}' for v in t.list('Localization/VoiceMeta') if v.startswith('Mods/Gustav/Localization/English/Soundbanks/')]


