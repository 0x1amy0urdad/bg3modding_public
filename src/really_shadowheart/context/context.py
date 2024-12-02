from __future__ import annotations

###################
# Initialization
###################

import bg3moddinglib as bg3
import os
import os.path


class context:
    __root_path: str
    __env: bg3.bg3_modding_env
    __tool: bg3.bg3_modding_tool
    __files: bg3.game_files

    __env_ea: bg3.bg3_modding_env
    __tool_ea: bg3.bg3_modding_tool

    def __init__(self, mod_name : str, mod_uuid : str) -> None:
        self.__root_path = os.getcwd()
        if not os.path.isfile(os.path.join(self.__root_path, 'ReallyShadowheart.ipynb')):
            raise RuntimeError(f"Wrong root_path: {self.__root_path}. Please update it such that it points to a directory containing this notebook.")

        full_game = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Baldurs Gate 3\\Data"
        self.__env = bg3.bg3_modding_env(os.path.join(self.__root_path, "env"), bg3_data_path = full_game)
        self.__tool = bg3.bg3_modding_tool(self.__env)
        self.__files = bg3.game_files(self.__tool, mod_name, mod_uuid)

        home_dir_path = os.path.join(os.getenv('HOMEDRIVE'), os.getenv('HOMEPATH'))
        if not isinstance(home_dir_path, str) or not os.path.isdir(home_dir_path):
            raise RuntimeError('cannot determine path to the home directory; please, define HOMEDRIVE and HOMEPATH environment variables')
        #ea_patch_6 = home_dir_path + "\\.home\\bg3_history\\ea_patch6\\Data"
        #ea_patch_7 = home_dir_path + "\\.home\\bg3_history\\ea_patch7\\Data"
        ea_patch9_hf32 = home_dir_path + "\\.home\\bg3_history\\ea_patch9_hotfix32\\Data"

        self.__env_ea = bg3.bg3_modding_env(os.path.join(self.__root_path, "env_ea"), bg3_data_path = ea_patch9_hf32)
        self.__tool_ea = bg3.bg3_modding_tool(self.__env_ea)

    @property
    def root_path(self) -> str:
        return self.__root_path

    @property
    def env(self) -> bg3.bg3_modding_env:
        return self.__env

    @property
    def tool(self) -> bg3.bg3_modding_tool:
        return self.__tool

    @property
    def env_ea(self) -> bg3.bg3_modding_env:
        return self.__env_ea

    @property
    def tool_ea(self) -> bg3.bg3_modding_tool:
        return self.__tool_ea

    @property
    def files(self) -> bg3.game_files:
        return self.__files

    def create_meta_lsx(self, mod_version: tuple[int, int, int, int]) -> None:
        # meta.lsx
        self.__files.create_meta_lsx(mod_version, author="iamy0urdad", display_name="Really Shadowheart", description="Really Shadowheart")
        self.__files.copy_mod_logo(self.__root_path)
