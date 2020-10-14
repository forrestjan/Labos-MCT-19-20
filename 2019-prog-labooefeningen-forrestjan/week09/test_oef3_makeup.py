from model.MakeUpRepository import MakeUpRepository
from model.MakeUpProduct import MakeUpProduct
from model.ProductColor import ProductColor

lst_products = MakeUpRepository.load_products()
print(lst_products)

te_zoeken = input("geef zoeknaam op >")
lst_rslt = MakeUpRepository.search_product(lst_products, te_zoeken)
lst_rslt.sort()

for item in lst_rslt:
    print(item)
