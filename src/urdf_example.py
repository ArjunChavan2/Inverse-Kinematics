"""Tiny example: reading a URDF with the standard library's xml.etree.

This only shows the XML plumbing. Deciding what the elements *mean*, which
descriptions are valid, and the forward kinematics are your job
(spec/ROBOT_DESCRIPTION.md in the student kit).

    python3 src/urdf_example.py some_robot.urdf
"""
import sys
import xml.etree.ElementTree as ET


def local(tag):
    """An element's local name. With a default namespace (xmlns="..."), ElementTree
    reports tags as "{uri}joint": compare local names, never raw tags."""
    return tag.rsplit("}", 1)[-1] if isinstance(tag, str) else ""


def first_child(element, name):
    """The first direct child with this local name, or None."""
    return next((child for child in element if local(child.tag) == name), None)


def load(text):
    """Parse URDF text; raises xml.etree.ElementTree.ParseError if it is not well-formed XML."""
    if text.startswith("\ufeff"):  # a URDF may start with a byte-order mark; drop it
        text = text[1:]
    return ET.fromstring(text)


def main():
    with open(sys.argv[1], encoding="utf-8") as f:
        robot = load(f.read())
    print("root element:", local(robot.tag), "name:", robot.get("name"))
    for child in robot:  # iterating an element visits its direct children only
        if local(child.tag) == "joint":
            origin = first_child(child, "origin")
            print("joint", child.get("name"), child.get("type"),
                  "origin xyz:", origin.get("xyz") if origin is not None else None)


if __name__ == "__main__":
    main()
