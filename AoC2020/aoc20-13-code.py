arrival = 1000507
x = None
data = (29,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,631,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13,19,x,x,x,23,x,x,x,x,x,x,x,383,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17)

#arrival=939
#data=(7,13,x,x,59,x,31,19)
#data=(17,x,13,19)
#data=(1789,37,47,1889)

buses = [a for a in data if a != None]
departures = [(arrival // a+1)*a-arrival for a in buses]
mint = min(departures)
pos = departures.index(mint)
print(f'bus={buses[pos]} mint={mint} result 1 = {mint*buses[pos]}')

# part 2
# https://pl.wikipedia.org/wiki/Chi%C5%84skie_twierdzenie_o_resztach
# http://adamski.is.pw.edu.pl/index.php/4-5-chinskie-twierdzenie-o-resztach/

buses2 = [(a,i) for i,a in enumerate(data) if a != None]
print(buses2) 

found = False
length = len(buses2)
a0, a1 = buses2[0]

for b0, b1 in buses2[1:]:
    print(f'({b0=} {b1=})')

    i0, i1 = 1, 1
    p0 = a0 * i0 + a1
    p1 = b0 * i1 + b1
    found = False

    while not found:
        if p0>p1:
#            i1 += 1
#            p1 = b0 * i1 + b1
#           optimization for large numbers:
            p1 = (((p0-b1)//b0))*b0+b1
            if p0>p1:
                p1+=b0
        elif p0<p1:
            i0 += 1
            p0 = a0 * i0 + a1
        else:
            found=True
            a0 = a0*b0
            a1 = p0
            print(f'{a0=} {a1=} result = {a0-a1}')
    
