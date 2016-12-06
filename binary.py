def add_binary(a,b):
    binary = bin(a + b)
    watabe = str(binary)
    print watabe[2:]
    # I am aware that it isn't good practice to name variables watabe. Sorry.
    
    
add_binary(1, 1)
add_binary(0,1)
