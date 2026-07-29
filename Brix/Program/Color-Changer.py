from Config.Util import *
from Config.Config import *

Title("Color Changer")

colors_preview = [
    ("black", 0), ("white", 255), ("gray", 128), ("red", 255), ("green", 128),
    ("blue", 128), ("yellow", 255), ("cyan", 255), ("magenta", 255), ("purple", 128),
    ("pink", 255), ("orange", 255), ("brown", 139), ("lime", 255), ("indigo", 75),
    ("violet", 238), ("teal", 128), ("gold", 255), ("navy", 128), ("maroon", 128),
    ("coral", 255), ("crimson", 220), ("turquoise", 128), ("darkred", 139),
    ("darkgreen", 100), ("darkblue", 139), ("lightgray", 211), ("hotpink", 255),
]

try:
    print(f"""\n{white}Available colors:
{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    row = ""
    for i, (name, v) in enumerate(colors_preview):
        c = f"\033[38;2;{v};{max(0,v-60)};{max(0,v-80)}m" if i > 0 else f"\033[38;2;0;0;0m"
        row += f" {c}■\033[0m {white}{name}{reset}"
        if len(row) > 60:
            print(row)
            row = ""
    if row:
        print(row)

    print(f"{red}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n{reset}")

    count = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} 2 or 3 colors ? (2/3) -> {reset}").strip()
    if count not in ["2", "3"]:
        ErrorChoice()
        Continue()
        Reset()

    count = int(count)
    chosen = []
    for i in range(count):
        name = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Color {i+1} -> {reset}").strip().lower()
        rgb = _color_name_to_rgb(name)
        if rgb == (128, 128, 128) and name not in ("gray", "grey"):
            if name not in _COLOR_NAMES and not name.startswith("#"):
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Unknown color, using gray")
        chosen.append(name)

    settings_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "settings.py")
    with open(settings_path, "w") as f:
        f.write("# Couleurs du degrade (2 ou 3 couleurs)\n")
        f.write("# Nom anglais ou code hex (#rrggbb)\n")
        f.write("gradient_colors = [\n")
        for c in chosen:
            f.write(f'    "{c}",\n')
        f.write("]\n")

    preview = []
    for c in chosen:
        r, g, b = _color_name_to_rgb(c)
        preview.append(f"\033[48;2;{r};{g};{b}m   \033[0m")

    print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} New gradient saved: {' -> '.join(preview)} {white}{' -> '.join(chosen)}{reset}")
    print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Restart to see changes !")

    Continue()
    Reset()
except Exception as e:
    Error(e)
