import pandas as pd
import argparse
import os
import re
import json

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o','--wordcounts')
    parser.add_argument('-d','--cleandialog')

    args = parser.parse_args()
    word_counts_json = args.wordcounts
    clean_dialog = args.cleandialog
    return word_counts_json, clean_dialog

def load_stop_words(stop_words_address):
    stop_words = []
    with open(stop_words_address, 'r') as f:
        words = f.read().split("\n")
    for i, word in enumerate(words):
        if i < 6:
            continue
        stop_words.append(word.strip())
    return stop_words

def process_dialog(dialog,stopwords):
    # replace punctuation characters with a space
    dialog = re.sub(r"\ *[\(\)\[\]\,\-\.\?\!\:\;\#\&]+\ *", " ", str(dialog))
    # split words into list
    dialog = dialog.split()
    # lower case all words and exclude words that are not alphabetic
    dialog = [word.lower() for word in dialog if word.isalpha()]
    # remove all stopwords
    for stop in stopwords:
        dialog = list(filter((stop).__ne__, dialog))

    return dialog

def produce_count(clean_dialog,stopwords):
    # read clean_dialog file
    dialog = pd.read_csv(clean_dialog,sep='\t')
    o = {}
    a = {}
    h = {}
    e = {}
    c = {}
    m= {}
    p = {}
    for index,row in dialog.iterrows():
        category = row['category']
        dialog = process_dialog(row['full_text'],stopwords)

        if category == 'o':
            for word in dialog:
                try:
                    o[word] += 1
                except:
                    o[word] = 1
        elif category == 'a':
            for word in dialog:
                try:
                    a[word] += 1
                except:
                    a[word] = 1
        elif category == 'h':
            for word in dialog:
                try:
                    h[word] += 1
                except:
                    h[word] = 1
        elif category == 'e':
            for word in dialog:
                try:
                    e[word] += 1
                except:
                    e[word] = 1
        elif category == 'c':
            for word in dialog:
                try:
                    c[word] += 1
                except:
                    c[word] = 1
        elif category == 'm':
            for word in dialog:
                try:
                    m[word] += 1
                except:
                    m[word] = 1
        elif category == 'p':
            for word in dialog:
                try:
                    p[word] += 1
                except:
                    p[word] = 1

    '''
    filtered_words = [k for k, v in all_speech.items() if v >= 5]
    twilight = {k:v for k,v in twilight.items() if k in filtered_words}
    apple = {k: v for k, v in apple.items() if k in filtered_words}
    rari = {k: v for k, v in rari.items() if k in filtered_words}
    pinkie = {k: v for k, v in pinkie.items() if k in filtered_words}
    rainbow = {k: v for k, v in rainbow.items() if k in filtered_words}
    flutter = {k: v for k, v in flutter.items() if k in filtered_words}
    '''
    result = {"visuals":a,"characters":e,"cast":c,"plot":p,"money":m,"harry styles":h,"other":o}

    jsonObj = json.dumps(result, indent=2)
    return jsonObj

def main():
    # parse arguments
    word_counts_json, clean_dialog = parse()
    # load stopwords
    stopwords = load_stop_words('../data/stopwords.txt')
    jsonObj= produce_count(clean_dialog,stopwords)

    directory = os.path.dirname(word_counts_json)
    if not os.path.exists(directory):
        os.mkdir(directory)
    with open(word_counts_json, 'w+') as f:
        f.write(jsonObj)
    f.close()


if __name__ == '__main__':
    main()
