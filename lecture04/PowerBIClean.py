# 'dataset' holds the input data for this script 输入数据集即输出同名，固定好为dataset
import pandas as pd

#df=pd.read(dataset)
completeddata=dataset.fillna(method='backfill',inplace=False)
dataset['FilledValues']=completeddata["SMI missing values"] # replace column name with yours

