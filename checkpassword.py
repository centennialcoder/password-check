#
# checkpassword.py - check for most common 1000 passwords
# 
#

import sys
import argparse

usage = \
"""
checkpassword.py - Check if password is 1000 most common

Usage:
    checkpassword [password]
Returns:
    "Not common password" or
    "Common password"
"""

def ReadPasswords():
    pwFile = "1000-most-common-passwords.txt" 
    with open(pwFile, "r") as f:      
        passwords = f.read().splitlines()
    return passwords

if sys.argv.count == 1:
    print(usage)
    sys.exit(1)

parser = argparse.ArgumentParser(description='Check a password for low entropy')
parser.add_argument('testPassword', metavar='testPassword', type=str)
args = parser.parse_args()

passwords = ReadPasswords()

if args.testPassword in passwords:
    print("Common password")
else:
    print("Not common password")



        

    
    