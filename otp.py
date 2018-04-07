#!/usr/bin/env python
import os, sys       # do not use any other imports/libraries
# specify here how much time your solution required
#By Rashad Suleymanov


def bytestring_to_int(s):
    i = 0
    for c in s:
        i = i << 8
        i = i | ord(c)
    return i
    
    

def int_to_bytestring(i, l):
    # your implementation here
    s = ''
    for c in xrange(0,l):
        tmp = chr(i & 255)
        i = i >> 8
        s = tmp + s
    return s


def encrypt(pfile, kfile, cfile):
    # your implementation here
    #print pfile
    msg_str = open(pfile).read()
    key_str = os.urandom(len(msg_str))
    
    n = open(kfile, "w")
    n.write(key_str)
    n.close()

    msg_int = bytestring_to_int(msg_str)
    key_int = bytestring_to_int(key_str)
    chipher_int = msg_int ^ key_int
    chipher_str = int_to_bytestring(chipher_int, len(key_str))

    n = open(cfile, "w")
    n.write(chipher_str)
    n.close()
   
    pass
    

def decrypt(cfile, kfile, pfile):
    # your implementation here
    cipher_str = open(cfile).read()
    key_str = open(kfile).read()

    cipher_int = bytestring_to_int(cipher_str)
    key_int = bytestring_to_int(key_str)
    msg_int = cipher_int ^ key_int
    msg_str = int_to_bytestring(msg_int, len(key_str))
    n = open(pfile, "w")
    n.write(msg_str)
    n.close()
    
    
    pass

def usage():
    print "Usage:"
    print "encrypt <plaintext file> <output key file> <ciphertext output file>"
    print "decrypt <ciphertext file> <key file> <plaintext output file>"
    sys.exit(1)

if len(sys.argv) != 5:
    usage()
elif sys.argv[1] == 'encrypt':
    encrypt(sys.argv[2], sys.argv[3], sys.argv[4])
elif sys.argv[1] == 'decrypt':
    decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
else:
    usage()
