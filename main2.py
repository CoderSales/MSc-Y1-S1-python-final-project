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
