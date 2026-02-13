# Python - Input/Output  
**Holberton School - Higher Level Programming**

This directory contains my completed tasks for the **0x0B. Python - Input/Output** project.

All scripts are written in Python 3.8.5, follow pycodestyle (2.7.*), are executable, and have been tested on Ubuntu 20.04 LTS.

## Files

| #  | File                      | Description                                                                                   |
|----|---------------------------|-----------------------------------------------------------------------------------------------|
| 0  | `0-read_file.py`          | Function `read_file` that reads a text file (UTF8) and prints it to stdout.                   |
| 1  | `1-write_file.py`         | Function `write_file` that writes a string to a text file (UTF8) and returns the number of characters written. |
| 2  | `2-append_write.py`       | Function `append_write` that appends a string at the end of a text file (UTF8) and returns the number of characters added. |
| 3  | `3-to_json_string.py`     | Function `to_json_string` that returns the JSON representation of an object (string).        |
| 4  | `4-from_json_string.py`   | Function `from_json_string` that returns an object (Python data structure) represented by a JSON string. |
| 5  | `5-save_to_json_file.py`  | Function `save_to_json_file` that writes an Object to a text file using JSON representation. |
| 6  | `6-load_from_json_file.py`| Function `load_from_json_file` that creates an Object from a “JSON file”.                    |
| 7  | `7-add_item.py`           | Script that adds all command-line arguments to a Python list and saves them to `add_item.json`. |
| 8  | `8-class_to_json.py`      | Function `class_to_json` that returns the dictionary description for JSON serialization of an object (works with simple data structures). |
| 9  | `9-student.py`            | Class `Student` with public attributes `first_name`, `last_name`, `age` and method `to_json()`. |
|10  | `10-student.py`           | Class `Student` (inherits from task 9) with `to_json(attrs=None)` that retrieves a dictionary representation filtered by a list of attributes if provided. |
|11  | `11-student.py`           | Class `Student` (inherits from task 10) with `reload_from_json(json)` that replaces all attributes of the Student instance from a dictionary. |
|12  | `12-pascal_triangle.py`   | Technical interview preparation: function `pascal_triangle(n)` that returns a list of lists of integers representing Pascal’s triangle of `n`. |
|100| `100-append_after.py`     | Function `append_after` that inserts a line of text after each line containing a specific string. |
|101| `101-stats.py`            | Script that reads stdin line by line and computes metrics (file size and HTTP status code counts) — log parsing exercise. |

## Usage

All Python scripts can be executed directly:

```bash
./0-read_file.py my_file.txt
python3 7-add_item.py "item1" "item2" "item3"
