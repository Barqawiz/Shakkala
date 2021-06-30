#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example code using Shakkala library
"""
import os
from Shakkala import Shakkala

if __name__ == "__main__":
    input_text = "فإن لم يكونا كذلك أتى بما يقتضيه الحال وهذا أولى"

    folder_location = './'

    # create Shakkala object
    sh = Shakkala(folder_location, version=3)

    # prepare input
    input_int = sh.prepare_input(input_text)

    print("finished preparing input")

    print("start with model")

    model, graph = sh.get_model()

    # with graph.as_default():
    logits = model.predict(input_int)[0]

    print("prepare and print output")
    predicted_harakat = sh.logits_to_text(logits)

    final_output = sh.get_final_text(input_text, predicted_harakat)
    print(final_output)

    print("finished successfully")
