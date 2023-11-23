# LISTS

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
    print(word_is_line_Source)
    list_of_individual_words = word_is_line_Source.split(' ') 

    for wordSource in list_of_individual_words: # wordSource not reused
        print(wordSource)
        # inner loop:
        fileDolch = open('sourceEnglishEasy.txt',"r", encoding = 'utf8')
        for line_Dolch in fileDolch:
            # print(line_Dolch) # print 4 working # prints words
            if word_is_line_Source == line_Dolch:
                currentLanguage = 'English'
                language_key_for_list = 'list' + currentLanguage
                language_key_for_count = 'count' + currentLanguage
                current_list = language_key_for_list

# increment count of each language count for which the (word from sourceText) is present
                if wordSource in 'EnglishEasy.txt':
                    countEnglish=countEnglish+1


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



print(countEnglish)
