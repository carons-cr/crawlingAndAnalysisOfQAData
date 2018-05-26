#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : tags_outputer.py

import xlwt;

class TagsOutputer(object):
    def __init__(self):
	self.tags = [];
    
    def collect_tags(self):
	for i in range(0, 10):
	    tag = {};
	    tag["tagName"] = i;
	    tag["blogNumber"] = i + 1;
	    self.tags.append(tag);
    
    def output_tags(self):
	workBook = xlwt.Workbook();
	workSheet = workBook.add_sheet("tags");

	workSheet.write(0, 0, "tagName");
	workSheet.write(0, 1, "blogNumber");
	i = 1;
	for tag in self.tags:
	    workSheet.write(i, 0, tag["tagName"]);
	    workSheet.write(i, 1, tag["blogNumber"]);
	    i = i + 1;
	workBook.save("tags.xls");
	
		 
