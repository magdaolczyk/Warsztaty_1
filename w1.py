import random

def guess():
    while True:
        try:
            x = random.randint(1, 101)
            a = 0
            while a != x:
                a = int(input("Zgadnij liczbę: "))
                if a < x:
                    print("Za mało!")
                elif a > x:
                    print("Za dużo!")
                else:
                    print("Zgadłeś!")
        except ValueError:
            print("To nie jest liczba")
        return

guess()