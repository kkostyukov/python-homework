#!/usr/bin/python3
"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""
import random


class Card():
    def __init__(self, name):
        self.name = name
        self.game_card = ''
        self.card = [
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--'],
            ['--', '--', '--', '--', '--', '--', '--', '--', '--']
        ]
        self.gen_card()

    def gen_card(self):
        numbers_for_card = []
        for itm in range(1, 91):
            numbers_for_card.append(itm)
        random.shuffle(numbers_for_card)

        i = 0
        while i < 3:
            position = [itm for itm in range(0, 9)]
            random.shuffle(position)
            pos = [position.pop(0) for _ in range(5)]
            pos.sort()
            numbers_line = [numbers_for_card.pop(0) for _ in range(5)]
            numbers_line.sort()
            for j in pos:
                self.card[i][j] = str(numbers_line.pop(0))
            i += 1
        new_card = ''
        for i in range(3):
            for j in range(9):
                new_card = new_card + str(self.card[i][j]) + '  '
            new_card = new_card + '\n'
        self.game_card = f'Карточка игрока: {self.name}\n{new_card}'


class Game:
    def __init__(self):
        self._gen_bag()
        self.playgame()

    def _gen_bag(self):
        self.bag = []
        for itm in range(1, 91):
            self.bag.append(str(itm))
        random.shuffle(self.bag)
        return self.bag

    def playgame(self):
        print(player_card.game_card)
        print(computer_card.game_card)

        for num in self.bag:
            # спрашиваем игрока и проверяем его карточку
            player_answer = input(f'Выпало число: {num}, зачеркнуть?(д/н)\n')
            number_in_card = None

            # Проверяем ответ Да
            if player_answer == 'д':
                for i in range(0, 3):
                    number_in_card = num in player_card.card[i]
                    if number_in_card == True:
                        player_card.card[i][player_card.card[i].index(num)] = f'\{num}/'
                        print(self.GenStrCard(player_card))
                        print(self.GenStrCard(computer_card))
                        break
            if number_in_card == False:
                print('В вашей карте нет выпавшего числа. Вы проиграли!')
                break

            # Проверяем ответ Нет
            number_in_card = None
            if player_answer == 'н':
                for i in range(0, 3):
                    number_in_card = num in player_card.card[i]
                    if number_in_card == True:
                        print('В вашей карте есть выпавшее число. Вы проиграли!')
                        break
            if number_in_card == True:
                break
            else:
                print(self.GenStrCard(player_card))
                print(self.GenStrCard(computer_card))

            # Компьютер сам проверяет свою карточку и отмечает выпавшее число
            for i in range(0, 3):
                numberInCard2 = num in computer_card.card[i]
                if numberInCard2 == True:
                    computer_card.card[i][computer_card.card[i].index(num)] = f'\{num}/'
                    print(self.GenStrCard(player_card))
                    print(self.GenStrCard(computer_card))
                    break
                else:
                    continue

            # Надо завершить игру если все числа в одной из карточек отмечены
            check = 0
            check2 = 0
            for itm in range(1, 91):
                for i in range(0, 3):
                    if str(itm) in player_card.card[i]:
                        check = 1
                    if str(itm) in computer_card.card[i]:
                        check2 = 1
            if check == 0:
                print(f'Игрок {player_card.name} победил!')
                break
            elif check2 == 0:
                print(f'Игрок {computer_card.name} победил!')
                break

    def GenStrCard(self, plaerName):
        self.newCard = ''
        for i in range(3):
            for j in range(9):
                self.newCard = self.newCard + str(plaerName.card[i][j]) + '  '
            self.newCard = self.newCard + '\n'
        return f'Карточка игрока: {plaerName.name}\n{self.newCard}'


if __name__ == '__main__':
    name = input('Введите имя игрока ')
    player_card = Card(name)
    computer_card = Card('Компьютер')
    Game()
