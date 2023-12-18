# Final project for 2023's 219114/115 Programming I
**Database**

| File                        |
|-----------------------------|
| Advisor_pending_request.csv |
| Member_pending_request.csv  |
| Login.csv                   |
| person.csv                  |
| project.csv                 |


**Database.py**
   - **CSV Class**
Reads a CSV file and returns its contents as a list of dictionaries.
Path to the CSV file is constructed using the current working directory.
   - **Database Class**
Represents a database that can store tables.
Provides methods to insert and search tables.
   - **Table Class**
Represents a table with various operations (join, filter, aggregate, select, etc.).
Supports insert operation to add entries to a list of dictionaries.

| Class | Method | Action                                                                                          |
|--|--|-------------------------------------------------------------------------------------------------|
| CSV Class | init | initializes the class. It sets the __location__ <br/>attribute to the current working directory. |
| CSV Class | read_csv | Reads a CSV file specified by csv_name and returns <br/>its contents as a list of dictionaries. |
| CSV Class | write_csv| Writes the contents of the table (a list of dictionaries) to a CSV file specified by csv_name.  |
| Database Class | init | Initializes the class with an empty list called database.                                       |
| Database Class | insert | Inserts a table (an instance of the Table class) into the database list.                        |
| Database Class | search | Searches for a table in the database by its name and returns it if found, otherwise returns None. |
| Table Class | __init__ | Initializes the class with a name (table_name) and initial data (table), which is a list of dictionaries. |
| Table Class | join | Performs an inner join with another table (other_table) based on a common key. Returns a new Table instance. |
| Table Class | filter | Filters the table based on a given condition function and returns a new Table instance.         |
| Table Class | aggregate | Aggregates data in the table using a specified aggregation function on a aggregation_key.       |
| Table Class | select | Selects specific attributes from the table and returns a new list of dictionaries.              |
| Table Class | __str__ | Returns a string representation of the table, including its name and data.                                                                                                |
| Table Class | insert |  Appends a new row (dictionary) to the table.                                                                                                |
| Table Class | update_row | Updates a specific row in the table based on primary key conditions.                                                                                                |


   
3. **project_manage.py**
   - **Student Class**
Represents a student with specific actions like creating projects, checking inbox, viewing and responding to invitations.
    - **Lead Class**
Inherits from the Student class and adds lead-specific actions like sending invitations, adding/removing members, and modifying projects.
    - **Member Class**
Represents a member with actions like seeing projects and modifying projects.
    - **Advisor Class**
Represents an advisor with actions like managing requests, viewing all projects, approving projects, and commenting on projects.
    - **Admin Class**
Represents an admin with actions like managing the database, editing, and deleting projects.
    - **Faculty Class**
Represents a faculty member with actions like viewing supervisor requests, managing requests, viewing all projects, and commenting on projects.
    - **Initializing Function**
Initializes the database with tables by reading CSV files.
    - **Login_base Function**
Handles user login, takes a username and password, and returns user information if valid.
    - **Write_csv Function**
Writes the modified tables back to CSV files.
    - **Exit Function**
Calls write_csv and prints a message on program exit.
    - **Main Function**
Calls the run method of the user based on their role.
    - **Main Block**
Calls initializing, login_base, and sets up the user based on the role returned from login_base.
Calls main function.
Calls exit function on program completion

| Class | Method | Action | Role |
|--|--|--------|---------|

