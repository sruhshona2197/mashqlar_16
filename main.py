# 1
class kitob:
    def __init__(self, nomi, muallif, sahifa_soni):
        self.nomi = nomi
        self.muallif = muallif
        self.sahifa_soni = sahifa_soni

    def info(self):
        print(f"nomi: {self.nomi}")
        print(f"muallif: {self.muallif}")
        print(f"sahifa_soni: {self.sahifa_soni}")

k1 = kitob("o'tkan kunlar", "abdulla qodiriy", 300)
k1.info()


# 2
class talaba:
    def __init__(self, ism, yosh, kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs

    def info(self):
        print(f"talaba ismi: {self.ism}")
        print(f"talaba yosh: {self.yosh}")
        print(f"talaba kurs: {self.kurs}")

t1 = talaba("Ali", 20, 2)
t2 = talaba("Vali", 22, 3)

t1.info()
t2.info()
