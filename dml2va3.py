
# masala yechishda ketma ketlik
# -- from
# -- where(ustunlarga shart beradi)
# -- group by(guruhlaydi)
# -- having
# -- select
# -- order by(tartiblab beradi)
# -- limit
#
#
# --------------------------------DML2----------------------------------------------------------
# --1m)...3chi categoriyadagi eng arzon mahsulotlar
# -- select * from products
# -- where category_id=3 and unit_price =(select min(unit_price)from products where category_id=3)
#
# --2m)...1997yilning 7oyidagi kechikkan zakazlar soni
# -- select * from orders
# -- where shipped_date>required_date and to_char(order_date,'YYYY-MM')='1997-07'
#
# --3m)...hech bolmaganda bitta mahsuloti bor bolgan categoriyalar chiqarilsin
# --select * from categories
# --insert into categories(category_id,category_name,description)
# --values
# --(9,'test_category','kkkkkkk')
#
# --select *
# -- from categories
# -- where exists(
# -- select * from product
# -- where product_id=category.product_id);
#
# --4m)...[2]chi categoriyadan [6]chi categoriyagacha narxi 10$ dan baland bolgan va product_name ning 1chi harfi 'C' bolgan productlar chiqarilsin
# -- select * from products where category_id between 2 and 6
# -- and unit_price > 10 and product_name like 'C%';
#
# --5m)..amerikalik customerlar soni
# -- select company_name, country from customers where country in('USA')
#
# --------------------------------DML3==== GROUP BY===----------------------------------------------------------
#
# -- ==========================================GROUP BY=================================================
# --1m)...category_id boyicha guruhlaymiz va har bir categorydagi mahsulotlarni sanaymiz;
# -- select category_id , count(*) as product_count
# -- from products
# -- group by category_id;
#
#
# --2m)...1997yilning har bir oyidagi kechikkan zakazlar sonini chiqaring
# -- select to_char(order_date,'YYYY-MM') as yilning_oyi_boyicha, count(*) k_zakazlar_soni
# -- from orders
# -- where to_char(order_date,'YYYY')='1997' and shipped_date>required_date
# -- group by to_char(order_date,'YYYY-MM');
#
#
# --3m)...1997yilning mart oyidagi kunlik zakazlari soni(kun boyicha guruhlanadi)
# -- select to_char(order_date,'YYYY-MM-DD') AS YIL_OY_KUN,COUNT(*)
# -- FROM ORDERS
# -- WHERE TO_CHAR(ORDER_DATE,'YYYY-MM')='1997-03'
# -- GROUP BY TO_CHAR(ORDER_DATE,'YYYY-MM-DD');
#

# -- ============================HAVING(aggregat funksiyalardan qaytgan qiymatlarga having bilan shart beriladi, group by dan keyin yoziladi )===========================
# --4m)...1997yilning har bir oyidagi zakazlar chiqarilsin, faqat 10tadan kop zakaz tushganlari(count jadvalda yoq u agregat funksiya shuning uchun unga having bn shart beramiz)
# -- select to_char(order_date,'YYYY-MM') AS YIL_OY_KUN,COUNT(*)
# -- FROM ORDERS
# -- WHERE TO_CHAR(ORDER_DATE,'YYYY')='1997'
# -- GROUP BY TO_CHAR(ORDER_DATE,'YYYY-MM')
# -- HAVING COUNT(*)>10
#
#
# --5m)...1997yilning har bir oyidagi zakazlari, har bir categoriyadagi productlar soni hisoblansin, faqat productlar soni 10dan kop bolgan categoriyalar  chiqarilsin
# -- select category_id, count(*) from products
# -- group by category_id
# -- having count(*)>10

# vazifa
# -- 97yil har bir oyida har bir hodimning zakazlari soni
# -- vazifa
# -- 1...1chi categordagi productlar 96yi har bir oyida mahsulotga qancga zakas tushgan (zakazlar soni) 10dan qimmat
# -- 2.....3chi category dagi eng arzon mahsulot ga 97yi 7oyida yetkazib bergan supplierlar
# -- 3.....98yilning marta oyidagi  zakazlarni sotib olgan mijozlar ga xizmat qilgan xodimlar
# -- 4.....har bir categorydagi eng qimmat mahsulot 96yilda qanchadan sotilgan
# -- 5......97yilda amerikalik customerga xizmat korsatgan amerikalik supplier aniqlansin
# -- 6......5chi categrydagi mahsulotlarga 97yilda xizmat korsatgan xodimlar
# --7........amerikalik har bir shahri 97yil har bir oyida qanchadan zakaz olgan

