

## 获取 http://www.quanshuwang.com 的小说

	上面的文档 novel.py
	
	
## 点断续传<br/>
	scrapy 框架内置的断点续爬，但是如果你的爬虫有用到cookie的话那就会很难受了。
	启动爬虫：  scrapy crawl somespider -s JOBDIR=crawls/somespider-1
	暂停： ctrl + c <br/>
	重新启动爬虫： scrapy crawl somespider -s JOBDIR=crawls/somespider-1


获取以空格分隔的 倒数第一个值
=TRIM(RIGHT(SUBSTITUTE(H2," ",REPT(" ",99)),99))