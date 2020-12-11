def main ():#line:2
    OO00O0O00O0OOO000 ='y'#line:3
    while OO00O0O00O0OOO000 .lower ()=='y':#line:4
        OO00OOO000OOO0OO0 =getNapier ()#line:7
        O0OOOOO00OO0OO0O0 =convertNapier (OO00OOO000OOO0OO0 )#line:8
        print ("The first number is: {:,}".format (O0OOOOO00OO0OO0O0 ))#line:10
        OOOOOO0OOOOO0000O =getNapier ()#line:13
        OOOOOOOOOO0O0OO00 =convertNapier (OOOOOO0OOOOO0000O )#line:14
        print ("The second number is: {:,}".format (OOOOOOOOOO0O0OO00 ))#line:16
        O0O00O00O0O00O000 =getOperator ()#line:19
        O0O0OO0O0OO0O00O0 =doMath (O0OOOOO00OO0OO0O0 ,OOOOOOOOOO0O0OO00 ,O0O00O00O0O00O000 )#line:21
        print ("The result is {:,} or {}".format (O0O0OO0O0OO0O00O0 ,decimalToNapier (O0O0OO0O0OO0O00O0 )))#line:23
        OO00O0O00O0OOO000 =input ("Do you want to repeat the program? Y/n: ")#line:26
def getNapier ():#line:30
    OO00O00000OOO0000 =input ("Enter Napier's number: ")#line:32
    while not OO00O00000OOO0000 .isalpha ():#line:34
        OO00O00000OOO0000 =input ("Something's wrong. Try again.\nEnter Napiers number: ")#line:35
    return OO00O00000OOO0000 #line:38
def convertNapier (s ):#line:43
    OO00OO0O0OOO0O0O0 =0 #line:44
    for O0OO0OO0O0O00O0O0 in s :#line:47
        OO00OO0O0OOO0O0O0 +=2 **(ord (O0OO0OO0O0O00O0O0 )-ord ('a'))#line:49
    return OO00OO0O0OOO0O0O0 #line:52
def getOperator ():#line:57
    OOO00000O0OO0OO00 =input ("Enter the desired arithmetic operation: ")#line:59
    while OOO00000O0OO0OO00 not in ['+','-','/','*']:#line:62
        OOO00000O0OO0OO00 =input ("Something's wrong. Try again.\nEnter the desired arithmetic operation: ")#line:63
    return OOO00000O0OO0OO00 #line:66
def doMath (n1 ,n2 ,op ):#line:71
    if op =='+':#line:75
        return n1 +n2 #line:76
    elif op =="-":#line:77
        if n1 >=n2 :#line:82
            return n1 -n2 #line:83
        elif n2 >n1 :#line:84
            return -1 *(n2 -n1 )#line:85
    elif op =="/":#line:86
        return n1 /n2 #line:87
    elif op =="*":#line:88
        return n1 *n2 #line:89
def decimalToNapier (num ):#line:96
    OO0OO00OO0OO00000 =""#line:97
    O00OO0O00O00000OO =False #line:98
    if num ==0 :#line:101
        return "\"\""#line:104
    else :#line:105
        if num <0 :#line:108
            O00OO0O00O00000OO =True #line:109
            num *=-1 #line:110
        O00O000O00O0OO000 =67108863 #line:112
        OO0O0O00OO0OO0OO0 =33554432 #line:113
        OOO000OOOOO0O0OO0 =""#line:114
        if num >O00O000O00O0OO000 :#line:120
            OOO0O00O000OO0000 =num //OO0O0O00OO0OO0OO0 #line:121
            num -=OOO0O00O000OO0000 *OO0O0O00OO0OO0OO0 #line:122
            if OOO0O00O000OO0000 <=10 :#line:123
                for O00O0OOOO00OO000O in range (OOO0O00O000OO0000 ):#line:124
                    OOO000OOOOO0O0OO0 +="z"#line:125
            else :#line:126
                OOO000OOOOO0O0OO0 ="(z*{})".format (OOO0O00O000OO0000 )#line:127
        while num !=0 :#line:131
            OO0OO00OO0OO00000 +=str (num %2 )#line:132
            num //=2 #line:133
        O00O0O00O00O0000O =0 #line:135
        O0OO0O0O00OOO000O =""#line:136
        for O0O0O0O0O00O0OO00 in OO0OO00OO0OO00000 :#line:139
            if O0O0O0O0O00O0OO00 =="1":#line:140
                O0OO0O0O00OOO000O +=chr (O00O0O00O00O0000O +ord ('a'))#line:141
            O00O0O00O00O0000O +=1 #line:142
        if O00OO0O00O00000OO :#line:147
            if OOO000OOOOO0O0OO0 :#line:148
                return "-{}{}".format (O0OO0O0O00OOO000O ,OOO000OOOOO0O0OO0 )#line:149
            else :#line:150
                return "-{}".format (O0OO0O0O00OOO000O )#line:151
        else :#line:152
            if OOO000OOOOO0O0OO0 :#line:153
                return "{}{}".format (O0OO0O0O00OOO000O ,OOO000OOOOO0O0OO0 )#line:154
            else :#line:155
                return "{}".format (O0OO0O0O00OOO000O )#line:156
main ()#line:160
