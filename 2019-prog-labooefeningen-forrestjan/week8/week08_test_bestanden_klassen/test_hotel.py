from model.Hotel import Hotel
from model.Hotelgast import Hotelgast

hotel_howest = Hotel("howest")
print(f"{hotel_howest}")

hotel_howest.check_in("Walcarius", "Stijn")
hotel_howest.check_in("Laprudence", "Christophe")
print(f"{hotel_howest.gasten}")
#
# hotel_howest.bestel_drank("Walcarius", "Stijn", 100)
#
# print("\n")
# hotel_howest.print_info_gasten()
# print("Stijn betaalt zijn schuld")
# hotel_howest.vereffen_saldo_gast("Walcarius", "Stijn")
# print("******************")
# hotel_howest.check_out("Walcarius", "Stijn")
# print("******************")
# print("\n")
# hotel_howest.print_info_gasten()
