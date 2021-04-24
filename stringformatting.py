n = int(input())

for i in range(1, n+1):
    decimal = i
    binary = bin(decimal)
    octal = oct(decimal)
    hexadecimal = hex(decimal)
    width = len(bin(n)[2:])
    print(str(decimal).rjust(width), end=' ')
    print(str(octal[2:]).rjust(width), end=' ')
    print(str(hexadecimal[2:]).rjust(width).upper(), end=' ')
    print(str(binary[2:]).rjust(width), end=' ')
    print()
