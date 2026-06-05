import tkinter as tk

def run():
    try:
        n = int(entry.get())
        if 100 <= n <= 999:
            fn = n // 100
            res.config(text=f"Первая цифра: {fn}")
        else:
            res.config(text="Число должно быть трехзначным!")
    except:
        res.config(text="Введите корректное число!")

root = tk.Tk()
root.title("практос 2")
root.geometry("500x500")

tk.Label(root, text="Введите трехзначное число:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)

tk.Button(root, text="Старт", command=run).pack(pady=10)
res = tk.Label(root, text="Первая цифра: ")
res.pack(pady=10)

root.mainloop()