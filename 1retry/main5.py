from forDolch import language

languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']

makingDictionaryOfWordsPerLanguage = {
    'English': {'listEnglish' : [], 'countEnglish' : 0},
    'French':  {'listFrench' :  [], 'countFrench' : 0},
    'German' : {'listGerman' : [], 'countGerman' : 0},
    'Spanish' : {'listSpanish' : [], 'countSpanish' : 0},
    'Italian' : {'listItalian' : [], 'countItalian' : 0}
}

def strip_line_breaks(word):
    for word in file:
    if '\n' in word:
        word=word.replace("\n", "")
        return word


def compare_words_and_if_match_return_English_language(wordDolch, word, file_name_dolch):
    """
    3 Parameters:

    wordDolch : is the current Dolch word
    word : is the current word from the sourceTextWiki file
    file_name_dolch : gets .txt extension stripped to give English (the language (to be used later for counting English words) )
    """
    if wordDolch == word: # words from file
        lang = file_name_dolch.rstrip('.txt')
        print(lang)
        return lang


def drive_single_dolch_file(languageDolchs):
    """
    
    """
    for language in languageDolchs:
        single_dolch_file(language)

def single_dolch_file(language):
    """
    takes input: language list
    output: one Dolch language list
    """
    for language in languageDolchs:
        # do something:

        return language


def file_reader(file, read="r", encoding="utf8"):
    """
    takes a file
    uses open()
        - with parameters:
            1. file
            2. "r" # for read
            3. encoding="utf8" # kwarg specifying to use unicode encoding (for characters like a with an accent acute and other non ASCII characters)
    Q/ Possibly only need to specify file at runtime?

    returns something
    what is variable? (returned)
    """
    variable=open(file, read, encoding)
    return variable



def dolchinator( all_the_dolch_words ):
    """
    outputs a single dolch word
    """
    for dolch in all_the_dolch_words:
        return dolch


languageSources = ['sourceEnglish.txt', 'sourceFrench.txt', 'sourceGerman.txt', 'sourceSpanish.txt', 'sourceItalian.txt']

# outer loop:


for languageSource in languageSources: 
    fileSource = open(languageSource,"r", encoding="utf8")
    for word_is_line_Source in fileSource:
        list_of_individual_words = word_is_line_Source.split(' ') 

        for wordSource in list_of_individual_words:

            # inner loop:
            for languageDolch in languageDolchs:
                fileDolch = open(languageDolch,"r")
                for word_per_line_Dolch in fileDolch:
                    # print(word_per_line_Dolch) # comment out word print as too many # working print 1
                    print(word_per_line_Dolch) # print 4 working # prints words
                    if word_is_line_Source == word_per_line_Dolch:
                        currentLanguage = languageSource[6:languageSource.find(".")]
                        language_key_for_list = 'list' + currentLanguage
                        language_key_for_count = 'count' + currentLanguage
                        current_list = makingDictionaryOfWordsPerLanguage[currentLanguage][language_key_for_list]
                        
                        current_count = makingDictionaryOfWordsPerLanguage[currentLanguage][language_key_for_count] # 0 to start off with
                        
                        # append to list:
                        current_list.append(wordSource) # appendwhat?: append wordSource
                        # add to count:
                        current_count=current_count+1

a = makingDictionaryOfWordsPerLanguage["English"]['countEnglish']
b = makingDictionaryOfWordsPerLanguage["French"]["countFrench"]
c = makingDictionaryOfWordsPerLanguage["German"]["countGerman"]
d = makingDictionaryOfWordsPerLanguage["Spanish"]["countSpanish"]
e = makingDictionaryOfWordsPerLanguage["Italian"]["countItalian"]

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

languageOfArticle = maximum_checker(a,b,c,d,e)
print(languageOfArticle)
