# -*- coding: utf-8 -*-
import os
import re
#import chilkat

#charset = chilkat.CkCharset()

gqdz = []

class printFilde:
    def __init__(self, filePath):
        self.path = filePath
    def isFind(self, line, chars):
        for i in chars:
		    if i in line:
				return 1
        return 0
    def isStart_end(self, line, start, end):
		if (line.startswith(start) or line.startswith("����" + start) or line.startswith("��������" + start) or line.startswith("��������" + start)) and line.endswith(end):
		    return 1
		else:
			return 0
    def printFile(self, dstFile):
        print dstFile
        file = open(self.path)
        dst=open(dstFile, 'w+')
        lines = []
        chars = ['�ָ���','&gt;&gt','.*����.*����','.*@.*d4-d2-d2',
                 '(.*\[.*\].*\.��.*��.*\[.*\]){1,15}',
                 '^[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2}',
                 '^\d{4,7}>\d{4,10}>\d{4,7}',
                 '(.*��.*					  ){3,15}','���߱���ؼ���','����...','====']

        replChar= {"&quot;":"\"","&lt;":"<","&gt;":">","&#183;":"��", "&nbsp;":" ","&hellip;":"...", "&mdash;":"-", "&amp;":"&", "&ldquo;":"��","&rdquo;":"��",
                   "&#8226;":".", "&#8764;":"~"}
      
        #for i in file:
            #lines.append(i)
        old=""
        title_index = 0
        for i in file:
            i = i.strip()
            i = i.replace("\t", "")
            #m = re.search("����.*http.*", i)
            #i = i.lower()
            #m = re.search(".*tieku001.*", i)
            #if m is not None:
                #continue
            #m = re.search(".*http.*", i)
            #if m is not None:
                #gqdz.append(i)
            #continue
            if old == i:
                #print '�����ظ���' + i
                continue
            old = i
            
            if self.isFind(i, chars) == 1:
                continue
            if self.isStart_end(i, "http:/", ".jpg"):
            	continue
            if self.isStart_end(i, "http:/", ".shtml"): 
            	continue
            if self.isStart_end(i, "http:/", ".html"): 
            	continue
            if self.isStart_end(i, "http:/", ".htm"): 
            	continue
            if self.isStart_end(i, "[ͼ:", ".jpg]"): 
            	continue
            if "���ӣ�" in i:
            	continue
            if "�������ص�ַ��" in i:
            	continue
            if self.isStart_end(i, "��", "��") or self.isStart_end(i, "[", "]"):
                title_index = title_index + 1
            	print i
            	dst.write("��" + str(title_index) + "�� " + i+ "\n")
            	continue
            for key in replChar.keys():
                i = i.replace(key, replChar[key])
            dst.write(i + "\n")
        dst.close()
        print 'ת����ɣ�Դ�ļ���',
        print self.path,
        print '��Ŀ���ļ���',
        print dstFile


folder ="d:/txt"
os.chdir( folder)
L = os.listdir(folder)
for i in L:
    fl = printFilde("d:/txt/" + i)
    fpath = "d:/txt2/" + i
    fl.printFile(fpath)

for i in gqdz:
    index = i.find("http")
    print i[index:]
