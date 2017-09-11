#! /usr/bin/env python

import random

statera = []
ahsoka = []
girrina = []
ventress = []
random_chars = []

def dice():
    temp = []
    temp.append(random.randint(1, 4))
    temp.append(random.randint(1, 6))
    temp.append(random.randint(1, 8))
    temp.append(random.randint(1, 10))
    temp.append(random.randint(1, 12))
    temp.append(random.randint(1, 20))
    return temp
    #return list(d4, d6, d8, d10, d12, d20)


def printer(*name):

    for i in range(len(name)):

        print("|{:>22}             |".format(name[i][6]))

        print("|" + ("-" * 35) + "|")

        print("|{0:>6}{1:>6}{2:>6}{3:>6}{4:>6}{5:>6}"
              .format("d4 |", "d6 |", "d8 |", "d10 |", "d12 |", "d20 |"))

        print("|" + ("-" * 35) + "|")

        print("|{0:>6}{1:>6}{2:>6}{3:>6}{4:>6}{5:>6}"
              .format(str(name[i][0]) + " |", str(name[i][1]) + " |", str(name[i][2]) + " |",
                      str(name[i][3]) + " |", str(name[i][4]) + " |", str(name[i][5]) + " |"))
        print("|" + ("-" * 35) + "|")


statera = dice()
statera.append("Statera")

ahsoka = dice()
ahsoka.append("Ahsoka")

girrina = dice()
girrina.append("Gir'rina")

ventress = dice()
ventress.append("Ventress")

anakin = dice()
anakin.append("Anakin")

random_chars = dice()
random_chars.append("Random")

printer(statera, ahsoka, girrina, ventress, anakin, random_chars)
#dnd_roller("Statera")
#dnd_roller("Ahsoka")
#dnd_roller("Gir'rina")
#dnd_roller("Asajj Ventress")
#dnd_roller("Everyone else")
