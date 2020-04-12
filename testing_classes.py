class User():
    def __init__(self, name, number=100):
        self.name = name
        self.number = number

    def top(self):
        print('Welcome to the website,', self.name)

    def menu(self):
        print("""Home
Post
Profile""")

class Mod(User):
    def __init__(self, name):
        super().__init__(name)

    def top(self):
        super().top()

    def menu(self):
        super().menu()
        print("""Modify
Flag
Comment""")

class Admin(Mod):
    def __init__(self, name):
        super().__init__(name)

    def top(self):
        super().top()
        
    def menu(self):
        super().menu()
        print("""Remove
Delete
Ban""")

#user is automatically instantiated into User Class
print('Register : ')
new_user = User(input('Welcome, please enter your name '))
new_user.top()
new_user.menu()


#user has been upgraded to Moderator Class
new_user = Mod(new_user.name)
print('You\'ve been a member for 2 years now, ')
print('We\'ve upgraded your account to Moderator')
new_user.menu()


#user has been upgraded to Administrator Class
new_user = Admin(new_user.name)
print('We\'ve upgraded your account to Admin!!!!')
new_user.menu()










