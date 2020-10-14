totaal_seconde = int(input("Geef het aantal seconde op "))

#hoeveel dagen/uren/minuten/seconde zitten hierin

aantal_sec_1dag = 24 * 60 * 60
#we voeren een gehele deling uit: uit resultaaat is dan een niet-komma getal
aantal_dagen = totaal_seconde //aantal_sec_1dag
print(aantal_dagen)

#de rest van een delen kan je via de modulo-operator dit is het ´%' andere uitleg:het is een modulo en je houd de rest over aje een deling maakt dus je bekijkt wat je overhoud  na een deling 
rest_seconde = totaal_seconde % aantal_sec_1dag
#stap 2: bereken hoeveel volle uren in de rest zitten
aantal_sec_in_1uur = 60 * 60
aantal_uren = rest_seconde // aantal_sec_in_1uur
print(aantal_uren)
rest_seconde = rest_seconde % aantal_sec_in_1uur

#stap 3 hoeveel volle mintuen zitten er in de rest
aantal_sec_1mintuut = 60
aantal_minuten = rest_seconde // aantal_sec_1mintuut
print(aantal_minuten)
rest_seconde = rest_seconde % aantal_sec_1mintuut

print(f"{aantal_dagen}:{aantal_uren}:{aantal_minuten}:{rest_seconde}")