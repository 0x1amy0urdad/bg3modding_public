import os
import os.path
import pytest
import shutil
import time

import bg3moddinglib

BG3_TOOLS_CACHE_DIR = os.path.join(os.path.dirname(__file__), "__bg3_tools_cache__")

@pytest.fixture(scope="session")
def env_path() -> str:
    dirname = "bg3modding_test_" + hex(int(time.time() * 1e6))
    temp_dir_env_vars = ["TMP", "TEMP", "TMPDIR"]
    for env_var in temp_dir_env_vars:
        tmp_dirname = os.getenv(env_var)
        if tmp_dirname:
            break
    if not tmp_dirname:
        raise FileNotFoundError("Cannot find a suitable temporary path.")
    result = os.path.join(tmp_dirname, dirname)
    if os.path.isdir(BG3_TOOLS_CACHE_DIR):
        try:
            with open(os.path.join(BG3_TOOLS_CACHE_DIR, "__timestamp__"), "rt") as f:
                timestamp = int(f.readline())
                if int(time.time()) > timestamp + 86400:
                    shutil.rmtree(BG3_TOOLS_CACHE_DIR)
                else:
                    shutil.copytree(BG3_TOOLS_CACHE_DIR, result)
        except:
            pass
    if not os.path.isdir(result):
        os.makedirs(result)
    return result.replace('\\', '/')

@pytest.fixture(scope="session")
def resources_path() -> str:
    return os.path.join(os.path.dirname(__file__), "resources").replace('\\', '/')

@pytest.fixture(scope="session")
def bg3_modding_env(env_path, resources_path) -> bg3moddinglib.bg3_modding_env:
    config_content = '{"bg3_data_path": "' + resources_path + '"}'
    with open(os.path.join(env_path, "config.json"), "wt") as f:
        f.write(config_content)
    result = bg3moddinglib.bg3_modding_env(env_path)
    if not os.path.isdir(BG3_TOOLS_CACHE_DIR):
        shutil.copytree(result.lslib_path, os.path.join(BG3_TOOLS_CACHE_DIR, os.path.basename(result.lslib_path)))
        shutil.copytree(result.windiff_path, os.path.join(BG3_TOOLS_CACHE_DIR, os.path.basename(result.windiff_path)))
        with open(os.path.join(BG3_TOOLS_CACHE_DIR, "__timestamp__"), "wt") as f:
            f.write(str(int(time.time())))
    return result
