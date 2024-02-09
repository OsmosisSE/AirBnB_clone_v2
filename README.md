# 0x00. AirBnB clone - The console
## Description
This project is a command-line interface (CLI) implementation of an AirBnB clone. It allows users to interact with objects such as Users, Places, Cities, States, and more, similar to the functionality of the AirBnB website.

## Command Interpreter
The command interpreter provides a command-line interface for interacting with the AirBnB objects. Here's how to get started with the command interpreter:

### How to Start
To start the command interpreter, run the `console.py` script located in the project directory.

```bash
$ ./console.py
```

### How to Use
#### Once the command interpreter is started, you can use the following commands:

* help: Display the list of available commands.
* create <class_name>: Create a new instance of the specified class.
* show <class_name> <object_id>: Show details of the specified object.
* destroy <class_name> <object_id>: Delete the specified object.
* all <class_name>: Display details of all objects of the specified class.
* update <class_name> <object_id> <attribute_name> "<attribute_value>": Update the specified attribute of the object.
* quit: Exit the command interpreter.

### Examples
#### Here are some examples of using the command interpreter:
```bash
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create User
45e6fa10-0bc1-44b1-9405-1d051e3e9efc
(hbnb) show User 45e6fa10-0bc1-44b1-9405-1d051e3e9efc
[User] (45e6fa10-0bc1-44b1-9405-1d051e3e9efc) {'created_at': datetime.datetime(2024, 2, 7, 10, 30, 0, 123456), 'updated_at': datetime.datetime(2024, 2, 7, 10, 30, 0, 123456)}
(hbnb) quit
$
```

