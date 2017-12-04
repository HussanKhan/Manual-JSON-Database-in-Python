import json

def read_json(name):
    try:
        with open(name, 'r') as load_file:
            data = json.load(load_file)
        return data
    except FileNotFoundError:
        print('Filename must be case matched, File not found.')

def create_database(name,**kwargs):
    database = {name:[kwargs]}
    with open(name, 'w') as new_file:
        json.dump(database, new_file)

def show_database(name):
    data = read_json(name)
    for thing in data[name]:
        print(thing)

def append_json(name):
    quit_condition = 'on'
    new_list = {}
    for key, value in empty_list.items():
        new_list[key] = input(key + ": ")
        if new_list[key].lower() == 'q':
            quit_condition = 'q'
            break
    if quit_condition == 'q':
        return 'q'
    data = read_json(name)

    data[name].append(new_list)

    with open(name, 'w') as new_file:
        json.dump(data, new_file)
        new_file.close()

def remove_entry(name):
    index_database(name)
    number = input("\nWhich entry would you like to remove?: ")
    try:
        remove_dict = index_dict[int(number)]

        data = read_json(name)

        data_index = data[name].index(remove_dict)

        del data[name][data_index]

        with open(name, "w") as write_data:
            json.dump(data, write_data)
            write_data.close()

        print("\nEntry Removed: " + str(remove_dict))
        print('\nCurrent Logs')
        index_database(name)
    except KeyError:
        print('Entry not found')

def index_database(name):
    data = read_json(name)
    try:
        i = 0
        for thing in data[name]:
            i += 1
            index_dict[i] = thing

        for key, value in index_dict.items():
            print("\n" + str(key) + ". " + str(value))
    except TypeError:
        pass

def json_dict_creation():
    x = 0
    while x < 1:
        quit_list = ['q','Q']
        key = input("\nEnter Name of Category: ")
        if key in quit_list:
            x += 1
            break
        value = input(key+": ")
        if value in quit_list:
            x += 1
            break
        else:
            data_values[key] = value

def empty_value_container():
    for key, value in data_values.items():
        empty_list[key] = ""

def append_loaded_json(name):
    new_list = {}

    data = read_json(name)

    try:
        for key, value in data[name][0].items():
            new_list[key] = input(key + ": ")

        data = read_json(name)

        data[name].append(new_list)

        with open(name, 'w') as new_file:
            json.dump(data, new_file)
            new_file.close()
    except TypeError:
        pass

print('Welcome to Manual JSON Database in Python')

while True:

    index_dict = {}
    data_values = {}
    empty_list = {}

    print('\nPress: C = create new json database, L = to load/view current json database, R = to remove an entry, A = Append a JSON file, Q = to quit program')
    selection = input('\n: ')

    if selection.lower() == 'c':
        name = input('\nDatabase name (without .json): ')

        name = str(name)+".json"

        print('\nUse q to stop adding keys')

        json_dict_creation()

        empty_value_container()

        print("\n" + str(empty_list))

        create_database(name,**data_values)

        show_database(name)

        print('\nContinue adding to created JSON dictionary | Press Q to quit')
        while True:
            append_json(name)
            info = append_json(name)
            if info == 'q':
                break
            show_database(name)
    elif selection.lower() == 'l':
        name = input('\nDatabase name (without .json): ')
        name = str(name)+".json"
        index_database(name)

    elif selection.lower() == 'a':
        name = input('\nDatabase name (without .json): ')
        name = str(name)+".json"
        print('\nAppend Loaded JSON File Named: ' + str(name))
        append_loaded_json(name)

    elif selection.lower() == 'r':
        name = input('\nDatabase name (without .json): ')
        name = str(name)+".json"
        remove_entry(name)

    else:
        break
