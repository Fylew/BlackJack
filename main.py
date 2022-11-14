import random

def Mainmenu():

    maximum = 21
    player = input("Введите ваше имя: ")
    player = Gamer(player)
    oponent = Gamer("Гросмейстер")
    player.Score_print()
    while True:
        choice = int(input("Выберете действие:\n1 - Взять карту\n2 - Себе\n"))
        if choice == 1:
            player.Hand_to_take()
            player.Score_print()
        elif choice == 2:
            while True:
                if oponent.score_hand < 17:
                    oponent.Hand_to_take()
                else:
                    break
            oponent.Score_print()
            break
        else:
            print("Не корректный ввод")



    if player.score_hand < maximum:
        if oponent.score_hand < maximum:
            if player.score_hand > oponent.score_hand:
                print("Игрок : {} Победил".format(player.name))
            else:
                print("Игрок : {} Проиграл".format(player.name))
        else:
            print("Игрок : {} Победил".format(player.name))


    elif player.score_hand > maximum:
        print("Игрок : {} Проиграл".format(player.name))

cards = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 1,
    "Валет" : 2,
    "Дама" : 3,
    "Король" : 4,
    "Туз" : 11
}

class Gamer:

    def __init__(self,name):
        self.name = name
        self.hand_cards = [random.choice(list(cards)) for i in range(2)]
        self.score_hand = 0
        self.Score()

    def Hand_to_take(self):
        self.hand_cards.append(random.choice(list(cards)))
        self.Score()
    def Score(self):
        for i in self.hand_cards:
            self.score_hand += cards[i]

    def Score_print(self):

        print("{} {} {}".format("~" * 10, self.name, "~" * 10))
        print("В ваших руках карты : {}".format(self.hand_cards))
        print("Ваш счет = {}".format(self.score_hand))

Mainmenu()