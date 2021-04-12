import baostock as bs
import pandas as pd

def getStockBasic(code):
    # 获取证券基本资料
    rs = bs.query_stock_basic(code=code)
    # 打印结果集
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    return pd.DataFrame(data_list, columns=rs.fields)

def getQueryHistoryKDataPlus(code,start_date,end_date):
    rs = bs.query_history_k_data_plus(code,
        "date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,peTTM,pbMRQ,psTTM,pcfNcfTTM,isST",
        start_date=start_date, end_date=end_date, 
        frequency="d", adjustflag="3") #frequency="d"取日k线，adjustflag="3"默认不复权
    print('query_history_k_data_plus respond error_code:'+rs.error_code)
    print('query_history_k_data_plus respond  error_msg:'+rs.error_msg)
    #### 打印结果集 ####
    data_list = []
    while (rs.error_code == '0') & rs.next():
        # 获取一条记录，将记录合并在一起
        data_list.append(rs.get_row_data())
    result = pd.DataFrame(data_list, columns=rs.fields)
    return result

End_date="2021-4-9"

# 登陆系统
lg = bs.login()
# 显示登陆返回信息
print('login respond error_code:'+lg.error_code)
print('login respond  error_msg:'+lg.error_msg)


rs = bs.query_all_stock(day=End_date)
print('query_all_stock respond error_code:'+rs.error_code)
print('query_all_stock respond  error_msg:'+rs.error_msg)

#### 打印结果集 ####
data_list = []
while (rs.error_code == '0') & rs.next():
    # 获取一条记录，将记录合并在一起
    data_list.append(rs.get_row_data())
result = pd.DataFrame(data_list, columns=rs.fields)

for row in range(result.shape[0]):
    code_name=result.loc[row]["code_name"]
    code=result.loc[row]["code"]
    
    code_basic_info=getStockBasic(code)
    print("Getting info:",code,code_name)
    # print(code_basic_info)
    for col in code_basic_info:
        if col not in result.columns.tolist():
            result[col]=""
            result.loc[row][col]=code_basic_info.loc[0][col]
        else:
            result.loc[row][col]=code_basic_info.loc[0][col]

for row in range(result.shape[0]):
    code_name=result.loc[row]["code_name"]
    code=result.loc[row]["code"]
    start_date=result.loc[row]["outDate"]
    print("Getting Detail info:",code,code_name)
    detail_info=getQueryHistoryKDataPlus(code=code,start_date=start_date,end_date=End_date)
    detail_info.to_csv("output/stock_database/"+code_name+"_"+code+".csv", encoding="utf-8", index=False)
#### 结果集输出到csv文件 ####   
result.to_csv("output/all_stock_basic_info.csv", encoding="utf-8", index=False)
print(result)

# 登出系统
bs.logout()