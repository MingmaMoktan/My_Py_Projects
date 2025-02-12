####################
# NAMING VARIABLES #
####################

# Exercise 1
f = ["apple", "orange"]
for t in f:
    print(t)

# Exercise 2
n = 25
g = [75, 80, 85, 90, 95]
s = 0
for x in g:
    s += x
avg = s / len(g)

# Exercise 3
class Person:
    m_fn = "" # User's firstname
    m_sn = "" # User's lastname

############
# COMMENTS #
############

# Exercise 1

# Here we create a list
fruits = ["apple", "orange"]
# Here we loop
for fruit in fruits:
    print(fruit) # Print the fruit

##################
# NAMING CLASSES #
##################

# Exercise 1

class Car:
    def spawnCoolCar():
        pass
    def delete_car():
        pass
    def GimmeCar():
        pass

#######
# DRY #
#######

# Exercise 1

def print_response(message):
    print(f"Error: {message}")

def print_success(message):
    print(f"Success: {message}")

def print_warning(message):
    print(f"Warning: {message}")

#############
# FUNCTIONS #
#############

# Exercise 1

def create_page_and_initialize_tools_and_render():
    pass

################
# GUARD CLAUSE #
################

# Exercise 1

def create_transaction(transactionId, account, amount):
    if transactionId:
        if account:
            if amount > 0:
                return True, "Transaction created succesfully."
            else:
                return False, "Money should be over 0."
        else:
            return False, "Account should be set."
    else:
        return False, "Transaction ID should be set."