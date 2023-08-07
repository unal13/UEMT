import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import cx_Oracle

conStr = 'system/P@localhost:1521/xepdb1'

BG_IMAGE_PATH = "C:\\Users\\emrei\\PycharmProjects\\1.Projekt\\Login.png"
INTERFACE_BG_IMAGE_PATH = "C:\\Users\\emrei\\PycharmProjects\\1.Projekt\\Interface.png"
REGISTER_BG_IMAGE_PATH = "C:\\Users\\emrei\\PycharmProjects\\1.Projekt\\Register.png"


class BaseWindow:
    def __init__(self, app, width, height):
        self.app = app
        self.root = tk.Toplevel()
        self.root.geometry(f"{width}x{height}")
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - width) / 2
        y = (self.root.winfo_screenheight() - height) / 2
        self.root.geometry(f"+{int(x)}+{int(y)}")
        self.root.resizable(False, False)
        self.function_menu = self.create_menu()

    def create_menu(self):
        menu_bar = tk.Menu(self.root, bg='orange', fg='white', font=('Arial', 12, 'bold'))
        function_menu = tk.Menu(menu_bar, tearoff=0, bg='orange', fg='white', font=('Arial', 12, 'bold'))
        function_menu.add_command(label="F1: Hilfe?", command=self.show_help)
        function_menu.add_command(label="F2: Kennwort ändern", command=self.change_password)
        function_menu.add_command(label="F3: Informationen", command=self.show_info)
        menu_bar.add_cascade(label="Funktionen", menu=function_menu)
        return menu_bar

    def show_help(self):
        messagebox.showinfo("Hilfe", "Hier könnte Ihre Hilfe stehen.")

    def change_password(self):
        messagebox.showinfo("Kennwort ändern", "Hier könnte Ihre Kennwortänderungs-Logik stehen.")

    def show_info(self):
        messagebox.showinfo("Informationen", "Hier könnten Ihre Informationen stehen.")

    def go_back(self):
        self.root.destroy()
        self.app.create_interface_window()

class LoginWindow(BaseWindow):
    def __init__(self, app):
        bg_image = Image.open(BG_IMAGE_PATH)
        super().__init__(app, bg_image.width, bg_image.height)
        bg_image = bg_image.resize((bg_image.width, bg_image.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.username_entry = tk.Entry(self.root, width=30, font=('Arial', 12))
        self.username_entry.insert(0, "Username")
        self.username_entry.bind("<FocusIn>", self.clear_username)
        self.username_entry.bind("<FocusOut>", self.fill_username)
        self.username_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)
        self.password_entry = tk.Entry(self.root, show="*", width=30, font=('Arial', 12))
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", self.clear_password)
        self.password_entry.bind("<FocusOut>", self.fill_password)
        self.password_entry.place(relx=0.5, rely=0.63, anchor=tk.CENTER)
        self.login_button = tk.Button(self.root, text="Login", command=self.login, bg='orange', fg='white', font=('Arial', 12, 'bold'))
        self.login_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)
        self.register_button = tk.Button(self.root, text="Register", command=self.register, bg='orange', fg='white', font=('Arial', 12, 'bold'))
        self.register_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
        self.root.config(menu=None)

    def register(self):
        self.app.create_register_window()

    def clear_username(self, event):
        if self.username_entry.get() == "Username":
            self.username_entry.delete(0, tk.END)


    def fill_username(self, event):
        if self.username_entry.get() == "":
            self.username_entry.insert(0, "Username")

    def clear_password(self, event):
        if self.password_entry.get() == "Password":
            self.password_entry.delete(0, tk.END)

    def fill_password(self, event):
        if self.password_entry.get() == "":
            self.password_entry.insert(0, "Password")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print("Versuchter Login mit:", username, password)
        if username != "Username" and password != "Password":
            self.root.destroy()
            self.app.create_interface_window()


class InterfaceWindow(BaseWindow):
    def __init__(self, app):
        bg_image = Image.open(INTERFACE_BG_IMAGE_PATH)
        super().__init__(app, bg_image.width, bg_image.height)
        bg_image = bg_image.resize((bg_image.width, bg_image.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.config(menu=self.function_menu)
        tk.Button(self.root, text="Wareneingang", command=self.open_wareneingang, bg='orange', fg='white', font=('Arial', 12, 'bold')).place(relx=0.5, rely=0.4, anchor=tk.CENTER)
        tk.Button(self.root, text="Warenausgang", command=self.open_warenausgang, bg='orange', fg='white', font=('Arial', 12, 'bold')).place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        tk.Button(self.root, text="Sonderfunktionen", command=self.open_sonderfunktionen, bg='orange', fg='white', font=('Arial', 12, 'bold')).place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        tk.Button(self.root, text="Abmelden", command=self.abmelden, bg='orange', fg='white', font=('Arial', 12, 'bold')).place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def open_wareneingang(self):
        self.root.destroy()
        self.app.create_wareneingang_window()

    def open_warenausgang(self):
        self.root.destroy()
        self.app.create_warenausgang_window()

    def open_sonderfunktionen(self):
        self.root.destroy()
        self.app.create_sonderfunktionen_window()

    def abmelden(self):
        self.root.destroy()
        self.app.create_login_window()

class WareneingangWindow(BaseWindow):
    def __init__(self, app):
        bg_image = Image.open(INTERFACE_BG_IMAGE_PATH)
        super().__init__(app, bg_image.width, bg_image.height)
        bg_image = bg_image.resize((bg_image.width, bg_image.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.config(menu=self.function_menu)
        tk.Button(self.root, text="Zurück", command=self.go_back, bg='orange', fg='white', font=('Arial', 12, 'bold')).pack()

class WarenausgangWindow(BaseWindow):
    def __init__(self, app):
        bg_image = Image.open(INTERFACE_BG_IMAGE_PATH)
        super().__init__(app, bg_image.width, bg_image.height)
        bg_image = bg_image.resize((bg_image.width, bg_image.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.config(menu=self.function_menu)
        tk.Button(self.root, text="Zurück", command=self.go_back, bg='orange', fg='white', font=('Arial', 12, 'bold')).pack()

class SonderfunktionenWindow(BaseWindow):
    def __init__(self, app):
        bg_image = Image.open(INTERFACE_BG_IMAGE_PATH)
        super().__init__(app, bg_image.width, bg_image.height)
        bg_image = bg_image.resize((bg_image.width, bg_image.height), Image.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.config(menu=self.function_menu)
        tk.Button(self.root, text="Zurück", command=self.go_back, bg='orange', fg='white', font=('Arial', 12, 'bold')).pack()

    class RegisterWindow:
        def __init__(self, app, parent):
            self.app = app
            self.root = tk.Toplevel(parent)
            self.root.title("Register")

            # Load the background image
            bg_image = Image.open(REGISTER_BG_IMAGE_PATH)

            # Set a fixed size for the image
            bg_image = bg_image.resize((800, 600), Image.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.bg_label = tk.Label(self.root, image=self.bg_photo)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.fullname_entry = self.create_entry("Vorname Nachname", 0)
            self.username_entry = self.create_entry("NutzerID", 1)
            self.password_entry = self.create_entry("Kennwort", 2, show="*")
            self.confirm_password_entry = self.create_entry("Kennwort wiederholen", 3, show="*")

            tk.Button(self.root, text="Register", command=self.register).grid(row=4, column=1)
            tk.Button(self.root, text="Abbrechen", command=self.root.destroy).grid(row=5, column=1)

        def create_entry(self, text, row, **kwargs):
            entry = tk.Entry(self.root, **kwargs)
            entry.insert(0, text)
            entry.bind("<FocusIn>", lambda args: entry.delete(0, 'end') if entry.get() == text else None)
            entry.bind("<FocusOut>", lambda args: entry.insert(0, text) if entry.get() == "" else None)
            entry.grid(row=row, column=1)
            return entry

        def register(self):
            username = self.username_entry.get()
            password = self.password_entry.get()
            confirm_password = self.confirm_password_entry.get()
            full_name = self.fullname_entry.get()

            if password != confirm_password:
                messagebox.showerror("Error", "Passwords do not match")
                return

            conn = cx_Oracle.connect(conStr)
            cur = conn.cursor()
            try:
                cur.execute(
                    "INSERT INTO ÜMT.user_t (benutzer, userbez, dzins, kennwort) VALUES (:username, :full_name, SYSDATE, :password)",
                    {"username": username, "full_name": full_name, "password": password}
                )
            except cx_Oracle.DatabaseError as error:
                messagebox.showerror("Error", "Could not register user: " + str(error))
            else:
                conn.commit()
                messagebox.showinfo("Success", "User registered successfully")
            cur.close()
            conn.close()


class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.change_window(self.create_login_window)

    def create_register_window(self):
        return RegisterWindow(self, self.current_window.root)

    def register(self):
        self.create_register_window()

    def change_window(self, window_creator):
        self.current_window = window_creator()

    def create_login_window(self):
        return LoginWindow(self)



    def create_interface_window(self):
        return InterfaceWindow(self)

    def create_wareneingang_window(self):
        return WareneingangWindow(self)

    def create_warenausgang_window(self):
        return WarenausgangWindow(self)

    def create_sonderfunktionen_window(self):
        return SonderfunktionenWindow(self)





if __name__ == "__main__":
    app = MyApp()
    tk.mainloop()
