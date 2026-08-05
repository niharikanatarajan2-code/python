switches=int(input("Enter the smart switch value(decimal): "))
print("\n===My Smart Switch Bit Monitor===")
print("Decimal Value:",switches)
print("Binary Value:",format(switches,'08b'))
on_count=bin(switches).count('1')
print("Total Switches ON:",on_count)
print("\nSwitch Status:")
for bit in range(8):
    mask=1<<bit
    if switches & mask:
        print(f"Switch {bit+1}: ON")
    else:
        print(f"Switch {bit+1}: OFF")
bit_to_check=int(input("\nEnter switch number to check (0-7): "))
mask=1<<bit_to_check
print("Bit Mask:",format(mask,'08b'))