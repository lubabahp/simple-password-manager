from cyrptography.fernet import Fernet   # import encryption tool


class PasswordManager:   
# blueprint for password manager. everything that relates to passwords in this class.

  def __init__(self):    
  # constructor. a special function that runs automatically when you create an object

    self.key = None   # the self thing attaches this specific key to the object and remembers it forever
    self.password_file = None 
    self.password_dict = {}    # obviously the password dictionary

