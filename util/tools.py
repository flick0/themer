import json

import aiohttp


async def catppuccin_scrape() -> bool:
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://raw.githubusercontent.com/catppuccin/palette/main/css/catppuccin.css"
        ) as resp:
            resp = await resp.text()
            resp = (
                resp.replace(":root {", "")
                .replace("}", "")
                .replace(" ", "")
                .replace(";", "")
            )
            raw = resp.split("\n")
            colors = {}
            for line in raw:
                line = line.strip()
                if len(line) < 1:
                    continue
                if line.count("-") != 4:
                    continue
                line = line.split(":")
                name = line[0][6:].split("-")
                flavour = name[0]
                name = name[1]
                color = line[1]
                if not colors.get(flavour):
                    colors[flavour] = {}
                colors[flavour][name] = color
                with open("./data/catppuccin.json", "w") as f:
                    json.dump(colors, f, indent=4)
            return True
