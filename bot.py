#coding:utf-8
#http://python-twitter.readthedocs.io/en/latest/_modules/twitter/models.html#Status
#Statusのメソッド
import twitter
import ConfigParser
import os
import sys
import random
import datetime
import re

from TweetRc import TweetRc
from word2vec import Return_word2vec

COUNT = 1


def GetMyAuth():
    rc  = TweetRc()
    consumer_key = rc.GetConsumerKey()
    consumer_secret = rc.GetConsumerSecret()
    access_key = rc.GetAccessKey()
    access_secret = rc.GetAccessSecret()
    if not consumer_key or not consumer_secret or not access_key or not access_secret:
        print 'Some keys not found.'
    api = twitter.Api(consumer_key,consumer_secret,access_key,access_secret)
    return api

def Strip_user_from_tweet(string):
    string = re.sub('(@.*)\s','',string)
    string = string.replace(' ','')
    return string

def Read_from_tweet(api):
    reply = api.GetMentions(count=COUNT)
    target = reply[0].user.screen_name
    return target,Strip_user_from_tweet(reply[0].text)

def Tweet(api,target,word):
    status = api.PostUpdate("@"+target+" 似ている言葉:".decode('utf-8')+word)
    print "Tweeted: "+target+" 似ている言葉:".decode('utf-8')+word

def main():
    api = GetMyAuth()
    target,word = Read_from_tweet(api)
    simword = Return_word2vec(word)
    print "simword:",simword
    Tweet(api,target,simword)
    
if __name__ == '__main__':
    main()
