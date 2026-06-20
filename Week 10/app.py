import tkinter as tk

# File read Sign In function
def sign_in():
    user = username.get()
    pwd = password.get()

    try:
        file = open("users.txt", "r")

        for line in file:
            u, p = line.strip().split(",")

            if user == u and pwd == p:
                result.config(text="Login Successful")
                file.close()
                return

        result.config(text="Invalid Login")
        file.close()

    except:
        result.config(text="No User Found")


# File write Sign Up function
def sign_up():
    user = username.get()
    pwd = password.get()

    file = open("users.txt", "a")
    file.write(user + "," + pwd + "\n")
    file.close()

    result.config(text="Account Created")


# sign in window
def sign_in_window():
    global username, password, result

    tk.Label(root, text="Username").pack()

    username = tk.Entry(root)
    username.pack()

    tk.Label(root, text="Password").pack()

    password = tk.Entry(root, show="*")
    password.pack()

    tk.Button(root, text="Sign In", command=sign_in).pack()

    tk.Button(root, text="Sign Up", command=sign_up).pack()

    result = tk.Label(root, text="")
    result.pack()


# sign up window
def sign_up_window():
    pass


# main menu window
def main_menu():
    pass


# root window
root = tk.Tk()
root.title("Application")
root.geometry("300x200")

sign_in_window()

root.mainloop()