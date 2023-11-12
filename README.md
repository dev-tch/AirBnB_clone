![logo project Hbnb.](https://github.com/dev-tch/AirBnB_clone/blob/main/pictures/hbnb_logo.png)


## Background Context
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

## Execution
Your shell should work like this in interactive mode:
````
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
````
But also in non-interactive mode: (like the Shell project in C)
````
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
````
### Supported commands
1. quit: to exit the program
   > Usage: ``quit `` 
   ```
   vagrant@ubuntu-focal:~/.../AirBnB_clone$ ./console.py
   (hbnb) quit
   vagrant@ubuntu-focal:~/.../AirBnB_clone$
   ```
3. help: to show supported commands or info about specific command
   > Usage: `` help or help <command name> `` 
   ````
   vagrant@ubuntu-focal:~/.../AirBnB_clone$ ./console.py
   (hbnb) help

   Documented commands (type help <topic>):
   ========================================
   EOF  all  count  create  destroy  help  quit  show  update

   (hbnb) help all
   Print all string representation of all instances
   (hbnb)
4. create <class name> : create new instance object of type class name
    > Usage: `` create <class name> `` 
   ````
   (hbnb) create BaseModel
   14d44bea-45c5-4799-b8a0-6a81969e80bd
   (hbnb)
   ````
   
5. show 'class name' 'id' : Prints the string representation of an instance based on the class name and id
    > Usage: `` show <class name> <id> `` 
   ````
   (hbnb) show BaseModel 14d44bea-45c5-4799-b8a0-6a81969e80bd
   [BaseModel] (14d44bea-45c5-4799-b8a0-6a81969e80bd) {'id': '14d44bea-45c5-4799-b8a0-6a81969e80bd', 'created_at': datetime.datetime(2023, 11, 12, 23, 2, 4, 680825), 'updated_at': datetime.datetime(2023, 11, 12, 23, 2, 4,    680846)}
   (hbnb)
   ````
6. destroy: Deletes an instance based on the class name and id
   > Usage: `` destroy <class name> <id> `` 
   ````
   (hbnb) destroy BaseModel 14d44bea-45c5-4799-b8a0-6a81969e80bd
   (hbnb)
   ````
7. all: Prints all string representation of all instances based or not on the class name
   > Usage: `` all or  all <class name> `` 
   ```
   (hbnb) all
   ["[BaseModel] (bf9194b3-6cbb-4401-a686-c9c6bdae0ae4) {'id': 'bf9194b3-6cbb-4401-a686-c9c6bdae0ae4', 'created_at': datetime.datetime(2023, 11, 12, 17, 7, 4, 432550), 'updated_at': datetime.datetime(2023, 11, 12, 17,       7, 4, 432678), 'name': 'My First Model', 'my_number': 89}", "[User] (df12dc43-0902-462d-8ef8-da9b0698a4c0) {'id': 'df12dc43-0902-462d-8ef8-da9b0698a4c0', 'created_at': datetime.datetime(2023, 11, 12, 23, 15, 4,         263378), 'updated_at': datetime.datetime(2023, 11, 12, 23, 15, 4, 263399)}", "[BaseModel] (ebd30f7e-ecf9-422f-bd4d-25e5c5c0e9d4) {'id': 'ebd30f7e-ecf9-422f-bd4d-25e5c5c0e9d4', 'created_at': datetime.datetime(2023,       11, 12, 23, 15, 21, 575863), 'updated_at': datetime.datetime(2023, 11, 12, 23, 15, 21, 575886)}"]
   (hbnb) all User
   ["[User] (df12dc43-0902-462d-8ef8-da9b0698a4c0) {'id': 'df12dc43-0902-462d-8ef8-da9b0698a4c0', 'created_at': datetime.datetime(2023, 11, 12, 23, 15, 4, 263378), 'updated_at': datetime.datetime(2023, 11, 12, 23, 15,       4, 263399)}"]
   (hbnb)
   ```
8. update :  Updates an instance based on the class name and id by adding or updating attribute
   > Usage: ``update <class name> <id> <attribute name> "<attribute value>" ``
   ````
   (hbnb) update User df12dc43-0902-462d-8ef8-da9b0698a4c0  first_name "tijani"
   (hbnb) all User
   ["[User] (df12dc43-0902-462d-8ef8-da9b0698a4c0) {'id': 'df12dc43-0902-462d-8ef8-da9b0698a4c0', 'created_at': datetime.datetime(2023, 11, 12, 23, 15, 4, 263378), 'updated_at': datetime.datetime(2023, 11, 12, 23, 53, 23, 19802), 'first_name': 'tijani'}"]
   (hbnb)
   ````

