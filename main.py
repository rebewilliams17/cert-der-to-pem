"""Cert DER to PEM — Convert a DER or CER certificate to PEM text you can paste."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='cert_der_to_pem',
        description='Convert a DER or CER certificate to PEM text you can paste.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Cert DER to PEM')
    print('The binary cert as PEM.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
