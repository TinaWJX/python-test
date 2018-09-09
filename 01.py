#-*-coding:utf8-*-
import os

def search_file(filedir,target):
    os.chdir(filedir)

    for each_file in os.listdir(os.curdir):
        ext = os.path.splitext(each_file)[1]
        if ext in target:
            vedio_list.append(os.getcwd()+os.sep+each_file+os.linesep)
        if os.path.isdir(each_file):
            search_file(each_file,target)
            os.chdir(os.pardir)

#start_dir = input('请输入待查找的初始目录')
start_dir=os.getcwd()
program_dir = os.getcwd()

target = ['.mp4','.avi','.py','.txt']
vedio_list=[]
search_file(start_dir,target)

f = open(program_dir+os.sep+'vedioList.txt','w')
for i in vedio_list:
    f.writelines(i)
f.close