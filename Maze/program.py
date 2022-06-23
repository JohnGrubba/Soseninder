import json

wall_character = "██"
nothing =        "  "
player =         "00"

with open("maze.json", "r") as f:
    data = json.load(f)
size = list(data["size"])

strs = ""
for x in range(size[0]):
    for y in range(size[1]):
        # Find button
        for btn in data["fields"]:
            if btn["x"] == x and btn["y"] == y:
                if btn["wall"]: strs += wall_character
                else: strs += nothing
    strs += "\n"
print(strs)