'''
Created on 2017年6月29日

@author: wei.wang7
'''
import datetime
import xlsxwriter
import time, random

arr=(7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2)
last=('1','0','X','9','8','7','6','5','4','3','2')
def makeNew():
    '''随机生成18位身份证号码'''
    t=time.localtime()[0]
    x='%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                       random.randint(1,99),
                                       random.randint(1,99),
                                       random.randint(t-80,t-18),
                                       random.randint(1,12),
                                       random.randint(1,28),
                                       random.randint(1,999))
    y=0
    for i in range(17):
        y+=int(x[i])*arr[i]
    
    return '%s%s' %(x,last[y%11])

header=['序号1','序号2','电话号码','名','姓名','身份证号','电子邮箱']

workbook=xlsxwriter.Workbook("data_prepare.xlsx")
worksheet=workbook.add_worksheet()

col=0
for item in (header):
    worksheet.write(0,col,item)
    col+=1

line_number=99
phone_begin_with='135'
for i in range(1,line_number+1):
    time1=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:16]   #20位
    fraction=datetime.datetime.now().strftime('%H%M%S%f')[:8]   #12位
    worksheet.write(i,0,time1)
    worksheet.write(i,1,time1+'hw')
    worksheet.write(i,2,phone_begin_with+fraction)
    time.sleep(0.01)
    
arabic_chs_map={0:'零', 1:'一', 2:'二', 3:'三', 4:'四', 5:'五', 6:'六', 7:'七', 8:'八', 9:'九'}
first_name='孙'
first_name_pinyin='sun'
for i in range(1, line_number+1):
    if i<10:
        last_name='零'+arabic_chs_map.get(i)
        mail_box_no='0'+str(i)
    else:
        last_name=arabic_chs_map.get(int(i/10))+arabic_chs_map.get(i%10)
        mail_box_no=str(i)
    worksheet.write(i,3,last_name)
    worksheet.write(i,4,first_name+last_name)
    worksheet.write(i,5,makeNew())
    worksheet.write(i,6,first_name_pinyin+mail_box_no+'@163.com')

workbook.close()

