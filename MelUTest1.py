# NAME:         Melissa
# Guess:        We are making some kind of number filter, but I'm not sure what kind, yet... Maybe a cheat code or access code validator?

# Example
def hello_world():
    return "Hello!"

def function_1(data):
    n = 1
    while n * (n + 1) // 2 <= data:
        if n * (n + 1) // 2 == data:
            return True
        n += 1
    return False

def main():
    print("Function 1: ", function_1(1))

main()
