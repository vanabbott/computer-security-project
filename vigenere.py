#!/usr/bin/env python3

from ctypes import sizeof

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rotate_alph_dec(alph, rotations):
    res = (alphabet * 3)[rotations-1 : len(alphabet) + rotations - 1]
    new_str = ""
    for index, letter in enumerate(alph):
        for i, l in enumerate(res):
            if l == letter:
                new_str += alphabet[i]
                break
    
    return new_str

def rotate_alph_enc(alph, rotations):
    res = (alphabet * 3)[len(alphabet) - (rotations-1) : 2*len(alphabet) - (rotations - 1)]
    new_str = ""
    for index, letter in enumerate(alph):
        for i, l in enumerate(res):
            if l == letter:
                new_str += alphabet[i]
                break
    
    return new_str

def find_index(let):
    i = 1
    for l in alphabet:
        if let == l:
            return i
        i += 1

def encrypt(message, key):
    message = message.replace(" ", "")
    key = key.replace(" ", "")
    period = len(key)
    alphs = []
    count = 0
    key = key.upper()
    message = message.upper()
    cipher = ""
    rotations = list()
    for l in key:
        alphs.append("")
        rotations.append(find_index(l))
    
    for l in message.replace(" ",""):
        alphs[count % period] += l
        count += 1
    
    for i in range(period):
        alphs[i] = rotate_alph_enc(alphs[i], rotations[i])

    for i in range(len(alphs[0])):
        for j in range(period):
            if i < len(alphs[j]) and j < len(alphs):
                cipher += alphs[j][i]

    return cipher


def decrypt(cipher, key):
    cipher = cipher.replace(" ", "")
    key = key.replace(" ", "")
    period = len(key)
    alphs = []
    count = 0
    key = key.upper()
    cipher = cipher.upper()
    message = ""
    rotations = list()
    for l in key:
        alphs.append("")
        rotations.append(find_index(l))
    
    for l in cipher.replace(" ",""):
        alphs[count % period] += l
        count += 1
    
    for i in range(period):
        alphs[i] = rotate_alph_dec(alphs[i], rotations[i])

    for i in range(len(alphs[0])):
        for j in range(period):
            if i < len(alphs[j]) and j < len(alphs):
                message += alphs[j][i]

    return message

