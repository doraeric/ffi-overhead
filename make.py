#!/usr/bin/env python3
import argparse
from pathlib import Path
import subprocess

CFLAGS = "-fPIC -O2 -Wall -Wextra -Wno-unused-parameter"


def clean():
    Path("newplus", "plus.o").unlink(missing_ok=True)
    Path("newplus", "libnewplus.a").unlink(missing_ok=True)
    Path("newplus", "libnewplus.so").unlink(missing_ok=True)
    Path("c_hello").unlink(missing_ok=True)
    Path("go_hello").unlink(missing_ok=True)
    Path("rust_hello").unlink(missing_ok=True)


def print_run_sh(cmd: str):
    print(f"> {cmd}")
    subprocess.run(cmd, shell=True)


def build_lib():
    print_run_sh(f"gcc -c newplus/plus.c -o newplus/plus.o {CFLAGS}")
    print_run_sh(f"ar crs newplus/libnewplus.a newplus/plus.o")
    print_run_sh(
        "gcc -o newplus/libnewplus.so -shared -O2 "
        "-Wl,--whole-archive newplus/libnewplus.a -Wl,--no-whole-archive"
    )


def build_c():
    print_run_sh(f"gcc -o c_hello -O2 hello.c newplus/libnewplus.so {CFLAGS}")


def build_go():
    print_run_sh("go build -o go_hello hello.go")


def build_rust():
    print_run_sh("rustc -C opt-level=2 -C opt-level=2 -o rust_hello hello.rs -L .")


def build_all():
    build_lib()
    build_c()
    build_go()
    build_rust()


def run(count: int = 1000000):
    files = list(Path(".").glob("*_hello"))
    print(f"Running {len(files)} files")
    for f in files:
        print_run_sh(f"./{f} {count}")


if __name__ == "__main__":
    pser = argparse.ArgumentParser()
    sub = pser.add_subparsers()
    sub.add_parser("clean").set_defaults(func=clean)
    sub.add_parser("build").set_defaults(func=build_all)
    sub.add_parser("build:lib").set_defaults(func=build_lib)
    sub.add_parser("build:c").set_defaults(func=build_c)
    sub.add_parser("build:go").set_defaults(func=build_go)
    sub.add_parser("build:rust").set_defaults(func=build_rust)
    run_all_pser = sub.add_parser("run")
    run_all_pser.set_defaults(func=run)
    run_all_pser.add_argument("count", type=int)
    args = vars(pser.parse_args())
    func = args.pop("func")
    func(**args)
