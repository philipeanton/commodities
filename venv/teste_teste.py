from bloomberg import BBG
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from calendars import DayCounts

dc = DayCounts(dc='bus/252', calendar='anbima')
start_date =  "28-aug-1997"
end_date= '28-jun-2019'


bbg = BBG()
try:
    df2 = bbg.fetch_series(securities=['LLU99 Comdty', 'LLV99 Comdty'],
                           fields=['LAST_PRICE'],
                           startdate=start_date,
                           enddate=end_date)
except KeyError as e:
    pass

d_c1 = df2['LLU99 Comdty'].dropna().index[-1][1].to_pydatetime()
d_c2 = df2.index[-1][1].to_pydatetime()

res = dc.days(pd.to_datetime(start_date), d_c1)
print(res)
res = dc.days(pd.to_datetime(start_date), d_c2)
print(res)