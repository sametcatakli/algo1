import os


dna = "20tcag2tgtg2atg2at2gacgtg2c3atagacgtg2cg2cg2cgctcga2tcgcac2t"
def adn(seq):
    res = ""
    for i in range(len(seq)):
        if seq[i].isdigit():
            res += str(seq[i + 1] * (int(seq[i]) - 1))
        else:
            res += seq[i]
    print(res)


adn(dna)
