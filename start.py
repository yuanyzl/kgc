from scrapy.cmdline import execute
if __name__=='__main__':
    spiderName=input("请输入蜘蛛名")
    execute('scrapy crawl {spiderName}'.format(spiderName=spiderName).split())