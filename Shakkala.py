#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
import helper
import os
import tensorflow as tf
from keras.models import Model
from keras.models import load_model
from keras.optimizers import Adam
from keras.losses import sparse_categorical_crossentropy
from keras.preprocessing.sequence import pad_sequences
import numpy as np


class Shakkala:

    # intial
    #max_sentence = 495

    def __init__(self, folder_location, version=3):

        assert folder_location != None, "model_location cant be empty, send location of keras model"

        model_folder = os.path.join(folder_location, 'model')
        if version == 1:
            self.max_sentence = 495
            self.model_location = os.path.join(model_folder, ('simple_model' + '.h5'))
        elif version == 2:
            self.max_sentence = 315
            self.model_location = os.path.join(model_folder, ('middle_model' + '.h5'))
        elif version == 3:
            self.max_sentence = 315
            self.model_location = os.path.join(model_folder, ('second_model6' + '.h5'))

        dictionary_folder = os.path.join(folder_location, 'dictionary')
        input_vocab_to_int  = helper.load_binary('input_vocab_to_int',dictionary_folder)
        output_int_to_vocab = helper.load_binary('output_int_to_vocab',dictionary_folder)

        self.dictionary = {
                "input_vocab_to_int":input_vocab_to_int,
                "output_int_to_vocab":output_int_to_vocab}

    # model
    def get_model(self):
        print('start load model')
        model = load_model(self.model_location)
        print('end load model')
        graph = tf.get_default_graph()

        return model, graph

    # input processing

    def prepare_input(self, input_sent):

        assert input_sent != None and len(input_sent) < self.max_sentence, \
        "max length for input_sent should be {} characters, you can split the sentence into multiple sentecens and call the function".format(self.max_sentence)

        input_sent = [input_sent]

        return self.__preprocess(input_sent)

    def __preprocess(self, input_sent):

        input_vocab_to_int = self.dictionary["input_vocab_to_int"]

        input_letters_ids  = [[input_vocab_to_int.get(ch, input_vocab_to_int['<UNK>']) for ch in sent] for sent in input_sent]

        input_letters_ids  = self.__pad_size(input_letters_ids, self.max_sentence)

        return input_letters_ids

    # output processing

    def logits_to_text(self, logits):
        text = []
        for prediction in np.argmax(logits, 1):
            if self.dictionary['output_int_to_vocab'][prediction] == '<PAD>':
                continue
            text.append(self.dictionary['output_int_to_vocab'][prediction])
        return text

    def get_final_text(self,input_sent, output_sent):
        return helper.combine_text_with_harakat(input_sent, output_sent)

    def clean_harakat(self, input_sent):
        return helper.clear_tashkel(input_sent)

    # common
    def __pad_size(self, x, length=None):
        return pad_sequences(x, maxlen=length, padding='post')
