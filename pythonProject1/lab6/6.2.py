alph = {
    "а": 1,
    "б": 3,
    "в": 1,
    "г": 3,
    "д": 2,
    "е": 1,
    "ё": 3,
    "ж": 5,
    "з": 5,
    "и": 1,
    "й": 4,
    "к": 2,
    "л": 2,
    "м": 2,
    "н": 1,
    "о": 1,
    "п": 2,
    "р": 1,
    "с": 1,
    "т": 1,
    "у": 2,
    "ф": 10,
    "х": 5,
    "ц": 5,
    "ч": 5,
    "ш": 8,
    "щ": 10,
    "ъ": 10,
    "ы": 4,
    "ь": 3,
    "э": 8,
    "ю": 8,
    "я": 3
}
sl = input()
t = 0
for i in sl:
    t += alph[i.lower()]
print(t)
