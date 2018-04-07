#!/usr/bin/python

import hashlib, sys

sys.path = sys.path[1:] # removes script directory from hmac.py search path
import hmac # do not use any other imports/libraries
#print "[?] Enter key:",
#key = raw_input()

def mac(filename):
    print "[?] Enter key:",
    key = raw_input()
    digest = readAndDigest(filename, key)
    print "Calculated HMAC-SHA256:", digest
    print "[+] Writing HMAC DigestInfo to", filename+".hmac"
    writeDigest(filename,digest)

def readAndDigest(filename, key):
    f = open(filename, 'rb')
    digest_maker = hmac.new(key,'None', hashlib.sha256)
    while True:
        data = f.read(512)
        if data == "":
            break
        digest_maker.update(data)
    digest = digest_maker.hexdigest()
    f.close()
    return digest

def writeDigest(filename, digest):
    g = open(filename+".hmac", "wb")
    g.write(digest)
    g.close()
    pass

def readHashFile(filename):
    hData = open(filename+".hmac").read()
    return hData

def verify(filename):
    print "[+] Reading HMAC DigestInfo from", filename+".hmac"
    hashData = readHashFile(filename)
    print "HMAC-SHA256 digest: ", hashData
    print "[?] Enter key:",
    key = raw_input()
    digest_calculated = readAndDigest(filename, key)
    if digest_calculated != hashData:
        print "[-] Wrong key or message has been manipulated!"
    else:
        print "[+] HMAC verification successful!"


def usage():
    print "Usage:"
    print "-verify <filename>"
    print "-mac <filename>"
    sys.exit(1)

if len(sys.argv) != 3:
    usage()
elif sys.argv[1] == '-mac':
    mac(sys.argv[2])
elif sys.argv[1] == '-verify':
    verify(sys.argv[2])
else:
    usage()
