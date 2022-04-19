#!/usr/bin/env python3
import binascii
message = '0110100001100101011011000110110001101111001000000110010101100100'
cipher = '1100101011101101101000100110010101011111101101110011100001110011'
key3 = '0100110001001111010101100100010101000011010100110100111001000100,1010100001101010011011111010101100100000111001000100010011000100,1111010101100100010101000011010100110100111001000100010011000100'
shifts = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
SBOX = [
# Box-1
[
[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
[0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
[4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
[15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
],
# Box-2

[
[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10],
[3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
[0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
[13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
],

# Box-3

[
[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
[13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
[13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
[1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]

],

# Box-4
[
[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
[13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
[10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
[3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
],

# Box-5
[
[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
[14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
[4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
[11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
],
# Box-6

[
[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
[10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
[9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
[4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]

],
# Box-7
[
[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
[13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
[1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
[6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
],
# Box-8

[
[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
[1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
[7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
[2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
]

]
ip = [58, 50, 42, 34, 26, 18, 10, 2, 
60, 52, 44, 36, 28, 20, 12, 4, 62, 
54, 46, 38, 30, 22, 14, 6, 64, 56, 
48, 40, 32, 24, 16, 8, 57, 49, 41, 
33, 25, 17, 9, 1, 59, 51, 43, 35,
27, 19,	11,	3, 61, 53, 45, 37, 29,
21,	13,	5, 63, 55, 47, 39, 31, 23, 15, 7]

ip_1 = [40,	8,	48,	16,	56,	24,	64,	32,
39,	7,	47,	15,	55,	23,	63,	31,
38,	6,	46,	14,	54,	22,	62,	30,
37,	5,	45,	13,	53,	21,	61,	29,
36,	4,	44,	12,	52,	20,	60,	28,
35,	3,	43,	11,	51,	19,	59,	27,
34,	2,	42,	10,	50,	18,	58,	26,
33,	1,	41,	9,	49,	17,	57,	25]
pc1 = [57,	49,	41,	33,	25,	17,	9,
1,	58,	50,	42,	34,	26,	18,
10,	2,	59,	51,	43,	35,	27,
19,	11,	3,	60,	52,	44,	36,
63,	55,	47,	39,	31,	23,	15,
7,	62,	54,	46,	38,	30,	22,
14,	6,	61,	53,	45,	37,	29,
21,	13,	5,	28,	20,	12,	4]
pc2 = [14, 17,   11,	24,	1,	5,
3,	28,	15,	6,	21,	10,
23,	19,	12,	4,	26,	8,
16,	7,	27,	20,	13,	2,
41,	52,	31,	37,	47,	55,
30,	40,	51,	45,	33,	48,
44,	49,	39,	56,	34,	53,
46,	42,	50,	36,	29,	32]
e = [32, 1,	2,	3,	4,	5,
4,	5,	6,	7,	8,	9,
8,	9,	10,	11,	12,	13,
12,	13,	14,	15,	16,	17,
16,	17,	18,	19,	20,	21,
20,	21,	22,	23,	24,	25,
24,	25,	26,	27,	28,	29,
28,	29,	30,	31,	32,	1]

p =[16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,10,
2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

def b2d(b):
    return int(b, 2)
def d2b(d):
    return bin(d)[2:].zfill(4)

def permute_1(key, table):
    key_m = ''
    for x in table:
        key_m += key[x-1]
    return key_m

def XOR(b1, b2):
    result = ""
    for index in range(len(b1)):
        if b1[index] == b2[index]:
            result += '0'
        else:
            result +='1'
    return result

def shift_left(string, n):
    return string[n:]+string[:n]

def gen_keys(k):
    k = permute_1(k, pc1)
    c0 = k[:28]
    d0 = k[28:]

    keys = list()
    for i, r in enumerate(shifts):
        cn = shift_left(c0, r)
        dn = shift_left(d0, r)
        #print(len(dn))
        key_m = permute_1(cn+dn, pc2)
        keys.append(key_m)
        #print("Key " + str(i+1) + ": " + key_m)
        d0 = dn
        c0 = cn
    return keys

def encrypt(m, key):
    keys = gen_keys(key)
    m_ip = permute_1(m, ip)
    l0 = m_ip[:32]
    r0 = m_ip[32:]
    i = 0
    while i <= 15:
        l1 = r0
        r1 = XOR(l0, func_f(r0, keys[i]))
        r0 = r1
        l0 = l1
        i+=1

    c = permute_1(r1 + l1, ip_1)
    return c

def decrypt(c, key):
    keys = gen_keys(key)
    c_ip = permute_1(c, ip)
    #print(c_ip)
    l0 = c_ip[0:32]
    r0 = c_ip[32:64]
    i = 15
    while i >= 0:
        l1 = r0
        r1 = XOR(l0, func_f(r0, keys[i]))
        r0 = r1
        l0 = l1
        i-=1

    om = permute_1(r1 + l1, ip_1)
    return om

def func_f(r, k):
    er = permute_1(r, e)
    k_er = XOR(er, k)
    result = ""

    for i, s in enumerate(SBOX):
        sixbit = ""
        sixbit = k_er[i*6:i*6+6]
        result += d2b(s[b2d(sixbit[0]+sixbit[5])][b2d(sixbit[1:5])])

    return permute_1(result, p)

def bin_asc(b):
    bi = int(b, 2)
    bn = bi.bit_length() + 7 // 8
    ba = bi.to_bytes(bn, "big")
    return ba.decode()

def triple_encrypt(m, key):
    three_keys = key.split(",")
    c1 = encrypt(m, three_keys[0])
    m2 = decrypt(c1, three_keys[1])
    c2 = encrypt(m2, three_keys[2])
    return c2


def triple_decrypt(c, key):
    c = c.strip()
    #c = ''.join(format(ord(i), '08b') for i in c)
    three_keys = key.split(",")
    m1 = decrypt(c, three_keys[2])
    c2 = encrypt(m1, three_keys[1])
    m2 = decrypt(c2, three_keys[0])
    return bin_asc(m2)

def split_bits(b):
    bit_array = list()
    n = len(b)
    segments = n//64
    for i in range(segments):
        bit_array.append(b[64*i:i*64+64])

    return bit_array

def pad_str(s):
    sn = s.strip()
    n = len(sn)
    if n % 8 != 0:
        for i in range((n//8)*8+8 - n):
            sn += '|'
    return sn

def iter_te(m, key=key3):
    cba = list()
    m = pad_str(m)
    m = ''.join(format(ord(i), '08b') for i in m.strip())
    mba = split_bits(m)
    for b in mba:
        cba.append(triple_encrypt(b,key))
    return ''.join(cba)

def iter_td(c, key=key3):
    mba = list()
    c = c.strip()
    cba = split_bits(c)
    for b in cba:
        mba.append(triple_decrypt(b,key))
    return str(''.join(mba))