ls = sorted(map(int, input('Enter All Bid : ').split()))

if len(ls) < 2:
    print('not enough bidder')
elif ls[-1] == ls[-2]:
    print('error : have more than one highest bid')
else:
    print('winner bid is {} need to pay {}'.format(ls[-1], ls[-2]))