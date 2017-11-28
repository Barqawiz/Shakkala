import os
import glob
from nltk.tokenize import sent_tokenize, word_tokenize
from bs4 import BeautifulSoup

def list_files(folder_path, file_type):

    path = os.path.join(folder_path,'**',('*.'+file_type) )
    files = glob.glob(path, recursive=True)
    return files


def load_text_data(file_path):
    """
    Load dataset
    """
    input_file = os.path.join(file_path)
    with open(input_file, "r") as f:
        data = f.read()

    return get_sentences(data)

def load_xml_data(file_path):
    """
    Load dataset
    """
    input_file = os.path.join(file_path)
    with open(input_file, "r") as f:
        data = f.read()

    soup = BeautifulSoup(data, "lxml")

    return get_sentences(soup.get_text())

def get_sentences(data):

    return [sent for line in data.split('\n') if line for sent in sent_tokenize(line)]
