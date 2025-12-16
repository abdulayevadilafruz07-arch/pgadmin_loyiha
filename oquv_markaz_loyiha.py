# create table if not exists Teachers(
# id serial primary key,
# full_name varchar(50) not null,
# phone varchar(20),
# specialty varchar(30) not null,
# created_at varchar(30)not null
# );
#
# create table if not exists Students(
# id serial primary key,
# full_name varchar(50) not null,
# phone varchar(20),
# birth_date varchar(20) not null,
# created_at varchar(30) not null
# );
#
# create table if not exists payments(
# id serial primary key,
# student_id varchar(20),
# group_id varchar(20),
# amount integer check (amount>0),
# payment_date varchar (20),
# payment_type varchar (20)
# );
#
# create table if not exists groups(
# id serial primary key,
# name varchar(50) not null,
# course_id varchar(20) not null,
# teacher_id varchar(20) not null,
# start_date varchar(20) not null,
# status varchar(50) not null
# );
#
# create table if not exists enrollments(
# id serial primary key,
# student_id varchar(20) not null,
# group_id varchar(20) not null,
# joined_date varchar(20)
# );
#
# create table if not exists courses(
# id serial primary key,
# name varchar(50) not null,
# price integer check (price>0),
# duration_month varchar(30),
# created_at varchar(30)
# );
#
# create table if not exists homework(
# id serial primary key,
# group_id varchar(20) not null,
# teacher_id varchar(20) not null,
# title varchar(30) not null,
# description varchar(100),
# deadline varchar(30)
# );
#
# create table if not exists admins(
# id serial primary key,
# full_name varchar(50) not null,
# phone varchar(20),
# password varchar(20),
# role varchar(30)
# );
#
# create table if not exists attendance(
# id serial primary key,
# student_id varchar(20) not null,
# group_id varchar(20) not null,
# lesson_date varchar(30) not null,
# status varchar(50)
# );










