#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sqlite3
import time

_db_name = 'test.db'

def create_table():
    conn = sqlite3.connect(_db_name)
    print("Opened database successfully")
    c = conn.cursor()
    # c.execute('''
    #     CREATE TABLE COMPANY(
    #         ID INT PRIMARY KEY     NOT NULL,
    #         NAME           TEXT    NOT NULL,
    #         AGE            INT     NOT NULL,
    #         ADDRESS        CHAR(50),
    #         SALARY         REAL
    #     );
    #     '''
    # )
    c.execute('''
        create table job (
            `id` int not null autoincrement,
            `category_id` smallint(4) not null,
            `name` varchar(45) not null,
            `order_id` int(11) not null,
            `status` smallint(4) not null default 0,
            `start_time` timestamp default null,
            `end_time` timestamp default null,
            `create_time` timestamp default current_timestamp,
            `update_time` timestamp default current_timestamp, 
            primary key(`id`)
        );
        '''
    )
    print("Table created successfully")
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect(_db_name)
    c = conn.cursor()
    print("Opened database successfully")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (1, 'Paul', 32, 'California', 20000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

    c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
        VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

    conn.commit()
    print("Records created successfully")
    conn.close()


def select_data():
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    print("Opened database successfully")

    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = {0}, NAME = {1}, ADDRESS = {2}, SALARY = {3} \n".format(row[0], row[1], row[2], row[3]))
    print("Operation done successfully")
    conn.close()

def update_data():
    conn = sqlite3.connect(_db_name)
    c = conn.cursor()
    print("Opened database successfully")

    c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
    conn.commit()
    print("Total number of rows updated : {0}".format(conn.total_changes))
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = {0}, NAME = {1}, ADDRESS = {2}, SALARY = {3} \n".format(row[0], row[1], row[2], row[3]))
    print("Operation done successfully")
    conn.close()

def del_data():
    conn = sqlite3.connect(_db_name)
    c = conn.cursor()
    print("Opened database successfully")
    c.execute("DELETE from COMPANY where ID=2;")
    conn.commit()
    print("Total number of rows deleted : {0}".format(conn.total_changes))
    cursor = conn.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = {0}, NAME = {1}, ADDRESS = {2}, SALARY = {3} \n".format(row[0], row[1], row[2], row[3]))
    print("Operation done successfully")
    conn.close()


def exec_sql(sql, params = None):
    conn = sqlite3.connect(_db_name)
    c = conn.cursor()
    if params is not None:
        cursor = c.execute(sql, params)
    else:
        cursor = c.execute(sql)
    for row in cursor:
        print(row)
    conn.commit()
    print("exec sql ok.")
    conn.close()




def handle_job():
    sql = '''
        create table job (
            `id` INTEGER PRIMARY KEY AUTOINCREMENT,
            `category_id` smallint(4) not null,
            `name` varchar(45) not null,
            `order_id` int(11) not null,
            `status` smallint(4) not null default 0,
            `start_time` timestamp default null,
            `end_time` timestamp default null,
            `create_time` timestamp default current_timestamp,
            `update_time` timestamp default current_timestamp
        );
    '''
    # sql = "INSERT INTO job2 (`category_id`,`name`,`order_id`,`status`,`start_time`) VALUES (?, ?, ?, ?, ?)"
    # exec_sql(sql, [1, '煮面', 1, 0, time.time()])
    # exec_sql(sql, [2, '煮馄饨', 2, 0, time.time()])
    # exec_sql(sql, [3, '煮馄饨', 3, 0, time.time()])

    # sql = "select max(id) from job;"

    # sql = "UPDATE job set order_id = 2 where ID=2"
    exec_sql(sql)
    # print(get_id())

def get_id():
    job_id = None
    conn = sqlite3.connect(_db_name)
    c = conn.cursor()
    cursor = c.execute('select max(id) from job;')
    for row in cursor:
        job_id = row[0]
    conn.commit()
    print("exec sql ok.")
    conn.close()
    return job_id

def main():
    # create_table()
    # insert_data()
    # select_data()
    # update_data()
    # del_data()
    handle_job()

if __name__ == "__main__":
    main()