from collections import defaultdict
import datetime

def solution(S):
    answer = []
    s = S.split("\n")
    pic_dict = defaultdict()
    time_dict = defaultdict(list)

    for idx, i in enumerate(s):
        j = i.split(',')
        city = j[1].strip()
        
        t = j[2][1:].split(' ')
        time = t[0].split('-') + t[1].split(':')s
        time = list(map(int, time))
        dtime = datetime.datetime(time[0],time[1],time[2],time[3],time[4],time[5])
        time_dict[city] += [[idx, dtime]]

    for idx, i in enumerate(s):
        j = i.split(',')
        name = idx
        extension = j[0][j[0].find('.'):]
        city = j[1]
        time = j[2]
        pic_dict[name] = [extension, city]

    for key, value in pic_dict.items():
        temp = ""
        city = value[1].strip()
        extension = value[0]
        number = ""
        
        c = time_dict[city]
        sc = sorted(c, key=lambda x:x[1])
        clen = len(c)
        num = 0
        for idx, i in enumerate(sc):
            if i[0] == key:
                num = idx+1
        if clen >= 10 and num < 10:
            number = '0' + str(num)
        else:
            number = str(num)

        temp = city + number + extension
        answer.append(temp)

    return '\n'.join(answer)
