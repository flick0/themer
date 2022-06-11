import json
import subprocess
import os

HOME = "/home/{}".format(
    subprocess.run(["whoami"], stdout=subprocess.PIPE).stdout.decode("utf-8")
).strip()

paths = {
    "common": f"{HOME}/color.json",
    "kitty": os.getenv("KITTY_CONFIG_DIRECTORY")
    or f"{HOME}/.config/kitty/kitty.conf",
}


async def apply(colors: dict) -> tuple[str, str]:
    try:
        Common.set(colors)
        yield ("Common", None)
    except Exception as e:
        yield ("Common", e)
    try:
        Kitty().set(colors)
        yield ("Kitty", None)
    except Exception as e:
        yield ("Kitty", e)


class Common:
    def set(colors: dict) -> None:
        subprocess.run(
            f"touch {paths['common']}".split(), stdout=subprocess.PIPE
        )
        with open(paths["common"], "w") as f:
            json.dump(colors, f, indent=4)

    def get() -> dict:
        subprocess.run(
            f"touch {paths['common']}".split(), stdout=subprocess.PIPE
        )
        with open(paths["common"], "r") as f:
            return json.load(f)


class Kitty:
    def __init__(self):
        self.conf = """
font_family      JetBrains Mono Medium
bold_font        JetBrains Mono Bold
italic_font      JetBrains Mono Italic
bold_italic_font JetBrains Mono Bold Italic

window_padding_width 10.0

# The basic colors
foreground              {foreground}
background              {background}
selection_foreground    {background}
selection_background    {selection}

# Cursor colors
cursor                  {selection}
cursor_text_color       {background}

# URL underline color when hovering with mouse
url_color               {url}

# OS Window titlebar colors
wayland_titlebar_color system
macos_titlebar_color system

# Tab bar
active_tab_foreground   {background}
active_tab_background   {selection}
inactive_tab_foreground {foreground}
inactive_tab_background {background}
tab_bar_background      {background}

# marks
mark1_foreground {background}
mark1_background {cyan}
mark2_foreground {background}
mark2_background {green}
mark3_foreground {background}
mark3_background {blue}

# black
color0 {black}
color8 {gray}

# red
color1 {red}
color9 {red}

# green
color2  {green}
color10 {green}

# yellow
color3  {yellow}
color11 {yellow}

# blue
color4  {blue}
color12 {blue}

# magenta
color5  {magenta}
color13 {magenta}

# cyan
color6  {cyan}
color14 {cyan}

# white
color7  {white}
color15 {lightgray}
"""

    def set(self, colors: dict) -> None:
        conf = (
            self.conf.replace("{foreground}", colors["text"])
            .replace("{background}", colors["base"])
            .replace("{selection}", colors["mauve"])
            .replace("{url}", colors["sapphire"])
            .replace("{black}", colors["crust"])
            .replace("{gray}", colors["mantle"])
            .replace("{red}", colors["red"])
            .replace("{green}", colors["green"])
            .replace("{yellow}", colors["yellow"])
            .replace("{blue}", colors["blue"])
            .replace("{magenta}", colors["maroon"])
            .replace("{cyan}", colors["sky"])
            .replace("{white}", colors["lavender"])
            .replace("{lightgray}", colors["surface2"])
        )
        with open(paths["kitty"], "w") as f:
            f.write(conf)
