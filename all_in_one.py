#!/usr/bin/env python3

class call:

    print('''Following is the list to get what you desire
    1. How to get input from user
    2. File I/O
    3. A simple example of Class and fuctions
    4. Python loops
    10. Oops I'm in wrong code, sorry gotta go''')

    choice = int(input("What code you wanna see : $"))
    print('''\nHere you go sir, \n \n************\n''')

    def callout_first(self):
        f = open('ex11.py')
        for line in f:
            print(line.rstrip())

    def callout_second(self):
        f = open('ex14.py')
        for line in f:
            print(line.rstrip())

    def callout_third(self):
        f = open('class.py')
        for line in f:
            print(line.rstrip())

    def callout_fourth(self):
        print('\n************************* \n')
        f = open('for.py')
        for line in f:
            print(line.rstrip())

    def callout_fifth(self):
        print('\n************************* \n')
        f = open('while.py')
        for line in f:
            print(line.rstrip())

def main():
    auto = call()
    while auto.choice!=10:
        if auto.choice == 1:
            auto.callout_first();break
        elif auto.choice == 2:
            auto.callout_second(); break
        elif auto.choice == 3:
            auto.callout_third(); break
        elif auto.choice == 4:
            print('''There are following two basic loops in Python ? Where your interests lies ?
            a. for
            b. while''')
            option = input("\nTell me now, which one you want $")
            if option == 'a':
                auto.callout_fourth(); break
            elif option == 'b':
                auto.callout_fifth(); break
            else:
                print('\n Incorrect selection, Select the option from above list PLEASE')


    print('''\n************ You got what you want, now get lost ;) ********''')


if __name__ == "__main__":
    main()
