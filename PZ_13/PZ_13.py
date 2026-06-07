#В исходном текстовом файле(hotline1.txt) найти все номера телефонов,
#соответствующих шаблону 8(000)000-00-00. Посчитать количество полученных
#элементов. После фразы «Горячая линия» добавить фразу «Министерства
# образования Ростовской области», выполнив манипуляции в новом файле.
import re
with open("PZ_13/hotline1.txt", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r"8\(\d{3}\)\d{3}-\d{2}-\d{2}"
phones = re.findall(pattern, content)

print("найденные номера:", phones)
print("кол-во полученных элементов:", len(phones))

new_content = content.replace("«Горячая линия»", "«Горячая линия» Министерства образования Ростовской области")

with open("PZ_13/hotline_new.txt", "w", encoding="utf-8") as outfile:
    outfile.write(new_content)