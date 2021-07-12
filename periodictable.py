#!/usr/bin/env python3

"""
The periodic table of the elements organizes
all known chemical elements into a single table.

periotictable.py - This program present this table and lets the user access
                    additional information about each element. These informations
                    has been compiled from wikipedia and stor in a file called
                    'periodictable.csv'.
                    (https://inventwithpython.com/periodictable.csv)
"""

import sys
import string
import os
import csv
import colorama
from colorama import Back, Fore, Style
colorama.init(autoreset=True)


def periodictable():
    '''Function to blueprint the Periodic Table of Elements.'''

    space = ' '
    tab = '\t'
    print(f'\n{Style.BRIGHT}{Fore.CYAN}{tab*3}-+-+ PERIODIC TABLE OF THE ELEMENTS +-+-{Style.RESET_ALL}\n')
    for i in range(0, 19):
        if str(i) == '0':
            i = space
        print(str(i) + space, end='  ')

    print(f'\n\n1{space*3}H{space*75}He')

    print(f'\n2{space*2}Li{space*2}Be{space*46}B{space*4}C{space*4}N{space*4}O{space*4}F{space*4}Ne')

    print(f'\n3{space*2}Na{space*2}Mg{space*46}Al{space*3}Si{space*3}P{space*4}S{space*4}Cl{space*3}Ar')

    print(f'\n4{space*3}K{space*2}Ca{space*3}Sc{space*2}Ti{space*2}V{space*3}Cr{space*2}Mn{space*2}Fe{space*2}Co{space*2}Ni{space*3}Cu{space*3}Zn{space*3}Ga{space*3}Ge{space*3}As{space*3}Se{space*3}Br{space*3}Kr')

    print(f'\n5{space*2}Rb{space*2}Sr{space*3}Y{space*3}Zr{space*2}Nb{space*2}Mo{space*2}Tc{space*2}Ru{space*2}Rh{space*2}Pd{space*3}Ag{space*3}Cd{space*3}In{space*3}Sn{space*3}Sb{space*3}Te{space*3}I{space*4}Xe')

    print(f'\n6{space*2}Cs{space*2}Ba{space*3}La{space*2}Hf{space*2}Ta{space*2}W{space*3}Re{space*2}Os{space*2}Ir{space*2}Pt{space*3}Au{space*3}Hg{space*3}Tl{space*3}Pb{space*3}Bi{space*3}Po{space*3}At{space*3}Rn')

    print(f'\n7{space*2}Fr{space*2}Ra{space*3}Ac{space*2}Rf{space*2}Db{space*2}Sg{space*2}Bh{space*2}Hs{space*2}Mt{space*2}Ds{space*3}Rg{space*3}Cn{space*3}Nh{space*3}Fl{space*3}Mc{space*3}Lv{space*3}Ts{space*3}Og\n')

    print(f'{space*12}Ce{space*2}Pr{space*2}Nd{space*2}Pm{space*2}Sm{space*2}Eu{space*2}Gd{space*2}Tb{space*3}Dy{space*3}Ho{space*3}Er{space*3}Tm{space*3}Yb{space*3}Lu\n')

    print(f'{space*12}Th{space*2}Pa{space*2}U{space*3}Np{space*2}Pu{space*2}Am{space*2}Cm{space*2}Bk{space*3}Cf{space*3}Es{space*3}Fm{space*3}Md{space*3}No{space*3}Lr')

    print()


def print_element(row):
    print(f'\n\t{Style.BRIGHT}{Back.BLUE}{Fore.BLACK}-+-+ ELEMENT DETAILS +-+-')
    print(f'\tElement: {row[2]}')
    print(f'\tSymbol: {row[1]}')
    print(f'\tOrigin of name: {row[3]}')
    print(f'\tAtomic number: {row[0]}')
    print(f'\tGroup: {row[4]}')
    print(f'\tPeriod: {row[5]}')
    print(f'\tAtomic weight: {row[6]}')
    print(f'\tDensity: {row[7]} g/cm^3')
    print(f'\tMelting point: {row[8]} °K')
    print(f'\tBoiling point: {row[9]} °K')
    print(f'\tSpecific heat capacity: {row[10]} J/(g*K)')
    print(f'\tElectronegativity: {row[11]}')
    print(f"\tAbundance in earth's crust: {row[12]} mg/kg\n")


def main():

    if len(sys.argv) != 2:
        print('Usage: ./periodictable.py [option]')
        print('option: atomic number or symbol')
    else:
        periodictable()

        csv_file = open('periodictable.csv')
        csv_reader = csv.reader(csv_file)

        option = sys.argv[1]
        row = []
        for line in csv_reader:
            if (option == line[0] or option.title() == line[1]):
                row = line
            else:
                pass

        if row:
            print_element(row)
        else:
            print('This input does not match any element.')


if __name__ == '__main__':
    main()
