import secrets
import string
import pyperclip
import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

class initalWindow:
    def __init__(self):
      self.window = tk.Tk()
      self.window.title("Password Generator")
      self.window.geometry("320x128")
      self.window.resizable(False, False)
      self.label1 = tk.Label(self.window, text="Password Length:  ", font=("Arial", 12)).grid(row=0, column=0)
      self.entry1 = tk.Entry(self.window, font=("Arial", 12))
      self.entry1.grid(row=0, column=1)
      self.button1 = tk.Button(self.window, text="      Go!      ", bg="gray", command=self.passwordgeneration)
      self.button1.place(relx=0.50, rely=0.50, anchor="center")
      self.window.mainloop()

    def passwordgeneration(self):
      try:
        pwd_length = int(self.entry1.get())
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation
        alphabet = letters + digits + special_chars
        pwd = ''
        for i in range(pwd_length):
          pwd += ''.join(secrets.choice(alphabet))
        while True:
          pwd = ''
          for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))
          if (any(char in special_chars for char in pwd) and 
              sum(char in digits for char in pwd)>=2):
                  break
        self.copytoClip(pwd)
      except ValueError:
         failWindow()

    def copytoClip(self, pwd):
        pyperclip.copy(pwd)
        pyperclip.paste
        self.entry1.delete(0, 'end')
        popupWindow()
        

class popupWindow:
    def __init__(self):
      self.window = tk.Toplevel()
      self.window.title("Password Generated")
      self.label1 = tk.Label(self.window, text="A new password with the specified length has been generated and copied to your clipboard.\n", font=("Arial", 12)).grid(row=0, column=1)
      self.button1 = tk.Button(self.window, text="   Ok   ", bg="gray", command=self.nukeself)
      self.button1.grid(row=1, column=1)
      self.window.mainloop()

    def nukeself(self):
       self.window.destroy()

class failWindow:
    
    def __init__(self):
      self.window = tk.Toplevel()
      self.window.title("Value Error")
      self.window.resizable(False, False)
      self.label1 = tk.Label(self.window, text="Did you really just try to generate a password without a specified length?\n", font=("Arial", 14)).grid(row=0, column=1)
      img_url = "https://i.kym-cdn.com/photos/images/newsfeed/000/956/638/5bc.gif"
      response = requests.get(img_url)
      img_data = response.content
      img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
      self.label2 = tk.Label(self.window, image=img).grid(row=1, column=1)
      self.button1 = tk.Button(self.window, text="Take me back!", bg="gray", command=self.nukeself)
      self.button1.grid(row=2, column=1)
      self.window.mainloop()

    def nukeself(self):
       self.window.destroy()



initalWindow()
