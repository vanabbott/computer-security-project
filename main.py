#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import rsa

schemeLabel = tk.Label
message = ''

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1300x1000')
        self.title('Message Encryption and Decryption')


        # message input entry 
        self.message = tk.StringVar()
        txtbx = ttk.Entry(self, textvariable=self.message)

        # cipher output textbox
        encrypted_message = ttk.Label(self, text="Encrypted Message:")
        self.new_cipher = tk.Text(self, height=9, width=75)
        
        
        # cipher input entry
        self.cipher = tk.StringVar()
        txtbxD = ttk.Entry(self, textvariable=self.cipher)

        # decrypted message output textbox
        decrypted_message = ttk.Label(self, text="Decrypted Message:")
        self.orig_message = tk.Text(self, height=12, width=75)
        
        # Menubutton variable
        self.selected_scheme = tk.StringVar()
        self.selected_scheme.trace("w", self.change_scheme_label)
        # create the menu button

        # select scheme widget
        self.create_menu_button()

        # encryption widgets
        txtbx.pack()
        self.create_enc_button()
        encrypted_message.pack()
        self.new_cipher.pack()

        # decryption widgets
        txtbxD.pack()
        self.create_dec_button()
        decrypted_message.pack()
        self.orig_message.pack()
    
    # encryption button
    def create_enc_button(self):
        cb = ttk.Button(self, text='encrypt', command=self.perform_message_encrypt)
        cb.pack()

    # decryption button
    def create_dec_button(self):
        cb = ttk.Button(self, text='decrypt', command=self.perform_message_decrypt)
        cb.pack()
    
    # action when encryption button is pressed
    # encrypt message and write it to new_cipher textbox
    def perform_message_encrypt(self, *args):
        self.new_cipher.delete("1.0",tk.END)
        self.new_cipher.pack()
        self.new_cipher.insert("1.0", rsa.encrypt(self.message.get()))
        self.new_cipher.pack()
        return

    # action when encryption button is pressed
    # decrypt message and write it to orig_message textbox
    def perform_message_decrypt(self, *args):

        self.orig_message.delete("1.0",tk.END)
        self.orig_message.pack()
        om = rsa.decrypt(self.cipher.get())
        print(om)
        self.orig_message.insert("1.0", om)
        self.orig_message.pack()

        '''
        c = self.cipher.get("1.0", tk.END)
        om = rsa.decrypt(c)
        print(om)
        self.orig_message.insert("1.0", om)
        self.orig_message.pack()
        '''
        return


    # change title when different scheme is selected
    def change_scheme_label(self, *args):
        self.title('Message Encryption and Decryption for the '+self.selected_scheme.get() + ' scheme')

    # create drop down scheme selector menu
    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        schemes = ('RSA', 'Vigenere', 'Triple DES', 'AES')

        # create the Menubutton
        menu_button = ttk.Menubutton(self, text='Select a scheme')

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