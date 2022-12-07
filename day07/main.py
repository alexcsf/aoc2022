import re

DIR = "dir"
FILE = "file"

root = {"children": list(), "prev": {}, "name": "/", "type": DIR, "size": 0}


def cd(node: object, path: str):
    if path == "/":
        return root
    if path == "..":
        node["prev"]["size"] += node["size"]
        return node["prev"]
    child = {"children": list(), "prev": node, "name": path, "type": DIR, "size": 0}
    node["children"].append(child)
    return child


def get_sizes(node: object):
    xxs = [get_sizes(x) for x in node["children"] if x["type"] == DIR]
    return [node["size"]] + [x for xs in xxs for x in xs]


def print_nodes(node: object, indent=0):
    """Like `tree`, but worse."""
    print(f'{" " * indent}- {node["name"]} ({node["type"]}, size={node["size"]})')
    for sub_dir in node["children"]:
        print_nodes(sub_dir, indent + 2)


with open("day07/input.txt", mode="r", encoding="utf-8") as file:
    node = root
    while line := re.sub(r"^\$ ", "", file.readline().rstrip()):
        if line[:2] == "ls":
            continue
        cmd, args = line.split(maxsplit=1)
        if cmd == "dir":
            continue
        if cmd == "cd":
            node = cd(node, args)
        else:
            size, name = int(cmd), args
            node["children"].append(
                {"name": name, "size": size, "type": FILE, "children": []}
            )
            node["size"] += size
    root["size"] = sum(x["size"] for x in root["children"])
    sizes = [size for size in get_sizes(root)]
    unused = 70000000 - root["size"]
    print("1:", sum(filter(lambda x: x <= 100000, sizes)))
    print("2:", min(filter(lambda x: x + unused >= 30000000, sizes)))
