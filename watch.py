#!/usr/bin/env python3

import os
import argparse
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler, FileSystemEvent
import subprocess
import time
from typing import List
from datetime import datetime, timedelta, timezone


PYTHON_COMMAND = "python3"
COMMAND_REPEAT_TIME = 0.1


class CommandEventHandler(FileSystemEventHandler):
    def __init__(self, command: str, file: str):
        self.command = command
        self.file = file
        self.last_ran = 0

    def on_modified(self, event: FileSystemEvent):
        if time.monotonic() - self.last_ran < COMMAND_REPEAT_TIME:
            return

        if event.src_path == self.file:
            print(f"\n[{get_new_york_time()}] $ {self.command}")

            start_time = time.monotonic()
            # TODO: can we run this in the same shell?
            subprocess.run(self.command, shell=True, text=True)
            end_time = time.monotonic()

            print(f"\ncommand finished in {end_time-start_time:.1f} seconds")
            self.last_ran = time.monotonic()


def create_command(file: str, args: List[str]) -> str:
    command_list = [PYTHON_COMMAND] + [file] + args
    return " ".join(command_list)


def get_new_york_time():
    ny_time = datetime.now(timezone.utc) - timedelta(hours=5)
    return ny_time.strftime("%H:%M:%S")


if __name__ == "__main__":
    # TODO: this is currently optimized for running python programs, can we make it more general?
    parser = argparse.ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("command_args")  # TODO: get multiple arguments
    args = parser.parse_args()

    command_args = [args.command_args]
    command = create_command(args.file, command_args)
    print(f'watching file "{args.file}" and running command "{command}"')

    path = os.path.abspath(os.path.expanduser(args.file))
    event_handler = CommandEventHandler(command, path)
    observer = Observer()
    observer.schedule(event_handler, ".")
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()
