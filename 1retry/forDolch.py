def languageSourcesTo_wordSource(languageSources):
    # outer loop:
    for languageSource in languageSources: 
        fileSource = open(languageSource,"r", encoding="utf8")
        for word_is_line_Source in fileSource:
            list_of_individual_words = word_is_line_Source.split(' ') 

            for wordSource in list_of_individual_words:
                