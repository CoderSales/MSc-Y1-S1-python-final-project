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


"""

languageDolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']

makingDictionaryOfWordsPerLanguage = {
    'English': {'listEnglish' : [], countEnglish = 0}

listFrench = []
countFrench = 0

listGerman = []
countGerman = 0

listSpanish = []
countSpanish = 0

listItalian = []
countItalian = 0

languageSources = ['sourceEnglish.txt', 'sourceFrench.txt', 'sourceGerman.txt', 'sourceSpanish.txt', 'sourceItalian.txt']

# outer loop:
for languageSource in languageSources: 
    fileSource = open(languageSource,"r")
    for lineSource in fileSource:
        for wordSource in lineSource:
            #if wordSource in lineSource:
                # do something
                # pass

            # (from last line): for every word in each line of the source text for a given language:
            # (now, look at next bit of code): go through each word in all 5 language dolch word lists (really inefficient, I know):

            # inner loop:
            for languageDolch in languageDolchs:
                fileDolch = open(languageDolch,"r")
                for lineDolch in fileDolch:
                    for wordDolch in lineDolch:

                        # and finally,
                        # if the current word of the current language Source text
                        # is also present in the ____other_thing____variable____
                        # of the dolch word list for the current language
                        # is 

                        if wordSource == wordDolch:
                            # get lang
                            currentLanguage=languageSource.slice[6:]
                            
                            # get both list and count
                            # append to list
                            # add to count
                            pass

# get word




