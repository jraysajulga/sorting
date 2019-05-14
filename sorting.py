

sortee = ["glycolysis III",
"superpathway of L-aspartate and L-asparagine biosynthesis",
"coenzyme A biosynthesis II",
"coenzyme A biosynthesis I",
"phosphopantothenate biosynthesis I",
"pantothenate and coenzyme A biosynthesis I",
"glycolysis IV",
"pantothenate and coenzyme A biosynthesis III",
"urate biosynthesis/inosine 5'-phosphate degradation",
"5-aminoimidazole ribonucleotide biosynthesis I",
"5-aminoimidazole ribonucleotide biosynthesis II",
"inosine-5'-phosphate biosynthesis I",
"inosine-5'-phosphate biosynthesis II",
"superpathway of guanosine nucleotides de novo biosynthesis II",
"superpathway of adenosine nucleotides de novo biosynthesis II",
"superpathway of 5-aminoimidazole ribonucleotide biosynthesis",
"UDP-N-acetylmuramoyl-pentapeptide biosynthesis I",
"pyrimidine deoxyribonucleotides de novo biosynthesis III",
"adenine and adenosine salvage III",
"pyrimidine deoxyribonucleotide phosphorylation",
"superpathway of pyrimidine nucleobases salvage",
"adenosine ribonucleotides de novo biosynthesis",
"adenosine deoxyribonucleotides de novo biosynthesis II",
"guanosine ribonucleotides de novo biosynthesis",
"guanosine deoxyribonucleotides de novo biosynthesis II",
"superpathway of guanosine nucleotides de novo biosynthesis I",
"superpathway of adenosine nucleotides de novo biosynthesis I",
"superpathway of purine nucleotides de novo biosynthesis I",
"purine ribonucleosides degradation",
"tRNA charging"]

sorter = ["Glycolysis IV",
"Glycolysis III",
"Guanosine ribonucleotides de novo biosynthesis",
"Adenosine ribonucleotides de novo biosynthesis",
"Superpathway of guanosine nucleotides de novo biosynthesis I",
"Superpathway of pyrimidine nucleobases salvage",
"Urate biosynthesis/inosine 5'-phosphate degradation",
"Adenosine deoxyribonucleotides de novo biosynthesis II",
"Guanosine deoxyribonucleotides de novo biosynthesis II",
"Superpathway of adenosine nucleotides de novo biosynthesis I",
"Superpathway of adenosine nucleotides de novo biosynthesis II",
"Purine ribonucleosides degradation",
"Adenine and adenosine salvage III",
"Superpathway of guanosine nucleotides de novo biosynthesis II",
"Pyrimidine deoxyribonucleotides de novo biosynthesis III",
"Pyrimidine deoxyribonucleotide phosphorylation",
"Superpathway of 5-aminoimidazole ribonucleotide biosynthesis",
"Superpathway of purine nucleotides de novo biosynthesis I",
"Inosine-5'-phosphate biosynthesis I",
"Inosine-5'-phosphate biosynthesis II",
"Coenzyme A biosynthesis II",
"Coenzyme A biosynthesis I",
"Superpathway of L-aspartate and L-asparagine biosynthesis",
"UDP-N-acetylmuramoyl-pentapeptide biosynthesis I",
"Phosphopantothenate biosynthesis I",
"Pantothenate and coenzyme A biosynthesis I",
"Pantothenate and coenzyme A biosynthesis III",
"tRNA charging",
"5-aminoimidazole ribonucleotide biosynthesis II",
"5-aminoimidazole ribonucleotide biosynthesis I"]



for row in sortee:
    for i, key in enumerate(sorter):
        if key.lower() == row.lower():
            print(i + 1)


