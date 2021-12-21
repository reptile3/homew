"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""
"""
Не смог решаить ошибку, не доделал
"""

import sqlite3
import os


def delete_id(id_delete):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''DELETE FROM user
            WHERE id=?;''',
            (id_delete))
    session.commit()
    return cursor.fetchone()

def update_tabble(id_update,cout_new):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''UPDATE user
            SET cout = ?
            WHERE id = ?;
            ''',
            (cout_new,id_update))
    session.commit()
    return cursor.fetchone()

def show_all():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """SELECT * FROM user;
            """)
    all_results = cursor.fetchall()
    for elements in all_results:
        print(elements)
    session.commit()
    return cursor.fetchone()


def create_products():
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''
        CREATE TABLE user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR UNIQUE,
            price INTEGER,
            cout INTREGER,
            comment VARCHAR
            );
            '''
        )
    session.commit()
    return cursor.fetchone()

def add_product(new_product):
    with sqlite3.connect("products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            '''
        INSERT INTO user (name, price, cout, comment)
            VALUES (?,?,?,?);

            ''',
            (new_product),
        )

    session.commit()
    listen()

if __name__=='__main__':



    
