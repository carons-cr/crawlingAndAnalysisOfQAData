#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : spider_main.py

import tags_outputer;

class SpiderMain(object):
    def __init__(self):
	self.tagsOutputer = tags_outputer.TagsOutputer();
    
    def crawl(self):
        self.tagsOutputer.collect_tags();
	self.tagsOutputer.output_tags();

if __name__ == "__main__":
    spiderMain = SpiderMain();
    spiderMain.crawl();
