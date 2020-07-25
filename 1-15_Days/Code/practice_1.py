#判断一个输入是否为素数
input1 = int(input('请输入：'))
div = input1 - 1
for i in range(2,input1):
    res = input1 % div
    if res ==  0:
        print(" %d不是素数" %input1)
        break
    div -= 1
    if div ==1:
        # print(" %d是素数" %input1)
        print(input1+'是素数')

#求最大公约数和最小公倍数
#（a，b）×[a，b]=a×b；【】为最小公倍数，（）为最大公约数

