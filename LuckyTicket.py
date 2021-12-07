c = 0
for LuckyTicket in range(1000000):
    num1 = (LuckyTicket // 100000) % 10
    num2 = (LuckyTicket // 10000) % 10
    num3 = (LuckyTicket // 1000) % 10
    num4 = (LuckyTicket // 100) % 10
    num5 = (LuckyTicket // 10) % 10
    num6 = LuckyTicket % 10

    if num1+num2+num3 == num4+num5+num6:
        c += 1
        print(num1, num2, num3, num4, num5, num6)