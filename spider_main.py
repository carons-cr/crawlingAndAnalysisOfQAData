#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : spider_main.py

import html_downloader, tags_outputer;

class SpiderMain(object):
    def __init__(self):
	self.downloader = html_downloader.HtmlDownloader();
	self.tagsOutputer = tags_outputer.TagsOutputer();
    
    def crawlTags(self, url):
	html_content = self.downloader.download(url);
        self.tagsOutputer.collect_tags();
	self.tagsOutputer.output_tags();

if __name__ == "__main__":
    url_tag = "https://ask.csdn.net/tags";
    spiderMain = SpiderMain();
    spiderMain.crawlTags(url_tag);
