# R1 first loan daily rate, D1 after the first period of days, R2 increase in daily rate for second loan,
# D2 after second period of days, R3 rate of 3rd loan, D3 after 3rd period of days, K how much you are willing to pay
# Data to test      1000, 3, 500, 10, 1500, 7, 21000
def get_days_of_power(R1, D1, R2, D2, R3, D3, K):
    # create a list for period of days and daily rate
    d = [D1, D2, D3]
    r = [R1, R2, R3]
    # get the minimum days in list
    days = min(d)
    index = 0
    # length of d is 3
    for i in range(len(d)):
        # if d at i is equal to the days in list
        if d[i] == days:
            # use that day i as index
            index=i
            break
    # index is still 0, rate = 1000 from R1
    rate = r[index]


    # K is our max amount we will pay, 21000
    while K >= rate:
        # 21000-1000 K=20000 after first iteration
        K -= rate
        # days will keep adding until it equals a day in d list
        days += 1
        # 7 is in d
        if days in d:
            for i in range(len(d)):
                # keep checking index of i until it equals days 7, which would be 2
                if d[i] == days:
                    index=i
                    break
            # rate 1000 + r[2] 1500
            rate += r[index]
    # days 13 - 3 = 10
    return days-min(d)

print(get_days_of_power(1000, 3, 500, 10, 1500, 7, 21000))

# print(get_days_of_power(R1=3000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=700000))
# print(get_days_of_power(R1=500, D1=3, R2=500, D2=10, R3=500, D3=7, K=21000))
# print(get_days_of_power(R1=1300, D1=0, R2=500, D2=0, R3=1500, D3=7, K=10000))
# print(get_days_of_power(R1=10000, D1=3, R2=500, D2=10, R3=1500, D3=7, K=11000))