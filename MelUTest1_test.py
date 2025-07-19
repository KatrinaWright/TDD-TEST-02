import MelUTest1 as M1;

# Example Passing Test
def test_hello_pass():
    assert M1.hello_world() == "Hello!"

# Example Failed Test
# Uncomment, run once & then comment out again
#def test_hello_fail():
#    assert hello.hello_world() == "Hello World!"

#########################
#  HW Assignment Tests  #
#########################

# Problem 1 Tests
def test_function_one():
    assert M1.function_1( 1 ) == True
    
def test_function_zero():
    assert M1.function_1( 0 ) == False

def test_function_three():
    assert M1.function_1( 3 ) == True

def test_function_ss():
    assert M1.function_1( 15 ) == True

def test_function_list():
    list = [ 1, 3, 6, 10, 15, 21, 28, 36, 45, 55] 
    for num in list:
        assert M1.function_1( num ) == True

