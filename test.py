#!/usr/bin/env python
# -*- coding: utf-8 -*-
# prosty skrypt oparty na Morfeuszu2

import morfeusz2


# — Liczba: pojedyncza sg, mnoga pl
liczba =    {
	    'sg':'pojedyncza',
	    'pl':'mnoga'
	    }
# — Przypadek: mianownik nom, dopełniacz gen, celownik dat, biernik acc, narzędnik
#   inst, miejscownik loc, wołacz voc
przypadek = { 
	    'nom':'mianownik',
	    'gen':'dopelniacz',
	    'dat':'celownik',
	    'acc':'biernik',
	    'inst':'narzednik',
	    'loc':'miejscownik',
	    'vox':'wolacz'
	    }
# — Rodzaj: męski osobowy m1, męski zwierzęcy m2, męski rzeczowy m3, żeński f, ni-
#   jaki zbiorowy n1, nijaki zwykły n2, przymnogi osobowy p1, przymnogi zwykły p2,
#   przymnogi opisowy p3
rodzaj =    {
	    'm1':'męski osobowy',
	    'm2':'męski zwierzęcy',
	    'm3':'męski rzeczowy',
	    'f':'żeński',
	    'n1':'nijaki zbiorowy',
	    'n2':'nijaki zwykły',
	    'p1':'przymnogi osobowy',
	    'p2':'przymnogi zwykły',
	    'p3':'przymnogi opisowy'
	    }
# — Osoba: pierwsza pri, druga sec, trzecia ter
osoba =	    {
	    'pri':'pierwsza',
	    'sec':'druga',
	    'ter':'trzecia'
	    }
# — Stopień: równy pos, wyższy comp, najwyższy sup
stopien =   {
	    'pos':'równy',
	    'comp':'wyższy',
	    'sup':'najwyższy'
	    }
# — Aspekt: niedokonany imperf, dokonany perf
aspekt =    {
	    'imperf':'niedokonany',
	    'perf':'dokonany'
	    }
# — Zanegowanie: niezanegowana aff, zanegowana neg
zanegowanie = {
	    'aff':'niezanegowana',
	    'neg':'zanegowana'
	    }
# — Akcentowość: akcentowana akc, nieakcentowana nakc
akcentowosc = {
	    'akc':'akcentowana',
	    'nakc':'nieakcentowana'
	    }
# — Poprzyimkowość: poprzyimkowa praep, niepoprzyimkowa npraep
# — Akomodacyjność: uzgadniająca congr, rządząca rec
# — Aglutynacyjność: aglutynacyjna agl, nieaglutynacyjna nagl
# — Wokaliczność: wokaliczna wok, niewokaliczna nwok

def parseString(ciag,pretty):
    ciagU = ciag.decode('utf8')
    objMorf = morfeusz2.Morfeusz()
    if pretty:
	print "Ale ładne"
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
		print el

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
    args = parser.parse_args()

    ciag = args.input_string
    if args.pretty:
	parseString(ciag,True)
    else:
	parseString(ciag,False)
	
