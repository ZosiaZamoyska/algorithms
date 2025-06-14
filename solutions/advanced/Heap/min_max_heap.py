'''
    You are given a list of numbers. If a number is positive, it is added to a set. If a number is 0, then we are inquiring the result of substraction between largest and smallest number in the set.
    Then, both of the elements are deleted from the set. 
    
    For given list, output the result of substraction between max and min.

    
'''

class KopiecBinarny:
    def __init__(self, tryb='max'):  # tryb: 'max' lub 'min'
        self.t = [None]
        self.n = 0
        self.tryb = tryb

    def _porownaj(self, a, b):
        return a > b if self.tryb == 'max' else a < b

    def wstaw(self, e):
        self.n += 1
        self.t.append(e)
        w = self.n
        while w > 1 and self._porownaj(self.t[w], self.t[w // 2]):
            self.t[w], self.t[w // 2] = self.t[w // 2], self.t[w]
            w //= 2

    def usun(self):
        if self.n == 0:
            return None
        wynik = self.t[1]
        self.t[1] = self.t[self.n]
        self.n -= 1
        self.t.pop()
        self.przywroc(1)
        return wynik

    def przywroc(self, i):
        lewy = 2 * i
        prawy = 2 * i + 1
        najlepszy = i

        if lewy <= self.n and self._porownaj(self.t[lewy], self.t[najlepszy]):
            najlepszy = lewy
        if prawy <= self.n and self._porownaj(self.t[prawy], self.t[najlepszy]):
            najlepszy = prawy
        if najlepszy != i:
            self.t[i], self.t[najlepszy] = self.t[najlepszy], self.t[i]
            self.przywroc(najlepszy)

    def peek(self):
        return self.t[1] if self.n >= 1 else None

    def empty(self):
        return self.n == 0


def przetworz_operacje(operacje):
    kopiec_max = KopiecBinarny('max')
    kopiec_min = KopiecBinarny('min')
    usun = {}

    for op in operacje:
        if op > 0:
            kopiec_max.wstaw(op)
            kopiec_min.wstaw(op)
            usun[op] = False
        elif op == 0:
            # Usuwanie wartości oznaczonych jako usunięte z góry kopców
            while not kopiec_max.empty() and usun.get(kopiec_max.peek(), False):
                kopiec_max.usun()
            while not kopiec_min.empty() and usun.get(kopiec_min.peek(), False):
                kopiec_min.usun()

            if kopiec_max.empty() or kopiec_min.empty():
                continue

            maks = kopiec_max.usun()
            mini = kopiec_min.usun()
            usun[maks] = True
            usun[mini] = True

            print(f"Różnica: {maks - mini} (max: {maks}, min: {mini})")

# Przykład:
operacje = [5, 3, 17, 0, 10, 84, 19, 6, 0, 22, 9, 0, 0]
przetworz_operacje(operacje)
