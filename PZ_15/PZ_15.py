#Приложение ТОРГОВАЯ ФИРМА для автоматизированного контроля продаж
# товаров торговой фирмы. БД должна содержать таблицу Продажа товаров со следующей
# структурой записи: Дата продажи, Товар, Сумма, Скидка, Филиал, Менеджер.
import sqlite3
with sqlite3.connect("trading_firm.db") as conn:
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sales")
    cursor.execute("""
        CREATE TABLE sales (
            date TEXT, product TEXT, amount REAL, discount REAL, branch TEXT, manager TEXT
        )
    """)

    data = [
        ("2026-06-01", "Ноутбук", 75000, 5, "Западный", "Иванов"),
        ("2026-06-01", "Смартфон", 45000, 0, "Центральный", "Петров"),
        ("2026-06-02", "Ноутбук", 80000, 10, "Северный", "Сидоров"),
        ("2026-06-02", "Монитор", 25000, 3, "Центральный", "Иванов"),
        ("2026-06-03", "Клавиатура", 5000, 0, "Западный", "Петров"),
        ("2026-06-03", "Смартфон", 50000, 5, "Северный", "Иванов"),
        ("2026-06-04", "Мышь", 3000, 0, "Центральный", "Сидоров"),
        ("2026-06-04", "Ноутбук", 75000, 0, "Западный", "Петров"),
        ("2026-06-05", "Принтер", 18000, 7, "Северный", "Иванов"),
        ("2026-06-05", "Монитор", 23000, 0, "Западный", "Сидоров")
    ]
    cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", data)

    try:
        print("результаты поиска")
        for q in [
            "SELECT * FROM sales WHERE manager = 'Иванов'",
            "SELECT * FROM sales WHERE amount > 40000 AND discount = 0",
            "SELECT * FROM sales WHERE branch = 'Западный' AND product = 'Ноутбук'"
        ]:
            print(f"Запрос: {q}\nРезультат: {cursor.execute(q).fetchall()}\n")


        cursor.execute("UPDATE sales SET discount = 15 WHERE product = 'Ноутбук'")
        cursor.execute("UPDATE sales SET branch = 'Западный' WHERE manager = 'Петров' AND branch = 'Центральный'")
        cursor.execute("UPDATE sales SET amount = 20000 WHERE manager = 'Сидоров' AND product = 'Монитор'")
        conn.commit()
        print("таблица после редактирования\n", cursor.execute("SELECT * FROM sales").fetchall(), "\n")

    
        cursor.execute("DELETE FROM sales WHERE amount < 4000")
        cursor.execute("DELETE FROM sales WHERE date = '2026-06-01' AND branch = 'Северный'")
        cursor.execute("DELETE FROM sales WHERE manager = 'Сидоров' AND product = 'Монитор'")
        conn.commit()
        print("таблица после удаления\n", cursor.execute("SELECT * FROM sales").fetchall())

    except sqlite3.Error as e:
        print(f"Ошибка БД: {e}")
