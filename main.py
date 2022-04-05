#!/usr/bin/env python3
'''import rsa
import tkinter as tk
from tkinter import ttk

message = "Hello world it is a mighty fine day out there"

def main():
    root = tk.Tk()
    root.title('Computer Security Final Project')
    root.geometry('600x400+50+50')

    mb = ttk.Menubutton(root)
    m = tk.Menu(mb, tearoff=False)
    mb["menu"] = m
    root.mainloop()
    
    c = rsa.encrypt(message)
    m = rsa.decrypt(c)
    print(m)
    return
if __name__=="__main__":
    main()'''

import tkinter as tk
from tkinter import ttk
import rsa

schemeLabel = tk.Label
message = ''

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1200x800')
        self.title('Message Encryption and Decryption')


        # message entry 
        self.message = tk.StringVar()
        txtbx = ttk.Entry(self, textvariable=self.message)
        txtbx.pack()

        # cipher textbox
        encrypted_message = ttk.Label(self, text="Encrypted Message:")
        encrypted_message.pack()
        self.new_cipher = tk.Text(self, height=15, width=100)
        self.new_cipher.pack()
        
        # cipher entry
        self.cipher = tk.Text(self, height=15, width=100 )
        self.cipher.pack()

        # decrypted message textbox
        decrypted_message = ttk.Label(self, text="Decrypted Message:")
        decrypted_message.pack()
        self.orig_message = tk.Text(self, height=10, width = 100)
        self.orig_message.pack()
        # calculate button

        self.create_calc_button()
        self.create_calc_buttonD()

        # Menubutton variable
        self.selected_scheme = tk.StringVar()
        self.selected_scheme.trace("w", self.change_scheme_label)
        # create the menu button
        self.create_menu_button()
    
    def create_calc_button(self):
        cb = ttk.Button(self, text='encrypt', command=self.perform_message_encrypt)
        cb.pack()

    def create_calc_buttonD(self):
        cb = ttk.Button(self, text='decrypt', command=self.perform_message_decrypt)
        cb.pack()
    
    def perform_message_encrypt(self, *args):
        self.new_cipher.delete("1.0",tk.END)
        self.new_cipher.pack()
        self.new_cipher.insert("1.0", rsa.encrypt(self.message.get()))
        self.new_cipher.pack()
        return

    def perform_message_decrypt(self, *args):
        self.orig_message.insert("1.0", rsa.decrypt(str(self.cipher.get("1.0", tk.END))))
        self.orig_message.pack()
        return


    def change_scheme_label(self, *args):
        self.title('Message Encryption and Decryption for the '+self.selected_scheme.get() + ' scheme')

    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        schemes = ('RSA', 'Vigenere', 'Triple DES', 'AES')

        # create the Menubutton
        menu_button = ttk.Menubutton(
            self,
            text='Select a scheme')

        # create a new menu instance
        menu = tk.Menu(menu_button, tearoff=0)

        for scheme in schemes:
            menu.add_radiobutton(
                label=scheme,
                value=scheme,
                variable=self.selected_scheme)

        # associate menu with the Menubutton
        menu_button["menu"] = menu

        menu_button.pack(expand=True)

def main():
    return

if __name__ == "__main__":
    app = App()
    app.mainloop()