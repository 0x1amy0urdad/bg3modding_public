from __future__ import annotations

from .context import files

from .build import run_build_procedures
from .initalization import initialization

from . import act1_romance
from . import act2_romance
from . import act3_romance
from . import banters
from . import betrayal_reactions
from . import bhaal_temple
from . import books
from . import breakup_line
from . import cloister
from . import conversations
from . import creepy_druid
from . import end_game_epilogue_married
from . import end_game_marriage_proposal
from . import greetings
from . import gur_putrid_bog
from . import hug_animations
from . import kiss_animations
from . import long_rest
from . import minthara
from . import mizora_aftermath
from . import relationship
from . import sharess_caress
from . import soundbank
from . import text_content
from . import wylls_good_manners

def build_mod(mod_version: tuple[int, int, int, int]) -> None:
    initialization(mod_version)

    run_build_procedures()

    files.build(verbose = True, lua_overrides = False)
