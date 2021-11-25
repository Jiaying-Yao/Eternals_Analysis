import argparse
import json
import math

ponies = ["visuals","characters","cast","plot","money","harry styles","other"]

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",'--ponycounts')
    parser.add_argument("-n", '--numwords')
    args = parser.parse_args()
    pony_counts = args.ponycounts
    num_words = int(args.numwords)
    return pony_counts, num_words


def tfidf(w,pony,script):
    tf = script[pony][w]
    count = 0
    for p in ponies:
        if w in list(script[p].keys()):
            count += 1
    idf = math.log(6/count)
    result = tf * idf
    return result

def main():
    pony_counts,num_words = parse()
    with open(pony_counts, 'r') as f:
        script = json.load(f)
    f.close()
    tfidf_matrix = {"visuals": {}, "characters": {}, "cast": {}, "plot": {}, "money": {}, "harry styles": {}, "other": {}}
    highest = {"visuals": [], "characters": [], "cast": [], "plot": [], "money": [], "harry styles": [], "other": []}
    for p in ponies:
        for word in list(script[p].keys()):
            tfidf_matrix[p][word] = tfidf(word,p,script)
        tfidf_matrix[p] = dict(sorted(tfidf_matrix[p].items(), key=lambda item: item[1],reverse=True))
        for i in range(num_words):
            highest[p].append(list(tfidf_matrix[p].keys())[i])
    jsonObj = json.dumps(highest,indent=2)
    with open("../salient_ten_words.json", 'w+') as f:
        f.write(jsonObj)
    f.close()

if __name__ == "__main__":
    main()