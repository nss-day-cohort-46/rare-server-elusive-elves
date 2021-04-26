class Users():

    def __init__(self, id, first_name, last_name, email, username, password, is_staff, bio, created_on, active):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.is_staff = is_staff
        self.bio = bio
        self.created_on = created_on
        self.active = active