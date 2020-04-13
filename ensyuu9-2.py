# coding: utf-8

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)


player = Hello()
player.say_hello()
