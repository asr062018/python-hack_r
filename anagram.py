string1 = str(raw_input())
string2 = str(raw_input())
# string1 = 'abc'
# string2 = 'cde'
def _check(string1,string2):
    list_str1=list(string1)
    list_str1.sort()
    list_str2=list(string2)
    list_str2.sort()
    add_str = set(list_str1+list_str2)
    extar = set(list_str1).intersection(set(list_str2))
    print len(add_str.difference(extar))

print len(string1), len(string2)
_check(string1,string2)

