KAPASITEETTI = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def sisaltyy(self, numero):
        apumuuttuja = 0

        for i in range(0, self.alkioiden_lkm):
            if numero == self.lukujono[i]:
                apumuuttuja += 1

        if apumuuttuja > 0:
            return True
        else:
            return False

    def lisaa(self, numero):
        if self.alkioiden_lkm == 0:
            self.lukujono[0] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            return True
        else:
            pass

        if not self.sisaltyy(numero):
            self.lukujono[self.alkioiden_lkm] = numero
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.lukujono) == 0:
                taulukko_old = self.lukujono
                self.kopioi_taulukko(self.lukujono, taulukko_old)
                self.lukujono = [0] * (self.alkioiden_lkm + self.kapasiteetti)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

            return True

        return False

    def poista(self, numero):
        sijainti = -1
        apumuuttuja = 0

        for i in range(0, self.alkioiden_lkm):
            if numero == self.lukujono[i]:
                sijainti = i  # siis luku löytyy tuosta kohdasta :D
                self.lukujono[sijainti] = 0
                break

        if sijainti != -1:
            for j in range(sijainti, self.alkioiden_lkm - 1):
                apumuuttuja = self.lukujono[j]
                self.lukujono[j] = self.lukujono[j + 1]
                self.lukujono[j + 1] = apumuuttuja

            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
