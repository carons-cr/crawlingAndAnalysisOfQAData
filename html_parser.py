#!/usr/lib/env/python2.7
#encoding=utf-8;
#pathName : html_parser.py

from bs4 import BeautifulSoup
import re;
import urlparse;

class HtmlParser(object):
    def parse_tags(self, html_content):
	if html_content is None:
	    return
	beautiful_soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8");
	tags = [];
	tag_nodes = beautiful_soup.find("div", class_="tags_list").find_all("a");
	for tag_node in tag_nodes:
	    new_tag = {};
	    new_tag["tagName"] = re.search(r"[^0-9]+", tag_node.get_text()).group();
	    new_tag["blogNumber"] = tag_node.find("em").get_text();
	    tags.append(new_tag);
	return tags;
