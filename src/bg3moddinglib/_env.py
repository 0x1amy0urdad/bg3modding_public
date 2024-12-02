from __future__ import annotations

import json
import os
import requests
import shutil
import time
import zipfile

from ._common import translate_path

from typing import cast

NORBYTE_LSLIB_EXPORT_TOOL_URL = ('https://github.com/Norbyte/lslib/releases/download/v1.19.5/', 'ExportTool-v1.19.5.zip')

class bg3_modding_env:
    __env_root_path: str
    __lslib_path: str
    __divine_exe: str
    __bg3_data_path: str
    __output_path: str


    def __init__(self, env_root_path: str, /, bg3_data_path: str | None = None) -> None:
        self.__env_root_path = env_root_path
        os.makedirs(env_root_path, exist_ok=True)
        self.__lslib_path = os.path.join(self.__env_root_path, "lslib")
        self.__divine_exe = os.path.join(self.__lslib_path, "Packed", "Tools", "divine.exe")
        self.__bg3_data_path = ""
        self.__output_path = os.path.join(self.__env_root_path, "out")
        self.__get_lslib()
        if bg3_data_path is not None:
            self.__bg3_data_path = translate_path(bg3_data_path)
        else:
            self.__read_config()
        self.__sanity_check()
        if os.path.isdir(self.__output_path):
            shutil.rmtree(self.__output_path)
        os.makedirs(self.__output_path)

    @property
    def env_root_path(self) -> str:
        return self.__env_root_path

    @property
    def lslib_path(self) -> str:
        return self.__lslib_path

    @property
    def divine_exe(self) -> str:
        return self.__divine_exe

    @property
    def bg3_data_path(self) -> str:
        return self.__bg3_data_path

    @property
    def output_path(self) -> str:
        return self.__output_path

    def __lslib_exists(self) -> bool:
        return os.path.isdir(self.__lslib_path) and os.path.isfile(self.__divine_exe)

    def __get_lslib(self) -> None:
        try:
            if self.__lslib_exists():
                return True
            temp_path = os.path.join(os.getenv("TEMP"), "bg3modding" + str(time.time()))
            url = NORBYTE_LSLIB_EXPORT_TOOL_URL[0] + NORBYTE_LSLIB_EXPORT_TOOL_URL[1]
            dest_file_path = os.path.join(temp_path, NORBYTE_LSLIB_EXPORT_TOOL_URL[1])
            try:
                bg3_modding_env.download_file(url, dest_file_path)
                with zipfile.ZipFile(dest_file_path) as zip:
                    zip.extractall(path=self.__lslib_path)
            finally:
                shutil.rmtree(temp_path)
        except Exception as exc:
            raise RuntimeError(f"Failed to download and extract lslib") from exc

    def __read_config(self) -> None:
        try:
            config_file_path = os.path.join(self.__env_root_path, "config.json")
            with open(config_file_path, "rt") as f:
                cfg = json.load(f)
            self.__bg3_data_path = translate_path(cast(str, cfg['bg3_data_path']))
            if 'output_path' in cfg:
                self.__output_path = translate_path(os.path.join(self.__env_root_path, cast(str, cfg['output_path'])))
        except Exception as exc:
            raise RuntimeError(f"Failed to read configuration from {config_file_path}") from exc

    def __sanity_check(self) -> None:
        try:
            if not (os.path.isfile(os.path.join(self.__bg3_data_path, "Gustav.pak")) \
                    and os.path.isfile(os.path.join(self.__bg3_data_path, "Shared.pak")) \
                    and os.path.isfile(os.path.join(self.__bg3_data_path, "Engine.pak")) \
                    and os.path.isdir(os.path.join(self.__bg3_data_path, "Localization"))):
                raise RuntimeError("Baldur's Gate III data files are not found at " + self.__bg3_data_path)
            if not os.path.isfile(self.__divine_exe):
                raise RuntimeError("Divine.exe, lslib and other tools are not found at " + self.__lslib_path)
        except Exception as exc:
            raise RuntimeError("Sanity check failed") from exc

    @staticmethod
    def download_file(url: str, dest_file_path: str) -> None:
        os.makedirs(os.path.dirname(dest_file_path))
        with open(dest_file_path, 'wb') as f:
            with requests.get(url, stream=True) as req:
                for part in req.iter_content(chunk_size=262144):
                    f.write(part)
