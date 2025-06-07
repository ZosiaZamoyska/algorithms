class KopiecBinarny:
    def __init__(self):
        self.t = [None]
        self.n = 0

    def wstaw(self, e):
        self.n += 1
        self.t.append(e)
        w = self.n
        while w > 1 and self.t[w] > self.t[w // 2]:
            self.t[w], self.t[w // 2] = self.t[w // 2], self.t[w]
            w //= 2

    def usun(self):
        if self.n == 0:
            return None
        maksimum = self.t[1]
        self.t[1] = self.t[self.n]
        self.n -= 1
        self.t.pop()
        self.przywroc(1)
        return maksimum

    def przywroc(self, i):
        lewy = 2 * i
        prawy = 2 * i + 1
        maks = i

        if lewy <= self.n and self.t[lewy] > self.t[maks]:
            maks = lewy
        if prawy <= self.n and self.t[prawy] > self.t[maks]:
            maks = prawy
        if maks != i:
            self.t[i], self.t[maks] = self.t[maks], self.t[i]
            self.przywroc(maks)

    def buduj(self):
        for i in range(self.n // 2, 0, -1):
            self.przywroc(i)

    def pokaz(self):
        print(self.t[1:self.n + 1])

kopiec = KopiecBinarny()
for e in [5, 3, 17, 10, 84, 19, 6, 22, 9]:
    kopiec.wstaw(e)

kopiec.pokaz()

print(kopiec.usun())
kopiec.pokaz()
