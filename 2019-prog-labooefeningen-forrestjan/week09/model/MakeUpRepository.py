import json
from .MakeUpProduct import MakeUpProduct
from .ProductColor import ProductColor


class MakeUpRepository:

    _filename = "doc/makeupproducts.json"

    @staticmethod
    def _read_local_json_file(bestandsnaam):
        fo = open(bestandsnaam, encoding='utf8')
        response_json = fo.read()
        fo.close()
        return json.loads(response_json)

    @staticmethod
    def load_products():
        # resultaat (list van objecten)
        list_results_products = []
        # de json(ruwe data)
        list_json = MakeUpRepository._read_local_json_file(
            MakeUpRepository._filename)

        for dict_item in list_json:
            try:
                temp_id = int(dict_item["id"])
                temp_brand = dict_item["brand"]
                temp_name = dict_item["name"]
                temp_price = dict_item["price"]
                temp_product_link = dict_item["product_link"]

                temp_productobject = MakeUpProduct(
                    temp_id, temp_brand, temp_name, temp_price, temp_product_link)
            # colors-> we maken gebruik van de klasse productcolors
            # een kleur is een list van dictionary van key product
                temp_all_colors = dict_item["product_colors"]
                for sub_dict in temp_all_colors:
                    temp_hex = sub_dict["hex_value"]
                    temp_name_color = sub_dict["colour_name"]
                    temp_colorobject = ProductColor(temp_name_color, temp_hex)
                    temp_productobject.add_productcolor(temp_productobject)
                list_results_products.append(temp_productobject)
            except Exception as ex:
                print(f"foutmelding: {ex}")
        return list_results_products

    @staticmethod
    def search_product(list_producten, pattern):
        # geeft een lijst met producten weg waarvan de pattern in de naam zit
        list_result = []
        for product in list_producten:
            if pattern.lower() in product.name.lower():
                list_result.append(product)
        return list_result
