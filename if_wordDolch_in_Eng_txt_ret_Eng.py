def get_language():
    wordDolch = 'free'
    file = open('English.txt', 'r', encoding='utf8')
    for line in file:
        list_of_words_per_line=line.split(" ")
        for words in list_of_words_per_line:
            if wordDolch in words: # words from file
                lang = file.rstrip('.txt')
                print(lang)
                return lang

language_returned = get_language()

print(language_returned)
