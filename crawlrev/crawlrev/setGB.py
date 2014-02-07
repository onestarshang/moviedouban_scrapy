#coding:utf-8
# 配置要抓取电影评论的评论人豆瓣ID
usr = 'onestar'
import sys, os
jsondir = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) 
#jsondir = os.path.abspath(os.path.join(parentf, '..'))
print jsondir
#配置刚才抓取的影评人评过的电影的json文件的路径

#mvjson = os.path.join(jsondir, 'onestar.json')
