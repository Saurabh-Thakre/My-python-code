#!/usr/bin/env python3

class Ramen:
    taste = 'Awesome taste'
    audience = 'Naruto Clan'

    def delicious(self):
        print(self.taste)

    def clan(self):
        print(self.audience)
        max = float("-inf")
        print(max)

def main():
    sakura = Ramen()
    sakura.delicious()
    sakura.clan()

if __name__ == '__main__': main()
