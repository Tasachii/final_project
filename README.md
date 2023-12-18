# Final project for 2023's 219114/115 Programming I

**Database**

| File                        |
|-----------------------------|
| advisor_pending_request.csv |
| member_pending_request.csv  |
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

| Class          | Method                   | Action                                                                                                                                                                                                                                                                                                  | Completion Percentag | Role    |
|----------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------|---------|
| Student Class  | __init__                 | Initializes the id, user (username), role, and request_box attributes for a Student.                                                                                                                                                                                                                    | **100%**             | Student |
| Student Class  | create_project           | Allows a student to create a new project: <br/>Takes input for project title. <br/>Sets the student as the lead of the project and initializes other members and advisor to 'none'. <br/>Updates the project information in the database. <br/>Updates the student's role to 'lead' in the login table. | **100%**             | Student |
| Student Class  | check_inbox              | Checks the inbox for pending invitations:<br/>Retrieves pending invitations for the student from the 'member' table. <br/>Prints information about each pending invitation.                                                                                                                             | **100%**             | Student |
| Student Class  | see_invite               | Shows pending invitations for the student:<br/>Filters invitations with a pending response for the student and prints the result                                                                                                                                                                        | **100%**             | Student |
| Student Class  | accept_invite            | Allows a student to accept an invitation:<br/>Takes input for the invitation token. <br/>Finds the corresponding invitation and project in the database. <br/>Updates the project by adding the student as a member. <br/>Updates the status of the invitation to 'accepted'.                           | **100%**             | Student |
| Student Class  | deny_invite              | Allows a student to deny an invitation:<br/>Displays pending invitations using the see_invite method. <br/>Takes input for the lead ID to deny the invitation for. <br/>Updates the status of the corresponding invitation to 'denied'.                                                                 | **100%**             | Student |
| Student Class  | run                      | Runs a loop displaying a menu for student actions:<br/>Check inbox <br/>Create a project <br/>Logout <br/>View invitation <br/>Accept invite <br/>Deny invite                                                                                                                                           | **100%**             | Student |
| Student Class  | __str__                  | Overrides the __str__ method to provide a string representation of the student.                                                                                                                                                                                                                         | **100%**             | Student |
| Lead Class     | __init__                 | Calls the constructor of the base class (Student) and initializes additional attributes specific to a Lead.                                                                                                                                                                                             | **100%**             | Lead    |
| Lead Class     | see_project              | Static method that displays information about all projects using the 'project' table.                                                                                                                                                                                                                   | **100%**             | Lead    |
| Lead Class     | sent_invite              | Allows a lead to send invitations to members:<br/>Takes input for the member ID to invite. <br/>Generates a unique invitation token and adds an entry to the 'member' table.                                                                                                                            | **100%**             | Lead    |
| Lead Class     | add_member               | Allows a lead to add a member to their project:<br/>Takes input for the ID of the member to add. <br/>Updates the project information in the 'project' table.                                                                                                                                           | **100%**             | Lead    |
| Lead Class     | remove_member            | Allows a lead to remove a member from their project:<br/>Takes input for the ID of the member to remove. <br/>Updates the project information in the 'project' table.                                                                                                                                   | **100%**             | Lead    |
| Lead Class     | submit_project           | Allows a lead to submit their project for evaluation:<br/>Updates the status of the project to 'Submitted' in the 'project' table.                                                                                                                                                                      | **100%**             | Lead    |
| Lead Class     | modify_project           | Allows a lead to modify their project:<br/>Takes input for the new project title and status. <br/>Updates the project information in the 'project' table.                                                                                                                                               | **100%**             | Lead    |
| Lead Class     | send_request_to_advisor  | Allows a lead to send a request to an advisor:<br/>Takes input for the ID of the advisor to send the request to. <br/>Adds an entry to the 'advisor' table.                                                                                                                                             | **100%**             | Lead    |
| Lead Class     | summit                   | Allows a lead to submit their project (similar to submit_project)..                                                                                                                                                                                                                                     | **100%**             | Lead    |
| Lead Class     | invite_advisor           | Allows a lead to invite an advisor to their project:<br/>Takes input for the ID of the advisor to invite. <br/>Adds an entry to the 'advisor' table.                                                                                                                                                    | **100%**             | Lead    |
| Lead Class     | run                      | Runs a loop displaying a menu for lead actions:<br/>Invite member <br/>Invite advisor <br/>Submit Project <br/>Logout                                                                                                                                                                                   | **100%**             | Lead    |
| Member Class   | __init__                 | Initializes id, user (username), and role attributes for a Member.                                                                                                                                                                                                                                      | **100%**             | Member  |
| Member Class   | see_project              | Retrieves projects from the database where the Member is the lead or a member. <br/>Prints information about those projects (title, lead, status).                                                                                                                                                      | **100%**             | Member  |
| Member Class   | request_status_change    | Allows a Member to request a status change for a project they are a part of.<br/>Takes input for project title and new status and prints a confirmation message.                                                                                                                                        | **100%**             | Member  |
| Member Class   | run                      | Runs a loop displaying a menu for Member actions: <br/>See My Projects <br/>Modify a Project <br/>Logout                                                                                                                                                                                                | **100%**             | Member  |
| Advisor Class  | __init__                 | Initializes id, user (username), and role attributes for an Advisor.                                                                                                                                                                                                                                    | **100%**             | Advisor |
| Advisor  Class | see_request_supervisor   | Displays requests for supervision made to the Advisor.                                                                                                                                                                                                                                                  | **100%**             | Advisor |
| Advisor  Class | manage_request           | Allows an Advisor to manage a specific project request by providing a response (accept/deny).                                                                                                                                                                                                           | **100%**             | Advisor |
| Advisor  Class | see_project              | Static method that displays information about all projects.                                                                                                                                                                                                                                             | **100%**             | Advisor |
| Advisor  Class | approve_project          | Static method that allows an Advisor to approve a project by providing the project title.                                                                                                                                                                                                               | **100%**             | Advisor |  
| Advisor Class  | comment_on_project       | Static method that allows an Advisor to add comments to a project by providing the project title and comment.                                                                                                                                                                                           | **100%**             | Advisor |
| Advisor Class  | evaluate_project         | Allows the advisor to evaluate a submitted project:<br/>Takes input for the project title, new status, and feedback.<br/>Updates the project status and provides feedback.                                                                                                                              | **100%**             | Advisor |
| Advisor Class  | run                      | Runs a loop displaying a menu for Advisor actions: <br/>See supervisor requests <br/>Manage requests <br/>See all projects <br/>Comment on a project <br/>Approve a project Logout                                                                                                                      | **100%**             | Advisor |
| Admin Class    | __init__                 | Initializes id, user (username), and role attributes for an Admin.                                                                                                                                                                                                                                      | **100%**             | Admin   |
| Admin Class    | manage_database          | Displays a menu for managing the database with options to edit or delete a project.                                                                                                                                                                                                                     | **100%**             | Admin   |
| Admin Class    | edit_project             | Static method that allows an Admin to edit a project's title and status.                                                                                                                                                                                                                                | **100%**             | Admin   |
| Admin Class    | delete_project           | Static method that allows an Admin to delete a project.                                                                                                                                                                                                                                                 | **100%**             | Admin   |
| Admin Class    | run                      | Runs a loop displaying a menu for Admin actions: <br/>Manage Database <br/>Logout                                                                                                                                                                                                                       | **100%**             | Admin   |
| Faculty Class  | __init__                 | Initializes id, user (username), and role attributes for a Faculty member.                                                                                                                                                                                                                              | **100%**             | Faculty |
| Faculty Class  | view_supervisor_requests | Displays requests for supervision made to any Advisor.                                                                                                                                                                                                                                                  | **100%**             | Faculty |
| Faculty Class  | manage_request           | Allows a Faculty member to manage a specific project request by providing a response (accept/deny).                                                                                                                                                                                                     | **100%**             | Faculty |
| Faculty Class  | view_all_projects        | Static method that displays information about all projects.                                                                                                                                                                                                                                             | **100%**             | Faculty |
| Faculty Class  | comment_on_project       | Static method that allows a Faculty member to add comments to a project by providing the project title and comment.                                                                                                                                                                                     | **100%**             | Faculty |
| Faculty Class  | run                      | Runs a loop displaying a menu for Faculty actions: <br/>View Supervisor Requests <br/>Manage Requests <br/>View All Projects <br/>Comment on a Project <br/>Logout                                                                                                                                      | **100%**             | Faculty |

