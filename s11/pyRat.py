from rational import Rational

class pyRat(object):
    """ pyRat:
           Petite calculatrice permettant de
           manipuler des fractions.
    """
    def __init__(self):
        self.version = '1.0'
        s1 = 'Welcome in pyRat ' + self.version + ' - Fractions Calculator'
        s2 = 'Mainly made by You!'
        blanks = ' ' * ((len(s1) - len(s2)) // 2)
        print(s1 + '\n' + blanks + s2 + blanks)
        print('\n' + 'Type \'help\' to know how to use pyRat')
        print('Type \'bye\', \'exit\' or \'quit\' to quit pyRat')

    def run(self):
        input_ = input('pyRat> ')
        if input_.strip() == 'quit' or \
           input_.strip() == 'exit' or \
           input_.strip() == 'bye':
            return False
        elif input_.strip() == 'help':
            self.displayHelp()
            return True
        try: 
            res = self.parse(input_.strip())
            print(res)
        except ValueError as e:
            print('Sorry but I cannot parse \'' + input_.strip() +
                  '\'. (But you can improve me!)')
            print('Type \'help\' if lost.')
        return True

    def parse(self, input_):
        if input_.find('+') != -1:
            index = input_.find('+')
            a = Rational(input_[:index])
            b = Rational(input_[index+1:])
            return a + b
        elif input_.find('*') != -1:
            index = input_.find('*')
            a = Rational(input_[:index])
            b = Rational(input_[index+1:])
            return a * b
        else:
            return Rational(input_)

    def displayHelp(self):
        line = ('-' * 26) + ' pyRat ' + self.version + ' ' + ('-' * 26)
        print(line)
        print('In version ' + self.version +
              ', pyRat can simplify fractions but also compute')
        print('sums and products of fractions!\n')
        print('Well... that\'s not bad but you can really improve pyRat')
        print('(see \"Exercices supplementaires\" '
              'for improvement\'s suggestions)')
        print(line)
        print('Examples of inputs:')
        print('   1/2 + 0.25')
        print('   0.1 * 3 / 5')
        print('   2/4')
        print(line)
        print('List of commands:')
        print('   quit / exit / bye: exit pyRat')
        print('   help: display this help')

if __name__ == '__main__':
    calculette = pyRat()
    while calculette.run():
        pass
