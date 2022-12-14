from dataclasses import dataclass
from typing import List
from fluoresce.models import Color
from fluoresce.paint import launch as launch_paint


def gallery_mode(canvas: str):
    print("gallery")


def paint_mode(canvas: str, colors: List[Color]):
    print("paint in", colors)
    launch_paint()

def regex_mode(canvas: str, colors: List[Color]):
    print("regex")


def version():
    print("version")


def display_mode():
    print("display")


def manage_colors():
    print("manage_colors")


def query_mode():
    print("query")
