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
import xlwt

class DisAna:
    '''printf("pre obj dis.y:%f, cur obj dis.y:%f, pre pre obj dis.y:%f ID:%d\n", tracking_buffer_[tracking_buffer_.size() - 1].distance_.y, cur, tracking_buffer_[tracking_buffer_.size() - 2].distance_.y, id_); '''
    def __init__(self, filename):
        self.preobjdis = {}
        self.curobjdis = {}
        self.prepreobjdis = {}
        self.prelist = []
        self.curlist = []
        self.preprelist = []
        self.filename = filename
        print(filename)
        self.GetPreObjDistance()

    def GetPreObjDistance(self):
        f = open(self.filename, 'r')
        contant = f.readlines()
        print(len(contant))
        preid=0
        for line in contant :
            m = line.split(' ')
            ids = m[3]
            if (ids not in self.preobjdis.keys()):
                self.preobjdis[ids] = []
                self.curobjdis[ids] = []
                self.prepreobjdis[ids] = []
            pre = m [0]
            cur = m [1]
            prepre = m [2]
            self.preobjdis[ids].append(pre)
            self.curobjdis[ids].append(cur)
            self.prepreobjdis[ids].append(prepre)
        index = [int(x) for x in self.preobjdis.keys()]
        index = sorted(index)
        for x in index:
            self.prelist.extend(self.preobjdis[str(x)])
            self.curlist.extend(self.curobjdis[str(x)])
            self.preprelist.extend(self.prepreobjdis[str(x)])
            #print (x, len(self.prepreobjdis[str(x)]), self.prepreobjdis[str(x)])
        print(len(self.prelist))
        print(len(self.curlist))
        print(len(self.preprelist))

    def ConfPlt(self):
        x = [x for x in range(len(self.prelist))]
        diff = [float(self.curlist[i]) - float(self.prelist[i]) for i in range(len(self.prelist))]
        plt.figure(figsize = (8, 4))
        plt.plot(x, self.prelist,":", label="$PreObjectDis$", color="green", linewidth=1)
        plt.plot(x, self.curlist,".", label="$CurObjectDis$", color="blue", linewidth=1)
        plt.plot(x, self.preprelist,"-.", label="$prepreObjectDis$", color="brown", linewidth=1)
        plt.plot(x, diff, label="$diff$", color="red", linewidth=1)
        #plt.ylim(-10, 100)
        #plt.xlim(0, 100)
        plt.legend()
        plt.show()

    def to_excel(fpath):
        #创建workbook和sheet对象
        workbook = xlwt.Workbook() #注意Workbook的开头W要大写
        sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
        #向sheet页中写入数据
        sheet1.write(0,0,'this should overwrite1')
        sheet1.write(0,1,'aaaaaaaaaaaa')
        """
        #-----------使用样式-----------------------------------
        #初始化样式
        style = xlwt.XFStyle()
        #为样式创建字体
        font = xlwt.Font()
        font.name = 'Times New Roman'
        font.bold = True
        #设置样式的字体
        style.font = font
        #使用样式
        sheet.write(0,1,'some bold Times text',style)
        """
        #保存该excel文件,有同名文件时直接覆盖
        workbook.save('E:\\Code\\Python\\test2.xls')
        print ('创建excel文件完成！')

if (__name__ == "__main__"):
    d = DisAna(sys.argv[1])
    workbook = xlwt.Workbook() #注意Workbook的开头W要大写
    sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
    index = [int(x) for x in d.preobjdis.keys()]
    index = sorted(index)
    count=0
    for x in index:
        print(x, type(x), len(d.preobjdis[str(x)]))
        for i in range(len(d.preobjdis[str(x)])):
            sheet1.write(count,  0, d.preobjdis[str(x)][i])
            sheet1.write(count,  1, d.prepreobjdis[str(x)][i])
            sheet1.write(count,  2, d.curobjdis[str(x)][i])
            sheet1.write(count,  3, x)
            count += 1
    print(count)
    workbook.save('data_analysis.xls')
    print("done")
    d.ConfPlt()
