import json
from typing import T


class Catppuccin:
    def __init__(self, flavour):
        self.flavour = flavour
        with open("./data/catppuccin.json", "r") as f:
            self.colors = json.load(f)

    def pallete(self, flavour: str = None) -> dict:
        flavour = flavour or self.flavour
        return self.colors[flavour]

    def color(self, use="base", flavour=None, str=True) -> str | int:
        if str:
            return self.pallete(flavour=flavour)[use]
        return int(self.pallete(flavour=flavour)[use].replace("#", ""), 16)
