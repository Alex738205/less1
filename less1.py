
def strcounter1(s):
    for sym in set(s):
        count = 0
        for sud_sym in s:
            if sym == sud_sym:
                count +=1
        print(f'{sym} - {count}')

strcounter1('zzzzzzzzzz')     


def strcounter2(s):
    for sym in set(s):
        print(f'{sym} - {s.count(sym)}')

strcounter2('abcsfh')     


def strcounter3(s):
    sym_dict = {}
    for sym in set(s):
        sym_dict[sym] = sym_dict.get(sym, 0) + 1

    for sym, count in sym_dict.items():
        print(f'{sym} - {count}')

strcounter3('abcsf')    

