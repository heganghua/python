#encoding=utf-8
#mport threadpool
import threading
import requests
import re
import pymysql

# allowed_domains = ['http://www.quanshuwang.com/']


# #########数据库操作#############

conn = pymysql.connect(
    host='',
    user='',
    passwd='',
    db='',
    port=,
    charset='utf8'
)
cursor = conn.cursor()

# #########数据库操作#############

#requests 函数
def get_content(url):
    response = requests.get(url)
    response.encoding = 'gbk'
    result = response.text
    return result


#获取一个分类下面中第一页的所有小说url
def get_novel_list(pages,type):
    urls = 'http://www.quanshuwang.com/list/{}_{}.html'.format(type,pages)
    result = get_content(urls)
    reg = r'<a target="_blank" title="(.*?)" href="(.*?)" class="clearfix stitle">'
    novel_list = re.findall(reg, result)
    #print(novel_list)
    return novel_list

#获取所有小说章节页url
def get_novel_content(url):
    result = get_content(url)
    reg = r'<a href="(.*?)" class="reader"'
    try:
        novel_content = re.findall(reg, result)[0]
    except:
        return r'章节出错'
    #print(novel_content)
    return novel_content

#获取所有小说章节页面里面所有章节的url
def get_novel_chapter_url_list(url):
    result = get_content(url)
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    novel_chapter_list =  re.findall(reg,result)
    #print (novel_chapter_list)
    return novel_chapter_list

#获取所有小说章节内容
def get_novel_chapter_content(url):
    print(url)
    result = get_content(url)
    reg = r'style5\(\);</script>(.*?)<script type="text/javascript">style6'
    try:
        novel_chapter_content = re.findall(reg, result, re.S)[0]
    except:
        return u'内容出错'
    #print(novel_chapter_content)
    return novel_chapter_content


#调用函数，获取小说相关信息，写入数据库
def novel_type(pages,type):
    #获取小说的名称和小说章节url
    for novel_name,novel_url in get_novel_list(pages,type):
        #print(novel_name,novel_url)
        #获取小说章节列表内容
        novel_content_url = get_novel_content(novel_url)
        #执行SQL语句
        cursor.execute("insert into novel_name(name) values('{}')" .format(novel_name))
        novelid = cursor.lastrowid  #获取章节表中的外键字段，
        conn.commit()
        print('{}----------写入成功'.format(novel_name))
        #获取小说章节内容
        for chapter_url, chapter_name in get_novel_chapter_url_list(novel_content_url):
            novel_chapter_content = get_novel_chapter_content(chapter_url)

            # 执行SQL语句
            cursor.execute(
                "insert into novel_content(chapter, content, nameid) values('{}', '{}', {})".format(
                    chapter_name, novel_chapter_content.replace("'", r"\'"), novelid))
            conn.commit()
            print('{}----------写入成功'.format(chapter_name))


def start(type):
    for pages in range(1, 100):  #生成每个类型下面的页码，比如玄幻魔法下面的第三页
        novel_type(pages,type)   # pages :  页码    type : 小说分类



if __name__ == '__main__':
    for type in range(1,11):
        start(type)
    # threads = []
    # for type in range(1, 13):
    #     thread = threading.Thread(target = start, args=(type,))
    #     threads.append(thread)
    #
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    # for t in threads:
    #     t.
    #
    # for t in threads:
    #     t.join()

    cursor.close()  #关闭游标
    conn.close()    #关闭连接

    # threads = [threading.Thread(target=start,arges(type,)) for type in range(1,13)]
    # for t in threads:
    #     t.start()  # 启动线程
    # for t in threads:
    #     t.join()  # 等待每个线程结束
    #
    # #
    # # #创建12个线程
    # # for types in range(1,13):
    # #     pages = 0
    # #     for p in range(1, 933):
    # #         pages = p
    # #         continue
    # #     thread = threading.Thread(target=novel_type,args(types, pagess))
    # #
    # #
    # #启动线程
    # for t in threads:
    #     t.start()    #启动线程
    # for t in threads:
    #     t.join()    #等待每个线程结束
    # #novel_type(pages)








