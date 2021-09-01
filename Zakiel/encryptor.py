import string
import random
import itertools
import sys
from time import sleep

'''
Main Encryptor for Zakiel file.
'''


class Encrypt:
    def __init__(self, text, EncryptCode: tuple) -> None:

        # EncryptCode = (dupliCount:first_duplication, sliceCount:second_slicing)

        self.text = text
        self.ecode = EncryptCode
        self.dupli = []
        self.sli = []

    def first_duplication(self) -> None:
        # Getting a list from the text
        textList = [i for i in self.text]
        # Looping through the Text List
        for char in textList:
            # Constructing a Temporary list to be appended to the Duplicated List (self.dupli)
            dupli = []
            dupli.clear()
            # Generating an iterator from range(given the first value of the EncryptCode)
            for integer in range(int(self.ecode[0])):
                '''
                If i (an integer) is divisible by 2 (even) then the character will be appended
                to the Temporary list first before the integer (i), or else the integer (i) will
                be appended to the Temporary list first before the character.
                '''
                state = (integer % 2) == 0
                if state:
                    dupli.append(char)
                    dupli.append(str(integer))
                else:
                    dupli.append(str(integer))
                    dupli.append(char)
            # Finally appending the Temporary list to the Duplicated list with a newline
            self.dupli.append(dupli)

    def second_slicing(self) -> None:
        Ftemp_list = []
        Stemp_list = []

        # Decompressing the 2D duplicated list
        for temp_list in self.dupli:
            '''
            Slicing each List in Duplicated List and appending it into two
            separate temporary lists (Ftemp_list, Stemp_list)
            '''
            Ftemp_list.append(temp_list[0:(len(temp_list) // 2 - 1)])
            Stemp_list.append(
                temp_list[len(temp_list) // 2:len(temp_list) - 1])

        # Reversing the Second temporary list
        rev_Stemp_list = list(reversed(Stemp_list))

        for idx in range(len(rev_Stemp_list)):
            state = (idx % 2) == 0
            if state:
                self.sli.append(rev_Stemp_list[idx])
                self.sli.append(Ftemp_list[idx])
            else:
                self.sli.append(Ftemp_list[idx])
                self.sli.append(rev_Stemp_list[idx])


class Decrypt:
    def __init__(self, DecryptCode: tuple) -> None:
        pass


ecode = (44,)

enc = Encrypt('Hello Im Being Duplicated all over', ecode)
enc.first_duplication()
enc.second_slicing()
some_list = ['a', 'b', 'c']

inversed_list = list(reversed(some_list))

print(enc.sli)
