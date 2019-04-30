"""
Weddings I - Guest List
"""

# Imagine for this problem set that you are planning a wedding. 


# A) Define a class called "Guest" to help you manage all the information about each invitee. This should initially include instance attributes for the guests's name, phone, and an optional "invite_sent" that defaults to False. Guest should also include an instance method called "send_invite()", which changes the value of invite_sent to True once you send an invitation to that guest.



# B) Next, define a child class called "Bridesmaid", which includes the same initial attributes and inherits Guest's instance method.



# C) Finally, create at least one instance of each class and do the following:
### Call send_invite() on each instance.
### Check whether Bridesmaid is a child of Guest and vice versa.

# A)
class Guest():
    def __init__(self, name, phone, invite_sent = False):
        self.name = name
        self.phone = phone
        self.invite_sent = invite_sent

    def send_invite(self):
        self.invite_sent = True
        return None

# B)
class Bridesmaid(Guest):
    def __init__(self, name, phone, invite_sent = False):
        self.name = name
        self.phone = phone
        self.invite_sent = invite_sent


# C)
michelle = Guest('Michelle Addison', 9205150102)
angelika = Bridesmaid('Angelika Vasilieva', 2019352087)

print(michelle.invite_sent) # False
michelle.send_invite()
print(michelle.invite_sent) # True

print(angelika.invite_sent) # False
angelika.send_invite()
print(angelika.invite_sent) # True

def check_class(child, parent):
    if isinstance(child, parent):
        return True
    else:
        return False

print(check_class(angelika, Bridesmaid)) # True
print(check_class(angelika, Guest)) # True

print(check_class(michelle, Guest)) # True
print(check_class(michelle, Bridesmaid)) # False

