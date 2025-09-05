# make_icons_table.py
# Generates a LaTeX file with a grid of icons from a multipage PDF.

OUTPUT_FILE = "icons_table_mod.tex"
PDF_NAME = "bootstrapicons_complete.pdf"
NUM_PAGES = 2078   # change to your actual number
ICONS_PER_ROW = 5  # number of icons per row
ROWS_PER_PAGE = 9  # number of rows per page before page break

with open('names.txt', "r", encoding="utf-8") as nf:
    names = [line.strip() for line in nf if line.strip()]

j = 0

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(r"""\documentclass{article}
\usepackage{graphicx}
\usepackage{xcolor}
\definecolor{red-200}{HTML}{f1aeb5}
\usepackage[margin=0.2cm]{geometry}
\begin{document}
\pagenumbering{gobble}
""")

    for i in range(1, NUM_PAGES + 1):
        # Start a new table at the beginning or after every page break
        if (i - 1) % (ICONS_PER_ROW * ROWS_PER_PAGE) == 0:
            if i > 1:
                f.write(r"\end{tabular}\end{center}\newpage" + "\n")
            f.write(r"\begin{center}" + "\n")
            f.write(r"\renewcommand{\arraystretch}{1.5}" + "\n")
            f.write(r"\setlength{\tabcolsep}{6pt}" + "\n")
            f.write(r"\begin{tabular}{*" + str(ICONS_PER_ROW) + "{c}}" + "\n")

        # Add icon cell
        entry = (
            "\\begin{tabular}{@{}c@{}}"
            f"\\includegraphics[page={i},width=1.5cm]{{{PDF_NAME}}}\\\\"
            r"[-10pt]\scriptsize \colorbox{red-200}{\texttt{\bf " + f"{i}" + r"}}\\"  
            r"[-4pt]\scriptsize \texttt{\bf " + f"{names[j]}" + r"} \vspace{4mm}"
            "\\end{tabular}"
        )
        j += 1
        f.write(entry)

        # Row/column handling
        if i % ICONS_PER_ROW == 0:
            f.write(r" \\" + "\n")  # end row
        else:
            f.write(" & ")

    # Close last table
    f.write(r"\end{tabular}\end{center}" + "\n")
    f.write(r"\end{document}" + "\n")

nf.close()
print(f"LaTeX file written to {OUTPUT_FILE}")