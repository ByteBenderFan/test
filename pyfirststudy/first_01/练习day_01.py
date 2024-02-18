name="传智播客"
stock_price=19.99
growth=1.2
days=7
daima="003032"
factor=stock_price*1.2**7
print(f"公司:{name},股票代码:{daima},当前股价:{stock_price}")

print("增长系数是%.1f,经过%d天的增长后,股价达到了%.2f元"%(growth,days,factor))