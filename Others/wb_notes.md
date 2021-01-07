### Indicators that are either deprecated, deleted or just causing issues
-> current account balance
-> gdp per person
-> rural population growth


## From Evans Mugi:
May I suggest adding the following with an eye on interest rates, currency movement and debt levels? These have historically shown to have a strong correl with ratings upgrades and downgrades, and do speak to sovereign risk
We do like to keep an eye on how these variables are trending as do have some implications on the book

##** Debt & FX **
External Debt % GDP   -> {DT.DOD.PVLX.CD: Present value of external debt (current US$)} / GDP
External Debt + **Internal Debt** % GDP -> {GB.DOD.FRGN.CD: External debt, end year (current US$)} + 
External Debt % Total Exports -> {GB.DOD.FRGN.CD: External debt, end year (current US$)} / {BX.GSR.GNFS.CD: Exports of goods and services (BoP, current US$)}
**ADDED** Exports% GDP -> {NE.EXP.GNFS.ZS: Exports of goods and services (% of GDP)}
Total Interest Payments % Total Exports -> {GC.XPN.INTP.CN: Interest payments (current LCU)} / {BX.GSR.GNFS.CD: Exports of goods and services (BoP, current US$)}

Months of Import Cover
-> {FI.RES.TOTL.MO: Total reserves in months of imports}
-> {FI.RES.TOTL.MO.WB: Total reserves in months of imports of goods and services}

Short Term External Debt Due % Reserves
Current A/c Balance + FDI / GDP
-> {BN.CAB.XOKA.CD: Current account balance (BoP, current US$)} + {BN.KLT.DINV.CD: Foreign direct investment, net (BoP, current US$)} / {NY.GDP.MKTP.CD: GDP (current US$)}
-> {BN.CAB.XOKA.GD.ZS: Current account balance (% of GDP)}

##** Government's Fiscal Position **
Fiscal Balance % GDP -> {GC.BAL.CASH.CD: Fiscal balance, cash surplus/deficit (current US$)} +++
Tax Revenue % GDP -> {GC.TAX.TOTL.GD.ZS: Tax revenue (% of GDP)} +++ 

##** Growth **
GDP/Capita  **DONE**
Real GDP Growth Rate 3 yr average -> {"NY.GDP.MKTP.KD.ZG": "GDP growth (annual %)"} +++
Level of inflation in last year -> {"NY.GDP.DEFL.KD.ZG": "Inflation, GDP deflator (annual %)"} +++
Private Sector Credit Growth
-> {"FM.AST.DOMO.CN": "Net domestic credit to private sector, stock (current LCU)"} +++
-> {DT.INT.MIBR.CD: PPG, IBRD (INT, current US$)}
-> {DT.INT.MIDA.CD: PPG, IDA (INT, current US$)}
-> {DT.INT.MLAT.CD: PPG, multilateral (INT, current US$)}
-> {DT.INT.OFFT.CD: PPG, official creditors (INT, current US$)}
-> {DT.INT.OFFT.CD: PPG, official creditors (INT, current US$)}
-> {DT.INT.PBND.CD: PPG, bonds (INT, current US$)}
-> {DT.INT.PCBK.CD: PPG, commercial banks (INT, current US$)}
-> {IC.CRED.ACC.CRD.RK: Rank: Getting credit (1=most business-friendly regulations)}


## ** On the qualitative side **
Quality of economic policies - this can be a binary based on whether country is on a certain type of IMF program or not
[Index of economic freedom score](https://www.heritage.org/index/ranking?version=448) -> to use BS4
Ease of doing business index
-> {“Ease of Doing Business Index”: “IC.BUS.EASE.XQ”.}
-> {IC.BUS.EASE.DFRN.DB1014: Global: Ease of doing business score (DB10-14 methodology)}

GINI index/ Gini coefficient -> {"SI.POV.GINI": "Gini index (World Bank estimate)"} +++
[Current LCU means Current Local Currency](https://datacatalog.worldbank.org/gdp-capita-current-lcu#:~:text=GDP%20is%20the%20sum%20of,the%20value%20of%20the%20products.) 
