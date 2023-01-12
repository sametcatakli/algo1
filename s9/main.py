import convertir
import sys

def lecture(nom):
    with open(nom, "r") as desc:
        content = desc.read()

    return content


# text = lecture("decalage.txt")


def nettoyage(texte):
    list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]
    text = texte.lower()
    text = text.strip()
    res = []
    for i in text:
        if i in list:
            res.append(i)
    normal_string = "".join(res)
    print(normal_string)


# nettoyage("Hello313*éèàçygzefyugfGTFTFIYTF"
# "€Salutété")


def idx_from_letter(c):
    return ord(c) - ord('a')


def lettre_from_idx(i):
    return chr(ord('a') + i)


def chiffrement_decalage(texte, u):
    res = ''
    for c in texte:
        new_index = (idx_from_letter(c) + u) % 26
        res += lettre_from_idx(new_index)
    return res


def dechriffrement_decalage(texte, u):
    return chiffrement_decalage(texte, -u)


def chiffrement_substitution(texte, dico):
    text = lecture(texte)
    res = ""
    for c in text:
        res += dico.get(c, c)
    return res


def dico_reverse(dico):
    res = {}
    for key, value in dico.items():
        res[value] = key
    return res


def dechiffrement_substitution(texte, dico):
    dic = dico_reverse(dico)
    res = chiffrement_substitution(texte, dic)
    return res



# dico = convertir.convert("dico.txt")
# print(dechiffrement_substitution("substitution.txt", dico))

