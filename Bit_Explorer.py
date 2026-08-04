a=10
b=6
def bits(n,width=4):
    return format(n &((1<<width)-1),f'0{width}b')
print("===Bit Explorer===")
print("a=",a,"->",bits(a))
print("b=",b,"->",bits(b))
print()
print("AND a&b",a&b,"->",bits(a&b))
print("OR a|b=",a|b,"->",bits(a|b))
print()
print("NOT ~a=",~a&0xFF,"->",bits(~a,8))
print("XOR a^b=",a^b,"->",bits(a^b))
print()
print("LEFT a<<1=",a<<1,"(a x 2)")
print("RIGHT a>>1=",a>>1,"(a / 2)")
