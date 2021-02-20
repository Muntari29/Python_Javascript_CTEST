# 능력치와 '파이어볼' 출력하기

class Wizard:
    def __init__(self,**kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.armor = kwargs['armor']

    def attack(self):
        print('파이어볼')

x = Wizard(health = 545, mana = 210, armor =10)
print(x.health, x.mana, x.armor)
x.attack()

