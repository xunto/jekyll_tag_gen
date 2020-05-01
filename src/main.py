import argparse
import os
from argparse import Namespace

from src import tags


def dir_path(string):
    if os.path.isdir(string):
        return string
    else:
        raise NotADirectoryError(string)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--input', dest="jekyll_project_path", type=dir_path, required=True)
    parser.add_argument('--layout', dest="tags_layout", required=True)

    return parser.parse_args()


def main():
    args: Namespace = parse_arguments()
    tags.generate(args.jekyll_project_path, args.tags_layout)


if __name__ == "__main__":
    main()
