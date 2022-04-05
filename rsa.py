#!/usr/bin/env python3
import binascii
from math import gcd
p = 448500690975152607978063537675655100228561968640743033264994624907311301727954618776592131432970453319274164757456900360809613450208308427051224715601825715694126659023243326653708932560006426538354434994211909696350939307259469268464399327307567418024237505252087309516604048747469861472120690296679
q = 797142830676371202783106590305499953807978464831617412146739794698696574269657813361892048534053769911087232366556200569808067035904716519320282044787921526677805285799163501701004063525600697748650815091626560388355572839685532622148490117538712600176513505164969571526664640345723199170240816113027

n = p * q
phi_n = (p-1) * (q-1)

e = int(phi_n) - 1
d = pow(e, -1, int(phi_n))

def coprime(a, b):
    return gcd(a,b) == 1

def encrypt(m):
    m = m.strip()
    b = bytes(m, 'utf-8')
    c = pow(int.from_bytes(b, byteorder='big', signed=False), int(e), int(n))
    return str(c)

def decrypt(c):
    c = c.strip()
    m = pow(int(c), int(d), int(n))
    b = bin(m)
    bi = int(b, 2)
    bn = bi.bit_length() * 7 // 8
    ba = bi.to_bytes(bn, "big")
    return str(ba.decode())

