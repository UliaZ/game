# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/
x=0
class Woodchuck:
    def chuck (x):
        print('woodchuck chuck wood')
    def move (self):
        print('Я прыгаю со скоростью ', self.speed)
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
woodchuck = Woodchuck('Bella', 50)
woodchuck.move()
woodchuck.chuck()