OUTPUT_FILE = "commands.txt"
NAMES = "./names.txt"
NUM_PAGES = 2078
COMMAND_NAME = r"\defineBicon"

with open('./names.txt', "r", encoding="utf-8") as nf:
    names = [line.strip() for line in nf if line.strip()]

j = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for i in range(1, NUM_PAGES + 1):        
        f.write(COMMAND_NAME + r"{" + str(i) + r"}{" + names[j] + r"}" + "\n")
        j += 1

nf.close()
f.close()