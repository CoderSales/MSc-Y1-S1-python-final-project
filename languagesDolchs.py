from open_holder import opener

def list_of_Dolchs():
    dolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']
    for dolch_file_name in dolchs:
        opened = opener(dolch_file_name)
        dict_object_dolchs.update(opened)
    return dict_object_dolchs
