"""
- This project looks at 5 Latin character languages: English, French, German, Spanish, Italian
- 2 lists: 1. list of Dolch words, 2. list of source texts
- Each list contains 5 different languages
- have empty list of words for the 5 languages
- each empty list is paired with a count of words found in that language

- have the same for loop structure which occurs twice (outer loop and inner loop):
- first for each of the source texts
- then for each of the Dolch word lists
- then finally it does a comparison

- TODO:
- if found in languageDolch: (i.e. potential language match) :
- append to list      (for all languages in which the word is found in the Dolch word list)
- AND increment count (for all languages in which the word is found in the Dolch word list)

- Finally:
- which ever is the highest count
- this is the language detected.

References:
(0) VScode with Python Extension featuring Intellisense
(1) slice() | W3Schools | https://www.w3schools.com/python/ref_func_slice.asp
(2) Google Search string: | python pass contents of a variable name into a dictionary reference | https://www.google.com/search?q=python+pass+contents+of+a+variable+name+into+a+dictionary+reference&rlz=1C1YTUH_enIE1084IE1084&oq=python+pass+contents+of+a+variable+name+into+a+dictionary+reference&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEJMzE3MzRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8 
(3) Result: | Use square brackets to access a dictionary key using a variable, e.g. my_dict[variable]. | https://bobbyhadz.com/blog/python-use-variable-to-access-dictionary-key#:~:text=Use%20square%20brackets%20to%20access,my_dict%5Bstr(variable)%5D%20.
(4) Google Search string: | python method to find index position of a character in a string | https://www.google.com/search?q=python+method+to+find+index+position+of+a+character+in+a+string&rlz=1C1YTUH_enIE1084IE1084&oq=python+method+to+find+index+position+of+a+character+in+a+string&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEJMjU1NzlqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
(5) Result: | Python String find() with Examples | https://sparkbyexamples.com/python/python-string-find-with-examples/#:~:text=find()%20method%20is%20used,character%20or%20String%20not%20found.
(6) 3.11.6 Documentation » The Python Tutorial | https://docs.python.org/3.11/tutorial/index.html
(7) dictionaries | https://docs.python.org/3.11/tutorial/datastructures.html#dictionaries
(8) Bug | Google Search string | UnicodeDecodeError: 'charmap' codec can't decode byte 0x90 in position 23: character maps to <undefined> | https://www.google.com/search?q=UnicodeDecodeError%3A+%27charmap%27+codec+can%27t+decode+byte+0x90+in+position+23%3A+character+maps+to+%3Cundefined%3E&rlz=1C1YTUH_enIE1084IE1084&oq=UnicodeDecodeError%3A+%27charmap%27+codec+can%27t+decode+byte+0x90+in+position+23%3A+character+maps+to+%3Cundefined%3E&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRg60gEHNjQzajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
(9) Fix | You specify the encoding when you open the file: ```python      file = open(filename, encoding="utf8")   ``` | UnicodeDecodeError: 'charmap' codec can't decode byte X in position Y: character maps to <undefined> | StackOverflow | https://stackoverflow.com/questions/9233027/unicodedecodeerror-charmap-codec-cant-decode-byte-x-in-position-y-character
(10) Implementation: | Google Search string | python read() method | https://www.google.com/search?q=python+read()+method&rlz=1C1YTUH_enIE1084IE1084&oq=python+read()+method&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDc3ODVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
(11) Result: | Python File read() Method | W3Schools | https://www.w3schools.com/python/ref_file_read.asp
(12) Google Search string: | python open() method | https://www.google.com/search?q=python+open()+method&rlz=1C1YTUH_enIE1084IE1084&oq=python+open()+method&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjIICAQQABgWGB4yCAgFEAAYFhgeMggIBhAAGBYYHjIICAcQABgWGB4yCAgIEAAYFhgeMggICRAAGBYYHtIBCDc4MzNqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
(13) Result: | Python open() Function | W3Schools | https://www.w3schools.com/python/ref_func_open.asp
(14) Google Search string: | python open() function | https://www.google.com/search?q=python+open()+function&rlz=1C1YTUH_enIE1084IE1084&oq=python+open()+function&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIICAIQABgWGB4yCAgDEAAYFhgeMggIBBAAGBYYHjIICAUQABgWGB4yBggGEEUYPDIGCAcQRRhB0gEIOTYxN2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
(15) Result: | open() | encoding='utf-8' | Python 3.11 | Documentation| https://docs.python.org/3.11/library/functions.html#open

Note:
Using python --version | Python 3.11.6

"""

languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']

makingDictionaryOfWordsPerLanguage = {
    'English': {'listEnglish' : [], 'countEnglish' : 0},

    'French':  {'listFrench' :  [], 'countFrench' : 0},

    'German' : {'listGerman' : [], 'countGerman' : 0},

    'Spanish' : {'listSpanish' : [], 'countSpanish' : 0},

    'Italian' : {'listItalian' : [], 'countItalian' : 0}
}

languageSources = ['sourceEnglish.txt', 'sourceFrench.txt', 'sourceGerman.txt', 'sourceSpanish.txt', 'sourceItalian.txt']

# outer loop:
for languageSource in languageSources: 
    fileSource = open(languageSource,"r", encoding="utf8") # open(filename, encoding="utf8")
    for word_is_line_Source in fileSource: # word_is_line_Source replaces lineSource (and more importantly wordSource) 
        # for wordSource in lineSource: # try commenting out this to try to solve letter printing at print 2
        # if wordSource in lineSource:
            # do something
            # pass

        # (from last line): for every word in each line of the source text for a given language:
        # (now, look at next bit of code): go through each word in all 5 language dolch word lists (really inefficient, I know):
        print(word_is_line_Source) # print 2 # prints only letters
        # inner loop:
        for languageDolch in languageDolchs:
            fileDolch = open(languageDolch,"r")
            for word_per_line_Dolch in fileDolch: # note each line is a word, so do not go down a level, else will have letters not words # was wordDolch
                # for word_per_line_Dolch in lineDolch: # word_per_line_Dolch was wordDolch

                # and finally,
                # if the current word of the current language Source text
                # is also present in the ____other_thing____variable____
                # of the dolch word list for the current language
                # is 

                # print(word_per_line_Dolch) # comment out word print as too many # working print 1
                
                if word_is_line_Source == word_per_line_Dolch:
                    # get lang
                    currentLanguage = languageSource[6:languageSource.find(".")] # English # hopefully type is String 
                    # so if word is English then,
                    # we get:
                    # get both list:
                    # current_list = makingDictionaryOfWordsPerLanguage[currentLanguage][0].listEnglish # [] to start off with
                    # debugging above line:

                    # now: do same for list: or reverse order
                    language_key_for_list = 'list' + currentLanguage


                    # now: construct variable name count + currentLanguage
                    # for use as key for inner object in dictionary makingDictionaryOfWordsPerLanguage
                    language_key_for_count = 'count' + currentLanguage
                    

                    current_list = makingDictionaryOfWordsPerLanguage[currentLanguage][language_key_for_list]
                    # print(current_list) # comment print to try to reduce excess output
                    # and count:
                    current_count = makingDictionaryOfWordsPerLanguage[currentLanguage][language_key_for_count] # 0 to start off with
                    # append to list:
                    current_list.append(wordSource) # appendwhat?: append wordSource
                    # add to count:
                    current_count=current_count+1

# Next do a count of which count is most:
# So: 
# max function on all 5:
# So:
# first go down to start to define max function
# then come back up and define arguments a-e:

# define variables that will be used as argumwntsto call max function:
a = makingDictionaryOfWordsPerLanguage["English"]['countEnglish']

b = makingDictionaryOfWordsPerLanguage["French"]["countFrench"]

c = makingDictionaryOfWordsPerLanguage["German"]["countGerman"]

d = makingDictionaryOfWordsPerLanguage["Spanish"]["countSpanish"]

e = makingDictionaryOfWordsPerLanguage["Italian"]["countItalian"]

languageOfArticle = maximum_checker(a,b,c,d,e)

def maximum_checker(a,b,c,d,e):
    maximum=a
    if b>maximum:
        maximum=b
    if c>maximum:
        maximum=c
    if d>maximum:
        maximum=d
    if e>maximum:
        maximum=e
    return maximum