ipt1 = int(input())
ipt2 = int(input())

opt1 = ipt1 * ((ipt2 % 100) % 10)
opt2 = ipt1 * ((ipt2 % 100)//10)
opt3 = ipt1 * (ipt2//100)
result = ipt1 * ipt2

print(opt1, opt2, opt3, result)
