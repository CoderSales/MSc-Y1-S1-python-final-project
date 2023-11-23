languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']
languageSources = ['sourceEnglish.txt', 'sourceFrench.txt', 'sourceGerman.txt', 'sourceSpanish.txt', 'sourceItalian.txt']

English = 'English'
French = 'French'
German = 'German'
Spanish = 'Spanish'
Italian = 'Italian'

countEnglish = 0
countFrench = 0
countGerman = 0
countSpanish = 0
countItalian = 0


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
                        current_list = language_key_for_list
                        
                        current_count = language_key_for_count # 0 to start off with
                        
                        # add to count:
                        current_count=current_count+1

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
print(languageOfArticle)
