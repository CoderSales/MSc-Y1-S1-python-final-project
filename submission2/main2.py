languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']
languageSourceList = ['sourceEnglish.txt', 'sourceFrench.txt', 'sourceGerman.txt', 'sourceSpanish.txt', 'sourceItalian.txt']
languageSource = 'sourceEnglish.txt'
English = 'English'
French = 'French'
German = 'German'
Spanish = 'Spanish'
Italian = 'Italian'
languageList = [English, French, German, Spanish, Italian]
countEnglish = 0
countFrench = 0
countGerman = 0
countSpanish = 0
countItalian = 0
for languageSource in languageSourceList:
    fileSource = open(languageSource,"r", encoding="utf8")
    for word_is_line_Source in fileSource:
        list_of_individual_words = word_is_line_Source.split(' ') 
        for wordSource in list_of_individual_words:
            for languageDolch in languageDolchs:
                fileDolch = open('sourceEnglish.txt',"r", encoding = 'utf8')
                for line_Dolch in fileDolch:
                    if word_is_line_Source == line_Dolch:
                        currentLanguage = 'English'
                        language_key_for_list = 'list' + currentLanguage
                        language_key_for_count = 'count' + currentLanguage
                        current_list = language_key_for_list
                        if wordSource in 'English.txt':
                            countEnglish=countEnglish+1
                        if wordSource in line_Dolch:
                            countEnglish=countEnglish+1
                        if 'comme' in line_Dolch:
                            countFrench = countFrench+1
                        current_count_name = language_key_for_count
                        current_count=countEnglish
                        current_count_name
                        current_count = current_count+1
print("count of English dolch words is: ",countEnglish)
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
print("countFrench = ",countFrench)
if countEnglish > countFrench:
    print("count of English Dolch words is greater than count of French Dolch words.")
    print("The text is in English")
