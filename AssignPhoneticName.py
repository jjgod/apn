#!/usr/bin/python

import argparse, sys, pinyin
import AddressBook

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reset", action="store_true", default=False,
                    help="reset the entries with a phonetic name already")
parser.add_argument("-d", "--dryrun", action="store_true", default=False,
                    help="do not alter the entries, only print output")
args = parser.parse_args()

def is_cjk_char(x):
    # Punct & Radicals
    if x >= 0x2e80 and x <= 0x33ff:
        return 1

    # Fullwidth Latin Characters
    if x >= 0xff00 and x <= 0xffef:
        return 1

    # CJK Unified Ideographs &
    # CJK Unified Ideographs Extension A
    if x >= 0x4e00 and x <= 0x9fbb:
        return 1
    # CJK Compatibility Ideographs
    if x >= 0xf900 and x <= 0xfad9:
        return 1

    # CJK Unified Ideographs Extension B
    if x >= 0x20000 and x <= 0x2a6d6:
        return 1

    # CJK Compatibility Supplement
    if x >= 0x2f8000 and x <= 0x2fa1d:
        return 1

    return 0

def contain_cjk_char(line):
    # print "@: %s" % (line.encode("utf-8")) 

    for ch in line:
       if is_cjk_char(ord(ch)):
           return 1

    return 0

def assign_pinyin(person, propertyName, phoneticPropertyName):
    name = person.valueForProperty_(propertyName)

    if name and contain_cjk_char(name):
        pname = person.valueForProperty_(phoneticPropertyName)
        if not args.reset and pname:
            return None

        name_py = pinyin.hanzi2pinyin(name).capitalize()
        if not args.dryrun:
            person.setValue_forProperty_(name_py, phoneticPropertyName)

        return (name, name_py)

    return None

ab = AddressBook.ABAddressBook.sharedAddressBook()

for person in ab.people():
    lname_pair = assign_pinyin(person,
                               AddressBook.kABLastNameProperty,
                               AddressBook.kABLastNamePhoneticProperty)
    fname_pair = assign_pinyin(person,
                               AddressBook.kABFirstNameProperty,
                               AddressBook.kABFirstNamePhoneticProperty)

    if fname_pair or lname_pair:
        print "%s%s (%s%s%s)" % ((lname_pair and lname_pair[0]) or "",
                                 (fname_pair and fname_pair[0]) or "",
                                 (lname_pair and lname_pair[1]) or "",
                                 (fname_pair and fname_pair and " ") or "",
                                 (fname_pair and fname_pair[1]) or "")

print "Done."
ab.save()

