#!/usr/bin/env python3
"""
toolrunner.py - Run multiple tools on a folder and its subfolders.

Usage:
    python toolrunner.py --folder <path> --tools <tool1,tool2,...>

The script will walk the folder tree and run each specified tool
against every directory and file it encounters.  It is very
flexible: the tools are plain shell commands, so you can pass
arguments to them directly in the `--tools` argument.

Examples:

    # Run black and isort on the current project
    python toolrunner.py --folder . --tools black,isort

    # Run flake8 on every file but only on python files
    python toolrunner.py --folder src --tools "flake8 --select=E9"
"""

import argparse
import os
import subprocess
import sys


def run_tool_on_path(tool_cmd: str, target_path: str) -> None:
    """Execute a shell command `tool_cmd` on `target_path`.

    The command is executed with ``shell=True`` so that users can
    supply flags and arguments directly.
    """
    cmd = f"{tool_cmd} {target_path}"
    try:
        if args.verbose:
            print(f"Running: {cmd}")
        result = subprocess.run(
            cmd,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr, file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error running '{tool_cmd}' on {target_path}", file=sys.stderr)
        print(e.stderr, file=sys.stderr)


def find_all_targets(folder: str):
    """Yield all directories and files under `folder`.

    For tools that operate on directories (e.g. `black`, `isort`)
    the directory itself is yielded.  Files are also yielded so
    that tools which expect a file path (e.g. a static analyser)
    can be applied.
    """
    for root, dirs, files in os.walk(folder):
        yield root  # directory itself
        for f in files:
            yield os.path.join(root, f)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run selected tools on a folder and its subcomponents."
    )
    parser.add_argument(
        "--folder", required=True, help="Target folder to scan"
    )
    parser.add_argument(
        "--tools", required=True, help="Comma‑separated list of tool commands"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Print command output"
    )
    args = parser.parse_args()

    folder = os.path.abspath(args.folder)
    tools = [t.strip() for t in args.tools.split(",") if t.strip()]

    if not os.path.isdir(folder):
        print(f"{folder} is not a directory", file=sys.stderr)
        sys.exit(1)

    targets = list(find_all_targets(folder))

    for tool in tools:
        for target in targets:
            run_tool_on_path(tool, target)
