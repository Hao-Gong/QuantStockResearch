import csv
import datetime
class recode:
    def __init__(self,open_,high_,low_,close_):
        self.open = float(open_)
        self.high = float(high_)
        self.low = float(low_)
        self.close = float(close_)
        
class stock:
    def __init__(self,code_):
        self.code = code_
        self.record_dic_s = {}
        
    def add_record(self,date_,open_,high_,low_,close_):
        r = recode(open_,high_,low_,close_)
        self.record_dic_s[date_] = r
        
    
    
def load_from_file(path):
    rows = []
    with open(path,'r',encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            rows.append(row)
    
    st = stock(rows[1][1])
    for r in rows[1:]:
        st.add_record(r[0],r[2],r[3],r[4],r[5])
    
    # print(st.record_dic_s)
    
def getdate(n):
    today = datetime.date.today()
    mmm = "2021-08-05"
    mmm = datetime.datetime.strptime(mmm, "%Y-%m-%d").date()
    targetday = mmm - datetime.timedelta(days=n)
    targetday = str(targetday)
    # mm = today - targetday
    # print(targetday,type(targetday))