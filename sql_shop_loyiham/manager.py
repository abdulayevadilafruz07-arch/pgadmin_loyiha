# from .db_shop import Database
#
# class SHopManager:
#     def __init__(self):
#         self.db = Database()
#
#     # Qo'shish
#     def add_product(self,name,price,quantity):
#         conn=self.db.get_connection()
#         cur=conn.cursor()
#         cur.execute("INSERT INTO products (name,price,quantity) VALUES (%s,%s,%s)",(name,price,quantity))
#         conn.commit()
#         cur.close()
#         conn.close()
#         print("mahsulot qoshildi")
#
#     # Korish
#     def view_products(self):
#         conn=self.db.get_connection()
#         cur=conn.cursor()
#         cur.execute("SELECT * FROM products ORDER BY id")
#         products=cur.fetchall()
#         cur.close()
#         conn.close()
#         if not products:
#             print("no products")
#         for p in products:
#             print(f"ID:{p[0]},name:{p[1]},price:{p[2]},quantity:{p[3]}")
#
#     # Tahrirlash
#     def update_product(self,product_id,price,quantity):
#         conn=self.db.get_connection()
#         cur=conn.cursor()
#         cur.execute("UPDATE products SET price=%s,quantity=%s WHERE id=%s",(price,quantity,product_id))
#         conn.commit()
#         cur.close()
#         conn.close()
#         print("mahsulot qoshildi")
#
#     # O'chirish'
#     def delete_product(self,product_id):
#         conn=self.db.get_connection()
#         cur=conn.cursor()
#         cur.execute("DELETE FROM products WHERE id=%s",(product_id,))
#         conn.commit()
#         cur.close()
#         conn.close()
#         print("mahsulot o'chirildi")
#
#     # Qidirish
#     def search_product(self,keyword):
#         conn=self.db.get_connection()
#         cur=conn.cursor()
#         cur.execute("SELECT * FROM products WHERE name ILIKE %s",(f"%keyword%",))
#         results=cur.fetchall()
#         cur.close()
#         conn.close()
#         if not results:
#             print("mahsulot topilmadi")
#         for p in results:
#             print(f"ID:{p[0]},name:{p[1]},price:{p[2]},quantity:{p[3]}")
#

