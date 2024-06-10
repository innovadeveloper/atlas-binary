class User():
    def __init__(self, name, password, email, active):
        self.name = name
        self.password = password
        self.email = email
        self.active = active

    def __str__(self):
        return self.name + ' ' + self.password + ' ' +  self.email + ' ' + str(self.active)