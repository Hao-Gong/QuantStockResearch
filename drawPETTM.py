import baostock as bs
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def data2NumpyNormalized(stock_data,name):
    np_data=data2Numpy(stock_data,name)
    np_data=np_data/np.max(np_data)
    return np_data

def data2Numpy(stock_data,name):
    np_data=result[name].to_numpy()
    float_list=[]
    for data in np_data:
        float_list.append(float(data))
    return np.array(float_list)

#### 登陆系统 ####
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)

#### 获取历史K线数据 ####
# 详细指标参数，参见“历史行情指标参数”章节
rs = bs.query_history_k_data_plus("sz.002151",
    "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
    start_date='2017-06-01', end_date='2021-4-9', 
    frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
print('query_history_k_data_plus respond error_code:'+rs.error_code)
print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

plt.plot(data2NumpyNormalized(result,"peTTM"),label="peTTM")
plt.plot(data2NumpyNormalized(result,"close"),label="close")
plt.legend()
plt.show()
#### 结果集输出到csv文件 ####
result.to_csv("output/history_k_data.csv", encoding="gbk", index=False)
# print(result)

#### 登出系统 ####
bs.logout()