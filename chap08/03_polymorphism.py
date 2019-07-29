# 다형성(Polymorphism)

class Armorsuite:
    def armor(self):
        print("armored")

class IronMan(Armorsuite):
    pass

def get_armored(suite):
    suite.armor()

if __name__ == '__main__':
    suite = Armorsuite()

    get_armored(suite)

    Iron_man = IronMan()

    get_armored(Iron_man)

