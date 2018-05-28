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
	    new_tag["tagName"] = re.search(r"[^0-9|\s]+", tag_node.get_text()).group();
	    new_tag["questionNumber"] = tag_node.find("em").get_text();
	    tags.append(new_tag);
	return tags;

    def _get_data_from_question_detail_node(self, question_detail_node):
	question_detail = {};
	try:
            q_time_node = question_detail_node.find("div", class_="q_time");
            question_detail["questionTime"] = re.search(r"[\d|.]+", q_time_node.find("span").get_text()).group();
            question_detail["userName"] = q_time_node.find("a").get_text();
   	    reward_node = q_time_node.find("b");
	    if reward_node is None: 
	        question_detail["reward"] = "0C";
	    else: 
                question_detail["reward"] = re.search(r"[\d|\w]+", reward_node.find("a").get_text()).group();
	    question_node = question_detail_node.find("dl").find("dt").find("a");
	    question_detail["questionId"] = re.search(r"[\d]+", question_node["href"]).group();
	    question_detail["questionUrl"] = question_node["href"];
            question_detail["questionTitle"] = question_node.get_text();
            answer_node = question_detail_node.find("a", class_="answer_num");
            question_detail["existSatisfactoryAnswer"] = answer_node["title"];
            question_detail["answerUrl"] = answer_node["href"];
            question_detail["answerNumber"] = answer_node.find("span").get_text();
	except:
	    print "detail failed--get data from question detail node is failed!";
	return question_detail;

    def _get_data_from_question_attention_node(self, question_attention_node):
	browseNumber = "";
	try:
	    browse_node = question_attention_node.find("em", class_="browse");
	    browseNumber = re.search(r"[0-9]+", browse_node.get_text()).group();
	except:
	    print "attention failed--get data from question attention node is failed!";
	return browseNumber;
    
    def _get_questions(self, beautiful_soup):
	questions = [];
	question_detail_nodes = beautiful_soup.find_all("div", class_="questions_detail_con");
	question_attention_nodes = beautiful_soup.find_all("div", class_="share_bar_con");
        for question_detail_node in question_detail_nodes:
	    question_detail = self._get_data_from_question_detail_node(question_detail_node);
	    questions.append(question_detail);  
	question_index = 0;
        for question_attention_node in question_attention_nodes:
	    browseNumber = self._get_data_from_question_attention_node(question_attention_node);
            questions[question_index]["browseNumber"] = browseNumber;
	    question_index = question_index + 1;
	return questions;

    def parse_questions(self, html_content):
	if html_content is None:
            return
        beautiful_soup = BeautifulSoup(html_content, "html.parser", from_encoding="utf-8");
        questions = self._get_questions(beautiful_soup);
	return questions;

