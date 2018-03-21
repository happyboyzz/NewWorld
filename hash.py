# -*- coding: utf-8 -*-
import hashlib
import re
import os
import pprint
CheckMode=hashlib.algorithms_available
#竖方向打印
print pprint.pprint(CheckMode)
print "input :CheckMode filename"
print "example:md5 96.txt"
while True:
    inputstr=raw_input("->")
    #判断有无输入
    if not inputstr:
        continue
    #输入格式化为列表
    inputlist=re.split("[ ]",inputstr)
    #判断输入参数数量是否正确
    if len(inputlist)!=2:
        print "args not right"
        continue
    #判断是否支持输入的算法
    if inputlist[0] not in CheckMode:
        print "%s not exist"% inputlist[0]
        continue
    #文件or字符串
    if os.path.isfile(inputlist[1]) :
        filename=inputlist[1]
        file=open(filename,"rb")
        str=file.read()
        #释放文件句柄
        file.close()
        print "file=>",
    else:
        str=inputlist[1]
        print "str=>",
    #哈希算法
    sha=hashlib.new(inputlist[0])
    sha.update(str)
    print sha.hexdigest()
    #释放占据大量内存的数据
    del str

