#!/usr/bin/env python3
import tkinter as tk
from tkinter import PhotoImage, ttk
import rsa
import vigenere
import des
import aes
import binascii



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('1100x800')
        self.title('Message Encryption and Decryption')
        self.resizable(False,False)
        self.backGroundImage = PhotoImage(file="images/security_background.png")
        self.backGroundImageLabel = tk.Label(self, image=self.backGroundImage)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)
        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.rowconfigure(2,weight=2)
        self.rowconfigure(3,weight=1)
        self.rowconfigure(4,weight=2)
        self.rowconfigure(5,weight=1)
        self.rowconfigure(6,weight=1)
        self.rowconfigure(7,weight=5)

        # message input entry 
        message_input = ttk.Label(self, text="Input Message to Encrypt")
        self.message = tk.StringVar()
        txtbx = ttk.Entry(self, textvariable=self.message)

        # encryption key input entry
        self.encrypt_message = tk.StringVar()
        self.encrypt_message.set("Input Key to Encrypt Message with")
        encryption_key_input = ttk.Label(self, textvariable=self.encrypt_message)
        self.encryptKey = tk.StringVar()
        txtbxEK = ttk.Entry(self, textvariable=self.encryptKey)

        # cipher output textbox
        encrypted_message = ttk.Label(self, text="Encrypted Message:")
        self.new_cipher = tk.Text(self, height=9, width=65)
        
        # cipher input entry
        cipher_input = ttk.Label(self, text="Input Cipher to Decrypt")
        self.cipher = tk.StringVar()
        txtbxD = ttk.Entry(self, textvariable=self.cipher)

        # decryption key input entry
        self.decrypt_message = tk.StringVar()
        self.decrypt_message.set("Input Key to Decrypt Cipher with")
        decryption_key_input = ttk.Label(self, textvariable=self.decrypt_message)
        self.decryptKey = tk.StringVar()
        txtbxDK = ttk.Entry(self, textvariable=self.decryptKey)

        # decrypted message output textbox
        decrypted_message = ttk.Label(self, text="Decrypted Message:")
        self.orig_message = tk.Text(self, height=9, width=65)
        
        # Menubutton variable
        self.selected_scheme = tk.StringVar()
        self.selected_scheme.set('Select a scheme')
        self.selected_scheme.trace("w", self.change_scheme_label)
        # create the menu button
        self.schemeLabel = tk.Label()
        # select scheme widget
        self.backGroundImageLabel.place(x=0, y=0)
        self.create_menu_button()


        #self.backGroundImageLabel.pack()
        # encryption widgets
        message_input.grid(column=0, row=1, sticky=tk.S)
        txtbx.grid(column=0, row=2, sticky=tk.N)
        encryption_key_input.grid(column=0, row=3, sticky=tk.S)
        txtbxEK.grid(column=0, row=4, sticky=tk.N)
        self.create_enc_button()
        encrypted_message.grid(column=0, row=6, sticky=tk.S)
        self.new_cipher.grid(column=0, row=7, sticky=tk.N)

        # decryption widgets
        cipher_input.grid(column=2, row=1, sticky=tk.S)
        txtbxD.grid(column=2, row=2, sticky=tk.N)
        decryption_key_input.grid(column=2, row=3, sticky=tk.S)
        txtbxDK.grid(column=2, row=4, sticky=tk.N)
        self.create_dec_button()
        decrypted_message.grid(column=2, row=6, sticky=tk.S)
        self.orig_message.grid(column=2, row=7, sticky=tk.N)
    
    # encryption button
    def create_enc_button(self):
        #self.enc_but = PhotoImage(file="images/encrypt_button.png", height=40, width=40)
        cb = ttk.Button(self, text='encrypt', command=self.perform_message_encrypt)
        cb.grid(column=0, row=5)

    # decryption button
    def create_dec_button(self):
        cb = ttk.Button(self, text='decrypt', command=self.perform_message_decrypt)
        cb.grid(column=2, row=5)
    
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
            if self.encryptKey.get():
                c = vigenere.encrypt(self.message.get(), self.encryptKey.get())
            else:
                c = "must enter key"
        elif self.selected_scheme.get() == "Triple DES":
            if self.encryptKey.get():
                c = des.iter_te(self.message.get(), self.encryptKey.get())
            else:
                c = des.iter_te(self.message.get())
            
        elif self.selected_scheme.get() == "AES":
            if self.encryptKey.get():
                c = aes.encrypt(self.message.get(), self.encryptKey.get())
            else:
                c = aes.encrypt(self.message.get(), '')
            
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
            if self.decryptKey.get():
                om = vigenere.decrypt(self.cipher.get(), self.decryptKey.get())
            else:
                om = "must enter key"
        elif self.selected_scheme.get() == "Triple DES":
            if self.decryptKey.get():
                om = des.iter_td(self.cipher.get(), self.decryptKey.get())
            else:
                om = des.iter_td(self.cipher.get())
            
        elif self.selected_scheme.get() == "AES":
            if self.decryptKey.get():
                om = aes.decrypt(self.cipher.get(), self.decryptKey.get())
            else:
                t = aes.decrypt(self.cipher.get(), '')
                #b = bytes(t, encoding='utf8')
                '''binary_int = int(t, 2)
                byte_number = binary_int.bit_length() + 7 // 8
                binary_array = binary_int.to_bytes(byte_number, "big")'''
                om = t

        else:
            om = "Please select a security scheme"
        print(om)
        self.orig_message.insert('1.0', om)
        return


    # change title when different scheme is selected
    def change_scheme_label(self, *args):
        self.title('Message Encryption and Decryption for the '+self.selected_scheme.get() + ' scheme')
        if self.selected_scheme.get() == 'RSA':
            self.encrypt_message.set("Input Key to Encrypt Message with e,n")
            self.decrypt_message.set("Input Key to Decrypt Message with d,n")
        elif self.selected_scheme.get() == 'Triple DES':
            self.encrypt_message.set("Input Key to Encrypt Message in form k1,k2,k3\neach being 64 bit binary")
            self.decrypt_message.set("Input Key to Decrypt Message in form k1,k2,k3\neach being 64 bit binary")
        elif self.selected_scheme.get() == 'AES':
            self.encrypt_message.set("Input Key to Encrypt Message with")
            self.decrypt_message.set("Input Key to Decrypt Message with")
        elif self.selected_scheme.get() == 'Vigenere':
            self.encrypt_message.set("Input Key to Encrypt Message with alphabetic characters")
            self.decrypt_message.set("Input Key to Decrypt Message with alphabetic characters")
        

    # create drop down scheme selector menu
    def create_menu_button(self):
        """ create a menu button """
        # menu variable
        schemes = ('RSA', 'Vigenere', 'Triple DES', 'AES')
        # create the Menubutton
        self.menu_button = ttk.Menubutton(self, textvariable=self.selected_scheme)

        # create a new menu instance
        menu = tk.Menu(self.menu_button, tearoff=0)
 
        for scheme in schemes:
            menu.add_radiobutton(
                label=scheme,
                value=scheme,
                variable=self.selected_scheme)

        # associate menu with the Menubutton
        self.menu_button["menu"] = menu

        self.menu_button.grid(column=1,row=0)

def main():
    return

if __name__ == "__main__":
    app = App()
    app.mainloop()
