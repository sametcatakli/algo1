import sys
from main import *
import convertir


def main():
    args = sys.argv
    if args[1] == 'd':
        if args[2] == 'c':
            text = lecture(args[3])
            result = chiffrement_decalage(text, int(args[4]))
            return result
        elif args[2] == 'd':
            text = lecture(args[3])
            result = dechriffrement_decalage(text, int(args[4]))
            return result

    if args[1] == 's':
        if args[2] == 'c':
            dico = convertir.convert(args[4])
            res = chiffrement_substitution(args[3], dico)
            return res


main()
