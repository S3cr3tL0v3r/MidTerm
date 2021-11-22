import pandas

df_train = pandas.read_csv('./data-classification/adult.data', sep=', ', engine='python', header=None, names=[
'age', 'workclass', 'fnlwgt', 
'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 
'sex' , 'capital-gain' , 'capital-loss',
'hours-per-week', 'native-country', "<50k"
])

df_test = pandas.read_csv('./data-classification/adult.test', sep=', ', engine='python', header=None, names=[
'age', 'workclass', 'fnlwgt', 
'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 
'sex' , 'capital-gain' , 'capital-loss',
'hours-per-week', 'native-country', "<50k"
])
df_test.drop(index=0, inplace=True)