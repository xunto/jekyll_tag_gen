import os
from pathlib import Path
from typing import List

import yaml

YAML_MARKER = "---"


def fetch_yaml(path):
    content: str

    with open(path) as f:
        content = f.read()

    content = content[content.find(YAML_MARKER) + len(YAML_MARKER):]
    content = content[:content.find(YAML_MARKER)]

    return yaml.load(content, Loader=yaml.FullLoader)


def fetch_tags(path) -> List[str]:
    obj = fetch_yaml(path)
    return obj["tags"]


def gen_tag_page(tag: str, tag_layout: str):
    obj = {
        "layout": Path(tag_layout).stem,
        "tag": tag
    }

    content = YAML_MARKER + "\n"
    content += yaml.dump(obj)
    content += YAML_MARKER

    return content


def generate(project_path: str, tags_path: str, tag_layout: str):
    posts_path = os.path.join(project_path, "_posts")

    if not os.path.isdir(posts_path):
        raise NotADirectoryError(posts_path)

    files = [os.path.join(posts_path, f) for f in os.listdir(posts_path)]
    files = [
        f for f in files
        if os.path.isfile(f)
        if f.endswith(".md")
    ]

    tags = set()
    for path in files:
        for tag in fetch_tags(path):
            tags.add(tag)

    if not os.path.exists(tags_path):
        os.mkdir(tags_path)

    for tag in tags:
        tag_page = gen_tag_page(tag, tag_layout)
        with open(os.path.join(tags_path, f"{tag}.md"), "w") as f:
            f.write(tag_page)
