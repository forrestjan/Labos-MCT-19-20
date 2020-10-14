rom model.Presentator import Presentator
# rom model.Tvprogramma import Tvprogramma
# rom model.Zender import Zender
# 
# 
# resentator1 = Presentator("Laura", "Tesoro")
# resentator2 = Presentator("Nathalie", "Meskens")
# 
# 
# rogramma1 = Tvprogramma("Belgium got talent", presentator1)
# rogramma2 = Tvprogramma("Beste kijkers", presentator2)
# rogramma2.is_actief = False
# 
#  Verkort
# rogramma3 = Tvprogramma("The Late Late Show", Presentator("James", "Corden"))
# 
# 
# ender1 = Zender("VTM", "NL")
# ender2 = Zender("FOX", "ENG")
# ender3 = Zender("TV China", "Chinees")
# 
# ender1.voeg_programma_toe(programma1)
# ender1.voeg_programma_toe(programma2)
# ender2.voeg_programma_toe(programma3)
# ender2.voeg_programma_toe("dit zal niet lukken")
# 
# rint("*** info zenders ***")
# rint(zender1)
# rint(zender2)
# rint(zender3)
# rint(f"**** volgende programma's zijn afgelopen van {zender1.naam}  ***")
# rint(zender1.zoek_afgelopen())
# rint(
#    f"**** volgend programma wordt willekeurig gekozen van {zender1.naam} ***")
# rint(zender1.selecteer_willekeurig_programma())
# rint(
#    f"Aantal verschillende zenders aangemaakt {Zender.geef_aantal_aangemaakte_zenders()}")
# 