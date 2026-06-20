import tkinter as tk

# Save username and password in file
def save_credentials():
    user = username.get()
    pwd = password.get()

    with open("credentials.txt", "a") as f:
        f.write(user + "," + pwd + "\n")

    result.config(text="Account Created")


# Check username and password
def check_credentials():
    user = username.get()
    pwd = password.get()

    with open("credentials.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")

            if user == u and pwd == p:
                result.config(text="Login Successful")
                return

    result.config(text="Invalid Username or Password")


# Sign In Window
def signin_window():
    global username, password, result

    tk.Label(root, text="Login").pack()

    username = tk.Entry(root)
    username.pack()

    password = tk.Entry(root, show="*")
    password.pack()

    tk.Button(root, text="Sign In",
              command=check_credentials).pack()

    tk.Button(root, text="Sign Up",
              command=save_credentials).pack()

    result = tk.Label(root, text="")
    result.pack()


root = tk.Tk()
root.title("Sign In")
root.geometry("300x200")

signin_window()

root.mainloop()