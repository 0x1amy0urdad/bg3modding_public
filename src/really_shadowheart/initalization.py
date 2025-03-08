from __future__ import annotations

import bg3moddinglib as bg3
import os
import os.path

from .context import (
    files,
    root_path
)

def initialization(mod_version: tuple[int, int, int, int] | None) -> None:
    files.create_meta_lsx(mod_version, author="iamy0urdad", display_name="Really Shadowheart", description="Really Shadowheart")
    files.copy_mod_logo(root_path)
    files.copy_script_extender_lua_files(os.path.join(root_path, "lua"))
    files.copy_osiris_goals(os.path.join(root_path, "osi"))
    files.copy_external_files(os.path.join(root_path, "loca"), "Mods/Gustav")
    #files.copy_external_files(os.path.join(root_path, "anubis"), "Game/Scripts/anubis")
