from lib2to3.pytree import convert
from socket import inet_pton
from fractions import Fraction
from tkinter import *
import os
import re

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

    classmethod
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
     



Menu().window_hello()
