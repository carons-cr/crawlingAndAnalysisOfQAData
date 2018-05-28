#!/usr/lib/env/python2.7
#encoding=utf-8
#pathName : tags_outputer.py

import xlwt;

class DatasOutputer(object):
    def output_tags(self, tags):
	workBook = xlwt.Workbook();
	workSheet = workBook.add_sheet("tags");

	workSheet.write(0, 0, "tagName");
	workSheet.write(0, 1, "questionNumber");
	i = 1;
	for tag in tags:
	    workSheet.write(i, 0, tag["tagName"]);
	    workSheet.write(i, 1, tag["questionNumber"]);
	    i = i + 1;
	workBook.save("tags.xls");
	
    def write_question_sheet_head(self, workSheet):
	workSheet.write(0, 0, "questionId");
        workSheet.write(0, 1, "questionUrl");
        workSheet.write(0, 2, "questionTime");
        workSheet.write(0, 3, "questionTitle");
        workSheet.write(0, 4, "userName");
        workSheet.write(0, 5, "reward");
        workSheet.write(0, 6, "existSatisfactoryAnswer");
        workSheet.write(0, 7, "answerUrl");
        workSheet.write(0, 8, "answerNumber");
        workSheet.write(0, 9, "browseNumber");   

    def write_question_sheet_body(self, workSheet, questions):
	i = 1;
        for question in questions:
            workSheet.write(i, 0, question["questionId"]);
            workSheet.write(i, 1, question["questionUrl"]);
            workSheet.write(i, 2, question["questionTime"]);
            workSheet.write(i, 3, question["questionTitle"]);
            workSheet.write(i, 4, question["userName"]);
            workSheet.write(i, 5, question["reward"]);
            workSheet.write(i, 6, question["existSatisfactoryAnswer"]);
            workSheet.write(i, 7, question["answerUrl"]);
            workSheet.write(i, 8, question["answerNumber"]);
            workSheet.write(i, 9, question["browseNumber"]);
            i = i + 1; 

    def output_questions(self, questions):
	workBook = xlwt.Workbook();
        workSheet = workBook.add_sheet("questions");
	self.write_question_sheet_head(workSheet);
	self.write_question_sheet_body(workSheet, questions);
        workBook.save("questions.xls");
