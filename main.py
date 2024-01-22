import pyxel
#https://github.com/kitao/pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width
        self.y = (self.y - 1) % pyxel.width


    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)
        pyxel.rect(self.y, 10, 8, 8, 9)

App()