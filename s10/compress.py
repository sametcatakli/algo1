"""Outil de (dé)compression de fichier.

Usage:
  compress.py (-c | -d) --t=<technique> --in=<fichier> [--out=<fichier>]

Options:
  -c                  Compresser le fichier.
  -d                  Décompresser le fichier.
  --t=<technique>      Technique de compression à utiliser.
  --in=<fichier>      Fichier à compresser/décompresser.
  --out=<fichier>     Fichier de sortie.

"""


def c_LZ(texte):
    with open(texte, 'r') as f:
        list_mots = []
        list_index = []
        for line in f:
            for mot in line.split():
                if mot not in list_mots:
                    list_mots.append(mot)
                list_index.append(list_mots.index(mot))  # seek() 
        return list_mots, list_index


def c_file_LZ(tuple):
    list_mots, list_index = tuple
    with open('LZ.txt', 'w') as f:
        for mot in list_mots:
            f.write(mot + '\n')
        f.write('\n')
        for index in list_index:
            f.write(str(index) + '\n')
    return 'LZ.txt'


def d_LZ(texte_cle):
    with open(texte_cle, 'r') as f:
        list_mots = []
        list_index = []
        for line in f:
            if line == '\n':
                break
            list_mots.append(line.strip())
        for line in f:
            list_index.append(int(line.strip()))
    with open('decompres.txt', 'w') as f:
        for index in list_index:
            f.write(list_mots[index] + ' ')


def c_ADN(texte):
    index = 0
    compressed_chain = ""
    with open(texte, 'r') as f:
        data = f.read().strip()
        len_data = len(data)
        try:
            for i in data:
                if i == '\n':
                    continue
                if i not in 'atgc':
                    print('*' + i + '*')
                    raise ValueError
            while index != len_data:
                count = 1
                while (index < len_data - 1) and (data[index] == data[index + 1]):
                    count = count + 1
                    index = index + 1
                if count == 1:
                    compressed_chain += (data[index])
                else:
                    compressed_chain += str(count) + (data[index])
                index = index + 1
            with open('adn_comp.txt', 'w') as f:
                f.write(compressed_chain)
            return compressed_chain
        except ValueError:
            print('badADNformat')
            return ''


def d_ADN(texte):
    with open(texte, 'r') as f:
        data = f.read().strip()
        len_data = len(data)
        index = 0
        decompressed_chain = ""
        while index != len_data:
            if data[index].isdigit():
                count = int(data[index])
                index = index + 1
                decompressed_chain += (data[index] * count)
            else:
                decompressed_chain += data[index]
            index = index + 1
        with open('adn_dec.txt', 'w') as f:
            f.write(decompressed_chain)
        return decompressed_chain


#c_ADN("adn.txt")
#d_ADN("adn_comp.txt")

import docopt

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    if args['--compress']:
        if args['--technique'] == 'LZ':
            c_file_LZ(c_LZ(args['--in']))
        elif args['--technique'] == 'ADN':
            c_ADN(args['--in'])
    elif args['--decompress']:
        if args['--technique'] == 'LZ':
            d_LZ(args['--in'])
        elif args['--technique'] == 'ADN':
            d_ADN(args['--in'])