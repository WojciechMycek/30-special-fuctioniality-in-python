from email import message
from lib2to3.pytree import convert
from platform import win32_edition
from socket import inet_pton
from fractions import Fraction
from tkinter import *
import os
import re
import random
import sys
from tkinter.tix import InputOnly
from xml.dom.expatbuilder import theDOMImplementation
from xmlrpc.client import _iso8601_format

class Menu():
    #variables
    list_changed_value = []
    friends_list = []
    #help_function
    def clear_console(self):
        os.system('cls' if os.name=='nt' else 'clear')

    def return_value(self,return_value):
        choice = input("Do you want to save value?")
        if choice == 1:
            self.get_value(return_value)

    def get_value(self,new_value):
        self.list_changed_value.append(new_value)

    def file(self):
        file = open("Your_file.txt", 'w')
        file.write(input("Please write: \n"))

    #1
    def start_menu(self):
        print("Hi! Welcome in interactive Python Menu")
        choice = int(input("What do you want to do?"))

        if choice == 1:
            self.convert_int_to_str_and_otherwise()

    #2
    def save_to_file(self):
         while True:
            self.file()
            choice = input("Do you want add more?")
            if choice == "y":
                self.file()
            elif choice == "n":
                break
            else:
                print("Bad choice please repeat!")

    #3
    def read_file(self):
        file = open("Names.txt", 'r')
        print(file.read())
    
    #5
    def create_csv_file(self):
        file = open("New.csv", 'w')
        newRecord = input("Please set your record \n")
        file.write(str(newRecord))
        file.close()

    #6
    def list_your_friends(self):
        while True:
            choice = input("Do you want add friend?")
            if choice == "y":
                self.friends_list.append(input("Add friend"))
                continue
            if choice == "n":
                break

    #7
    def del_friends_from_list(self):
        while True:
            choice = input("Do you want delete friend?")
            if choice == "y":
                self.friends_list.remove(input("Which friend do you want delete"))
                continue
            if choice == "n":
                break
    #8
    def gues_the_number(self):
        score = 0
        for i in range(0,5):
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            both_number = num1 + num2
            answer = int(input("Your answer is:"))
            print(num1 + num2)

        if answer == both_number:
            score += 1
        print("You score is: ", score)

    #9
    def gues_the_number_single(self):
        while True:
            num = random.randint(0, 9)
            print(num)
            user_number = int(input("What's your number?"))
            if num == user_number:
                break
            print("Won!")
    #10
    def gues_the_color(self):
        color_list = ['yellow', 'pink','black','red','white']
        color_random = random.choice(color_list)

        for i in range(0,5):
            print(str(i) + ". " +color_list[i])
            choose = int(input("Please pick one with number:"))
            print("You choice is: ", color_list[choose])

        if color_random == color_list[choose]:
            print("You've lost")
        elif color_random != color_list[choose]:
            print("I've won")

    #11
    def country(self):
        countries = ("Poland","German","Czech Republic", "Finland", "Dennmark")
        for i in range(0,4):
            print(countries[i])
        user_choice = input("Please fill name with country you've sawed")
        for i in range(0,4):
            if user_choice == countries[i]:
                print("Your country number is: ", i)
        choose = int(input("Please pick one with number:"))
        print("You choice is: ", countries[choose])

    #12
    def sets(self):
        X = set('mielonka')
        Y = set('szynka')
        print(X & Y)
        print(X | Y)
        print(X-Y)
        print(X > Y)
    #13
    def bits(self):
        X = 0xFF
        print(bin(X))
        print(X ^ 0b10101010)
        print('01010101',2)
        print(hex(85))
    #14
    def fraction(self):
        x = Fraction(1,1)
        y = Fraction(4,6)
        print(x+y)
    #15
    def delete_duplicate(self):
        print(set([1,2,3,4,5]) - set([1,2,4,5,6]))
    #16
    def regex_phone_number(self,records_lists_to_search):

        phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
        for i in range(len(records_lists_to_search)):
            mo = phoneNumRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)
    #17
    def find_area_code_number(self,records_lists_to_search):
        phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
        for i in range(len(records_lists_to_search)):
            mo = phoneNumRegex.findall(records_lists_to_search[i])
            if mo == None:
                return None
            else:
                print(mo)
    #18
    def comprehension_list(self):
        fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
        newlist = [x for x in fruits if "a" in x]
        print(newlist)
    #19
    def comprehension_sets(self):
        {c * 4 for c in 'mielonka'}
    #20
    def reverse_word(self,word):
        for i in reversed(word):
            print(i)

    #21
    def window_hello(self):
        root = Tk()
        root.title("Hi!")
        tittle_label = Label(root,text="Hello World!!")
        tittle_label.grid(row=0,column=0,pady=(10,0))
        root.mainloop()
    #22
    def gues_the_number(self):
        while True:
            number = random.randint(0,9)
            user_choice = input("Please guess the number: ")
            if number == user_choice:
                print("You won!")
                break
            else:
                print("Try again!")
                continue

    #23
    def list_of_friends_on_birthday(self):
        friends_list = []
        while True:
            decision = input("Do you want add someone?")
            if decision == "yes":
                friends_list.append(input("Please fill name:  "))
            elif decision == "no":
                for i in friends_list:
                    print("Your friend:  ", i)
                    break
            else:
                print("Wrong decision. Try again!")
                continue
    #24 
    def simple_dictioniary_phone(self):
        tel = {'Tomasz': 444,
               'Rafal': 789,
               'Marian': 766,
               'Jonasz': 344,
               'Maniek': 444}
        
        name = input("Please fill name: ")
        score = tel[name]

        if name in tel == False:
            print("There is no contact")
        else:
            print(score)

    #25
    def convert_int_to_str_and_otherwise(self):
        while True:
            value = input("Please set a value, that you want to convert")
            conversation_type = int(input("Please choose converstation type"))

            if conversation_type == 1:
                new_str_value = str(value)
                print("Converstation to str done!")
                self.start_menu()
                self.return_value(new_str_value)
                break
            elif conversation_type == 2:
                new_str_value = int(value)
                print("Converstation to int done!")
                self.start_menu()
                break
            elif conversation_type == 3:
                new_str_value = float(value)
                print("Converstation to float done!")
                self.start_menu()
                break
            else:
                print("Your choice is bad. Please try again!")

    #26
    def kolko_krzyzyk(self):
        theBoard = {
            'top-l': ' ', 'top-m': ' ', 'top-r': ' ',
            'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ',
            'low-l': ' ', 'low-m': ' ', 'low-r': ' '
            }

        turn = "X"
        for i in range(9):
            print(theBoard['top-l'] + ' | ' + theBoard['top-m'] + ' | ' + theBoard['top-r'])
            print("-----")
            print(theBoard['mid-l'] + ' | ' + theBoard['mid-m'] + ' | ' + theBoard['mid-r'])
            print("-----")
            print(theBoard['low-l'] + ' | ' + theBoard['low-m'] + ' | ' + theBoard['low-r'])
            print("Ruch gracza" + turn + "W ktorym polu stawiasz znak?")
            move = input()
            theBoard[move] = turn
            if turn == "X":
                turn = "0"
            else:
                turn = "X"
    #27
    def papier_kamien_nozyce():
        wins = 0
        losses = 0
        ties = 0

        while True:
            print('%s zwyciestw, %s porazek, %remisow' % (wins,losses,ties))
            while True:
                print("Podaj swoj wybor: (k)amien, (p)apier, (n)ozyce lub (w)yjscie")
                playerMove = input()
                if playerMove == 'w':
                    sys.exit()
                if playerMove == 'k' or playerMove == 'p' or playerMove == 'n':
                    break
                print("Wpisz litere k,p,n")

            if playerMove == 'k':
                print("Kamien kontra...")
            elif playerMove == 'p':
                print("Papier kontra...")
            elif playerMove == "n":
                print("Nozyce kontra ...")

            randomNumber = random.randint(1,3)
            if randomNumber == 1:
                computerMove = 'k'
                print("Kamien")
            elif randomNumber == 2:
                computerMove = 'p'
                print("Papier")
            elif randomNumber == 3:
                computerMove == 'n'
                print('Nozyce')

            if playerMove == computerMove:
                print("Mamy remis!")
                ties = ties + 1
            elif playerMove == 'k' and computerMove == 'n':
                print('Wygrales!')
                wins = wins +1
            elif playerMove == 'p' and computerMove == 'k':
                print("Wygrales!")
                wiins = wins + 1
            elif playerMove == 'n' and computerMove == 'p':
                wins = wins + 1
            elif playerMove == 'k' and computerMove == 'p':
                print('Przegrales')
                losses = losses + 1
            elif playerMove == 'p' and computerMove == 'n':
                print('Przegrales')
                losses = losses + 1
            elif playerMove == 'n' and computerMove == 'k':
                print('Przegrales!')
                losses = losses + 1
    #28
    def list_methods(self):
        list = []
        print("Define your list")
        print("How many elements?")
        elements = input()

        for i in range(elements):
            list.append(input("write your element: "))

        decision = input("What do you want to do with list?")
        if decision == 1:
            list.sort()
            print(list)
        elif decision == 2:
            list.reverse()
            print(list)
        elif decision == 3:
            list.sort(key =str.lower)
            print(list)
    #29
    def magic8ball(self):
        messages = ['To pewne',
                    'Zdecydowanie tak',
                    'Niejasnie, sprobuj ponownie',
                    'Zapytaj ponownie pozniej',
                    'Skoncentruj sie i zapytaj sie jeszcze raz',
                    'Moja odpowiedz brzmi nie',
                    'Bardzo watpliwe']
        print(messages[random.randint(0, len(messages) - 1)])
    #30
    def easy_peasy(self):
        while True:
            num = random.randint(0, 9)
            print(num)
            user_number = int(input("What's your number?"))
            if num == user_number:
                break
        print("Won!")
        

Menu().kolko_krzyzyk()
