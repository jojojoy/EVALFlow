import argparse
from .runners.base import run

def main():
    parser = argparse.ArgumentParser(prog="evalflow", description="EVALFlow CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_run = sub.add_parser("run", help="Run evaluation")
    p_run.add_argument("--config", required=True, help="Path to YAML config")
    p_run.add_argument("--out", required=True, help="Output directory for this run")

    args = parser.parse_args()
    if args.cmd == "run":
        res = run(args.config, args.out)
        print(res)

if __name__ == "__main__":
    main()
