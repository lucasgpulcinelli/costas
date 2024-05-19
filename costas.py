#!/usr/bin/env python3

from subprocess import Popen, PIPE
import datetime
import json
import os

OPTIONS_FILE = os.path.join(
    os.environ["HOME"], ".config", "costas", "costas.json")


def main(options):
    keyid = options["gpg-keyid"]
    base_dir = options["base-directory"]
    directories = options["directories"]
    ignore = options["ignore"]
    output_directory = options["output-directory"]

    assert type(keyid) == str
    assert os.path.isdir(base_dir)
    for d in directories:
        assert os.path.isdir(os.path.join(base_dir, d))
    for i in ignore:
        assert os.path.exists(os.path.join(base_dir, i))
    assert os.path.isdir(output_directory)

    filename = datetime.date.today().strftime("%Y-%m-%d")

    args = ["tar"]
    for i in ignore:
        args.append(f'--exclude={i}')
    args.extend(["-czf", "-"])
    args.extend(directories)

    tarout = Popen(args, cwd=base_dir, stdout=PIPE)

    gpgfile = open(f"{output_directory}/{filename}.gpg", "w")
    Popen(["gpg", "-r", keyid, "--encrypt", "-"],
          stdin=tarout.stdout, stdout=gpgfile).wait()
    gpgfile.close()


if __name__ == '__main__':
    f = open(OPTIONS_FILE)
    options = json.load(f)
    f.close()

    main(options)
