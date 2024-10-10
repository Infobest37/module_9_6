def all_variants(text):

    for i in text:
        yield i
    # Генерируем уникальные строки длиной в 2 символа которые идут по порядку и не повторяются друг с другом
    s = set() # используем множество, чтобы избежать повторов
    for i in range(len(text)):
        for j in range(len(text)):
            line_s = text[i:j+1] # переменная которая добавляет по одной букве в каждой строке зависимости от
            # длины слова
            if len(line_s) == 2 and i != j: # тут я делаю так чтоб в каждой строке было по две буквы и чтоб буквы
                # не повторялись друг с другом через множество
                s.add(line_s)
                yield line_s
    yield text







a = all_variants("abcclhgt")
for i in a:
    print(i)

