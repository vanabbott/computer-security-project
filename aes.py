#!/usr/bin/env python3

state_array = [[0 for x in range(4)] for x in range(4)]
s_box = [[]]
inv_s_box = [[]]

def sub_bytes(state_array, s_box):
    return state_array

def inv_sub_bytes(state_array, inv_s_box):
    return state_array

def shift_rows(state_array):
    return state_array

def inv_shift_rows(state_array):
    return state_array

def mix_columns(state_array):
    pass

def inv_mix_columns(state_array):
    pass

def add_round_key(state_array, round_key):
    pass

def inv_add_round_key(state_array, round_key):
    pass

def aes_round(state_array, round_key):
    state_array = sub_bytes(state_array, s_box)
    state_array = shift_rows(state_array)
    state_array = mix_columns(state_array)
    state_array = add_round_key(state_array, round_key)
    return state_array

def aes_final_round(state_array, round_key):
    state_array = sub_bytes(state_array, s_box)
    state_array = shift_rows(state_array)
    state_array = add_round_key(state_array)
    return state_array

def aes_inv_round(state_array, round_key):
    inv_sub_bytes(state_array, inv_s_box)
    inv_shift_rows(state_array)
    inv_add_round_key(state_array, round_key)
    inv_mix_columns(state_array)
    return state_array

def aes_inv_final_round(state_array, round_key):
    inv_sub_bytes(state_array, inv_s_box)
    inv_shift_rows(state_array)
    inv_add_round_key(state_array, round_key)
    return state_array

def encrypt(message, cipher_key):
    if len(cipher_key) == 16:
        rounds = 10
    elif len(cipher_key) == 24:
        rounds = 12
    elif len(cipher_key) == 32:
        rounds = 14

    for block in blocks:
        pass
    

def decrypt(cyphertext, cipher_key):
    pass
