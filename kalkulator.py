# Zadanie (kalkulator 4 działaniowy)
# W zadaniu należy napisać kalkulator wczytujący od użytkownika kolejno
# liczbę (pierwszy operand)
# znak +,-,* lub /
# liczbę (drugi operand)
# i zwracający wynik odpowiedniego działania kalkulatorowego
# Podaj nazwę 1 zmiennej: x
# Podaj nazwę 2 zmiennej: y
# Podaj symbol działania: znak

wybor = "t"
while (wybor =="t"):
    x=input("Podaj 1 liczbę: ")
    x=int(x)
    y=input("Podaj 2 liczbę: ")
    y=int(y)
    znak=input("Podaj znak z klawiatury\n")
    if y==0 and znak=="/":
        print("bzdura") 
        break
    if znak == "+":
        wynik = x + y
    elif znak == "-":
        wynik = x - y
    elif znak=="*":
        wynik = x * y
    elif znak=="/":
        wynik = x / y

    print("Wynikiem tego działania jest: ", wynik)
    wybor = input("Czy chcesz coś obliczyć? t/n: ")
