h, m, s = map(int, input('*** Converting hh.mm.ss to seconds ***\nEnter hh mm ss : ').split(' '))

if m < 0 or m > 59:
    print('mm({:02d}) is invalid!'.format(m))
    exit()
elif s < 0 or s > 59:
    print('ss({:02d}) is invalid!'.format(s))
    exit()
    
print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(h, m, s, h * 3600 + m * 60 + s))