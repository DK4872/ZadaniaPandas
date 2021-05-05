import pandas as pd
import numpy as np
import xlrd
import openpyxl

print('ZADANIE1')
a = pd.ExcelFile('imiona.xlsx')
da = pd.read_excel(a, header=0)
print(da)
print(' ')
print('ZADANIE2')
a = pd.ExcelFile('imiona.xlsx')
da = pd.read_excel(a, header=0)
print(' ')
print('tylko te rekordy gdzie liczba nadanych imion była mniejsza niż 1000 w danym roku')
print(da[da['Liczba'] < 1000])
print(' ')
print('tylko rekordy gdzie nadane imię jest takie jak Twoje')
print(da[da['Imie'] == 'DOMINIK'])
print(' ')
print('sumę wszystkich urodzonych dzieci w całym danym okresie')
print(da['Liczba'].sum())
print(' ')
print('sumę dzieci urodzonych w latach 2005-2010')
da4 = (da[(da.Rok >= 2005) & (da.Rok <= 2010)])
print(da4['Liczba'].sum())
print(' ')
print('sumę urodzonych chłopców w 2000 roku')
da5 = (da[(da.Rok == 2000) & (da.Plec == 'M')])
print(da5['Liczba'].sum())
print(' ')
print('najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)')
m = da[da.Plec == 'M']
k = da[da.Plec == 'K']
x = m.loc[m.groupby('Rok')['Liczba'].idxmax()]
y = k.loc[k.groupby('Rok')['Liczba'].idxmax()]
print(x[['Rok', 'Imie']])
print(y[['Rok', 'Imie']])
print(' ')
print('najbardziej popularne imię dziewczynki i chłopca w całym danym okresie')
maxM = m.loc[m['Liczba'].idxmax()]
maxK = k.loc[k['Liczba'].idxmax()]
print(maxM.Imie, maxK.Imie)
print(da.groupby(['Rok', 'Plec'])['Liczba'].max())
(da.groupby(['Rok', 'Plec']).agg({'Liczba': ['max']}))
print(' ')
print('ZADANIE3')
df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal=',')
print(' ')
print('listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)')
df1 = df.Sprzedawca
df1 = df1.drop_duplicates()
print(df1)
print(' ')
print('5 najwyższych wartości zamówień')
df2 = df
df2.Utarg = df2.Utarg.astype(float)
df2 = df2.sort_values(by='Utarg', ascending=False)
print(df2['Utarg'].head(5))
print(' ')
print('ilość zamówień złożonych przez każdego sprzedawcę')
print(df.groupby(['Sprzedawca']).agg({'Sprzedawca': ['count']}))
print(' ')
print('sumę zamówień dla każdego kraju')
print(df.groupby(['Kraj']).agg({'idZamowienia': ['count']}))
print(' ')
print('sumę zamówień dla roku 2005, dla sprzedawców z Polski')
df5 = df[(df['Kraj'] == "Polska")]
start = '2005-01-01'
end = '2005-12-31'
df5 = df5[(df5['Data zamowienia'] >= start) & (df5['Data zamowienia'] <= end)]
print(df5)
print(' ')
print('średnią kwotę zamówienia w 2004 roku')
start2 = '2004-01-01'
end2 = '2004-12-31'
df6 = df[(df['Data zamowienia'] >= start2) & (df['Data zamowienia'] <= end2)]
df6 = df6.Utarg
df6 = pd.to_numeric(df6, downcast='float')
print(df6.mean())
print(' ')
print('zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv')
df2004 = df[(df['Data zamowienia'] >= start2) & (df['Data zamowienia'] <= end2)]
df2005 = df[(df['Data zamowienia'] >= start) & (df['Data zamowienia'] <= end)]
df2004.to_csv('zamówienia_2004.csv', sep=';', header=True, index=False)
df2005.to_csv('zamówienia_2005.csv', sep=';', header=True, index=False)
