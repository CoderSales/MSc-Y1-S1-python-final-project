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

dolch_files = {'1':'English.txt', '2':'French.txt', '3':'German.txt', '4':'Spanish.txt', '5':'Italian.txt'} # unused

for dolch_files_k_vs in (dolch_files.items()): # dict_keys(['1', '2', '3', '4', '5']) | Pre-Debugging ##################

    print('\n', 'iline 16, oline 1: | ', dolch_files_k_vs, sep='') # dict_keys(['1', '2', '3', '4', '5']) Pre-Debugging ##############################################

### Solution to current Debugging session:
# dolch_files.items()[1]
print('\n########################## new: | dolch_files.values(): | ', dolch_files.values(), '\n', sep='')


print('\nilines 20-23, olines 2-11: [[START]] #######################################################')
for k in dolch_files_k_vs:

    print('\n', 'iline 20, oline 2 4 6 8 10: | ',  'test', '\n' , sep='') # test | # Pre-Debugging ####################################################################################

    # English.txt French.txt German.txt Spanish.txt Italian.txt [[UNKNOWN]]
    print('iline 23, oline 3 5 7 9 11: | ', 'k:', k) # dict_values(['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']) #################################

print('\nilines 20-23, olines 2-11: [[END]] #######################################################')

languageSourceList = {'1':'sourceEnglish.txt', '2':'sourceFrench.txt', '3':'sourceGerman.txt', '4':'sourceSpanish.txt', '5':'sourceItalian.txt'} # unused
languageList = [English, French, German, Spanish, Italian]
countList = [countEnglish, countFrench, countGerman, countSpanish, countItalian]

for i, languageSource in enumerate(languageSourceList): # Bug: i contains stuff?

    print("\n", "iline 29, oline 2: i: ", i, sep = "") # Question: what does this return? # Answer: 0 #########################################

    print('\n', 'iline 31, ','oline 3: ', 'languageSource: ', languageSource, '\n', sep="") # languageSource: sourceEnglish.txt ###############
    
    ######################################################################################################################################################

    print('################################################# DEBUGGING STARTS HERE (SEE NEXT 3 LINES): v #######################################################' '\n\n', 'fileSource = open(languageSource,"r", encoding="utf8")', '\n\n', '^ ABOVE LINE PRODUCES | THE FOLLOWING TRACEBACK ERROR: v', '\n', sep='')
    
    fileSource = open(languageSource,"r", encoding="utf8") # Error ################################## # Cause: can't open 1, and languageSource=1
    
    #Traceback (most recent call last):
    #File "C:\Users\steph\OneDrive\Documents\45-semester-1\module-language-engineering\10-week-10-on\1-py-final-proj\MSc-Y1-S1-python-final-project\submission2\main2.py", line 24, in <module>
    #    fileSource = open(languageSource,"r", encoding="utf8")
    #                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    #FileNotFoundError: [Errno 2] No such file or directory: '1'
    

    print("fileSource object:",fileSource) # <_io.TextIOWrapper name='sourceEnglish.txt' mode='r' encoding='utf8'>
    for j, line_Source in enumerate(fileSource):
        # print("j: ", j) # 0
        print("line_Source: ", line_Source,"",sep="") # line 1
        break
        list_of_individual_words = line_Source.split(' ') 
        for wordSource in list_of_individual_words:
            for languageDolch in languageDolchs:
                for i in range(len(languageDolchs)):
                    fileDolch = open(languageSourceList[i],"r", encoding = 'utf8')
                    for line_Dolch in fileDolch:
                        if line_Source == line_Dolch:
                            currentLanguage = 'English'
                            language_key_for_list = 'list' + currentLanguage
                            language_key_for_count = 'count' + currentLanguage
                            current_list = language_key_for_list
                            for language in languageSourceList: # pair 1 # working
                                for count in countList: # and pair 1 # working
                                    if wordSource in language:
                                        countEnglish=countEnglish+1
                                    if wordSource in line_Dolch:
                                        countEnglish=countEnglish+1
                                    if 'comme' in line_Dolch:
                                        countFrench = countFrench+1
                                    current_count_name = language_key_for_count
                                    current_count=countEnglish
                                    current_count_name
                                    current_count = current_count+1
print("count of English dolch words is:",countEnglish) # end -3
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
print("countFrench = ",countFrench, sep="") # end -2
if countEnglish > countFrench:
    print("count of English Dolch words is greater than count of French Dolch words.")
    print("The text is in English")
print("test", sep="") # end -1
print() # end -0
