#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : spider_main.py

import html_downloader, html_parser, datas_outputer;

class SpiderMain(object):
    def __init__(self):
	self.htmlDownloader = html_downloader.HtmlDownloader();
	self.htmlParser = html_parser.HtmlParser();
	self.datasOutputer = datas_outputer.DatasOutputer();
    
    def crawlTags(self, url):
	html_content = self.htmlDownloader.download(url);
	tags = self.htmlParser.parse_tags(html_content);	
	self.datasOutputer.output_tags(tags);

if __name__ == "__main__":
    url_tag = "https://ask.csdn.net/tags";
    spiderMain = SpiderMain();
    spiderMain.crawlTags(url_tag);
