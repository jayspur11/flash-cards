import sys
import re

with open("input.tex", "w+") as outfile:
    for filename in [f"ch{i}.txt" for i in range(1,13)]:
        with open(filename, "r") as infile:
            whole_input = infile.read()
            for card in whole_input.split("~~:~~"):
                if not card:
                    continue
                outfile.writelines(
                    "\\card{" + ("}{".join(card.split("~;~")) + "}").replace(
                        "\n", "\\\\").replace("^", "\\^{}").replace("_", "\_").
                    replace("&", "\&").replace("#", "\#").replace("%", "\%") +
                    "\n")
