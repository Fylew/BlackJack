from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,QWidget
import sys
import random

cards = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "Валет" : 2,
    "Дама" : 3,
    "Король" : 4,
    "Туз" : 11
}

class App(QWidget):

    def __init__(self):
        self.start()
        self.button()
        self.Player()
        self.Score()
        self.Score_print()
        self.Oponent()
    def start(self):
        self.main_menu = uic.loadUi("untitled.ui")
        self.main_menu.show()

    def Player(self):
        self.hand_cards = [random.choice(list(cards)) for i in range(2)]
        self.score_hand = 0

    def Score_print(self):
        self.main_menu.textBrowser.setText("В ваших руках карты : {}".format(self.hand_cards))
        self.main_menu.textBrowser.append("Ваш счет = {}".format(self.score_hand))
    def Op_Score_print(self):
        self.main_menu.textBrowser_2.setText("В ваших руках карты : {}".format(self.Op_hand_cards))
        self.main_menu.textBrowser_2.append("Ваш счет = {}".format(self.Op_score_hand))

    def Score(self):
        for i in self.hand_cards:
            self.score_hand += cards[i]

    def Op_Score(self):
        for i in self.Op_hand_cards:
            self.Op_score_hand += cards[i]

    def Hand_to_take(self):
        cart = random.choice(list(cards))
        print(cart)
        self.hand_cards.append(cart)
        self.score_hand += cards[cart]
        self.Score_print()

    def Oponent(self):
        self.flag = True
        self.Op_hand_cards = [random.choice(list(cards)) for i in range(1)]
        self.Op_score_hand = 0

    def OP_Hand_to_take(self):
        cart = random.choice(list(cards))
        self.Op_score_hand += cards[cart]
        self.Op_hand_cards.append(cart)
        self.Op_Score_print()
        if self.Op_score_hand < 15:
            self.OP_Hand_to_take()




    def button(self):
        self.main_menu.pushButton.clicked.connect(lambda: self.Hand_to_take())
        self.main_menu.pushButton_2.clicked.connect(lambda: self.OP_Hand_to_take())



if __name__ =="__main__":
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()