import time 

num = int(input("Enter a number: "))
milsec = int(input("Enter milliseconds to wait: "))

sec = milsec / 1000
time.sleep(sec)

sqrt = num ** 0.5

txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum=num, fsec=milsec, fsqrt=sqrt)
print(txt)
