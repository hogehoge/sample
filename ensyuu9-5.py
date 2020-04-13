# coding: utf-8
# RPGの攻撃シーン

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は" + enemy + "を攻撃した")

class Warrior(Player):
    def attack(self, enemy):
        print(self.name + "は" + enemy + "を猛攻撃した")


team = []
team.append(Player("勇者"))
team.append(Player("魔法使い"))
team.append(Warrior("戦士"))


for person in team:
    person.attack("スライム")
