from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        maara = 0
        for i in self.ostoskori:
            maara += 1
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for i in self.ostoskori:
            hinta += i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        self.ostoskori.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.ostoskori.remove(poistettava)

    def tyhjenna(self):
        self.ostoskori = []
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset = list()
        lisatyt_tuotteet = list()

        for tuote in self.ostoskori:
            if tuote.nimi() in lisatyt_tuotteet:
                for ostos in ostokset:
                    if ostos.tuote == tuote.nimi():
                        ostos.muuta_lukumaaraa(1)
            else:
                lisatyt_tuotteet.append(tuote.nimi())
                ostos = Ostos(tuote.nimi())
                ostokset.append(ostos)

        return ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on