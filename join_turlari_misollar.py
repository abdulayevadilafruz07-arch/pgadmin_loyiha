
# --============================================MAVZU(JOINLAR)=========================================
# --vazifa(boshidagi 10ta misol )
#
#
# --1misol)...
# -- select o.order_id,p.product_name,s.company_name as kompaniya_nomi, o.order_date
# -- from orders o
# -- inner join order_details od on o.order_id=od.order_id
# -- inner join products p on od.product_id=p.product_id
# -- inner join suppliers s on p.supplier_id=s.supplier_id
# -- where to_char(o.order_date,'YYYY-MM')='1996-07';
#
# --2misol)...
# -- select e.city,e.first_name as employee_dan_olingan_ism,c.company_name as customer_dan_olingan_comp
# -- from employees e
# -- inner join customers c on e.city=c.city;
#
# --3misol)...
# -- select to_char(order_date,'YYYY') as orderyear, p.product_name, c.company_name as customer_company,
# -- sum(od.quantity) as totalquantity
# -- from order_details od
# -- join orders o on od.order_id=o.order_id
# -- join products p on od.product_id=p.product_id
# -- join customers c on o.customer_id=c.customer_id
# -- group by to_char(order_date,'YYYY'),  p.product_name, c.company_name
# -- order by totalquantity desc limit 1;
#
#
# --4misol)...
# -- select p.product_name,p.unit_price,c.company_name as customercompany,
# -- sum(od.quantity) as totalquantity
# -- from order_details od
# -- join products p on od.product_id=p.product_id
# -- join orders o on od.order_id=o.order_id
# -- join customers c on o.customer_id=c.customer_id
# -- where p.unit_price<= all(select unit_price from products)
# -- group by p.product_id, p.product_name,p.unit_price,c.company_name
# -- order by totalquantity desc limit 1;
#
#
# --5misol)...
# -- select distinct p.product_name, p.unit_price
# -- from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- where p.unit_price< any(
# -- select unit_price
# -- from products
# -- )
# -- order by p.unit_price;
#
#
# --6misol)...
# -- select e.employee_id, e.first_name, e.last_name,e.title, count(o.order_id) as total_orders
# -- from employees e
# -- join orders o on e.employee_id=o.employee_id
# -- where e.country='USA'
# -- group by e.employee_id, e.first_name, e.last_name,e.title
# -- order by total_orders desc limit 6;
#
# --7misol)...
# -- select e.country,count(o.order_id) as total_orders
# -- from employees e
# -- join orders o on e.employee_id=o.employee_id
# -- group by e.country
# -- order by total_orders desc limit 1;
#
# --8misol)...
# -- select c.customer_id,c.company_name,
# -- sum(od.quantity*od.unit_price*(1-od.discount)) as totalamount
# -- from customers c
# -- join orders o on c.customer_id=o.customer_id
# -- join order_details od on o.order_id=od.order_id
# -- where to_char(o.order_date,'YYYY')='1997'
# -- group by  c.customer_id,c.company_name
# -- order by totalamount desc limit 5;
#
# --9misol)...
# -- select p.product_id,p.product_name, sum(od.quantity) as totalquantity
# -- from products p
# -- join order_details od on p.product_id=od.product_id
# -- group by p.product_id,p.product_name
# -- order by totalquantity limit 5;
#
# --10misol)...
# -- select p.product_name,p.unit_price,c.company_name as customercompany, s.company_name as suppliercompany
# -- from products p
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o  on od.order_id=o.order_id
# -- inner join customers c on o.customer_id=c.customer_id
# -- inner join suppliers s on p.supplier_id=s.supplier_id
# -- where p.category_id =1
# -- group by p.product_id, p.product_name, p.unit_price, c.company_name, s.company_name
# -- order by p.unit_price desc limit 10;

#
# --4m
# -- select p.product_name,p.unit_price,c.company_name,count(od.quantity)
# -- from order_details od
# -- join products p on od.product_id=p.product_id
# -- join orders o on od.order_id=o.order_id
# -- join customers c on o.customer_id=c.customer_id
# -- where p.unit_price<= all(select unit_price from products)
# -- group by p.product_name,p.unit_price,c.company_name
# -- having by(select count(od.quantity) from order_details)
#
# -- select p.product_name, to_char(o.order_date,'YYYY'),c.company_name,count(o.)
#
# -- 12m)...
# -- select s.company_name, count(o.order_id) from suppliers s
# -- inner join products p on s.supplier_id=p.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- where s.city='London'
# -- group by s.company_name
# -- having (o.order_id)=(select count(o.order_id) from suppliers s
# -- inner join products p on s.supplier_id=p.supplier_id
# -- inner join order_details od on p.product_id=od.product_id
# -- inner join orders o on o.order_id=od.order_id
# -- where s.city='London'
# -- group by s.company_name
# -- order by count(o.order_id) desc limit 1)
# -- order by count(o.order_id)
