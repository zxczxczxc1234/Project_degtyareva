#Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
import sqlite3

with sqlite3.connect("trading_firm.db") as conn:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sales")
    cursor.execute("CREATE TABLE sales (date TEXT, product TEXT, amount REAL, discount REAL, branch TEXT, manager TEXT)")


    with open("PZ_15/sales.txt", "r", encoding="utf-8") as f:
        next(f)
        data = [line.strip().split(',') for line in f]
    
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", data)

    try:
        print("Результат поиска")
        queries = [
            "SELECT * FROM sales WHERE manager = 'Иванов'",
            "SELECT * FROM sales WHERE amount > 40000 AND discount = 0",
            "SELECT * FROM sales WHERE branch = 'Западный' AND product = 'Ноутбук'"
        ]
        for q in queries:
            print(f"Запрос: {q}\nРезультат: {cursor.execute(q).fetchall()}\n")


        cursor.execute("UPDATE sales SET discount = 15 WHERE product = 'Ноутбук'")
        cursor.execute("UPDATE sales SET branch = 'Западный' WHERE manager = 'Петров' AND branch = 'Центральный'")
        cursor.execute("UPDATE sales SET amount = 20000 WHERE manager = 'Иванов' AND product = 'Принтер'")
        
        conn.commit()
        print("После редактирования")
        for row in cursor.execute("SELECT * FROM sales").fetchall(): print(row)
        print()


        cursor.execute("DELETE FROM sales WHERE amount < 4000")
        cursor.execute("DELETE FROM sales WHERE date = '2026-06-03' AND branch = 'Северный'")
        cursor.execute("DELETE FROM sales WHERE manager = 'Сидоров' AND product = 'Монитор'")
        
        conn.commit()
        print("После удаления")
        for row in cursor.execute("SELECT * FROM sales").fetchall(): print(row)

    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")
