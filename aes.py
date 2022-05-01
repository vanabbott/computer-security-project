#!/usr/bin/env python3

import codecs

globalKey = '2b7e151628aed2a6'
def XOR(b1, b2):
    one = len(b1)
    two = len(b2)
    if one < two:
        t = b1
        b1 = b2
        b2 = t
        t = one
        one = two
        two = t

    result = ""
    dif = one-two
    for _ in range(dif):
        b2 = '0'+b2
    for index in range(one):
        if b1[index] == b2[index]:
            result += '0'
        else:
            result +='1'
    return result

def xor(s1, s2):
    return tuple(a^b for a,b in zip(s1, s2))

class AES(object):
    Gmul = {}
    Rcon = ( 0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a )
    Sbox = (
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            )
    Sbox_inv = (
            0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
            0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
            0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
            0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
            0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
            0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
            0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
            0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
            0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
            0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
            0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
            0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
            0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
            0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
            0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
            )

    @staticmethod
    def rot_word(word):
        return word[8:] + word[:8]

    @staticmethod
    def sub_word(word):
        s = ''
        n = len(word)//8
        for i in range(n):  
            w = int(word[i*n:i*n+n], 2)
            s += bin(AES.Sbox[w])[2:]
        return s

    def key_schedule(self):
        expanded = []
        n = len(self.key)//self.nk
        for i in range(self.nk):
            expanded.append(self.key[i*n:i*n+n])
        
        for i in range(self.nk, self.nb * (self.nr+1)):
            t = expanded[i-1]
            if i % self.nk == 0:
                r = AES.rot_word(t)
                t = XOR( AES.sub_word( AES.rot_word(t) ), bin(AES.Rcon[i // self.nk])[2:]+"000000000000000000000000" )
            expanded.append( XOR(t, expanded[i-self.nk]))
        return expanded

    def add_round_key(self, rkey):
        k = ''.join(rkey)
        return XOR(str(self.state), k)

    def sub_bytes(self):
        s = ''
        n = len(self.state)//8
        for i in range(n):  
            w = int(self.state[i*8:i*8+8], 2)
            t = bin(AES.Sbox[w])[2:]
            z = ''
            if len(t) < 8:
                for _ in range(8-len(t)):
                    z+='0'
                t
            s = s+ z +t
        self.state = ''
        self.state = s

    def inv_sub_bytes(self):
        s = ''
        n = len(self.state)//8
        for i in range(n):  
            w = int(self.state[i*8:i*8+8], 2)
            t = bin(AES.Sbox_inv[w])[2:]
            z = ''
            if len(t) < 8:
                for _ in range(8-len(t)):
                    z+='0'
                t
            s = s+ z +t
        self.state = ''
        self.state = s

    def blockerize(self):
        n = (self.nk * 4)
        b = ['']*(n)
        for i in range(n):
            t = self.state[i*8:(i*8)+8]
            b[i] = t
        return b

    def shift_rows(self):
        rows = []
        s = self.blockerize()
        for r in range(4):
            rows.append( s[r::4] )
            rows[r] = rows[r][r:] + rows[r][:r]
        s = [ r[c] for c in range(4) for r in rows ]
        self.state = ''.join(s)

    def inv_shift_rows(self):
        rows = []
        s = self.blockerize()
        for r in range(4):
            rows.append( s[r::4] )
            rows[r] = rows[r][4-r:] + rows[r][:4-r]
        s = [ r[c] for c in range(4) for r in rows ]
        self.state = ''.join(s)

    @staticmethod
    def gmul(a, b):
        p = 0
        for c in range(8):
            if b & 1:
                p ^= a
            a <<= 1
            if a & 0x100:
                a ^= 0x11b
            b >>= 1
        return p

    def mix_columns(self):
        ss = []
        s = self.blockerize()
        for f in (0x02, 0x03, 0x0e, 0x0b, 0x0d, 0x09):
                self.Gmul[f] = tuple(self.gmul(f, x) for x in range(0,0x100))
        for c in range(4):
            col = []
            c = s[c*4:(c+1)*4]
            for i, n in enumerate(c):
                col.append(int(n,2))
            a = bin(self.Gmul[0x02][col[0]] ^ self.Gmul[0x03][col[1]] ^ col[2] ^ col[3])[2:]
            for _ in range(8-len(a)):
                a = '0'+a
            b = bin(col[0]  ^ self.Gmul[0x02][col[1]] ^ self.Gmul[0x03][col[2]] ^                 col[3])[2:]
            for _ in range(8-len(b)):
                b = '0'+b
            c = bin(col[0]  ^                 col[1]  ^ self.Gmul[0x02][col[2]] ^ self.Gmul[0x03][col[3]])[2:]
            for _ in range(8-len(c)):
                c = '0'+c
            d = bin(self.Gmul[0x03][col[0]] ^                 col[1]  ^                 col[2]  ^ self.Gmul[0x02][col[3]])[2:]
            for _ in range(8-len(d)):
                d = '0'+d
            ss.extend((a, b, c, d))
        self.state = ''.join(ss)
        self.Gmul = {}

    def inv_mix_columns(self):
        ss = []
        s = self.blockerize()
        for f in (0x02, 0x03, 0x0e, 0x0b, 0x0d, 0x09):
                self.Gmul[f] = tuple(self.gmul(f, x) for x in range(0,0x100))
        for c in range(4):
            col = []
            c = s[c*4:(c+1)*4]
            for i, n in enumerate(c):
                col.append(int(n,2))
            a = bin(self.Gmul[0x0e][col[0]] ^ self.Gmul[0x0b][col[1]] ^ self.Gmul[0x0d][col[2]] ^ self.Gmul[0x09][col[3]])[2:]
            for _ in range(8-len(a)):
                a = '0'+a
            b = bin(self.Gmul[0x09][col[0]] ^ self.Gmul[0x0e][col[1]] ^ self.Gmul[0x0b][col[2]] ^ self.Gmul[0x0d][col[3]])[2:]
            for _ in range(8-len(b)):
                b = '0'+b
            c = bin(self.Gmul[0x0d][col[0]] ^ self.Gmul[0x09][col[1]] ^ self.Gmul[0x0e][col[2]] ^ self.Gmul[0x0b][col[3]])[2:]
            for _ in range(8-len(c)):
                c = '0'+c
            d = bin(self.Gmul[0x0b][col[0]] ^ self.Gmul[0x0d][col[1]] ^ self.Gmul[0x09][col[2]] ^ self.Gmul[0x0e][col[3]])[2:]
            for _ in range(8-len(d)):
                d = '0'+d
            ss.extend((a, b, c, d))

        self.state = ''.join(ss)
        self.Gmul = {}
    
    def bin_asc(self, b):
        bi = int(b, 2)
        bn = bi.bit_length() + 7 // 8
        ba = bi.to_bytes(bn, "big")
        return ba.decode()

    def cipher(self, block):
        n = self.nk
        self.state = block
        keys = self.key_schedule()
        self.add_round_key(keys[0:n])

        for r in range(1, self.nr):
            self.sub_bytes()
            self.shift_rows()
            self.mix_columns()
            k = keys[r*n:(r+1)*n]
            self.add_round_key(k)

        self.sub_bytes()
        self.shift_rows()
        self.add_round_key(keys[self.nr*n:])
        return self.state

    def inv_cipher(self, block):
        n = self.nk
        self.state = block
        keys = self.key_schedule()
        k = keys[self.nr*n:(self.nr+1)*n]
        self.add_round_key(k)
        for r in range(self.nr-1, 0, -1):
            self.inv_shift_rows()
            self.inv_sub_bytes()
            k = keys[r*n:(r+1)*n]
            self.add_round_key(k)
            self.inv_mix_columns()

        self.inv_shift_rows()
        self.inv_sub_bytes()
        self.add_round_key(keys[0:n])
        return self.state

    def verifyKey(self, key):
        if len(key) >= 16:
            self.key = ''.join(format(ord(i), '08b') for i in key[:16])
        else:
            self.key = ''.join(format(ord(i), '08b') for i in globalKey)
    


class AES2(AES):
    def __init__(self):
        self.nb = 4
        self.nr = 10
        self.nk = 4

def split_bits(b):
    bit_array = list()
    n = len(b)
    segments = n//128
    for i in range(segments):
        bit_array.append(b[128*i:i*128+128])

    return bit_array

def pad_str(s):
    sn = s.strip()
    n = len(sn)
    if n % 8 != 0:
        for i in range((n//16)*16+16 - n):
            sn += '|'
    return sn

def encrypt(m, key):
    crypt = AES2()
    crypt.verifyKey(key.strip())
    cba = list()
    m = pad_str(m)
    m = ''.join(format(ord(i), '08b') for i in m.strip())
    mba = split_bits(m)
    for b in mba:
        cba.append(crypt.cipher(b))
    
    return ''.join(cba)

def bin2asc(b):
    s = ''
    n = len(b)//8
    #print(b)
    for i in range(n):
        #print(b[i*8:i*8+8])
        #print(int(b[i*8:i*8+8],2))
        s += chr(int(b[i*8:i*8+8],2))
    return s

def decrypt(c, key):
    crypt = AES2()
    crypt.verifyKey(key.strip())
    cba = list()
    c = pad_str(c)
    mba = split_bits(c)
    for b in mba:
        cba.append(crypt.inv_cipher(b))
    t = ''.join(cba)
    return bin2asc(t)
