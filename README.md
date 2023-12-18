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

| Class          | Method     | Action                                                                                                       | Completion Percentage |
|----------------|------------|--------------------------------------------------------------------------------------------------------------|-----------------------|
| CSV Class      | init       | initializes the class. It sets the __location__ <br/>attribute to the current working directory.             | **100%**              |
| CSV Class      | read_csv   | Reads a CSV file specified by csv_name and returns <br/>its contents as a list of dictionaries.              | **100%**              |
| CSV Class      | write_csv  | Writes the contents of the table (a list of dictionaries) to a CSV file specified by csv_name.               | **100%**              |
| Database Class | init       | Initializes the class with an empty list called database.                                                    | **100%**              |
| Database Class | insert     | Inserts a table (an instance of the Table class) into the database list.                                     | **100%**              |
| Database Class | search     | Searches for a table in the database by its name and returns it if found, otherwise returns None.            | **100%**              |
| Table Class    | __init__   | Initializes the class with a name (table_name) and initial data (table), which is a list of dictionaries.    | **100%**              |
| Table Class    | join       | Performs an inner join with another table (other_table) based on a common key. Returns a new Table instance. | **100%**              |
| Table Class    | filter     | Filters the table based on a given condition function and returns a new Table instance.                      | **100%**              |
| Table Class    | aggregate  | Aggregates data in the table using a specified aggregation function on a aggregation_key.                    | **100%**              |
| Table Class    | select     | Selects specific attributes from the table and returns a new list of dictionaries.                           | **100%**              |
| Table Class    | __str__    | Returns a string representation of the table, including its name and data.                                   | **100%**              |                               
| Table Class    | insert     | Appends a new row (dictionary) to the table.                                                                 | **100%**              |                                    
| Table Class    | update_row | Updates a specific row in the table based on primary key conditions.                                         | **100%**              |                                                                   

**project_manage.py**

- **Student Class**
  Represents a student with specific actions like creating projects,
  checking inbox, viewing and responding to invitations.
- **Lead Class**
  Inherits from the Student class and adds lead-specific actions like sending invitations,
  adding/removing members and modifying projects.
- **Member Class**
  Represents a member with actions like seeing projects and modifying projects.
- **Advisor Class**
  Represents an advisor with actions like managing requests, viewing all projects,
  approving projects, and commenting on projects.
- **Admin Class**
  Represents an admin with actions like managing the database, editing, and deleting projects.
- **Faculty Class**
  Represents a faculty member with actions like viewing supervisor requests, managing requests,
  viewing all projects, and commenting on projects.
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

| Class         | Method                  | Action                                                                                                                                                                                                                                           | Completion Percentag | Completion Percentage |
|---------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------|
| Student Class | __init__                | The constructor initializes the attributes of the Student and Lead classes. It takes three parameters: id, username, and role. These attributes include id, user (username), role, and request_box (an empty list).                              | **100%**             | Student               |
| Student Class | create_project          | This method allows a student to create a project. It prompts the user for the project title, sets the student as the lead of the project, and adds the project to the database. It also updates the student's role to 'lead' in the login table. | **100%**             | Student               |
| Student Class | check_inbox             | This method checks the inbox for pending invitations and prints information about each pending invitation, including the lead, project title, and status.                                                                                        | **100%**             | Student               |
| Student Class | see_invite              | This method prints the pending invitations for the student.                                                                                                                                                                                      | **100%**             | Student               |
| Student Class | accept_invite           | This method allows a student to accept an invitation by providing the invitation token. It updates the project's member slots and marks the invitation as accepted.                                                                              | **100%**             | Student               |
| Student Class | deny_invite             | This method allows a student to deny a specific invitation by providing the lead ID. It marks the invitation as denied.                                                                                                                          | **100%**             | Student               |
| Student Class | run                     | This method runs a loop allowing the user to choose various actions like checking the inbox, creating a project, viewing invitations, accepting invitations, denying invitations, or logging out.                                                | **100%**             | Student               |
| Student Class | __str__                 | This method returns a string welcoming the user to the Senior Project Report and stating their role.                                                                                                                                             | **100%**             | Student               |
| Lead Class    | see_project             | This is a static method that prints information about all projects.                                                                                                                                                                              | **100%**             | Lead                  |
| Lead Class    | sent_invite             | This method allows a lead to send an invitation to a member by providing the member's ID. It generates a unique token and adds the invitation to the database.                                                                                   | **100%**             | Lead                  |
| Lead Class    | add_member              | This method allows a lead to add a member to their project by providing the member's ID.                                                                                                                                                         | **100%**             | Lead                  |
| Lead Class    | remove_member           | This method allows a lead to remove a member from their project by providing the member's ID.                                                                                                                                                    | **100%**             | Lead                  |
| Lead Class    | modify_project          | This method allows a lead to modify their project's title and status.                                                                                                                                                                            | **100%**             | Lead                  |
| Lead Class    | send_request_to_advisor | This method allows a lead to send a request to an advisor by providing the advisor's ID. It adds the request to the advisor table.                                                                                                               | **100%**             | Lead                  |
| Lead Class    | summit                  | This method marks the lead's project as 'Submitted' and updates the project status in the database.                                                                                                                                              | **100%**             | Lead                  |
| Lead Class    | invite_advisor          | This method allows a lead to invite an advisor to their project by providing the advisor's ID. It adds the invitation to the advisor table.                                                                                                      | **100%**             | Lead                  |
| Lead Class    | run                     | This method runs a loop allowing the lead to choose actions like inviting members, inviting advisors, or logging out.                                                                                                                            | **100%**             | Lead                  |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| TMember Class | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |
| Member Class  | update_row              | Updates a specific row in the table based on primary key conditions.                                                                                                                                                                             | **100%**             |                       |         


