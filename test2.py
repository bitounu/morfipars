#!/usr/bin/env python
# -*- coding: utf-8 -*-
# prosty skrypt oparty na Morfeuszu2

import morfeusz2


# — Liczba: pojedyncza sg, mnoga pl
attribs =    {
	    'sg':'pojedyncza',
	    'pl':'mnoga',
# — Przypadek: mianownik nom, dopełniacz gen, celownik dat, biernik acc, narzędnik
#   inst, miejscownik loc, wołacz voc
	    'nom':'mianownik',
	    'gen':'dopelniacz',
	    'dat':'celownik',
	    'acc':'biernik',
	    'inst':'narzednik',
	    'loc':'miejscownik',
	    'vox':'wolacz',
# — Rodzaj: męski osobowy m1, męski zwierzęcy m2, męski rzeczowy m3, żeński f, ni-
#   jaki zbiorowy n1, nijaki zwykły n2, przymnogi osobowy p1, przymnogi zwykły p2,
#   przymnogi opisowy p3
	    'm1':'męski osobowy',
	    'm2':'męski zwierzęcy',
	    'm3':'męski rzeczowy',
	    'f':'żeński',
	    'n1':'nijaki zbiorowy',
	    'n2':'nijaki zwykły',
	    'p1':'przymnogi osobowy',
	    'p2':'przymnogi zwykły',
	    'p3':'przymnogi opisowy',
# — Osoba: pierwsza pri, druga sec, trzecia ter
	    'pri':'pierwsza',
	    'sec':'druga',
	    'ter':'trzecia',
# — Stopień: równy pos, wyższy comp, najwyższy sup
	    'pos':'równy',
	    'comp':'wyższy',
	    'sup':'najwyższy',
# — Aspekt: niedokonany imperf, dokonany perf
	    'imperf':'niedokonany',
	    'perf':'dokonany',
# — Zanegowanie: niezanegowana aff, zanegowana neg
	    'aff':'niezanegowana',
	    'neg':'zanegowana',
# — Akcentowość: akcentowana akc, nieakcentowana nakc
	    'akc':'akcentowana',
	    'nakc':'nieakcentowana',
# — Poprzyimkowość: poprzyimkowa praep, niepoprzyimkowa npraep
	    'praep':'poprzyimkowa',
	    'npraep':' niepoprzyimkowa',
# — Akomodacyjność: uzgadniająca congr, rządząca rec
	    'congr':'uzgadniająca',
	    'rec':' rządząca',
# — Aglutynacyjność: aglutynacyjna agl, nieaglutynacyjna nagl
	    'agl':'aglutynacyjna',
	    'nagl':' nieaglutynacyjna',
# — Wokaliczność: wokaliczna wok, niewokaliczna nwok
	    'wok':'wokaliczna',
	    'nwok':' niewokaliczna'
}


def parseString(ciag,pretty):
    ciagU = ciag.decode('utf8')
    objMorf = morfeusz2.Morfeusz()
    if pretty:
	print "Ale ładne"
	print type(attribs)
    else:
	out = objMorf.analyse(ciagU)
#	[x.encode('utf8') for x in out]
#	print out.encode('utf8')
#	print "ciag: %s" % ciag
#	print "ciagU: %s" % ciagU
	print out
	for wyraz in out:
	    print "------------------------------"
	    print "Wyraz:	%s" % wyraz[2][0]
	    print "Leksem:	%s" %  wyraz[2][1]
	    print "Uwagi:	%s" %  wyraz[2][3]
	    print "Uwagi2:	%s" %  wyraz[2][4]
	    print "Morfo:	%s" %  wyraz[2][2]
	    for el in wyraz[2][2].split(":"):
		if el in attribs:
		    print attribs[el]
#		print el.encode('utf8')
#		print el

if __name__ == "__main__":
    import argparse, sys, os, re
    from argparse import ArgumentParser

    parser = ArgumentParser(description="Morfeusz tester")
    parser.add_argument("-t", 
        dest="input_string", required=True,
        help="podaj string do analizy")
    parser.add_argument("-p", "--pretty",
        action="store_true",
        help="drukowanie ladnej tabelki")
#    parser.add_argument("-o",
#	dest="output_file", required=False,
#	help="podaj plik wynikowy")
    args = parser.parse_args()

    ciag = args.input_string
    if args.pretty:
	parseString(ciag,True)
    else:
	parseString(ciag,False)
	
