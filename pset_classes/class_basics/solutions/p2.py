"""
Phone Contacts
""" 

# Create a class called "Contact" that will store the below items for each contact in your phone. Instantiate two Contact instance objects.
    ### name (required)
    ### mobile_num
    ### work_num
    ### email

class Contact():
    def __init__(self, first_name, last_name = None, mobile_num = None, work_num = None, email = None):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_num = mobile_num
        self.work_num = work_num
        self.email = email


alejandra = Contact('Alejandra', 'Ochoa', 19034882739, 17243756608, 'alejandra.ochoa@gmail.com')

brad = Contact('Brad', 'Fenworth', 12284001753, email = 'brad.fenworth@gmail.com')

