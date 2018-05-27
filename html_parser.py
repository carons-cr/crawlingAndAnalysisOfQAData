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
	    new_tag["questionNumber"] = tag_node.find("em").get_text();
	    tags.append(new_tag);
	return tags;
    
    def _get_questions(self, beautiful_soup):
	questions = [];
	question_detail_nodes = beautiful_soup.find_all("div", class_="question_detail_con");
        for question_detail_node in question_detail_nodes:
	    question_detail = {};
	    q_time_node = question_detail_node.find("div", _class="q_time");
            question_detail["questionTime"] = re.search(r"[0-9]+", q_time_node.find("span").get_text()).group();
	    question_detail["userName"] = q_time_node.find("a").get_text();
	    question_detail["reward"] = q_time_node.find("b").find("a").get_text();
	    question_detail["questionTitle"] = question_detail_node.find("dl").find("dt").find("a").get_text();
	    answer_node = question_detail_node.find("a", _class="answer_num");
	    question_detail["existSatisfactoryAnswer"] = answer_node["title"];
	    question_detail["answerUrl"] = answer_node["href"];
	    question_detail["answerNumber"] = question_detail_node.find("a").find("span").get_text();
	    questions.append(question_detail);
	    print questions;
	    
	question_attention_nodes = beautiful_soup.find_all("div", class_="share_bar_con");
	i = 0;
        for question_attention_node in question_attention_nodes:
	    print len(questions);
            #questions[i]["browseNumber"] = re.search(r"[0-9]+", question_attention_node.find("em").get_text()).group();
	    i = i + 1;

    def parse_questions(self, html_content):
	if html_content is None:
            return
        beautiful_soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8");
        questions = self._get_questions(beautiful_soup);
	return questions;

