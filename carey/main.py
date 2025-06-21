import os

def create_files():
    with open("./carey/Main.tex", "r+") as f:
        lines = f.read().split("\\phantomsection")

    for i in range(len(lines)):
        path = f"./carey/chapter{i+1}"
        os.makedirs(path, exist_ok=True)
        with open(f"{path}/Main.tex", "w") as w:
            w.write(lines[i])

def write_main():
    with open("new.tex", "w") as f:
        f.write("\\documentclass[addpoints]{exam}\n")
        f.write("\\usepackage{carey}\n")
        f.write("\\newpage\n")
        f.write("\\tableofcontents\n")
        f.write("\\newpage\n")
        f.write("\\begin{document}\n")
        for i in range(83):
            f.write(f"\\import{{./Chapter{i+1}/}}{{Main.tex}}\n")
            f.write("\\newpage\n")
        f.write("\\end{document}")

write_main()
