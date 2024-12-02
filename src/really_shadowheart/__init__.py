
from .context import files

from .banters import fix_banters
from .betrayal_reactions import create_betrayal_reactions
from .bhaal_temple import (
    create_scene_shadowheart_cries_when_durge_dies,
    create_scene_shadowheart_kiss_durge_body_type_2,
    create_scene_shadowheart_kiss_durge_body_types_3_4,
)
from .breakup_line import create_breakup_line
from .build import run_build_procedures
from .cloister import patch_cloister_events
from .conversations import patch_conversations
from .creepy_druid import patch_creepy_druid
from .end_game_epilogue_married import create_conversation_epilogue_married_couple
from .end_game_marriage_proposal import create_scene_marriage_proposal
from .greetings import create_greetings
from .gur_putrid_bog import create_conversation_gur_monster_hunter_putrid_bog
from .hug_animations import (
    add_hugs_to_the_story,
    create_hugs_dialogs,
    create_hugs_timeline,
)
from .initalization import initialization
from .kiss_animations import patch_kiss_animations
from .minthara import patch_minthara_conversations
from .mizora_aftermath import patch_mizora_aftermath_scene
from .sharess_caress import patch_sharess_caress
from .skinny_dipping import patch_skinny_dipping_scene
from .soundbank import create_voice_metadata
from .text_content import create_text_content
from .wylls_good_manners import patch_wyll_greetings

def build_mod(mod_version: tuple[int, int, int, int]) -> None:
    initialization(mod_version)

    run_build_procedures()

    files.build(verbose = True)
