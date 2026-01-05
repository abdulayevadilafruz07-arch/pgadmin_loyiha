# from .manager import SHopManager
#
# def run_shop():
#     shop = SHopManager()
#     while True:
#         print('''
#     1. Mahsulot qo'shish
#     2.Mahsulotlarni ko'rish
#     3.Mahsulotni tahrirlash
#     4.Mahsulotni o'chirish
#     5.Mahsulot qidirish
#     0.Chiqish''')
#         choice = input("Tanlang")
#         if choice == "1":
#             name = input("Mahsulot nomi:")
#             price = float(input("Mahsulot price :"))
#             quantity = int(input("Mahsulot quantity :"))
#             shop.add_product(name, price, quantity)
#         elif choice == "2":
#             shop.view_products()
#         elif choice == "3":
#             p_id = int(input("Mahsulot id :"))
#             price = float(input("Yangi narx"))
#             quantity = int(input("Yangi miqdor"))
#             shop.update_product(p_id, price, quantity)
#         elif choice == "4":
#             p_id = int(input("Mahsulot id :"))
#             shop.delete_product(p_id)
#         elif choice == "5":
#             key = input("Qidiruv")
#             shop.search_product(key)
#         elif choice == "0":
#             print("Chiqildi")
#             break
#         else:
#             print("notog'ri tanlov, qayta urinib korish")
#
# if __name__ == '__main__':
#     run_shop()