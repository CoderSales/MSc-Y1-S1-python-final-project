from languagesDolchs import list_of_Dolchs

def looper_through_dolchs(one_specified_language_dolch_object):
    """
    should this parameter be a name of same?
    """

    saved_list_of_dolchs = use list_of_Dolchs()

    # loop (del comment)
    if one_specified_language_dolch_object in saved_list_of_dolchs:
        # hmmm ... how can we 
        # not just always return the first one
        # in the for loop?
        # should this be an
        # if statement instead?
        # with a map?
        return one_specified_language_dolch_object
