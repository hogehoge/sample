class Box:
    def __init__(self, item):
        self.item = item
        
    def open(self):
        print("宝箱を開けた。 " + self.item + "を手に入れた。")
        

class JewelryBox(Box):
    def look(self):
        print("宝箱はキラキラ輝いている。")
        

box = Box("ひのきの棒")
box.open()

jewelrbox = JewelryBox("銅の剣")
jewelrbox.open()
jewelrbox.look()
