from cyrptography.fernet import Fernet   # import encryption tool

# a module is a file consisting of python code. cyrptography is the module here.


class PasswordManager:  
# blueprint for password manager. everything that relates to passwords in this class. first time with OOP.

  def __init__(self):    
  # constructor. a special function that runs automatically when you create an object

    self.key = None   # the self thing attaches this specific key to the object and remembers it forever
    self.password_file = None
    self.password_dict = {}    # obviously the password dictionary
    ## i still kinda don't understand the self dot thing but hopefully i will when i run it
 
  # 1
  def create_key(self, path):    # path to store the key into a file (i think so we don't have to make the key again?). the key is for encrypting
    self.key = Fernet.generate_key()   # key can be used for encryption and decryption
    with open(path, "wb") as f:
      f.write(self.key)

      # this creates the key and stores it into the file for real.

  # 2
  # function for loading, so that we can decrypt it again with the same key and need not create a new one.
  def load_key(self, path):
    with open(path, "rb") as f:
      self.key = f.read()

      ## i don't understand the "as f" thing


   # 3
   def create_password_file(self, path, initial_values=None):    # This is for making the password file as name suggests but idk why initial values is set to none

    self.password_file = path

    if initial_values is not None:
      for key, values in initial_values.items():
        self.add_password(key, value)

     
    # 4
    def load_password_file(self, path):
      # decryption
      self.password_file = path  

      with open(path, "r") as f:
        for line in f:_
        site, encrypted = line.split(":")   # this just indicates whatever character u want site, encrypted the two things to be split with when it reads on screen i think. OH THE COMMA NOW MAKES SENSE!!
        self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()
        ## WHAT IS THIS .ENCODE() DECODE RUBBISH AHHHHH

    # 5
     def add_password(self, site, password):
      self.password_dict[site] = password    # lowk why is it site in square brackets

      if self.password_file is not None:
        with open(self.password_file, "a+") as f:
          encrypted = Fernet(self.key).encrypt(password.encode())
          f.write(site + ":" + encrypted.decode() + \n)    # OHHH THIS SHOWS THE PASSWORDS KINDA LIKE

    # 6
    def get_password(self, site):
      return self.password_dict[site]  



def main():
  password = {
    "email" = "1234567",
    "facebook" = "myfbpassword",
    "youtube" = "helloworld12"
  }    # these are the passwords alr stored ig

  pm = PasswordManager()    # 

  print("""What do you want to do?
  1. Create new key
  2. Load an existing key
  3. Create new password file
  4. Load existing password file
  5. Add a new password
  6. Get a password 
  7. Quit
  """)

  done = False   # cause the process or task is not finished while the main() runs. 

  while not done:

    choice = input("Enter your choice: ")
    if choice == "1":
      path = input("Enter path: ")
      pm.create_key(path)   # so user enters the path and that is put in the function # 1? and the pm dot thing is relating it to the instance idk
    elif choice == "2":
      path = input("Enter path: ")
      pm.load_key(path)
    elif choice == "3":  
      path = input("Enter path: ")
      pm.create_password_file(path, password)   # WHAT IS GOING ON HERE
    elif choice == "4":
      path = input("Enter path: ")
      pm.load_password_file(path) 
    elif choice == "5":
      site = input("Enter site: ")
      password = input("Enter password: ")
      pm.add_password(site, password)   # okay this acc kinda makes sense/ the user is inputting site and password and we call the function with that as the argument for it. 
    elif choice == "6":
      site = input("Enter the site you want the password for: ")
      pm.get_password(site)
      # i did not copy the tutorial for this part i guessed and intuited before i watched the tutorial and fixed 
    elif choice == "7":
      done = True   # now it is done and python knows. 
      print("Bye!")  
    else:
      print("Invalid choice.")


     

     
# pm = PasswordManager()    # this is an instance. i think an instance is a version of a class (which is a blueprint). say for example the class is the genes, and each instance (if there are multiple) are like siblings to each other i think.
# pm.create_key("mykey.key")
## run that, you get a key file?
