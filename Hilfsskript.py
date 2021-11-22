from numpy import double
import pandas as pd

print('Read train')
df_train: pd.DataFrame = pd.read_csv('./data-classification/adult.data', sep=', ', engine='python', header=None, names=[
'age', 'workclass', 'fnlwgt', 
'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 
'sex' , 'capital-gain' , 'capital-loss',
'hours-per-week', 'native-country', "<50k"
])

print('Read test')
df_test: pd.DataFrame = pd.read_csv('./data-classification/adult.test', sep=', ', engine='python', header=None, names=[
'age', 'workclass', 'fnlwgt', 
'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 
'sex' , 'capital-gain' , 'capital-loss',
'hours-per-week', 'native-country', "<50k"
])
df_test.drop(index=0, inplace=True)

def isNumber(val):
    return type(val) == int or type(val) == float or type(val) == double

def checkNumber(column, header):
    print(header + ' begin')
    for val in column:
        if not isNumber(val):
            print('\t' + str(type(val)))
            break
    print(header + ' end')

def nummern(df):
    title = 'age'
    checkNumber(df[title], title)
    title = 'fnlwgt'
    checkNumber(df[title], title)
    title = 'education-num'
    checkNumber(df[title], title)
    title = 'capital-gain'
    checkNumber(df[title], title)
    title = 'capital-loss'
    checkNumber(df[title], title)
    title = 'hours-per-week'
    checkNumber(df[title], title)

def whiteSpace(val):
    return val[0] == ' ' or val[-1] == ' '

def checkSpace(column, header):
    print(header + ' begin')
    for val in column:
        count = 0
        if whiteSpace(val):
            print(str(count) + ': \'' + str(val) + '\'')
        count += 1
    print(header + ' end')

def leerzeichen(df):
    title = 'workclass'
    checkSpace(df[title], title)
    title = 'education'
    checkSpace(df[title], title)
    title = 'marital-status'
    checkSpace(df[title], title)
    title = 'occupation'
    checkSpace(df[title], title)
    title = 'relationship'
    checkSpace(df[title], title)
    title = 'race'
    checkSpace(df[title], title)
    title = 'sex'
    checkSpace(df[title], title)
    title = 'native-country'
    checkSpace(df[title], title)
    title = '<50k'
    checkSpace(df[title], title)

print('+++++++++++++++\n++++ Train ++++\n+++++++++++++++')
leerzeichen(df_train)
print('++++++++++++++\n++++ Test ++++\n++++++++++++++')
leerzeichen(df_test)
