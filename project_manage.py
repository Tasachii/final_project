# import database module

from database import CSV, Database, Table
import csv
import datetime

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
        Title = input('Project Title')
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
        data_login = DB.search('member')
        for each in data_login.table:
            if self.id == each['Member_Id']:
                return each

    def see_invite(self):
        pending = DB.search('member')
        my_invite = pending.filter(lambda invite: invite['Member_Request'] == self.id and invite['Response'] == 'pending')
        print(my_invite.table)

    def accept_invite(self):
        project = DB.search('project')
        pending = DB.search('member')
        self.see_invite()
        lead_id = input('Input lead id to select project')
        for request in pending.table:
            if request['Member_Request'] == self.id and request['Lead'] == lead_id and request['Response'] == 'pending':
                request['Response'] = 'accept'

        for pro in project.table:
            if pro['Lead'] == lead_id:
                if pro['Member1'] == 'none':
                    pro['Member1'] = self.id
                else:
                    pro['Member2'] = self.id

    def deny_invite(self):
        project = DB.search('project')
        pending = DB.search('member')
        self.see_invite()
        lead_id = input('Input lead id to select project')

        for request in pending.table:
            if request['Member_Request'] == self.id and request['Lead'] == lead_id and request['Response'] == 'pending':
                request['Response'] = 'denied'



    def run(self):
        print(self)
        print()
        while True:
            print("--Choose--")
            print("1. Check inbox.")
            print("2. Create a project.")
            print("4. View invitation.")
            print("3. Logout.")
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
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.project = DB.search('project').filter(lambda project: project['Lead'] == self.id).table[0]
        self.run()

    def see_project(self):
        all_project = DB.search('project')
        print(all_project)

    def sent_invite(self):
        user_id = input('Search: ')
        login_table = DB.search('login')
        pending_invite_table = DB.search('member')

        for person in login_table.table:
            if person['ID'] == user_id:
                pending_invite_table.insert(
                    {
                        'Lead': self.id,
                        'Member_Request': user_id,
                        'Response': 'pending',
                        'project_title': self.project['Title']
                    }
                )


    def add_member(self):
        pass

    def remove_member(self):
        pass

    def modify_project(self):
        pass

    def send_request_advisor(self):
        pass

    def status(self):
        pass

    def summit(self):
        pass

    def run(self):
        print(self)
        print()
        while True:
            print("--Choose--")
            print("1. Invite member")
            print("3. Logout.")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.sent_invite()
            elif choice == 2:
                print()
                self.create_project()
            elif choice == 3:
                break
            else:
                print("you do not have permission")
            print()


class Member:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.run()

    def see_project(self):
        pass

    def modify_project(self):
        pass

    def run(self):
        pass


class Advisor:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.run()

    def see_request_supervisor(self):
        pass

    def manage_request(self):
        pass

    def see_project(self):
        pass

    def run(self):
        pass


class Admin:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.run()

    def run(self):
        pass


class Faculty:
    def __init__(self, id, username, role):
        self.id = id
        self.user = username
        self.role = role
        self.request_box = []
        self.run()

    def run(self):
        pass

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


def find_project(name):
    data_login = DB.search('login')


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
    # login = open('database/login.csv', 'w')
    # login_writer = csv.writer(login)
    # login_writer.writerow(['ID', 'username', 'password', 'role'])
    # for each in DB.search('login').table:
    #     login_writer.writerow(each.values())
    # login.close()

    write_csv('login.csv', ['ID', 'username', 'password', 'role'], DB.search('login').table)

    # person = open('database/persons.csv', 'w')
    # person_writer = csv.writer(person)
    # person_writer.writerow(['ID', 'first', 'last', 'type'])
    # for each in DB.search('person').table:
    #     person_writer.writerow(each.values())
    # person.close()

    write_csv('persons.csv', ['ID', 'first', 'last', 'type'], DB.search('persons').table)


    # project = open('database/project.csv', 'w')
    # project_writer = csv.writer(project)
    # project_writer.writerow(['Title','Lead','Member1','Member2','Advisor','Status'])
    # for each in DB.search('project').table:
    #     person_writer.writerow(each.values())
    # person.close()

    write_csv('project.csv', ['Title','Lead','Member1','Member2','Advisor','Status'], DB.search('project').table)


    # advisor_pending = open('database/Advisor_pending_request.csv', 'w')
    # advisor_pending_writer = csv.writer(advisor_pending)
    # advisor_pending_writer.writerow(['ProjectID', 'Advisor_Request', 'Response', 'Response_date'])
    # for each in DB.search('advisor').table:
    #     person_writer.writerow(each.values())
    # person.close()

    write_csv('Advisor_pending_request.csv', ['ProjectID', 'Advisor_Request', 'Response', 'Response_date'], DB.search('advisor').table)


    # member_pending = open('database/member_pending_request.csv', 'w')
    # member_pending_writer = csv.writer(member_pending)
    # member_pending_writer.writerow(['ProjectID', 'Member_Request', 'Response', 'Response_date'])
    # for each in DB.search('member').table:
    #     person_writer.writerow(each.values())
    # person.close()

    write_csv('member_pending_request.csv', ['Lead','project_title','Member_Request','Response'], DB.search('member').table)

    print('\n Program Exit')


# here are things to do in this function:
# write out all the tables that have been modified to the corresponding csv files
# By now, you know how to read in a csv file and transform it into a list of dictionaries. For this project, you also need to know how to do the reverse, i.e., writing out to a csv file given a list of dictionaries. See the link below for a tutorial on how to do this:

# https://www.pythonforbeginners.com/basics/list-of-dictionaries-to-csv-in-python


# make calls to the initializing and login functions defined above
initializing()
val = login_base()
# based on the return value for login, activate the code that performs activities according to the role defined for that person_id
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
        ("You Do Not Have Permission")


main()
# once everyhthing is done, make a call to the exit function
exit()