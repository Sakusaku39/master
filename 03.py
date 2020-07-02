
string = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str=""
s_len = []  #リストにしなさいって言われた

"""
（19-26なしでこれでいける）
string = string.replace(",","")
string = string.replace(".","")
"""
str = string.split()
#print(str)

length = len(str)
#print(length)

for i in range(length):
    num = len(str[i])
    if '.' in str[i] :
        num = num - 1
        #s_len = s_len + str(num) ←あかんかったやつ
        s_len.insert(i,num)
    elif ',' in str[i] :
        num = num - 1
        s_len.insert(i,num)
    else:
        s_len.insert(i,num)

print(s_len)
