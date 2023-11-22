# .replace() | w3schools | txt = "I like bananas"; x = txt.replace("bananas", "apples"); print(x) | https://www.w3schools.com/python/ref_string_replace.asp

# txt = "I like bananas"
# x = txt.replace("bananas", "apples")
# print(x)
file_name_dolch="English.txt"
wordDolch = 'the'
file = open(file_name_dolch, 'r', encoding='utf8')
for word in file:
    if '\n' in word:
        word=word.replace("\n", "")
    # print(word)
    # break
    if wordDolch == word: # words from file
        # print('hi')
        lang = file_name_dolch.rstrip('.txt')
        print(lang)
