# crawlingAndAnalysisOfQAData
crawl CSDN' Datas of Question and Answer, then analyzing it.
- crawling ideas：
  
  1.use urllib2 to download a html webpage with it's url and get content as string fommat.
  
  2.use BeautifulSoup to create DOM of html content and parse it to get useful datas.
- files description:
  
  1.spider_main.py: crawler Scheduler.
  
  2.html_downloader.py: downloading html webpage and get it's content as string formmat.
  
  3.html_parser.py: parsing html content and getting useful datas --all java questions and some tags in CSDN.
  
  4.datas_outputer.py: outputing all java questions, tags to excel.
  
  5.questions.xls: saving all java questions.
  
  6.tags.xls: saving tags.
