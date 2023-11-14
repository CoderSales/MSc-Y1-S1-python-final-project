languages = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']

listEnglish = []
countEnglish = 0

for language in languages: 
    file = open(language,"r")
        for line in file:
            if word in line:
                # do something
                pass
