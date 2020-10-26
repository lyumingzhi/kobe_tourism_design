#!/usr/bin/env python
# -*- coding:utf-8 -*-
import json

def extract(filename):
	twitters=[]
	with open(filename,'r', encoding='utf-8') as f:
		for line in f.readlines():
			twitters.append(json.loads(line))

	extracted_twitter=[]
	for tweet in twitters:
		# extracted_twitter.append({'date':tweet['date'],
		# 	'time':tweet['time'],
		# 	'tweet':tweet['tweet'],
		# 	'likes_count':tweet['likes_count'],
		# 	'retweets_count:':tweet['retweets_count']})
		extracted_twitter.append(tweet['tweet'])
	with open('extracted_tweet.json','w',encoding='utf-8') as f:
		json.dump(extracted_twitter,f,indent=4, ensure_ascii=False)
extract('kobe_tourism.json')