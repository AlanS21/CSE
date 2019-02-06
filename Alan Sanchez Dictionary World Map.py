world_map = {
    'NODE_1': {
        'NAME': "UNITED STATES OF AMERICA ",
        'DESCRIPTION': "Hello and Welcome to the USA.",
        'PATHS': {
          'NORTH': "NODE_2",
          'SOUTH': "NODE_3"
        }
    },
    'NODE_2': {
        'NAME': "CANADA",
        'DESCRIPTION': "Hello and welcome to the Canada ",
        'PATHS': {
          'SOUTH': 'NODE_1'
        }
    },
    'NODE_3': {
        'NAME': "MEXICO",
        'DESCRIPTION': "Hola bienvenido a Mexico ",
        'PATHS': {
          'SOUTH': 'NODE_1'
          'NORTH' 'NODE_1'
        }
    },
    'NODE_4': {
        'NAME': "NICARAGUA",
        'DESCRIPTION': " ",
        'PATHS': {
          'SOUTH': 'NODE_1'
        }
    },





}

directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
current_node = world_map["NODE_1"]


playing = True
while playing:
    print(current_node['NAME'])

    command = input(">_")
    if command in ['q', 'quit', 'exit']:
        playing = False
    elif command in directions:
        try:
            room_name = current_node["PATHS"][command]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way.")
    else:
        print("Command not recognized.")
