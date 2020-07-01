<p align="center">
<img src="https://lh3.googleusercontent.com/KegDzq2bU0WZjp9yJAgIrOLR9j0J4rQhD3VERnQBJ0lD8P4fy6929ZmX4LkeQ715_wYtkA7b1ziN10WrSB6TJPu2NNOrojbk2i8PhWHhgVwMPj_LtVc4mBsSksfdjbzB2kSAyVRsA-uyf3cjl7enuv_OrOa2yEDZLfzDt-VyhLKZqqxTTKO14A1wR3kE8hC_y12s36_3rgy0V7jImfo1Q85Z693bcRGUnNLeLwyryk4WbfZygMckXDyckkZdRm8dPC_ni0zhFu7i7NPL3SfmZdqwmoHiimaBQ0ZlIcnnOlOkvgPIywtEUBZCIF3l-V9ypwfU4Z9QBGWvl9edIi0c_OQRCYBA1JPUb4jCjx943vzCHFlLTZQS6xEOhqoiMMWh08kCJG7S3e62c-gYekeJ0IaCNzAmlx6-NbdOScI-jVOVukjB13LsXlvQsCaK6Juhj7RBZZvnFvWBbIELIJ59ksnL9hv23FENq5JRqOvxmdQPPDe0yB09xhOUuzH0n7u98ekXvalJhk62OI6iWZug832nBMwaISFhPAGGeX0urnXdmLkZMQLaQaDLEKaT88dFNkZPXlTrJKPOu26L2DwVbhPwVNaSgSfS8qFpxrMljUy851IgqSLbPdt6NJZvXMBRP08ltakEnVelp5oRGiB7BI8dJmoabkkUK3dIETvyNEWZnaHe8CWYUq22Nh6LNA=w1921-h812-no?authuser=0">
</p>

<h1 align="center"> Airbnb clone v1.0 </h1>

### Description 📝

This project is the first of four version of an Airbnb web application clone. This version work only from console using cmd python module. Was built with OOP so you can `create, show, all, update, destroy` Users or City objects among others.

### Usage 💻

#### Install

    $ git clone https://github.com/Manga08/AirBnB_clone

#### Execute

##### Interactive mode: <br />

Console shows prompt and wait for user type a command, interpretes and run input command and display prompt again. You can exit wiht **quit** command, **CTRL+C**, **CTRL+D** or **EOF**

```bash
$ ./console.py
(hbnb) create User
610ab350-2a74-4dca-bef4-a7584ea3328f
(hbnb) quit
```

##### Non-interactive mode: <br />

Shell interpretes and execute a command piped to its stdin. After execution, the prompt are not displayed neither waits for another user command input.

```bash
$ echo "create User" | ./console.py
(hbnb)
610ab350-2a74-4dca-bef4-a7584ea3328f
(hbnb)
$
```

##### Classes

- BaseModel
- User
- City
- State
- Amenity
- Place
- Review

##### Commands usage:

##### `create <class>`

```bash
(hbnh) create User
610ab350-2a74-4dca-bef4-a7584ea3328f
(hbnh)
------------------------------------
$ echo "create User" | ./console.py
(hbnb)
610ab350-2a74-4dca-bef4-a7584ea3328f
(hbnb)
$
```

##### show

```bash
(hbnh) show User 610ab350-2a74-4dca-bef4-a7584ea3328f
[User] (610ab350-2a74-4dca-bef4-a7584ea3328f) {'id': '610ab350-2a74-4dca-bef4-a7584ea3328f', 'created_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687603), 'updated_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687626)}
(hbnb)
------------------------------------
$ echo "show User 610ab350-2a74-4dca-bef4-a7584ea3328f" | ./console.py
(hbnb)
[User] (610ab350-2a74-4dca-bef4-a7584ea3328f) {'id': '610ab350-2a74-4dca-bef4-a7584ea3328f', 'created_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687603), 'updated_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687626)}
(hbnb)
$
```

##### all

```bash
(hbnh) all
["[User] (610ab350-2a74-4dca-bef4-a7584ea3328f) {'id': '610ab350-2a74-4dca-bef4-a7584ea3328f', 'created_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687603), 'updated_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687626)}"]
(hbnh)
------------------------------------
$ echo "all" | ./console.py
(hbnb)
["[User] (610ab350-2a74-4dca-bef4-a7584ea3328f) {'id': '610ab350-2a74-4dca-bef4-a7584ea3328f', 'created_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687603), 'updated_at': datetime.datetime(2020, 7, 1, 20, 21, 7, 687626)}"]
(hbnb)
$
```

##### update

```bash
(hbnh) update BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnh)
------------------------------------
$ echo "update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"" | ./console.py
(hbnb)
(hbnb)
$
```

##### destroy

```bash
(hbnh) destroy City 9faff9a-6318-451f-87b6-910505c55907
(hbnh)
------------------------------------
$ echo "destroy City 9faff9a-6318-451f-87b6-910505c55907" | ./console.py
(hbnb)
(hbnb)
$
```

##### count

```bash
(hbnh) count State
3
(hbnh)
------------------------------------
$ echo "count State" | ./console.py
(hbnb)
3
(hbnb)
$
```

##### help

```bash
(hbnh) help
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
------------------------------------
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
(hbnb)
$
```

```bash
(hbnh) help all
Prints all string representation of all instances
(hbnb)
------------------------------------
$ echo "help all" | ./console.py
(hbnb)
Prints all string representation of all instances
(hbnb)
$
```

### Project files

| **File**                                                                     | **Description**                                                                |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [AUTHORS](./AUTHORS)                                                         | Contains info about authors of the project                                     |
| [base_model.py](./models/base_model.py)                                      | Defines BaseModel class (parent class), and methods                            |
| [user.py](./models/user.py)                                                  | Defines subclass User                                                          |
| [amenity.py](./models/amenity.py)                                            | Defines subclass Amenity                                                       |
| [city.py](./models/city.py)                                                  | Subclass City                                                                  |
| [place.py](./models/place.py)                                                | Subclass Place                                                                 |
| [review.py](./models/review.py)                                              | Subclass Review                                                                |
| [state.py](./models/state.py)                                                | Subclass State                                                                 |
| [file_storage.py](./models/engine/file_storage.py)                           | Serializes and deserializes data to json                                       |
| [console.py](./console.py)                                                   | creates object, show object, destory objects, and updates attributes of object |
| [test_base_model.py](./tests/test_models/test_base_model.py)                 | unittests for base_model                                                       |
| [test_user.py](./tests/test_models/test_user.py)                             | unittests for user                                                             |
| [test_amenity.py](./tests/test_models/test_amenity.py)                       | unittests for amenity                                                          |
| [test_city.py](./tests/test_models/test_city.py)                             | unittests for city                                                             |
| [test_place.py](./tests/test_models/test_place.py)                           | unittests for place                                                            |
| [test_review.py](./tests/test_models/test_review.py)                         | unittests for review                                                           |
| [test_state.py](./tests/test_models/test_state.py)                           | unittests for state                                                            |
| [test_file_storage.py](./tests/test_models/test_engine/test_file_storage.py) | unittests for file_storage                                                     |
| [test_console.py](./tests/test_console.py)                                   | unittests for console                                                          |

### Built with 🛠

Python3, knowledge about how to use a command line interpreter, Ubuntu 14.04, python3 and pep8 style corrector.

#### Authors

David Gonzalez - [@davidgonzalezfx](https://github.com/davidgonzalezfx)<br>
Manuel Acero - [@Manga08](https://github.com/Manga08)
