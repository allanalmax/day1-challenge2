def generate_dict():
    squares = {}
    for element in range(1,16):
        squares[element] = element ** 2
    
    return squares

c = generate_dict()
print(c)