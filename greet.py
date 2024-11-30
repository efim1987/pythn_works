def hello(call_back, name):
    print(call_back(name))
def greet(name):
    return f"Hello, {name}"
hello(greet, "Ilya")
