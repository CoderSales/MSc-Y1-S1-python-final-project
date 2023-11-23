from open-holder import opener

def list_of_Dolchs():
    dolchs = ['English.txt', 'French.txt', 'German.txt', 'Spanish.txt', 'Italian.txt']
    for dolch_file_name in dolchs:
        opened = opener(dolch_file_name)
        return dict_with_file_objects_for_each_Dolch
