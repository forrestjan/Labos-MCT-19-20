# while is waneer we de voorwaarde niet kennen
# for is waneer we het einddoel kennen
# range is uw bereik
# als een range een getalf afloopt stop hij altijd an
# de voorlaatste waarde
# dus als je range 100 hebt stop hij na het uitvoeren van 99.

doel = 100
som = 0

for index in range(1, doel + 1):
    som = som + index
print(f"het totaal is {som}")
