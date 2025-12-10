import bcrypt



def hash_password(password):
    binary_password = password.encode("utf-8")
    salt=bcrypt.gensalt()
    hash_password=bcrypt.hashpw(binary_password,salt)
    return hash_password.decode("utf-8")

def validate_password(password):
    hash_password=hash.encode("utf-8")
    bin_password=password.encode("utf-8")  

    return(bcrypt.checkpw(bin_password, hash_password))



def register_user():
    name=input("enter your name")
    psw=input("enter a password")
    hash=hash_password(psw) 
    with open ("users.txt","a")as f:
        f.write(f"{name},{hash}\n")

       

def log_in_user():
    #password=input("enter your password:")

    with open("users.txt","r") as f:
        users=f.readlines()
        for user in users:
            name,hash_value = user.strip().split(",")
        if name == name:
              return hash_value     


 
 