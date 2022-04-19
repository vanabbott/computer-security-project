#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import rsa
import vigenere



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1300x1000')
        self.title('Message Encryption and Decryption')


        # message input entry 
        message_input = ttk.Label(self, text="Input Message to Encrypt")
        self.message = tk.StringVar()
        txtbx = ttk.Entry(self, textvariable=self.message)

        # encryption key input entry
        encryption_key_input = ttk.Label(self, text="Input Key to Encrypt Message with")
        self.encryptKey = tk.StringVar()
        txtbxEK = ttk.Entry(self, textvariable=self.encryptKey)

        # cipher output textbox
        encrypted_message = ttk.Label(self, text="Encrypted Message:")
        self.new_cipher = tk.Text(self, height=9, width=75)
        
        # cipher input entry
        cipher_input = ttk.Label(self, text="Input Cipher to Decrypt")
        self.cipher = tk.StringVar()
        txtbxD = ttk.Entry(self, textvariable=self.cipher)

        # decryption key input entry
        decryption_key_input = ttk.Label(self, text="Input Key to Decrypt Cipher with")
        self.decryptKey = tk.StringVar()
        txtbxDK = ttk.Entry(self, textvariable=self.decryptKey)

        # decrypted message output textbox
        decrypted_message = ttk.Label(self, text="Decrypted Message:")
        self.orig_message = tk.Text(self, height=12, width=75)
        
        # Menubutton variable
        self.selected_scheme = tk.StringVar()
        self.selected_scheme.trace("w", self.change_scheme_label)
        # create the menu button
        self.schemeLabel = tk.Label()
        # select scheme widget
        self.create_menu_button()

        # encryption widgets
        message_input.pack()
        txtbx.pack()
        encryption_key_input.pack()
        txtbxEK.pack()
        self.create_enc_button()
        encrypted_message.pack()
        self.new_cipher.pack()

        # decryption widgets
        cipher_input.pack()
        txtbxD.pack()
        decryption_key_input.pack()
        txtbxDK.pack()
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
        
        # check which encryption scheme was selected and encrypt accordingly
        if self.selected_scheme.get() == "RSA":
            if self.encryptKey.get():
                c = rsa.encrypt(self.message.get(), self.encryptKey.get())
            else:
                c = rsa.encrypt(self.message.get())
        elif self.selected_scheme.get() == "Vigenere":
            c = vigenere.encrypt(self.message.get(), self.encryptKey.get())
        elif self.selected_scheme.get() == "Triple DES":
            # IMPLEMENT DES ENCRYPTION HERE ON self.message.get() USING self.encryptKey.get()
            #
            # NOT DONE
            #
            c = "NOT YET DEVELOPED"

        elif self.selected_scheme.get() == "AES":
            # IMPLEMENT AES ENCRYPTION HERE ON self.message.get() USING self.encryptKey.get()
            #
            # NOT DONE
            #
            c = "NOT YET DEVELOPED"
        else:
            c = "Please select a security scheme"
        
    
        self.new_cipher.insert("1.0", c)
        
        return

    # action when encryption button is pressed
    # decrypt cipher and write it to orig_message textbox
    def perform_message_decrypt(self, *args):
        # delete any leftover data in decrypted message box
        self.orig_message.delete("1.0",tk.END)
        
        # check which decryption scheme was selected and decrypt accordingly

        if self.selected_scheme.get() == "RSA":
            if self.decryptKey.get():
                om = rsa.decrypt(self.cipher.get(), self.decryptKey.get())
            else:
                om = rsa.decrypt(self.cipher.get())
        elif self.selected_scheme.get() == "Vigenere":
            om = vigenere.decrypt(self.cipher.get(), self.decryptKey.get())
        elif self.selected_scheme.get() == "Triple DES":
            # IMPLEMENT DES DECRYPTION HERE ON self.cipher.get() USING self.decryptKey.get()
            #
            # NOT DONE
            #
            om = "NOT YET DEVELOPED"
        elif self.selected_scheme.get() == "AES":
            # IMPLEMENT AES DECRYPTION HERE ON self.cipher.get() USING self.decryptKey.get()
            #
            # NOT DONE
            #
            om = "NOT YET DEVELOPED"
        else:
            om = "Please select a security scheme"

        self.orig_message.insert('end', om)
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