import random
hour = 5

class Meter:
    def home_consumption(self):
        if 9 <= hour <= 18:
            return random.randint(3000,9000)
        else:
            return random.randint(0,2999)

class Deneme:
    def __init__(self, b):
        self.b = b
    def toplama(self):
        return self.b + 5
if __name__ == '__main__':
    a = Meter().home_consumption()
    cc = Deneme(a).toplama()
    print(a)
    print(cc)