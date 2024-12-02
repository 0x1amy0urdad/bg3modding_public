from __future__ import annotations

from typing import Callable

import sys

BUILD_PROCEDURES = list[tuple[str, Callable[[], None]]]()

def add_build_procedure(proc_name: str, proc: Callable[[], None]) -> None:
    BUILD_PROCEDURES.append((proc_name, proc))

def run_build_procedures() -> None:
    for build_proc_name, build_proc_callable in BUILD_PROCEDURES:
        sys.stdout.write(f'Running build procedure: {build_proc_name}\n')
        build_proc_callable()
    sys.stdout.write('All build procedures are completed\n')
