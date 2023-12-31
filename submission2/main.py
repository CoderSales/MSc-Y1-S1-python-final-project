"""
Problem 2:
You have five texts, each a different language. You want to be able to detect the language for
each of the texts. You want to be able to repeat that on other texts of the same languages.

Simplified Version:
only compares 2 languages
- only compares 1 word from French

TO RUN (on Windows VSCode git bash terminal):
(OPTIONAL):
python -m venv .venv
source .venv/Scripts/activate
NECESSARY:
python main.py


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
(5_1) Google Search string: | python how to access 1st element in object -tuple -javascript | https://www.google.com/search?q=python+how+to+access+1st+element+in+object+-tuple+-javascript&newwindow=1&sca_esv=584437237&rlz=1C1YTUH_enIE1084IE1084&sxsrf=AM9HkKnfAyxTehEWcOLY_IJTYucXIN7Jtg%3A1700613625945&ei=-U1dZYusOYeKgAbQ7KvwCA&ved=0ahUKEwjLjMy4r9aCAxUHBcAKHVD2Co4Q4dUDCBA&uact=5&oq=python+how+to+access+1st+element+in+object+-tuple+-javascript&gs_lp=Egxnd3Mtd2l6LXNlcnAiPXB5dGhvbiBob3cgdG8gYWNjZXNzIDFzdCBlbGVtZW50IGluIG9iamVjdCAtdHVwbGUgLWphdmFzY3JpcHRImjtQqwRYrTlwAngBkAEAmAEpoAGUAqoBATe4AQPIAQD4AQHCAgoQABhHGNYEGLAD4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp
(5_2) Google Search string: | python docummentation | https://www.google.com/search?q=python+docummentation&rlz=1C1YTUH_enIE1084IE1084&oq=python+docummentation&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgKGIAEMgkIAhAAGAoYgAQyCQgDEAAYChiABDIJCAQQABgKGIAEMgkIBRAAGAoYgAQyCQgGEAAYChiABDIJCAcQABgKGIAEMgkICBAAGAoYgAQyCQgJEAAYChiABNIBCDczOTRqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
(5_3) Google Search string: | python documentation | https://www.google.com/search?q=python+documentation&newwindow=1&sca_esv=584452497&rlz=1C1YTUH_enIE1084IE1084&sxsrf=AM9HkKnPl25K0SKNTwg9tO-hKuRQf22kvg%3A1700613740172&ei=bE5dZceRCqCihbIPgNqs0Ag&ved=0ahUKEwjH94fvr9aCAxUgUUEAHQAtC4oQ4dUDCBA&uact=5&oq=python+documentation&gs_lp=Egxnd3Mtd2l6LXNlcnAiFHB5dGhvbiBkb2N1bWVudGF0aW9uMgQQABhHMgQQABhHMgQQABhHMgQQABhHMgQQABhHMgQQABhHMgQQABhHMgQQABhHSP8fUN4eWN4ecAJ4ApABAJgBAKABAKoBALgBA8gBAPgBAcICChAAGEcY1gQYsAPiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp

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
(16) Google Search string: | split at space in python | https://www.google.com/search?q=split+at+space+in+python&rlz=1C1YTUH_enIE1084IE1084&oq=split+at+space+in+python&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMg0IAxAAGIYDGIAEGIoFMg0IBBAAGIYDGIAEGIoF0gEINjkxNGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
(17) Result: | Python String split() Method | W3Schools | https://www.w3schools.com/python/ref_string_split.asp
(18) Try It: | .split() | W3Schools | https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_split
(19) Google Search string: | Wikipedia | https://www.google.com/search?q=Wikipedia&rlz=1C1YTUH_enIE1084IE1084&oq=Wikipedia&gs_lcrp=EgZjaHJvbWUyDggAEEUYJxg5GIAEGIoFMgYIARAjGCcyBwgCEAAYgAQyBggDEEUYPDIGCAQQRRg8MgYIBRBFGDwyBggGEEUYQTIGCAcQBRhA0gEIMjc0M2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
(20) Wikipedia | home page | https://www.wikipedia.org/
(21) German Wikipedia article | Subject: Wikipedia | Language: German | https://de.wikipedia.org/wiki/Wikipedia
(22) German Wikipedia article | Subject: Wikipedia | Language: German | https://de.wikipedia.org/wiki/Wikipedia
(23) Site: Wikipedia | Subject: Wikipedia | Language: English | url: https://en.wikipedia.org/wiki/Wikipedia
(24) Site: Wikipedia | Subject: Wikipedia | Language: French | url: https://fr.wikipedia.org/wiki/Wikip%C3%A9dia
(25) Site: Wikipedia | Subject: Wikipedia | Language: German | url: https://de.wikipedia.org/wiki/Wikipedia
(26) Site: Wikipedia | Subject: Wikipedia | Language: Spanish | url: https://es.wikipedia.org/wiki/Wikipedia
(27) Site: Wikipedia | Subject: Wikipedia | Language: Italian | url: https://it.wikipedia.org/wiki/Wikipedia
(28) .replace() | w3schools | txt = "I like bananas"; x = txt.replace("bananas", "apples"); print(x) | https://www.w3schools.com/python/ref_string_replace.asp
(29) wireframe | Google Slides | https://docs.google.com/presentation/d/1VeGCvKP2BdCCTK8M-keXfscWV4U_7R38t5k2OwkeokI/edit?usp=sharing
(30) call python file from another
        https://www.google.com/search?q=how+to+call+from+another+python+file&rlz=1C1YTUH_enIE1084IE1084&oq=how+to+call+from+another+python+file&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yCAgCEAAYFhgeMggIAxAAGBYYHjINCAQQABiGAxiABBiKBTINCAUQABiGAxiABBiKBTINCAYQABiGAxiABBiKBTIGCAcQRRhA0gEINTkwM2owajeoAgCwAgA&sourceid=chrome&ie=UTF-8
        https://www.w3docs.com/snippets/python/how-can-i-make-one-python-file-run-another.html#:~:text=To%20run%20one%20Python%20file,function%20or%20the%20subprocess%20module.&text=This%20will%20execute%20the%20code,in%20the%20main.py%20file.&text=This%20will%20run%20the%20other.py%20script%20as%20a%20separate%20process.
     without exec
        https://www.google.com/search?q=how+to+call+from+another+python+file+without+exec+&newwindow=1&sca_esv=584750333&rlz=1C1YTUH_enIE1084IE1084&sxsrf=AM9HkKkaQTIdcLfA8TLoRF8KM8TmqmqxYA%3A1700707821659&ei=7b1eZc7wJ8CFhbIPr8-qkAo&ved=0ahUKEwiOm86sjtmCAxXAQkEAHa-nCqIQ4dUDCBA&oq=how+to+call+from+another+python+file+without+exec+&gs_lp=Egxnd3Mtd2l6LXNlcnAiMmhvdyB0byBjYWxsIGZyb20gYW5vdGhlciBweXRob24gZmlsZSB3aXRob3V0IGV4ZWMgMgUQIRigATIFECEYoAEyBRAhGKABMgUQIRigATIIECEYFhgeGB1I2LgCUKkGWL0bcAF4AZABAJgBZKABzgWqAQM5LjG4AQzIAQD4AQHCAgoQABhHGNYEGLADwgIGEAAYFhgewgILEAAYgAQYigUYhgPCAgcQIRigARgKwgIGECEYDRgV4gMEGAAgQYgGAZAGCA&sclient=gws-wiz-serp
        https://python-forum.io/thread-37119.html
     loads 1 file from another
Note:
Using python --version | Python 3.11.6
(31) index of or char At in python
        https://www.google.com/search?q=index+of+or+char+At+in+python&rlz=1C1YTUH_enIE1084IE1084&oq=index+of+or+char+At+in+python+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIICAEQABgWGB4yDQgCEAAYhgMYgAQYigUyDQgDEAAYhgMYgAQYigUyDQgEEAAYhgMYgAQYigXSAQg2MDE4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
     How to get char from string by index?
        https://stackoverflow.com/questions/8848294/how-to-get-char-from-string-by-index
    map python
        https://www.google.com/search?q=map+python&rlz=1C1YTUH_enIE1084IE1084&oq=map+python+&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDIMCAQQABhDGIAEGIoFMgcIBRAAGIAEMgcIBhAAGIAEMgYIBxBFGD3SAQgxOTE5ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
    Python map() function
        https://www.geeksforgeeks.org/python-map-function/
    ```python
    def addition(n):
        return n + n
    
    # We double all numbers using map()
    numbers = (1, 2, 3, 4)
    result = map(addition, numbers)
    ```
(32) dict append python
        https://www.google.com/search?q=dict+append+python&newwindow=1&sca_esv=584778317&rlz=1C1YTUH_enIE1084IE1084&sxsrf=AM9HkKlgSWIquaiH0eAG6RvtOg6AT1Haqg%3A1700714700245&ei=zNheZdvMDouBhbIP8Jy-oAE&ved=0ahUKEwjb4sn8p9mCAxWLQEEAHXCODxQQ4dUDCBA&uact=5&oq=dict+append+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiEmRpY3QgYXBwZW5kIHB5dGhvbjIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwAzIKEAAYRxjWBBiwA0jaB1CKB1iKB3ABeAGQAQCYAQCgAQCqAQC4AQPIAQD4AQHiAwQYACBBiAYBkAYI&sclient=gws-wiz-serp
        update()
        https://www.freecodecamp.org/news/add-to-dict-in-python/
(33) is it possible in python to call a function for each increment of a for loop? | https://www.google.com/search?q=is+it+possible+in+python+to+call+a+function+for+each+increment+of+a+for+loop%3F&rlz=1C1YTUH_enIE1084IE1084&oq=is+it+possible+in+python+to+call+a+function+for+each+increment+of+a+for+loop%3F&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQRRhA0gEJMTUzNzRqMWo3qAIAsAIA&sourceid=chrome&ie=UTF-8
        manual for loop | https://stackoverflow.com/questions/54714945/create-a-function-that-will-increment-by-one-when-called
    ```python
    def make_counter():
        count = -1
        def _():
            count += 1
            return count
        return _

    count_row = make_counter()

    Now count_row will return a new value on each call:
    >>> count_row()
    0
    >>> count_row()
    1
    ```
(34) nltk count words per language | https://www.google.com/search?q=nltk+count+words+per+lanugage&rlz=1C1YTUH_enIE1084IE1084&oq=nltk+count+words+per+lanugage&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKABMgkIAhAhGAoYoAHSAQg0OTEyajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
    real word count in NLTK | Removing Punctuation (with no regex) | https://stackoverflow.com/questions/10677020/real-word-count-in-nltk
(35) CS6361 Language Enginerring and Translation Technology
(36) Google Search string: | delete last git commit | https://www.google.com/search?q=delete+last+git+commit&rlz=1C1YTUH_enIE1084IE1084&oq=delete+last+git+commit&gs_lcrp=EgZjaHJvbWUyCQgAEEUYORiABDIHCAEQABiABDIHCAIQABiABDIICAMQABgWGB4yCAgEEAAYFhgeMggIBRAAGBYYHjIICAYQABgWGB4yDQgHEAAYChgWGB4Y8QQyCAgIEAAYFhgeMggICRAAGBYYHtIBCDUwMjJqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8
     Git delete last commit - GitHub Gist | https://gist.github.com/cutiko/0b1615c63504a940877541362cc51211#:~:text=To%20remove%20the%20last%20commit,remove%20the%20last%20two%20commits.
(37) len() | Getting Started With Python’s len() | https://realpython.com/len-python-function/#:~:text=The%20function%20len()%20is,with%20many%20different%20data%20types.
(38) W3Schools

for x in thisdict.values():
  print(x)

for x in thisdict.keys():
  print(x)

for x, y in thisdict.items():
  print(x, y)

    https://www.w3schools.com/python/python_dictionaries_loop.asp
(39) thisdict.items(): | Tryit Editor | https://www.w3schools.com/python/trypython.asp?filename=demo_dictionary_loop_items
"""


# LISTS
languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt'] # easyMode

# Choose a language file from the above list

# e.g. sourceEnglish.txt


# Switch to easy mode:
languageSource = 'sourceEnglish.txt'


languageDolch = 'English.txt'



# LANGUAGE NAMES
English = 'English'



# COUNTS
countEnglish = 0
countFrench = 0
countGerman = 0
countSpanish = 0
countItalian = 0


# outer loop:
fileSource = open(languageSource,"r", encoding="utf8")
for word_is_line_Source in fileSource:
    # print(word_is_line_Source)
    list_of_individual_words = word_is_line_Source.split(' ') 

    for wordSource in list_of_individual_words: # wordSource not reused
        # print(wordSource)
        # inner loop:
        for languageDolch in languageDolchs: # easyMode
            fileDolch = open('sourceEnglish.txt',"r", encoding = 'utf8')
            for line_Dolch in fileDolch:
                # print(line_Dolch) # print 4 working # prints words
                if word_is_line_Source == line_Dolch:
                    currentLanguage = 'English'
                    language_key_for_list = 'list' + currentLanguage
                    language_key_for_count = 'count' + currentLanguage
                    current_list = language_key_for_list

    # increment count of each language count for which the (word from sourceText) is present
                    if wordSource in 'English.txt':
                        countEnglish=countEnglish+1
                    if wordSource in line_Dolch:
                        countEnglish=countEnglish+1
                    if 'comme' in line_Dolch:
                        countFrench = countFrench+1

    # increment count


                    current_count_name = language_key_for_count # 0 to start off with
                    current_count=countEnglish
                    # add to count:
                    
                    # identifies language

                    current_count_name # =current_count+1

                    # next need TODO:
                    # make current_count variable

                    current_count = current_count+1



# decide which language the sourceText file is

print(type(countEnglish))



print("count of English dolch words is: ",countEnglish)

# decide which language the sourceText file is

# max checker

#  uncomment:


def maximum_checker(countEnglish,countFrench,countGerman,countSpanish,countItalian):
    maximum=countEnglish
    if countFrench>maximum:
        maximum=countFrench
    if countGerman>maximum:
        maximum=countGerman
    if countSpanish>maximum:
        maximum=countSpanish
    if countItalian>maximum:
        maximum=countItalian
    return maximum

languageOfArticle = maximum_checker(countEnglish,countFrench,countGerman,countSpanish,countItalian)
# print(languageOfArticle)
# print(countEnglish)

print("countFrench = ",countFrench)

if countEnglish > countFrench:
    print("count of English Dolch words is greater than count of French Dolch words.")
    print()
    print("The text is in English")
