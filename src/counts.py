import pandas as pd
import json

data = pd.read_csv('../data/re_annotated_lorna.tsv',sep='\t')
data = data[:1000]
categories = ['appearance','character','money','harry_styles','cast','plot','review','others']
cats = {'appearance':'a','character':'e','money':'m','harry_styles':'h','cast':'c','plot':'p','review':'r','others':'o'}
sents = {'positive':'p','neutral':'n','negative':'x'}

# count by category
def by_category(data):
    appearance = 0
    character = 0
    money = 0
    harry_styles = 0
    cast = 0
    plot = 0
    review = 0
    others = 0
    for index,row in data.iterrows():
        category = row['category']
        if category == 'a':
            appearance += 1
        elif category == 'e':
            character += 1
        elif category == 'm':
            money += 1
        elif category == 'h':
            harry_styles += 1
        elif category == 'c':
            cast += 1
        elif category == 'p':
            plot += 1
        elif category == 'r':
            review += 1
        elif category == 'o':
            others += 1
    category = {'appearance':appearance,'character':character,'money':money,'harry_styles':harry_styles,'cast':cast,'plot':plot,'review':review,'others':others}
    jsonObj = json.dumps(category, indent=2)
    with open('../count_by_category.json','w+') as f:
        f.write(jsonObj)
    f.close()

# count by sentiment
def by_sentiment(data, ):
    positive = 0
    neutral = 0
    negative = 0
    for index,row in data.iterrows():
        sentiment = row['sentiment']
        if sentiment == 'p':
            positive += 1
        elif sentiment == 'x':
            negative += 1
        elif sentiment == 'n':
            neutral += 1

    sentiment = {'positive':positive,'neutral':neutral,'negative':negative}
    jsonObj = json.dumps(sentiment, indent=2)
    with open('../count_by_sentiment.json', 'w+') as f:
        f.write(jsonObj)
    f.close()

# count by sentiment in each category
def by_cat_sent(data):
    d = {}
    for cat in categories:
        key = cat+'_sentiments'
        d[key] = {'positive':0,'neutral':0,'negative':0}
        for index, row in data.iterrows():
            if row['category'] == cats[cat]:
                if row['sentiment'] == 'p':
                    d[key]['positive'] +=1
                elif row['sentiment'] == 'n':
                    d[key]['neutral'] +=1
                elif row['sentiment'] == 'x':
                    d[key]['negative'] +=1
    jsonObj = json.dumps(d, indent=2)
    with open('../sentiment_in_each_category.json', 'w+') as f:
        f.write(jsonObj)
    f.close()

# count by category in each sentiment
def by_sent_cat(data):
    d = {}
    for sent in ['positive','neutral','negative']:
        key = sent+'_category'
        d[key] = {'appearance':0,'character':0,'money':0,'harry_styles':0,'cast':0,'plot':0,'review':0,'others':0}
        for index, row in data.iterrows():
            if row['sentiment'] == sents[sent]:
                category = row['category']
                if category == 'a':
                    d[key]['appearance'] += 1
                elif category == 'e':
                    d[key]['character'] += 1
                elif category == 'm':
                    d[key]['money'] += 1
                elif category == 'h':
                    d[key]['harry_styles'] += 1
                elif category == 'c':
                    d[key]['cast'] += 1
                elif category == 'p':
                    d[key]['plot'] += 1
                elif category == 'r':
                    d[key]['review'] += 1
                elif category == 'o':
                    d[key]['others'] += 1
    jsonObj = json.dumps(d, indent=2)
    with open('../category_in_each_sentiment.json', 'w+') as f:
        f.write(jsonObj)
    f.close()

def main():
    by_category(data)
    by_sentiment(data)
    by_cat_sent(data)
    by_sent_cat(data)

if __name__ == '__main__':
    main()