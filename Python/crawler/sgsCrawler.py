'''
Author: justinzhang
Email:  uestczhangchao@gmail.com/zhangchao3@unionpay.com
2014-7-24 9:44 Thursday
'''
import sys
import os
import time
import datetime

def getFirstPage(formData, url, savedFile):
    crawlCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + savedFile + '> log.cmd 2>&1;'
    parseCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + '- -q | ' + 'grep "<a href" | grep viewDetail | '+ "awk '{print $3}' | awk -F'=' '{print $2}' |"+' awk -F\\"'+" '{print $2}' | awk -F'(' '{print $2}' | awk -F\\' '{print $2}'"
#    print crawlCmd
    print parseCmd
#    crawlCmdRe = os.popen(crawlCmd).readlines()
    parseCmdRe = os.popen(parseCmd).readlines()
    for id in parseCmdRe:
        print id.strip()
#    print parseCmdRe


def getSecondPage(formData, url, savedFile, refUrl):
    crawlCmd = 'wget --post-data ' + "'" + formData + "' " + "--referer " + refUrl + " " + url + ' -O ' + savedFile + ' > log2.cmd 2>&1;'
    print crawlCmd
    crawlCmdRe = os.popen(crawlCmd).readlines()


if __name__ == '__main__':
    if len(sys.argv)==5:
        formData = sys.argv[1]
        url = sys.argv[2]
        savedFile = sys.argv[3]
        refUrl = sys.argv[4]
        getSecondPage(formData, url, savedFile, refUrl)
    elif len(sys.argv)==4:
        formData = sys.argv[1]
        url = sys.argv[2]
        savedFile = sys.argv[3]
        getFirstPage(formData, url, savedFile)
    else:
        print "Usage: Python sgsCrawler.py <formData> <URL> <saveDFile> [<refUrl>]"
