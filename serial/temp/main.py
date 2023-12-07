import machine

temppin = machine.ADC(4)
print(temppin.read_u16())
data = temppin.read_u16() * (3.3/65543)
print(data)

temp = 27 - (data - 0.706) / 0.001721
print(temp)