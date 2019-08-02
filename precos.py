from bloomberg import BBG
import pandas as pd

start_date = '17-oct-2001'
#end_date = pd.to_datetime('')
end_date= '09-oct-2003'
bbg = BBG()

# todos contratos negociados desde outubro de 2003
#df1 = bbg.fetch_series(securities=['CTV03 Comdty','CTZ03 Comdty','CTH04 Comdty','CTK04 Comdty','CTN04 Comdty','CTV04 Comdty','CTZ04 Comdty','CTH05 Comdty','CTK05 Comdty','CTN05 Comdty'],
df1 = bbg.fetch_series(securities=['CTV03 Comdty'],
                      fields=['PX_LAST'],
                      startdate=start_date,
                      enddate=end_date)
print(df1)

start_date = '12-dec-2001'
end_date= '05-dec-2003'
bbg = BBG()

df2 = bbg.fetch_series(securities=['CTZ03 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df2)

start_date = '14-mar-2002'
end_date= '09-mar-2004'
bbg = BBG()

df3 = bbg.fetch_series(securities=['CTH04 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df3)

start_date = '16-may-2002'
end_date= '06-may-2004'
bbg = BBG()

df4 = bbg.fetch_series(securities=['CTK04 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df4)

start_date = '17-jul-2002'
end_date= '08-jul-2004'
bbg = BBG()

df5 = bbg.fetch_series(securities=['CTN04 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df5)

start_date = '17-oct-2002'
end_date= '07-oct-2004'
bbg = BBG()

df6 = bbg.fetch_series(securities=['CTV04 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df6)

start_date = '13-dec-2002'
end_date= '08-dec-2004'
bbg = BBG()

df7 = bbg.fetch_series(securities=['CTZ04 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df7)

start_date = '17-mar-2003'
end_date= '08-mar-2004'
bbg = BBG()

df8 = bbg.fetch_series(securities=['CTH05 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df8)

start_date = '15-may-2003'
end_date= '06-may-2005'
bbg = BBG()

df9 = bbg.fetch_series(securities=['CTKO5 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df9)

start_date = '10-jul-2003'
end_date= '07-jul-2005'
bbg = BBG()

df10 = bbg.fetch_series(securities=['CTN05 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df10)

start_date = '10-oct-2003'
end_date= '07-oct-2005'
bbg = BBG()

df11 = bbg.fetch_series(securities=['CTV05 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df11)

start_date = '12-dec-2003'
end_date= '07-dec-2005'
bbg = BBG()

df12 = bbg.fetch_series(securities=['CTZ05 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df12)

start_date = '10-mar-2004'
end_date= '09-mar-2006'
bbg = BBG()

df13 = bbg.fetch_series(securities=['CTH06 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df13)

start_date = '14-may-2004'
end_date= '08-may-2006'
bbg = BBG()

df14 = bbg.fetch_series(securities=['CTK06 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df14)

start_date = '16-jul-2004'
end_date= '07-jul-2006'
bbg = BBG()

df15 = bbg.fetch_series(securities=['CTN06 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df15)


start_date = '15-oct-2004'
end_date= '09-oct-2006'
bbg = BBG()

df16 = bbg.fetch_series(securities=['CTV06 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df16)

start_date = '12-dec-2004'
end_date= '06-dec-2006'
bbg = BBG()

df17 = bbg.fetch_series(securities=['CTZ06 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df17)

start_date = '16-mar-2005'
end_date= '08-mar-2007'
bbg = BBG()

df18 = bbg.fetch_series(securities=['CTH07 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df18)

start_date = '09-may-2005'
end_date= '08-may-2007'
bbg = BBG()

df19 = bbg.fetch_series(securities=['CTK07 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df19)

start_date = '15-jul-2005'
end_date= '09-jul-2007'
bbg = BBG()

df20 = bbg.fetch_series(securities=['CTN07 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df20)

start_date = '11-oct-2005'
end_date= '09-oct-2007'
bbg = BBG()

df21 = bbg.fetch_series(securities=['CTV07 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df21)

start_date = '08-dec-2005'
end_date= '06-dec-2007'
bbg = BBG()

df22 = bbg.fetch_series(securities=['CTZ07 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df22)

start_date = '10-mar-2006'
end_date= '06-mar-2008'
bbg = BBG()

df23 = bbg.fetch_series(securities=['CTH08 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df23)

start_date = '09-may-2006'
end_date= '07-may-2008'
bbg = BBG()

df24 = bbg.fetch_series(securities=['CTK08 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df24)

start_date = '10-jul-2006'
end_date= '09-jul-2008'
bbg = BBG()

df25 = bbg.fetch_series(securities=['CTN08 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df25)

start_date = '11-oct-2006'
end_date= '09-oct-2008'
bbg = BBG()

df26 = bbg.fetch_series(securities=['CTV08 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df26)

start_date = '14-dec-2006'
end_date= '08-dec-2008'
bbg = BBG()

df27 = bbg.fetch_series(securities=['CTZ08 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df27)

start_date = '09-mar-2007'
end_date= '09-mar-2009'
bbg = BBG()

df28 = bbg.fetch_series(securities=['CTH09 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df28)

start_date = '16-may-2007'
end_date= '06-may-2009'
bbg = BBG()

df29 = bbg.fetch_series(securities=['CTK09 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df29)

start_date = '10-jul-2007'
end_date= '09-jul-2009'
bbg = BBG()

df30 = bbg.fetch_series(securities=['CTN09 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df30)

start_date = '10-oct-2007'
end_date= '08-oct-2009'
bbg = BBG()

df31 = bbg.fetch_series(securities=['CTV09 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df31)

start_date = '16-nov-2007'
end_date= '08-dec-2009'
bbg = BBG()

df32 = bbg.fetch_series(securities=['CTZ09 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df32)

start_date = '16-nov-2007'
end_date= '09-mar-2010'
bbg = BBG()

df33 = bbg.fetch_series(securities=['CTH10 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df33)

start_date = '16-nov-2007'
end_date= '06-may-2010'
bbg = BBG()

df34 = bbg.fetch_series(securities=['CTK10 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df34)

start_date = '16-nov-2007'
end_date= '08-jul-2010'
bbg = BBG()

df35 = bbg.fetch_series(securities=['CTN10 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df35)

start_date = '16-nov-2007'
end_date= '07-oct-2010'
bbg = BBG()

df36 = bbg.fetch_series(securities=['CTV10 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df36)

start_date = '01-dec-2007'
end_date= '08-dec-2010'
bbg = BBG()

df37 = bbg.fetch_series(securities=['CTZ10 Comdty'],
                       fields=['PX_LAST'],
                       startdate=start_date,
                       enddate=end_date)
print(df37)




# Grabs cashflow payments of corporate bonds
#df = bbg.fetch_cash_flow('EI1436001 Govt', pd.to_datetime('03-jul-2017'))
#print(df)

# Grabs weights of the components of an index
#df = bbg.fetch_index_weights(index_name='IBOV Index', ref_date=pd.to_datetime('03-jul-2017'))
#print(df)
#print(df.sum())

# Grabs all the contracts from a generic series
#futures_list = bbg.fetch_futures_list(generic_ticker='CT1 Comdty')
#print(futures_list)

# grabs the first notice date for each contract
#df_fn = bbg.fetch_contract_parameter(securities=futures_list, field='FUT_NOTICE_FIRST')
#print(df_fn)

# fetches fields with bulk data
#df_bulk = bbg.fetch_bulk_data(index_name='AAPL US Equity', field='PG_REVENUE', ref_date=start_date)
#print(df_bulk)

# fetches historical dividends
#df_div = bbg.fetch_dividends('AAPL US Equity', end_date)