#!/usr/bin/env python
# -*- coding:utf-8 -*-
import MeCab
from os import path
from wordcloud import WordCloud, STOPWORDS
import json
import emoji
import re
meaningful_types=['名詞','動詞','形容詞']
# meaningful_types=['動詞','形容詞']

revise_types=['代名詞','助動詞']
meaningless_words=['大阪','京都','神戸']
# (1) load the text file with the story
d = path.dirname(__file__)          # directory interface for file access


# (2) tokenize the text
# mct = MeCab.Tagger("-O chasen -d /usr/local/Cellar/mecab-ipadic")
def remove(text):
    remove_chars = '[a-zA-Z’#$%&\'()*+-/:;<=>?@★【】《》“”‘’[\\]^_`{|}]+'
    return re.sub(remove_chars, ' ', text)
def format_tag_result(x):
    pieces = []
    for i in x.splitlines()[:-1]: #结尾的"EOS"顺手去掉
        i = i.split()
        # print(i)
        if len(i)>=5:
            pieces.append((i[0], i[4]))#选择需要的内容
    return pieces

for i in range(1,2):
    with open(path.join(d, 'extracted_tweet'+str(i)+'.json'), encoding='utf-8') as f:
        momotaro = f.readlines()
    mct = MeCab.Tagger()
    momo_text = ''
    num=10000
    
    for sentence in momotaro[:10000]:
        sentence=emoji.demojize(sentence)
        sentence=remove(sentence)
        raw_word_dict = mct.parse(sentence)
        word_dict=format_tag_result(raw_word_dict)
        # print(raw_word_dict,word_dict)
        # exit()
        for word in word_dict:
            if_meaningful=False
            for meaningful_type in meaningful_types:
                if word[-1].find(meaningful_type)>=0:
                    if_meaningful=True
                    break
            for revise_type in revise_types:
                if word[-1].find(revise_type)>=0:
                    if_meaningful=False
                    break
            # for meaningless_word in meaningless_words:
            #     if word[0].find(meaningless_word)>=0:
            #         if_meaningful=False
            #         break
            if if_meaningful==True:
                momo_text=momo_text+word[0]+' '

    # momo_text+='可愛い'
    # (3) indicate words I don't want to include in the word cloud
    print(type(momo_text))
    stopwords = set(STOPWORDS)
    # stopwords.add("観光")
    # stopwords.add("神戸")
    for meaningless_word in meaningless_words:
        stopwords.add(meaningless_word)


    # (4) create the word cloud
    font_path = d + 'Japanese-Word-Cloud/NotoSansCJKjp-Light.otf'
    wordcloud = WordCloud(width=1200,height=600,background_color="white",max_words=2000, stopwords=stopwords, font_path=font_path,contour_width=3, contour_color='steelblue').generate(momo_text)

    image = wordcloud.to_image()
    # image.show()                    # display generated wordcloud
    image.save('sightseeing'+str(i)+'.png')
# # save wordcloud image
# wordcloud.to_file(path.join(d, "momo_word_cloud.png"))