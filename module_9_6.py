def all_variants(text):
    # while True:
    #     yield text[0]
    #     yield text[1]
    #     yield text[2]
    #     break
    # while True:
    #     yield text[0] + text[1]
    #     yield text[1] + text[2]
    #     break
    # yield text[0] + text[1] + text[2]

    for i in text:
        if i in text:
            yield i
    for j in text:
        if j == text[0]:
            yield j + text[1]
            yield text[1] + text[2]
    yield text






a = all_variants("abc")
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
for i in a:
    print(i)

