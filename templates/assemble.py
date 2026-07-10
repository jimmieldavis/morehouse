import re

IMG_DIR = "../assets/"
OUT_DIR = "../"
def read(name):
    with open(IMG_DIR + name, encoding='ascii') as f:
        return f.read()

BSD = read("bsd_b64.txt")
SS4REG = read("ss4reg_b64.txt")
SS4ITAL = read("ss4ital_b64.txt")
PINCKNEY = read("pinckney_web_b64.txt")
BASKETBALL = read("basketball_web_b64.txt")
TRACK = read("track_web_b64.txt")
FOOTBALL = read("football_web_b64.txt")
GOLF = read("golf_web_b64.txt")
GOLF_HC = read("golf_hc_b64.txt")

REPL = {
    "__BSD__": BSD,
    "__SS4REG__": SS4REG,
    "__SS4ITAL__": SS4ITAL,
    "__IMG_PINCKNEY__": PINCKNEY,
    "__IMG_BASKETBALL__": BASKETBALL,
    "__IMG_TRACK__": TRACK,
    "__IMG_FOOTBALL__": FOOTBALL,
    "__IMG_GOLF__": GOLF,
    "__IMG_GOLF_HC__": GOLF_HC,
}

files = [
    ("tpl_scoreboard.html", "final_scoreboard.html"),
    ("tpl_therecord.html", "final_therecord.html"),
    ("tpl_ledger.html", "final_ledger.html"),
]

for src, dst in files:
    with open(src, encoding='utf-8') as f:
        html = f.read()
    missing = []
    for k, v in REPL.items():
        if k not in html:
            missing.append(k)
        html = html.replace(k, v)
    with open(OUT_DIR + dst, 'w', encoding='utf-8') as f:
        f.write(html)
    leftover = re.findall(r"__[A-Z_]+__", html)
    print(dst, "bytes:", len(html), "| missing placeholders:", missing, "| leftover tokens:", leftover)
