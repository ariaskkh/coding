a = int(input(), 2)
b = int(input(), 2)

print(bin(a & b)[2:].zfill(10))
print(bin(a | b)[2:].zfill(10))
print(bin(a ^ b)[2:].zfill(10))
print(~bin(a))
# print(bin(~b)[2:].zfill(10))