import re

diagonals = [
    [-3,-2,-1,1,2,3],
    [-21,-14,-7,7,14,21],
    [-24,-16,-8,8,16,24],
    [-18,-12,-6,6,12,18]
]


symbols = {"1" :'A',
           "-1":'B',
           "0" :'_',
           "-2":'X'}

def stringDiag(diag,player=1):
    str_diag = ''
    for x in diag:
        if x == str(player):
            str_diag+= symbols[abs(player)]
        elif x == str(player*-1):
            str_diag+= symbols[-abs(player)]
        else:
            str_diag+= symbols[str(int(x))]
    return str_diag

def symbolsToNumbers(string_val):
    vector = []
    for i in range(6):
        vector.append(symbols[string_val[i]])
    return vector

def calculateOptions():
    temp_optins = {}
    keys = symbols.values()
    for one in keys:
        for two in keys:
            for three in keys:
                for four in keys:
                    for five in keys:
                        for six in keys:
                            str_val = f'{one}{two}{three}{four}{five}{six}'
                            str_weight = 0
                            if 'AAA' in str_val:
                                str_weight = 100
                            elif 'BBB' in str_val:
                                str_weight = 80
                            elif re.match('.*[AB_]X+[AB_].*', str_val):
                                continue
                            elif re.match('^X[AB_]X.*', str_val) or re.match('.*X[AB_]X$',str_val):
                                continue
                            elif re.match('[AB_]{1,2}X.*',str_val) or re.match('.*X[AB_]{1,2}$',str_val):
                                continue
                            elif re.match('.+A{2}.+', str_val) or re.match('AA_.*', str_val) or re.match('.*_AA', str_val): str_weight = 50
                            elif re.match('.+B{2}.+', str_val) or re.match('BB_.*', str_val) or re.match('.*_BB', str_val):
                                str_weight = 40
                            elif re.match('.*X[AB_]{2}X.*', str_val):
                                str_weight = 1
                            elif re.match('.*X_{3,4}X.*', str_val):
                                str_weight = 15
                            elif re.match('.*A[_]{3}.*', str_val) or re.match('.*[_]{3}A.*', str_val):
                                str_weight = 30
                            elif re.match('.*[A_]{3,4}.*', str_val) or re.match('.*[A_]{3,4}.*', str_val):
                                str_weight = 30
                            elif re.match('.*BABAB.*', str_val) or re.match('.*ABABB.*', str_val) or re.match('.*BBABA.*', str_val):
                                str_weight = 1
                            elif re.match('.*B_B.*', str_val):
                                str_weight = 25
                            elif re.match('.*B__.*', str_val) or re.match('.*__B.*',str_val) or  re.match('.*_B_.*',str_val):
                                str_weight = 10
                            elif re.match('.*X[AB_]{3}X.*', str_val):
                                str_weight = 1
                            else:
                                str_weight = 1
                                pass
                            temp_optins[str_val] = str_weight
    return temp_optins

surrounding_options = calculateOptions()
# print(surrounding_options)
#print(len(surrounding_options))