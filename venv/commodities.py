from bloomberg import BBG
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from calendars import DayCounts

dc = DayCounts(dc='bus/252', calendar='anbima')
d1 = pd.to_datetime('2015-01-01')
res = dc.eom_preceding(d1) # pega fim do mes
res = dc.isbus(d1) # verifica se é bd
res = dc.preceding(d1) # pegar um bd anterior


letras = ['F','G','H','J','K','M','N','Q','U','V','X','Z']
meses = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

def build_ticker(commodity,month, year):
    if month <= 12:
        letra = letras[month-1]
        y = year%100
        year_2d = f"{y:02d}"
    else:
        letra = letras[(month-1) % 12]
        y = (year + month // 12)%100
        year_2d = f"{y:02d}"
    return commodity+letra+year_2d+" Comdty"


bbg = BBG()


end_date= '29-jun-2019'
before = -1

list_ticker = ["LX","LL","LN","LA","LT"]
info_tickers = {}

for tck in list_ticker:
    list_excess_returns = []
    list_basis = []
    year_in_use = 1997

    for month_in_use in range(7, 13):
        #print("-"*50)
        if month_in_use == 1:
            date = datetime(year_in_use-1,12,1)
            last_day = dc.eom_preceding(date).date().day
            start_date = str(last_day) + '-'+ meses[-1] + '-' + str(year_in_use-1)
        else:
            date = datetime(year_in_use, month_in_use - 1, 1)
            last_day = dc.eom_preceding(date).date().day
            start_date = str(last_day) + '-' + meses[month_in_use - 2] + '-' + str(year_in_use)
        print(start_date)
        l = [build_ticker(tck, month_in_use, year_in_use), build_ticker(tck, month_in_use + 1, year_in_use)]
        try:
            df2 = bbg.fetch_series(securities=l,
                               fields=['LAST_PRICE'],
                               startdate=start_date,
                               enddate=end_date)
        except KeyError as e:
            continue

        if df2.shape[1] >= 2:
            list=df2[build_ticker(tck, month_in_use, year_in_use)].values
            list1=df2[build_ticker(tck, month_in_use + 1, year_in_use)].values
            first=list[0]
            first1=list1[0]

            #print(first)
            #print(first1)

            # EXCESS RETURN

            if before > 0:
                er = ( first - before ) / before
                # print("Preco Mes anterior",first)
                # print("Preco Mes atual",before)
                # print("Month:", er )
                list_excess_returns.append(er)
                # print(list_excess_returns)
                before = first1
            else:
                before = first1


            # BASIS
            d_c1 = df2[build_ticker(tck, month_in_use, year_in_use)].dropna().index[-1][1].to_pydatetime()
            d_c2 = df2.index[-1][1].to_pydatetime()

            res = dc.days(pd.to_datetime(start_date), d_c1)
            res1 = dc.days(pd.to_datetime(start_date), d_c2)

            if res1 - res > 0:
                basis = 365*( (first / first1) - 1 ) / (res1 - res)
                list_basis.append(basis)
                # print(basis)
                # print(list_basis)

    for year_in_use in range(1998,2011):
        for month_in_use in range(1, 13):
            if month_in_use == 1:
                date = datetime(year_in_use-1,12,1)
                last_day = dc.eom_preceding(date).date().day
                start_date = str(last_day) + '-'+ meses[-1] + '-' + str(year_in_use-1)
            else:
                date = datetime(year_in_use, month_in_use - 1, 1)
                last_day = dc.eom_preceding(date).date().day
                start_date = str(last_day) + '-' + meses[month_in_use - 2] + '-' + str(year_in_use)
            print(start_date)
            l = [build_ticker(tck, month_in_use, year_in_use), build_ticker(tck, month_in_use + 1, year_in_use)]
            #print(l)
            try:
                df2 = bbg.fetch_series(securities=l,
                                   fields=['LAST_PRICE'],
                                   startdate=start_date,
                                   enddate=end_date)
            except KeyError as e:
                continue

            if df2.shape[1] >= 2:
                list=df2[build_ticker(tck, month_in_use, year_in_use)].values
                list1=df2[build_ticker(tck, month_in_use + 1, year_in_use)].values
                first=list[0]
                first1=list1[0]

                #print(first)
                #print(first1)

                # EXCESS RETURN
                if before > 0:
                    er = ( first - before ) / before
                    # print("Preco Mes anterior",first)
                    # print("Preco Mes atual",before)
                    # print("Month:", er )
                    list_excess_returns.append(er)
                    # print(list_excess_returns)
                    before = first1
                else:
                    before = first1

                # BASIS
                d_c1 = df2[build_ticker(tck, month_in_use, year_in_use)].dropna().index[-1][1].to_pydatetime()
                d_c2 = df2.index[-1][1].to_pydatetime()

                res = dc.days(pd.to_datetime(start_date), d_c1)
                res1 = dc.days(pd.to_datetime(start_date), d_c2)
                if res1 - res > 0:
                    basis = 365*( (first / first1) - 1 ) / (res1 - res)
                    list_basis.append(basis)
                #print(basis)
    print("---------",tck,"---------")
    array = np.array(list_excess_returns)
    info_tickers[tck] = {"Excess Returns":list_excess_returns}
    print("Excess Return mean:",array.mean())
    print("Excess Return std:",array.std())

    array2 = np.array(list_basis)
    info_tickers[tck]["Basis"] = list_basis

    print("basis mean:",array2.mean())
    print("basis max:",array2.max())
    print("basis min:",array2.min())