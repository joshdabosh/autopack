def divider(vin,vout,r1):
    r2 = ((vout)*(r1))/(vin-vout)

    return r2

vin = int(raw_input('vin: '))
vout = int(raw_input('vout: '))
r1 = int(raw_input('r1: '))

print divider(vin, vout, r1)
