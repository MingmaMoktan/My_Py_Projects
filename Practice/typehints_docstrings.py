from typing import Optional, Union, Any, Dict, List

def greet(name: str) -> str:
    """
    Generates a greeting message for the given name>
    Here goes any additional information about the functions purpose.
    Args:
        name (str): The name of the person to greet.
        Returns:
            str: The greeting message.
    """
    return f"Hello, {name}"

def square(number: Optional[int]) -> Optional[int]:
    if number is None:
        return None
    return number * number

def sum_list(inp: List[int]) -> int:
    return sum(inp)

def to_str(value: Union[int, float, str]) -> str:
    return str(value)

def echo(value: Any) -> Any:
    return value

# To input the function inside the function.----------------------------------------------

def apply_function(func, a: int, b:int) -> int:
    """
    Applies the given function to two integers.
    Before applying the function, increments a and b by one.
    After applying, decrements the result by one. 
    
    args:
        func: the function to apply
        a(int): First Integer
        b(int): Second Integer
    
    Returns:
        int: the result after decrementing it by one
    """
    result = func(a, b)
    result-=1
    return result
def add_two_ints(a:int, b:int)->int:
    return a+b

def subtract(a:int, b:int)->int:
    return a-b

result = apply_function(add_two_ints, 10, 20)
print(result)

sub = apply_function(subtract, 20, 10)
print(sub)

# ----------------------------------------------------------------------------------------

def do_sth_dict(d: Dict[str, Any]):
    print(d)

if __name__ == "__main__":
    greet_string = greet("Mingma")
    print(greet_string)
    num_square = square(None)
    print(num_square)