with open("en-ru.txt", "r") as f:
    dict_en_ru = {}
    for line in f:
        word_pair = line.strip().split(" - ")
        en_word = word_pair[0]
        ru_words = word_pair[1].split(", ")
        dict_en_ru[en_word] = ru_words

dict_ru_en = {}
for en_word, ru_words in dict_en_ru.items():
    for ru_word in ru_words:
        if ru_word in dict_ru_en:
            dict_ru_en[ru_word].append(en_word)
        else:
            dict_ru_en[ru_word] = [en_word]

with open("ru-en.txt", "w") as f:
    for ru_word in sorted(dict_ru_en.keys()):
        en_words = ", ".join(sorted(dict_ru_en[ru_word]))
        f.write(f"{ru_word} - {en_words}\n")