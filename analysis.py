# -*- coding: utf-8 -*-
import os
import json 
import jieba
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
from pyecharts import Bar
import math
from pypinyin import lazy_pinyin

RAW_FILE = 'data/result.csv'

def plot_stars():
    """stars graph
    """

    df = pd.read_csv(RAW_FILE)
    data_list = list(df['stars'])
    print(len(data_list))
    print('max star = ',max(data_list))
    labels = [u'00~00', u'01~10', u'11~50', u'51~100', '101~500', '501~1000', '>1000']
    sizes = []
    sizes.append(len([pp for pp in data_list if pp == 0]))
    sizes.append(len([pp for pp in data_list if pp >= 1 and pp <= 10]))
    sizes.append(len([pp for pp in data_list if pp >= 11 and pp <= 50]))
    sizes.append(len([pp for pp in data_list if pp >= 51 and pp <= 100]))
    sizes.append(len([pp for pp in data_list if pp >= 101 and pp <= 500]))
    sizes.append(len([pp for pp in data_list if pp >= 501 and pp <= 1000]))
    sizes.append(len([pp for pp in data_list if pp >= 1001]))
    bar = Bar("stars", "stars hist graph of users")
    # bar.add("precipitation", labels, sizes, mark_line=["average"], mark_point=["max", "min"])
    bar.add("", labels, sizes, is_label_show=True, mark_line=["average"])
    bar.render('pics/stars.html')
   
def plot_repositories():
    """repos graph
    """

    df = pd.read_csv(RAW_FILE)
    data_list = list(df['repositories'])
    print('max repos = ',max(data_list))
    labels = [u'00~00', u'01~10', u'11~50', u'51~100', '101~500', '501~1000', '>1000']
    sizes = []
    sizes.append(len([pp for pp in data_list if pp == 0]))
    sizes.append(len([pp for pp in data_list if pp >= 1 and pp <= 10]))
    sizes.append(len([pp for pp in data_list if pp >= 11 and pp <= 50]))
    sizes.append(len([pp for pp in data_list if pp >= 51 and pp <= 100]))
    sizes.append(len([pp for pp in data_list if pp >= 101 and pp <= 500]))
    sizes.append(len([pp for pp in data_list if pp >= 501 and pp <= 1000]))
    sizes.append(len([pp for pp in data_list if pp >= 1001]))
    bar = Bar("repos", "repos hist graph of users")
    bar.add("", labels, sizes, is_label_show=True, mark_line=["average"])
    bar.render('pics/repositories.html')

def plot_following():
    """followings graph
    """

    df = pd.read_csv(RAW_FILE)
    data_list = list(df['following'])
    print('max folling = ',max(data_list))
    labels = [u'00~00', u'01~10', u'11~50', u'51~100', '101~500', '501~1000', '>1000']
    sizes = []

    sizes.append(len([pp for pp in data_list if pp == 0]))
    sizes.append(len([pp for pp in data_list if pp >= 1 and pp <= 10]))
    sizes.append(len([pp for pp in data_list if pp >= 11 and pp <= 50]))
    sizes.append(len([pp for pp in data_list if pp >= 51 and pp <= 100]))
    sizes.append(len([pp for pp in data_list if pp >= 101 and pp <= 500]))
    sizes.append(len([pp for pp in data_list if pp >= 501 and pp <= 1000]))
    sizes.append(len([pp for pp in data_list if pp >= 1001]))

    bar = Bar("following", "following hist graph of users")
    bar.add("", labels[1:], sizes[1:], is_label_show=True, mark_line=["average"])
    bar.render('pics/following.html')

def plot_followers():
    """followings graph
    """

    df = pd.read_csv(RAW_FILE)
    data_list = list(df['followers'])
    print('max followers = ',max(data_list))
    labels = [u'00~00', u'01~10', u'11~50', u'51~100', '101~500', '501~1000', '>1000']
    sizes = []

    sizes.append(len([pp for pp in data_list if pp == 0]))
    sizes.append(len([pp for pp in data_list if pp >= 1 and pp <= 10]))
    sizes.append(len([pp for pp in data_list if pp >= 11 and pp <= 50]))
    sizes.append(len([pp for pp in data_list if pp >= 51 and pp <= 100]))
    sizes.append(len([pp for pp in data_list if pp >= 101 and pp <= 500]))
    sizes.append(len([pp for pp in data_list if pp >= 501 and pp <= 1000]))
    sizes.append(len([pp for pp in data_list if pp >= 1001]))

    bar = Bar("followers", "followers hist graph of users")
    bar.add("", labels[1:], sizes[1:], is_label_show=True, mark_line=["average"])
    bar.render('pics/followers.html')


def plot_contributions():
    """contributions graph
    """

    df = pd.read_csv(RAW_FILE)
    data_list = list(df['contributions'])
    print('max contribution = ', max(data_list))
    labels = [u'00~00', u'01~10', u'11~50', u'51~100', '101~500', '501~1000', '>1000']
    sizes = []

    sizes.append(len([pp for pp in data_list if pp == 0]))
    sizes.append(len([pp for pp in data_list if pp >= 1 and pp <= 10]))
    sizes.append(len([pp for pp in data_list if pp >= 11 and pp <= 50]))
    sizes.append(len([pp for pp in data_list if pp >= 51 and pp <= 100]))
    sizes.append(len([pp for pp in data_list if pp >= 101 and pp <= 500]))
    sizes.append(len([pp for pp in data_list if pp >= 501 and pp <= 1000]))
    sizes.append(len([pp for pp in data_list if pp >= 1001]))

    bar = Bar("contributions", "contributions hist graph of users")
    bar.add("", labels[1:], sizes[1:], is_label_show=True, mark_line=["average"])
    bar.render('pics/contributions.html')

def plot_position():
    """positions analysis
    """
    df = pd.read_csv(RAW_FILE)
    data_list = list(df['position'])
    # 数据清理
    data_pos = [pp for pp in data_list if str(pp) != 'nan']
    # 中文转拼音
    places = []
    for data in data_pos:
        place = "".join(lazy_pinyin(data))
        places.append(place)

    wordcloud = WordCloud(background_color="white",width=1000, height=860, margin=2).generate(str(places))
    wordcloud.to_file('pics/places.jpg')
    # plt.imshow(wordcloud)
    # plt.axis("off")
    # plt.show()


def main():
    plot_stars()
    plot_repositories()
    plot_following()
    plot_followers()
    plot_contributions()
    plot_position()
if __name__ == '__main__':
    main()