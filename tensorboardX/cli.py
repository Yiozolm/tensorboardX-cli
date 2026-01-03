import argparse
import subprocess
import sys

from . import __version__


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="tensorboardx",
        description="TensorBoardX helper CLI.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show version and exit.",
    )
    parser.add_argument(
        "--logdir",
        help="Start TensorBoard with this log directory.",
    )
    parser.add_argument(
        "--bind-all",
        action="store_true",
        help="Bind TensorBoard to 0.0.0.0.",
    )
    parser.add_argument(
        "tensorboard_args",
        nargs=argparse.REMAINDER,
        help="Extra args passed to tensorboard (prefix with --).",
    )

    args = parser.parse_args(argv)
    if args.version:
        print(__version__)
        return 0

    if args.logdir is None and not args.tensorboard_args:
        parser.print_help()
        return 0

    extra_args = args.tensorboard_args
    if extra_args and extra_args[0] == "--":
        extra_args = extra_args[1:]

    cmd = ["tensorboard"]
    if args.logdir is not None:
        cmd.extend(["--logdir", args.logdir])
    if args.bind_all:
        cmd.append("--bind_all")
    if extra_args:
        cmd.extend(extra_args)

    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print(
            "tensorboard is not installed. Install it with `pip install tensorboard`.",
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
