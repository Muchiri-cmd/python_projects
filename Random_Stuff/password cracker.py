from random import choice 
possibilities=[0,1,2,3,4,5,6,7,8,9]

def get_mpesa_password(possibilities):
    mpesa_password=[]
    print("cracking.....")
     #use a while loop so as not to repeat numbers
    while len(mpesa_password)<4:
        pulled_digit=choice(possibilities)
        #only add digit if its not already in the password list
        if pulled_digit not in mpesa_password:
            print("pulled.."+str(pulled_digit))
            mpesa_password.append(pulled_digit)
    return mpesa_password

def check_password(tried_password,mpesa_password):
    #check all elements in trials if they are not in password
    #return false
    for element in tried_password:
        if element not in mpesa_password:
            return False
    return True
    #we must have a password eitherway

def make_random_combinations(possibilities):
    #return random combinations
    password=[]
    while len(password)<4:
        pulled_digit=choice(possibilities)
        #only adds to password if it hasnt been pulled
        if pulled_digit not in password:
            password.append(pulled_digit)

    return password

possibilities=[0,1,2,3,4,5,6,7,8,9]
mpesa_password=get_mpesa_password(possibilities)
tries=0
found=False

max_tries=1_000_000

while not found:
    another_try=make_random_combinations(possibilities)
    found=check_password(another_try,mpesa_password)
    tries+=1
    if tries>=max_tries:
        break

if found:
    print("match found")
    print("password is: "+str(mpesa_password))
    print("it took "+str(tries)+" attempts to get it")

else:
    print("Tried "+tries+" times unsuccessful ")
    print("match not found")
