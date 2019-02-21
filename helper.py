"""
License
-------
    The MIT License (MIT)

    Copyright (c) 2017 Tashkel Project

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

Created on Sat Dec 16 22:46:28 2017

@author: Ahmad Barqawi
"""
import os
import glob
import string
import re
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize

#convert using chr(harakat[0])
harakat   = [1614,1615,1616,1618,1617,1611,1612,1613]
connector = 1617


def save_binary(data, file, folder):
    location  = os.path.join(folder, (file+'.pickle') )
    with open(location, 'wb') as ff:
        pickle.dump(data, ff, protocol=pickle.HIGHEST_PROTOCOL)

def load_binary(file, folder):
    location  = os.path.join(folder, (file+'.pickle') )
    with open(location, 'rb') as ff:
        data = pickle.load(ff)

    return data

def get_sentences(data):

    return [sent for line in re.split("[\n,،]+", data) if line for sent in sent_tokenize(line.strip()) if sent]
    #return [sent for line in data.split('\n') if line for sent in sent_tokenize(line) if sent]

def clear_punctuations(text):
    text = "".join(c for c in text if c not in string.punctuation)
    return text

def clear_english_and_numbers(text):
     text = re.sub(r"[a-zA-Z0-9٠-٩]", " ", text);
     return text

def is_tashkel(text):
    return any(ord(ch) in harakat for ch in text)

def clear_tashkel(text):
    text = "".join(c for c in text if ord(c) not in harakat)
    return text

def get_harakat():
    return "".join(chr(item)+"|" for item in harakat)[:-1]

def get_taskel(sentence):

    output = []
    current_haraka = ""
    for ch in reversed(sentence):

        if ord(ch) in harakat:
            if (current_haraka is "") or\
            (ord(ch) == connector and chr(connector) not in current_haraka) or\
            (chr(connector) == current_haraka):
                current_haraka += ch
        else:
            if current_haraka == "":
                current_haraka = "ـ"
            output.insert(0, current_haraka)
            current_haraka = ""
    return output

def combine_text_with_harakat(input_sent, output_sent):
    #print("input : " , len(input_sent))
    #print("output : " , len(output_sent))
    
    """
    harakat_stack = Stack()
    temp_stack    = Stack()
    #process harakat
    for character, haraka in zip(input_sent, output_sent):
        temp_stack = Stack()

        haraka = haraka.replace("<UNK>","").replace("<PAD>","").replace("ـ","")

        if (character == " " and haraka != "" and ord(haraka) == connector):
            combine = harakat_stack.pop()
            combine += haraka
            harakat_stack.push(combine)
        else:
            harakat_stack.push(haraka)
    """

    #fix combine differences
    input_length  = len(input_sent)
    output_length = len(output_sent) # harakat_stack.size()
    for index in range(0,(input_length-output_length)):
        output_sent.append("")

    #combine with text
    text = ""
    for character, haraka in zip(input_sent, output_sent):
        if haraka == '<UNK>' or haraka == 'ـ':
            haraka = ''
        text += character + "" + haraka

    return text




class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)

    def to_array(self):
        return self.stack
