#!/usr/bin/env python3
import binascii
import codecs
from math import gcd
import gmpy2 as gmp
from gmpy2 import mpz

#default_p = 448500690975152607978063537675655100228561968640743033264994624907311301727954618776592131432970453319274164757456900360809613450208308427051224715601825715694126659023243326653708932560006426538354434994211909696350939307259469268464399327307567418024237505252087309516604048747469861472120690296679
#default_q = 797142830676371202783106590305499953807978464831617412146739794698696574269657813361892048534053769911087232366556200569808067035904716519320282044787921526677805285799163501701004063525600697748650815091626560388355572839685532622148490117538712600176513505164969571526664640345723199170240816113027
p = mpz()
q = mpz()
n = mpz()
phi_n = mpz()

e = mpz()
d = mpz()
r = mpz()
r = gmp.mpz_urandomb(gmp.random_state(42), 1024)
p = gmp.next_prime(r)
q = gmp.next_prime(p)



n = gmp.mul(p, q)
phi_n = gmp.mul(gmp.sub(p, 1), gmp.sub(q, 1))
e = -1
while e < 0:
    tr = gmp.mpz_urandomb(gmp.random_state(42), 1020)
    temp = gmp.next_prime(tr)
    if temp < phi_n:
        e = temp
e = gmp.sub(phi_n, 1)
d = gmp.invert(e, phi_n)
#print("Public Key: "+str(e)+","+str(n))
#print("Private Key: " +str(d)+","+str(n))

def encrypt(m, key=str(e)+","+str(n)):
    ee, nn = key.split(",")
    ee = mpz(ee)
    nn = mpz(nn.strip())
    m = m.strip()
    b = bytes(m, 'UTF-8')
    t = int.from_bytes(b, byteorder='big', signed=False)
    c = gmp.powmod(t, ee, nn)
    return str(c)

def decrypt(c, key=str(d)+","+str(n)):
    dd, nn = key.split(",")
    dd = mpz(dd)
    nn = mpz(nn.strip())
    c = c.strip()
    m = gmp.powmod(mpz(c), dd, nn)
    b = gmp.to_binary(m)

    b = bytes(reversed(b))
    return str(b.decode())


