# Final project for 2023's 219114/115 Programming I
1. **Database**
   - **Advisor_pending_request.csv**
   - **Member_pending_request.csv**
   - **login.csv**
   - **person.csv**
   - **project.csv**

2. **Database.py**
   - **CSV Class**
Reads a CSV file and returns its contents as a list of dictionaries.
Path to the CSV file is constructed using the current working directory.
    - **Database Class**
Represents a database that can store tables.
Provides methods to insert and search tables.
    - **Table Class**
Represents a table with various operations (join, filter, aggregate, select, etc.).
Supports insert operation to add entries to a list of dictionaries.
   
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