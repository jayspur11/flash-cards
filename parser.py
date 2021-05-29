import sys
import re
import glob

with open("input.tex", "w+") as outfile:
    for filename in glob.glob("*.txt"):
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
