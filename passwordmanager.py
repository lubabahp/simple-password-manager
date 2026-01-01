from cyrptography.fernet import Fernet   # import encryption tool

# a module is a file consisting of python code. cyrptography is the module here.


class PasswordManager:  
# blueprint for password manager. everything that relates to passwords in this class.

  def __init__(self):    
  # constructor. a special function that runs automatically when you create an object

    self.key = None   # the self thing attaches this specific key to the object and remembers it forever
    self.password_file = None
    self.password_dict = {}    # obviously the password dictionary
    # i still kinda don't understand constructors but i guess i will when i run it
 
  def create_key(self, path):    # path to store the key into a file (i think so we don't have to make the key again?). the key is for encrypting
    self.key = Fernet.generate_key()   # key can be used for encryption and decryption
    with open(path, "wb") as f:
      f.write(self.key)

      # this creates the ey and stores it into the file for real.




pm = PasswordManager()    # this is an instance? i'm not sure what an instance is.
pm.create_key("mykey.key")
# run that, you get a key file?





   # function for loading, so that we can decrypt it again with the same key and need not create a new one.
  def load_key(self, path):
    with open(path, "rb") as f:
      self.key = f.read()

      # i don't understand the "as f" thing
     

   def create_password_file(self, path, initial_values=None):    # This is for making the password file as name suggests but idk why initial values is set to none

    self.password_file = path

    if initial_values is not None:
      for key, values in initial_values.items():
        self.add_password(key, value)


    def load_password_file(self, path):
      # decryption
      self.password_file = path  

      with open(path, "r") as f:
        for line in f:_
        site, encrypted = line.split(":")   # this just indicateswhatever character u want site, encrupted the two things to be split with when it reads on screen i think. OH THE COMMA NOW MAKES SENSE!!
        self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
        # WHAT IS THIS .ENCODE() DECODE RUBBISH AHHHHH

    def add_password(self, site, password):
      self.password_dict[site] = password    # lowk why is it site in square brackets

      if self.password_file is not None:
        with open(self.password_file, "a+") as f:
          encrypted = Fernet(self.key).encrypt(password.encode())
          f.write(site + ":" + encrypted.decode() + \n)    # OHHH THIS SHOWS THE PASSWORS KINDA LIKE


    def get_password(self, site):
      return self.password_dict[site]  

def main():
  password = {
    "email" = "1234567",
    "facebook" = "myfbpassword",
    "youtube"
  }          
     

     

