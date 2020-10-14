#zelfoefening ik germaak oefening 6 zonder _ bij woorden voor te weten of het een verschil maakt buiten orde en netheid van de code 
totaalseconde = int(input("Geef het aantal seconden op "))

aantalsec1dag = 24 * 60 * 60

aantaldagen = totaalseconde // aantalsec1dag
print(aantaldagen)

restseconde = totaalseconde % aantalsec1dag

aantalsec1uur = 60 * 60 
aantaluren = restseconde // aantalsec1uur
print(aantaluren)
restseconde = restseconde % aantalsec1uur

aantalsec1minuut = 60 
aantalminuten = restseconde // aantalsec1minuut
print(aantalminuten)
restseconde = restseconde % aantalsec1minuut

print(f"{aantaldagen}:{aantaluren}:{aantalminuten}:{restseconde}")