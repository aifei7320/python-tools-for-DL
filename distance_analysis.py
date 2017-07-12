#*************************************************************************
#    > File Name: distance_analysis.py
#    > Author: zxf
#    > Mail: zhengxiaofeng333@163.com 
#    > Created Time: 2017年07月05日 星期三 13时23分10秒
#************************************************************************/

import matplotlib.pyplot as plt
import os
import numpy
import sys

class DisAna:
    '''printf("pre obj dis.y:%f, cur obj dis.y:%f, pre pre obj dis.y:%f ID:%d\n", tracking_buffer_[tracking_buffer_.size() - 1].distance_.y, cur, tracking_buffer_[tracking_buffer_.size() - 2].distance_.y, id_); '''
    def __init__(self, filename):
        self.preobjdis = {"":[]}
        self.curobjdis = {"":[]}
        self.prepreobjdis = {"":[]}
        self.prelist = []
        self.curlist = []
        self.preprelist = []
        self.filename = filename
        print(filename)
        self.GetPreObjDistance()

    def GetPreObjDistance(self):
        f = open(self.filename, 'r')
        contant = f.readlines()
        preid=0
        for line in contant :
            m = line.split(' ')
            ids = m[10].split(':')
            if (preid != int(ids[1][:-1])):
                preid = int(ids[1][:-1])
                self.preobjdis[str(preid)] = []
                self.curobjdis[str(preid)] = []
                self.prepreobjdis[str(preid)] = []
            prestr = m[2].split(':')
            curstr = m[5].split(':')
            prepre = m[9].split(':')
            self.preobjdis[str(preid)].append(prestr[1][:-1])
            self.curobjdis[str(preid)].append(curstr[1][:-1])
            self.prepreobjdis[str(preid)].append(prepre[1][:-1])
        print("prepre:%s"%len(self.prepreobjdis["1"]))
        index = [x for x in self.preobjdis]
        index.sort()
        for x in index:
            self.prelist.extend(self.preobjdis[str(x)])
            self.curlist.extend(self.curobjdis[str(x)])
            self.preprelist.extend(self.prepreobjdis[str(x)])
            print(len(self.prepreobjdis[str(x)]))
        print(len(self.prelist))
        print(len(self.curlist))
        print(len(self.preprelist))

    def ConfPlt(self):
        x = [x for x in range(len(self.prelist))]
        diff = [float(self.curlist[x]) - float(self.preprelist[x]) for x in range(len(self.prelist))]
        print(len(diff))
        plt.figure(figsize = (8, 4))
        plt.plot(x, self.prelist,":", label="$PreObjectDis$", color="green", linewidth=1)
        plt.plot(x, self.curlist,".", label="$CurObjectDis$", color="blue", linewidth=1)
        plt.plot(x, self.preprelist,"-.", label="$prepreObjectDis$", color="brown", linewidth=1)
        plt.plot(x, diff, label="$diff$", color="red", linewidth=1)
        #plt.ylim(-10, 100)
        #plt.xlim(0, 100)
        plt.legend()
        plt.show()

if (__name__ == "__main__"):
    d = DisAna(sys.argv[1])
    d.ConfPlt()
    #d1 = DisAna(sys.argv[2])
    #d1.ConfPlt()
    #d2 = DisAna(sys.argv[3])
    #d2.ConfPlt()
    #d3 = DisAna(sys.argv[4])
    #d3.ConfPlt()
