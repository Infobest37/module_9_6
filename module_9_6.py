def all_variants(text):
    while True:
        yield text[0]
        yield text[1]
        yield text[2]
        break
    while True:
        yield text[0] + text[1]
        yield text[1] + text[2]
        break
    yield text[0] + text[1] + text[2]

    # for i in text:
    #     if i in text:
    #         yield i
    #
    #     if i == text[0]:
    #         yield i + text[1]
    #     if i == text[1]:
    #         yield i + text[2]
    #     yield text






a = all_variants("abc")
for i in a:
    print(i)