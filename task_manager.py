#=====importing libraries starts ===========
import os
import sys
import datetime
#=====importing libraries ends ===========
#====User-Define Function starts==========
def validate_date(date,format):
    try:
        result = bool(datetime.datetime.strptime(date,format))
        return result
    except ValueError:
        return False
        
def get_current_date():
    date = datetime.datetime.now()
    formatted_date = date.strftime("%d %b %Y")
    return formatted_date

def input_validation(input):
    if input == "" or input.isspace() == True:
        print("You have entered nothing!")
        return False
    else:
        return True
  
def udpate_list(dictionary):
    file = None
    try:
        # Open user text file
        file = open('user.txt','r',encoding='utf-8') 
    
        # Store file into dictionary
        for line in file:
            key, value = line.split(', ')
            dictionary[key] = value.replace('\n','') # replaced '\n' with '' for my password to work
        
    except (FileNotFoundError,ValueError, IOError) as error:

        # Print error if file does not exist
        print(f"{error} - closing app")
        exit()
    
    finally:
    
        # Close file if is exist
        if file is not None:
            file.close()
 
def login(username, password):
    login_loop = True

    # Login loop will continue until login_loop = Fa'se
    while login_loop == True:
        username = input("Enter your username: ").lower()# All input will be lowercase
    
        # Check if username exist in dictionary
        if username in dict_user:
            password = input("Enter your password: ")
        
            # Check if password  equals value stored in that specific username key
            if password == dict_user[username]:
                print (f"Welcome {username}")
                return username
                # Terminate the loop
                login_loop = False
                
            else:
                print("Incorrect Password!")          
        else:
            print(f"{username} does not exist!")

def registration():
    new_user = input("Enter your username: ").lower()
       
    # Check if username already exist in dictionary
    if new_user in dict_user:
            print("username already exist")
    
    # Check if input is empty or only whitespaces               
    elif input_validation(new_user) == True:
        new_pass = input("Enter your new password: ")
                
        # Check if password is empty or only has whitespaces
        if input_validation(new_pass) == True:      
            # Define conf_pass
            conf_pass = ""
                    
            conf_pass = input("Enter password confirmation: ")
                
            # Check if password and password confirmation match
            if new_pass == conf_pass:
                try:
                    with open(user_file,'a', encoding='utf-8') as file:
                        file.write(f"{new_user}, {new_pass}\n")
                        print("New user added!")
                    
                # If there was a problem in writing the to file      
                except IOError as e:
                    print(f"There was an error in writing to file: {e}")
            else:
                print('password and password confirmation do not match!')

def add_task():
    user = input("Enter username: ")
        
    # Check if user is in the dictionary
    if user in dict_user:
            
        # Ask for title
        title = input("Enter task title: ")
            
        # Check if title is empty or only whitespaces
        if input_validation(title) == True:
            
            # Ask fot description
            description = input("Enter an description of the task: ")
            
            # Check if description is empty or only whitespaces
            if input_validation(description) == True:
            
                # Cancel if a comma is detected in description or title
                if description.find(",")  != -1 or title.find(",") != -1:
                    print("Please avoid using ',' in description ")
                
                else:
                    # Ask for due date
                    d_date = input("Enter due date in this format (9 Oct 2024): ")
            
                    # Check if d_date is empty or only has whitespaces
                    if input_validation(d_date) == True:
                    
            
                        # Check if due date is in valid format
                        valid_date = validate_date(d_date,"%d %b %Y")
                        if valid_date == False:
                            print("invalid date format!")
                        else:
                            # Generate current date
                            current_date = get_current_date()
             
                            try:
                
                            # Insert data into task text file
                                with open('tasks.txt','a', encoding='utf-8') as file:
                                    file.write(f"{user}, {title.capitalize()}, {description.capitalize()}, {d_date}, {current_date}, No\n")
                
                                print("New task added!\n")
                    
                            except (IOError, FileNotFoundError) as error:
                                print(f"Error: {error}")
    else:
        print(f"{user} does not exist\n")
        
def view_all_task():
    try:
            
        with open('tasks.txt','r', encoding='utf-8') as file:
            for line in file:
                    
                # Insert each section into it own variable
                user, title, description, d_date, c_date, status = line.split(', ')
                    
                # Print in a neat format
                print(f''' {title}
--------------------------------------------------
    personal: {user}
    description:
    {description}
    due date: {d_date}
    created on: {c_date}
    status: {status}''')
                    
    except (FileNotFoundError, IOError) as error:
        print(f"Error: {error}")

def view_my_task():
    try:
        with open('tasks.txt','r', encoding='utf-8') as file:
            for line in file:
                user, title, description, d_date, c_date, status = line.split(', ')
                if user == username:    
                    print(f''' {title}
-----------------------------------------------------
    description:
    {description}
    due date: {d_date}
    created on: {c_date}
    status: {status}''')   

    except (FileNotFoundError, IOError) as error:
        print(f"Error: {error}\n")

def statisrics(num_users, num_tasks):
    try:
            
        # Count number of users in file
        with open(user_file,'r', encoding='utf-8') as u_file:
            for line in u_file:
                num_users += 1

        # Count number of tasks in file
        with open("tasks.txt", 'r', encoding='utf-8') as t_file:
            for item in t_file:
                num_tasks += 1
            
        print(f"\ntotal users: {num_users}\ntotal tasks: {num_tasks}\n")
            
    except (FileNotFoundError, IOError) as error:
        print(f"Error: {error}")                                                
#====User-Define Function ends====
#====Defined variables starts=====
user_file = 'user.txt'

# Get the directory of user textfile
script_dr = os.path.dirname(os.path.abspath(sys.argv[0]))

# Change current directory to user textfile
os.chdir(script_dr)

# Store all user details into this dictionary
dict_user = {}

# Variable to couns users and tasks
num_tasks = 0
num_users =0

# username and password
username= ""
password = ""
#====Defined variables ends======
#====Login Section starts====
# To check if data is stored in dictionary
udpate_list(dict_user)

# login
username = login(username, password)
#====Login Section ends====    
while True:
    if username == "admin":
        
        # Present the menu to the user and 
        # Make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
s - statistics
e - exit
: ''').lower()
        
    else: 
          
        # Present the menu to the user and 
        # Make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        
        # Check if admin is logged in      
        if username == 'admin':      
            registration()
            udpate_list(dict_user)
        
        # Print message if user not admin            
        else:
            print("\nYou do not have authorisation!\n")    
                        
    elif menu == 'a':           
        add_task()                   
    elif menu == 'va':   
        view_all_task()                        
    elif menu == 'vm':     
        view_my_task()    
    elif menu == 's' and username == 'admin':
        statisrics(num_users,num_tasks)                        
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    else:
        print("You have entered an invalid input. Please try again\n")
        
        