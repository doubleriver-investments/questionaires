# IB Download Data

The data from IB is encrypted csv files.

### U_Activity_DATE.csv

Here is a sample of the data, it is pipe separated values.

|Type|AccountID|ConID|SecurityID|Symbol|BBTicker|BBGlobalID|SecurityDescription|AssetType|Currency|BaseCurrency|TradeDate|TradeTime|SettleDate|TransactionType|Quantity|UnitPrice|GrossAmount|SECFee|Commission|Tax|Net|NetInBase|TradeID|TaxBasisElection|Description|FxRateToBase|ContraPartyName|ClrFirmID|Exchange|MasterAccountID|Van|AwayBrokerCommission|OrderID|ClientReference|TransactionID|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|D|*||||||||AUD|USD|20221003||20221003|INTACC|0|0|-1.64|0|0|0|-1.64|-7.0|||INTEREST ACCRUAL POSTING|0.6||||||0||||
|D|*||||||||CAD|USD|20221003||20221003|INTACC|0|0|9.6|0|0|0|9.6|7|||INTEREST ACCRUAL POSTING|0.7||||||0||||
|D|*||||||||MXN|USD|20221005||20221005|DINT|0|0|-6.1|0|0|0|-6.1|-3|||MXN DEBIT INT FOR SEP-2022|0.04||||||0||||

### U_CashReport_DATE.csv

Starting and ending cash amounts reported, pipe separated values.

|Type|AccountID|ReportDate|Currency|BaseSummary|Label|Total|Securities|Futures|IBUKL|
|--|--|--|--|--|--|--|--|--|--|
|D||20221003|USD|Y|Starting Cash|4|4|7|0|
|D||20221003|USD|Y|Cash FX Translation Gain/Loss|-4|-4|0|0|
|D||20221003|USD|Y|Ending Cash|4|4|7|0|
|D||20221003|USD|Y|Ending Settled Cash|4|4|7|0|

### U_NAV_DATE.csv

Very simple one line report showing current balances.

|Type|AccountID|BaseCurrency|Cash|CashCollateral|Stocks|SecuritiesBorrowed|SecuritiesLent|Options|Bonds|Commodities|Funds|Notes|Accruals|DividendAccruals|SoftDollars|Totals|TWR|CFDUnrealizedPL|ForexCFDUnrealizedPL|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|D|U|USD|4|0|4|0|0|2|0|0|0|0|1|1|0|8|0.014095864|0|0|

### U_Position_DATE.csv

Position provides view of the cash, holdings each day.

|Type|AccountID|ConID|SecurityID|Symbol|BBTicker|BBGlobalID|SecurityDescription|AssetType|Currency|BaseCurrency|Quantity|QuantityInBase|CostPrice|CostBasis|CostBasisInBase|MarketPrice|MarketValue|MarketValueInBase|OpenDateTime|FxRateToBase|ReportDate|SettledQuantity|SettledQuantityInBase|MasterAccountID|Van|AccruedInt|OriginatingOrderID|Multiplier|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|D|U|5||EEM   221216P00035000|EEM 12 P35|BBG012SYNV32|EEM 16DEC22 35 P|OPT|USD|USD|2|0|1.2|2.83|2.83|1.6|3|3||1|20221003|0|0|||0||1|
|D|U|5||EEM   221216P00036000|EEM 12 P36|BBG012SYNW76|EEM 16DEC22 36 P|OPT|USD|USD|2|0|1.2|2.83|2.83|2.1|4|4||1|20221003|0|0|||0||1|
