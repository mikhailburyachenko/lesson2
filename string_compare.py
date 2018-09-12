
def string_comparashion(str1,str2):
    if isinstance(str1,str)==False or isinstance(str2,str)==False:
        return 0
    if str1==str2:
        return 1
    elif str2=="learn":
        return 3
    elif len(str2)>len(str1):
        return 2    

res=string_comparashion("s","learn")
print(res)