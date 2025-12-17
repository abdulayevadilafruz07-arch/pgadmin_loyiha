
# -- from
# -- where
# -- group by
# -- having
# -- select
# -- order by
# -- limit
#


# --1misol(order by)
# --select * from categories
# --order by category_name desc
#
# --2-misol(where)
# --select product_name , category_id from products
# --where category_id>3
#
# --3-misol(like)
# --select product_name , category_id from products
# --where category_id>3 and product_name like '_a%'
#
# --4-misol(between)
# --select product_name , category_id from products
# --where category_id between 4 and 6;
#
# --5-misol(between)
# --select * from orders
# --where order_date >='1997-03-01' and order_date<'1997-08-01'
#
# --6-misol(in)
# --select country from customers where country in ('US','UK');
#
# --7-misol(is null==bosh qiymatlarni tekshirish
# --is not null==bosh bolmagan qiymatlarni tekshirish)
# --select * from customers where country is null;
#
# --8-misol
# /*select *
# from employee
# where exists (
#     select *
# 	from department
# 	where department_id = employee.depatment_id
# );*/
#
#
# --9-misol(limit)
# --select * from employee limit 3;
#
# --10-misol(offset-limit nchisidan boshlab mtasini chiqarish uchun)
# --select product_name, category_id
# --from products
# --limit 2 offset 2;
#
# --11-misol
# --select max(unit_price) from products
#
# --12-misol(eng qimmat mahsulotning barcha malumotlari)
# --select * from products
# --where unit_price=(select max(unit_price) from products)
#
# --13-misol(to_char, extract)
# --select * from orders
# --where to_char(order_date, 'YYYY-MM')='1997-05'
# --extract (year from order_date)=1997 and extract (month from order_date)=5
#
# --uyga vazifa1
# --1-misol(product jadvalidan category_id si 3dan katta bolgan productlarni product_name boyicha saralansin)
# --2-misol(customer jadvalidan countrysi braziliya bolgan companiya_name ning 3chi harfi n bolgan kompaniyalar chiqarilsin )
# --3-misol(customer jadvalidan regioni britaniya bolgan va company_name ning oxiridan 3chi harfi a bolgan kompaniyalar chiqarilsin)
# --4-misol(product jadvalidagi ortacha narxlarni chiqaring)
# --5-misol(orders jadvalidan 1997yilning 7 oyidagi kechikkan zakazlar soni)
# --6-misol(product jadvalidan  1chi categorydagi eng qimmat mahsulotning barcha malumotlari chiqarilsin)
#
# --vazifa2
# --sxemaning categories, products, suppliers, order_details, orders jadvallarini kod bilan yaratamiz, foreign key qilib boglaymiz.
# --har biriga bir qoshishda 5ta mahsulot qoshamiz
# --select qilib hammasini korib olamiz
# --5ta mahsulotning 4chisini ochiramiz
# --5chi mahsulotning  3ta ustunini update qilamiz
# --suppliers jadvaliga ga muallif degan ustun qoshamiz (altertable ) keyin muallifni rename qilib aftrga ozgartiramiz
#
# vazifa2
# --categories,products,suppliers,order_details,orders
#
# create table if not exists categories(
# category_id smallint not null,
# category_name character varying(25) not null,
# description text,
# picture bytea
# );
#
#
# create table if not exists products(
# product_id smallint not null,
# product_name character varying(40) not null,
# supplier_id smallint,
# category_id smallint,
# quantity_per_unit character varying(25),
# unit_price real,
# units_in_stock smallint,
# units_on_order smallint,
# reorder_level smallint,
# discontinued integer not null
# );
#
#
# create table if not exists suppliers(
# supplier_id smallint not null,
# company_name character varying(40) not null,
# contact_name character varying(35),
# contact_title character varying(30),
# address character varying(60),
# city character varying(15),
# region character varying(15),
# postal_code character varying(10),
# country character varying(15),
# phone character varying(24),
# fax character varying(24),
# homepage text
# );
#
# create table if not exists order_details(
# order_id smallint not null,
# product_id smallint not null,
# unit_price real not null,
# quantity smallint not null,
# discount real not null
# );
#
# create table if not exists orders(
# order_id smallint not null,
# order_date date,
# required_date date,
# shipped_date date,
# ship_via smallint,
# freight real,
# ship_name character varying(50),
# ship_address character varying(60),
# ship_city character varying(15),
# ship_region character varying(20),
# ship_postal_code character varying(15),
# ship_country character varying(15)
# );
#
# /*alter table categories
# add constraint pk_categories
# primary key (category_id);
#
# alter table suppliers
# add constraint pk_suppliers
# primary key (supplier_id);
#
# alter table products
# add constraint pk_products
# primary key (product_id);
#
# alter table orders
# add constraint pk_orders
# primary key (order_id);
#
# alter table order_details
# add constraint pk_order_details
# primary key (order_id, product_id);
#
#
#
#
# alter table products
# add constraint fk_products_categories
# foreign key (category_id)
# references categories(category_id);
#
# alter table products
# add constraint fk_products_suppliers
# foreign key (supplier_id)
# references suppliers(supplier_id);
#
# alter table order_details
# add constraint fk_order_details_orders
# foreign key (order_id)
# references orders(order_id)
# on delete cascade;
#
# alter table order_details
# add constraint fk_order_details_products
# foreign key (product_id)
# references products(product_id)*/
#
#
# /*insert into categories(category_id,category_name,description)
# values
# (1,'name1', 'drinks'),
# (2,'name2', 'sauses'),
# (3,'name3', 'sweets'),
# (4,'name4', 'milk products'),
# (5,'name5', 'fish');
#
# insert into suppliers (supplier_id,company_name,country)
# values
# (1,'suppl A', 'USA'),
# (2,'suppl B', 'Germany'),
# (3,'suppl C', 'France'),
# (4,'suppl D', 'Japan'),
# (5,'suppl E', 'China');
#
# insert into products(product_id, product_name,supplier_id,category_id,unit_price,units_in_stock,discontinued)
# values
# (1,'tea',1,1,10.5,50,0),
# (2,'coffee',2,1,15.0,40,0),
# (3,'cheese',3,4,25.0,20,0),
# (4,'chocolate',4,3,8.0,100,0),
# (5,'fish',5,5,30.0,15,0);
#
# insert into orders(order_id,order_date,ship_country)
# values
# (1,'2024-01-01','USA'),
# (2,'2024-01-02','Germany'),
# (3,'2024-01-03','France'),
# (4,'2024-01-04','Japan'),
# (5,'2024-01-05','China');*/
#
#
# --select * from products
# --delete from products where product_id=4
# --select * from products
#
# --delete from orders where order-id=4
# --delete from suppliers where supplier_id=4
# --delete from categories where category-id=4
#
#
#
# /*update products
# set
# product_name='updated product',
# unit_price=99.8,
# units_in_stock=500
# where product_id=5;*/
#
# --select * from products
#
#
#
# --alter table suppliers
# --add column muallif varchar(100);
#
# --alter table suppliers
# --rename column muallif to aftor;
#

# # vazifa1
#
# --1-misol
# --select category_id, product_name from products
# --where category-id>3
#
# --2-3-misol
# --select company_name , country from customers
# --where country in ('Braziliya') and company_name like '%a__';
#
# --4-misol
# --select avg(unit_price) from products
#
#--5-misol
# --select order_date from orders
# --where to_char(order_date, 'YYYY-MM')='1997-07'
