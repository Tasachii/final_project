# import database module

from database import CSV, Database, Table
import csv
import uuid

# define a funcion called initializing
DB = Database()
csv1 = CSV()


class Student:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []

    def create_project(self):
        data_login = DB.search('project')
        login_table = DB.search('login')
        Title = input('Project Title: ')
        Lead_id = self.id
        project = {
            'Title': Title,
            'Lead': Lead_id,
            'Member1': 'none',
            'Member2': 'none',
            'Advisor': 'none',
            'Status': 'In-Progress'
        }
        data_login.insert(project)
        for i in login_table.table:
            if i['ID'] == self.id:
                i['role'] = 'lead'

    def check_inbox(self):
        inbox_table = DB.search('member')
        inbox_content = []
        for each in inbox_table.table:
            if self.id == each['Member_Request'] and each['Response'] == 'pending':
                inbox_content.append(each)

        print("Checking inbox for ID:", self.id)

        if not inbox_content:
            print("You don't have any messages.")
        else:
            for message in inbox_content:
                print(
                    f"Invitation from {message['Lead']} for project '"
                    f"{message['project_title']}' with status: {message['Response']}")

    def see_invite(self):
        pending = DB.search('member')
        my_invite = pending.filter(
            lambda invite: invite['Member_Request'] == self.id and invite['Response'] == 'pending')
        print(my_invite.table)

    def accept_invite(self):
        token = input('Enter the invitation token: ')
        pending = DB.search('member')
        project_table = DB.search('project')

        # Find the invitation by token
        invitation = next((invite for invite in pending.table if
                           invite['invitation_token'] == token and
                           invite['Member_Request'] == self.id
                           and invite['Response'] == 'pending'), None)

        if invitation:
            # Find the corresponding project
            for project in project_table.table:
                if (project['Title'] == invitation['project_title']
                        and project['Lead'] == invitation['Lead']):
                    # Update member slot in the project
                    if project['Member1'] == 'none':
                        project['Member1'] = self.id
                    elif project['Member2'] == 'none':
                        project['Member2'] = self.id
                    else:
                        print("Project is already full.")
                        return

                    # Update the status of the invitation
                    invitation['Response'] = 'accepted'
                    print("Invitation accepted successfully.")
                    return

            print("Project not found.")
        else:
            print("Invalid or expired invitation token.")

    def deny_invite(self):
        pending = DB.search('member')
        self.see_invite()
        lead_id = input('Input lead id to select project')

        for request in pending.table:
            if (request['Member_Request'] == self.id and request['Lead'] == lead_id
                    and request['Response'] == 'pending'):
                request['Response'] = 'denied'

    def run(self):
        print(self)
        print()
        while True:
            print("--Choose--")
            print("1. Check inbox")
            print("2. Create a project")
            print("3. Logout")
            print("4. View invitation")
            print("5. Accept invite")
            print("6. Deny invite")

            choice = int(input("Enter your choice: "))
            if choice == 1:
                print(self.check_inbox())
            elif choice == 2:
                print()
                self.create_project()
            elif choice == 3:
                break
            elif choice == 4:
                self.see_invite()
            elif choice == 5:
                self.accept_invite()
            elif choice == 6:
                self.deny_invite()
            else:
                print("you do not have permission")
            print()

    def __str__(self):
        return (f"Welcome {self.user} to Senior_Project Report."
                f"{self.role} is your role")


class Lead(Student):
    def __init__(self, id, username, role):
        super().__init__(id, username, role)
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.project = DB.search('project').filter(lambda project:
                                                   project['Lead'] == self.id).table[0]

    @staticmethod
    def see_project():
        all_project = DB.search('project')
        print(all_project)

    def sent_invite(self):
        user_id = input('Enter the ID of the member to invite: ')
        invitation_token = str(uuid.uuid4())  # Generate a unique token
        pending_invite_table = DB.search('member')

        pending_invite_table.insert({
            'Lead': self.id,
            'Member_Request': user_id,
            'Response': 'pending',
            'project_title': self.project['Title'],
            'invitation_token': invitation_token  # Add token to the invitation
        })
        print(f"Invitation sent with token: {invitation_token}")

    def add_member(self):
        member_id = input('Enter the ID of the member to add: ')
        project_table = DB.search('project')

        # Check if the member can be added
        if self.project['Member1'] == 'none':
            self.project['Member1'] = member_id
        elif self.project['Member2'] == 'none':
            self.project['Member2'] = member_id
        else:
            print("No available slot to add a new member.")
            return

        # Update the project record
        project_table.update_row('Lead', self.id, 'Member1', self.project['Member1'])
        project_table.update_row('Lead', self.id, 'Member2', self.project['Member2'])
        print("Member added successfully.")

    def remove_member(self):
        member_id = input('Enter the ID of the member to remove: ')
        project_table = DB.search('project')

        # Check if the member can be removed
        if self.project['Member1'] == member_id:
            self.project['Member1'] = 'none'
        elif self.project['Member2'] == member_id:
            self.project['Member2'] = 'none'
        else:
            print("Member not found in the project.")
            return

        # Update the project record
        project_table.update_row('Lead', self.id, 'Member1', self.project['Member1'])
        project_table.update_row('Lead', self.id, 'Member2', self.project['Member2'])
        print("Member removed successfully.")

    def modify_project(self):
        project_table = DB.search('project')
        new_title = input("Enter new project title: ")
        new_status = input("Enter new project status: ")

        # Update the project record
        self.project['Title'] = new_title
        self.project['Status'] = new_status
        project_table.update_row('Lead', self.id, 'Title', new_title)
        project_table.update_row('Lead', self.id, 'Status', new_status)
        print("Project modified successfully.")

    def send_request_to_advisor(self):
        advisor_id = input('Enter the ID of the advisor to send request to: ')
        advisor_request_table = DB.search('advisor')

        advisor_request_table.insert({
            'ProjectID': self.id,
            'Advisor_Request': advisor_id,
            'Response': 'pending',
            'Response_date': None
        })
        print("Request sent to advisor successfully.")

    def summit(self):
        project_table = DB.search('project')
        # Ensure the project exists and is led by the current user
        if self.project and self.project['Lead'] == self.id:
            self.project['Status'] = 'Submitted'
            project_table.update_row('Lead', self.id, 'Status', 'Submitted')
            print("Project submitted successfully.")
        else:
            print("No active project found or you are not the lead.")

    def invite_advisor(self):
        advisor_id = input('Enter the ID of the advisor to invite: ')
        advisor_request_table = DB.search('advisor')

        advisor_request_table.insert({
            'ProjectID': self.project['Title'],
            'Advisor_Request': advisor_id,
            'Response': 'pending'
        })
        print("Invitation sent to advisor successfully.")

    def run(self):
        print(self)
        while True:
            print("--Choose--")
            print("1. Invite member")
            print("2. Invite advisor")
            print("3. Logout.")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.sent_invite()
            elif choice == 2:
                self.invite_advisor()
            elif choice == 3:
                break
            else:
                print("Invalid choice")


class Member:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role

    def see_project(self):
        project_table = DB.search('project')
        my_projects = project_table.filter(
            lambda p: p['Lead'] == self.id or p['Member1'] == self.id or p['Member2'] == self.id)

        if not my_projects.table:
            print("You are not part of any projects.")
            return

        for project in my_projects.table:
            print(f"Title: {project['Title']}, Lead: {project['Lead']}, "
                  f"Status: {project['Status']}")

    def request_status_change(self):
        project_table = DB.search('project')
        my_projects = project_table.filter(lambda p: self.id in [p['Member1'], p['Member2']])

        if not my_projects.table:
            print("No projects found to modify.")
            return

        project_title = input("Enter the title of the project for which you want to request a status change: ")
        new_status = input("Enter your suggested new status: ")

        project_found = False
        for project in my_projects.table:
            if project['Title'] == project_title:
                project_found = True
                print(f"Status change request for '{project_title}' to '{new_status}' has been submitted.")
                break

        if not project_found:
            print("Project not found or you do not have permission to modify it.")

    def run(self):
        while True:
            print("-- Member Menu --")
            print("1. See My Projects")
            print("2. Modify a Project")
            print("3. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.see_project()
            elif choice == '2':
                self.request_status_change()
            elif choice == '3':
                break
            else:
                print("Invalid choice")


class Advisor:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role

    def see_request_supervisor(self):
        advisor_requests = DB.search('advisor').table
        for request in advisor_requests:
            if request['Advisor_Request'] == self.id:
                print(f"Project ID: {request['ProjectID']}, Response: {request['Response']}")

    def manage_request(self):
        self.see_request_supervisor()
        project_id = input("Enter Project ID to manage: ")
        response = input("Accept or Deny the request? (accept/deny): ")
        advisor_requests = DB.search('advisor')

        for request in advisor_requests.table:
            if request['ProjectID'] == project_id and request['Advisor_Request'] == self.id:
                request['Response'] = response
                print(f"Request for Project ID {project_id} has been {response}.")
                return
        print("Project ID not found or request not for this advisor.")

    @staticmethod
    def see_project():
        projects = DB.search('project').table
        for project in projects:
            print(f"Title: {project['Title']}, "
                  f"Lead: {project['Lead']}, Status: {project['Status']}")

    @staticmethod
    def approve_project():
        project_title = input("Enter the project title to approve: ")
        projects = DB.search('project')
        for project in projects.table:
            if project['Title'] == project_title:
                project['Status'] = 'Approved'
                print(f"Project '{project_title}' has been approved.")
                return
        print("Project title not found.")

    @staticmethod
    def comment_on_project():
        project_title = input("Enter the project title to comment on: ")
        comment = input("Enter your comment: ")
        # Here you should implement the logic to store the comment in your system.
        print(f"Comment added to project '{project_title}': {comment}")

    def run(self):
        while True:
            print("-- Advisor Menu --")
            print("1. See supervisor requests")
            print("2. Manage requests")
            print("3. See all projects")
            print("4. Comment on a project")
            print("5. Approve a project")
            print("6. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.see_request_supervisor()
            elif choice == '2':
                self.manage_request()
            elif choice == '3':
                self.see_project()
            elif choice == '4':
                self.comment_on_project()
            elif choice == '5':
                self.approve_project()
            elif choice == '6':
                break
            else:
                print("Invalid choice")


class Admin:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role

    def manage_database(self):
        print("Database Management")
        print("1. Edit a Project")
        print("2. Delete a Project")
        choice = input("Enter your choice: ")

        if choice == '1':
            self.edit_project()
        elif choice == '2':
            self.delete_project()
        else:
            print("Invalid choice")

    @staticmethod
    def edit_project():
        project_title = input("Enter the title of the project to edit: ")
        projects = DB.search('project')

        for project in projects.table:
            if project['Title'] == project_title:
                new_title = input("Enter new title (leave blank to keep current): ")
                new_status = input("Enter new status (leave blank to keep current): ")

                if new_title:
                    project['Title'] = new_title
                if new_status:
                    project['Status'] = new_status

                print(f"Project '{project_title}' has been updated.")
                return
        print("Project title not found.")

    @staticmethod
    def delete_project():
        project_title = input("Enter the title of the project to delete: ")
        projects = DB.search('project')

        for i, project in enumerate(projects.table):
            if project['Title'] == project_title:
                del projects.table[i]
                print(f"Project '{project_title}' has been deleted.")
                return
        print("Project title not found.")

    def run(self):
        while True:
            print("-- Admin Menu --")
            print("1. Manage Database")
            print("2. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.manage_database()
            elif choice == '2':
                break
            else:
                print("Invalid choice")


class Faculty:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role

    @staticmethod
    def view_supervisor_requests():
        advisor_requests = DB.search('advisor')

        for request in advisor_requests.table:
            print(
                f"Project ID: {request['ProjectID']}, Advisor Request:"
                f" {request['Advisor_Request']}, "
                f"Response: {request['Response']}")
        else:
            print('No request.')

    def manage_request(self):
        self.view_supervisor_requests()
        project_id = input("Enter Project ID to manage: ")
        response = input("Accept or Deny the request? (accept/deny): ")
        advisor_requests = DB.search('advisor')

        for request in advisor_requests.table:
            if request['ProjectID'] == project_id:
                request['Response'] = response
                print(f"Request for Project ID {project_id} has been {response}.")
                return
        print("Project ID not found.")

    @staticmethod
    def view_all_projects():
        projects = DB.search('project').table
        for project in projects:
            print(f"Title: {project['Title']}, "
                  f"Lead: {project['Lead']}, Status: {project['Status']}")

    @staticmethod
    def comment_on_project():
        project_title = input("Enter the project title to comment on: ")
        comment = input("Enter your comment: ")
        print(f"Comment added to project '{project_title}': {comment}")

    def run(self):
        while True:
            print("-- Faculty Menu --")
            print("1. View Supervisor Requests")
            print("2. Manage Requests")
            print("3. View All Projects")
            print("4. Comment on a Project")
            print("5. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.view_supervisor_requests()
            elif choice == '2':
                self.manage_request()
            elif choice == '3':
                self.view_all_projects()
            elif choice == '4':
                self.comment_on_project()
            elif choice == '5':
                break
            else:
                print("Invalid choice")


def initializing():
    """
    here are things to do in this function:
    create an object to read all csv files that will serve
    as a persistent state for this program
    create all the corresponding tables for those csv files
    see the guide how many tables are needed
    add all these tables to the database
    """

    csv_login = csv1.read_csv('database/login.csv')
    login_table = Table('login', csv_login)
    DB.insert(login_table)

    csv_person = csv1.read_csv('database/persons.csv')
    person_table = Table('persons', csv_person)
    DB.insert(person_table)

    csv_project = csv1.read_csv('database/project.csv')
    project_table = Table('project', csv_project)
    DB.insert(project_table)

    csv_advisor = csv1.read_csv('database/Advisor_pending_request.csv')
    advisor_table = Table('advisor', csv_advisor)
    DB.insert(advisor_table)

    csv_member = csv1.read_csv('database/Member_pending_request.csv')
    member_table = Table('member', csv_member)
    DB.insert(member_table)


def login_base():
    print("Welcome to Senior_Project Report Program")
    while True:
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        data_login = DB.search('login')
        for each in data_login.table:
            if username == each['username'] and password == each['password']:
                return each['ID'], each['role'], each['username']
        else:
            print("Invalid username or password pls try again")


# def data_person(ID):
#     person = DB.search('person')
#     person_filter = Table.filter(lambda x: x['ID'] == ID)
#     return person_filter.table[0]


# here are things to do in this function:
# add code that performs a login task
# ask a user for a username and password
# returns [ID, role] if valid, otherwise returning None

# define a function called exit

def write_csv(filename, head, dict):
    file = open("database/" + filename, 'w')
    writer = csv.DictWriter(file, fieldnames=head)
    writer.writeheader()
    writer.writerows(dict)
    file.close()


def exit():
    write_csv('login.csv', ['ID', 'username', 'password', 'role'], DB.search('login').table)
    write_csv('persons.csv', ['ID', 'first', 'last', 'type'], DB.search('persons').table)
    write_csv('project.csv', ['Title', 'Lead', 'Member1', 'Member2',
                              'Advisor', 'Status'], DB.search('project').table)
    write_csv('Advisor_pending_request.csv', ['ProjectID', 'Advisor_Request',
                                              'Response', 'Response_date'],
              DB.search('advisor').table)
    write_csv('member_pending_request.csv', ['Lead', 'project_title',
                                             'Member_Request', 'Response', 'invitation_token'],
              DB.search('member').table)

    print('\n Program Exit')


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries.
# For this project, you also need to know how to do the reverse, i.e., writing out to a csv file
# given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
initializing()
val = login_base()
# based on the return value for login, activate the code
# that performs activities according to the role
# defined for that person_id
print(val[1])
if val[1] == 'admin':
    user = Admin(val[0], val[2], val[1])
elif val[1] == 'student':
    user = Student(val[0], val[2], val[1])
elif val[1] == 'member':
    user = Member(val[0], val[2], val[1])
elif val[1] == 'lead':
    commands = ["Invite"]
    user = Lead(val[0], val[2], val[1])
elif val[1] == 'faculty':
    user = Faculty(val[0], val[2], val[1])
elif val[1] == 'advisor':
    user = Advisor(val[0], val[2], val[1])


def main():
    print(f"----------------------------------------------")
    try:
        user.run()
    except:
        "You Do Not Have Permission"


main()
# once everything is done, make a call to the exit function
exit()
