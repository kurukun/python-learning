name = "咕鹭"
stock_price = 20.11
stock_code = "003302"
factor = 1.2
growth_day = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股价：{stock_price}")
print("每日的增长系数是：%.2f，经过%d天的增长后，股价到达了%.2f" % (factor, growth_day, stock_price + factor * stock_price))