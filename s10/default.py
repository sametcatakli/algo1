import os



dna = "20tcag2tgtg2atg2at2gacgtg2c3atagacgtg2cg2cg2cgctcga2tcgcac2t"
def adn(seq):
    res = ""
    max = len(seq)
    j = 0
    count = 0
    for i in range(len(seq)):
        if seq[i].isdigit():
            j = i
            while seq[j + 1].isdigit:
                if import os



dna = "20tcag2tgtg2atg2at2gacgtg2c3atagacgtg2cg2cg2cgctcga2tcgcac2t"
def adn(seq):
    res = ""
    for i in range(len(seq)):
        if seq[i].isdigit():
            res += str(seq[i + 1] * (int(seq[i]) - 1))
        else:
            res += seq[i]
    print(res)


adn(dna)j != len(seq):
                    j += 1

                count += int(seq[i]) + int(seq[i + 1])

    print(count)


adn(dna)