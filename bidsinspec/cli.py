import argparse
from pathlib import Path

from bidsinspec.__version__ import __version__
from bidsinspec.workflows.report import ReportPipeline


def handler(args: argparse.Namespace) -> int:

    bids_dir: Path = args.bids_dir
    output_dir: Path = args.output_dir

    pipeline = ReportPipeline(
        bids_dir=bids_dir,
        output_dir=output_dir,
    )
    pipeline.create_workflow()
    pipeline.run()

    return 0


def create_parser() -> argparse.ArgumentParser:

    parser = argparse.ArgumentParser()

    parser.add_argument("bids_dir", type=Path, help="The BIDS directory to inspec.")
    parser.add_argument("output_dir", type=Path, help="The output directory.")
    parser.add_argument("-v", "--version", action="version", version=__version__)

    parser.set_defaults(handler=handler)

    return parser


def main() -> int:
    parser = create_parser()
    args = parser.parse_args()
    if hasattr(args, "handler"):
        return args.handler(args)

    parser.print_help()
    return 1
