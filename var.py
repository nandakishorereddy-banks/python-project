values = [10, 20, 30]  
result = 0
def process_data(data, multiplier=2):
    temp = data
    temp.append(40)  
    def inner_function():
        values = [100]   
        nonlocal_result = None 
        
        global result
        result = sum(temp) * multiplier
        
    inner_function()
    return result
    
original_id = id(values)
print(f"Before: values={values}, result={result}, id={original_id}")

output = process_data(values)

print(f"After: values={values}, result={result}, id={id(values)}")
print(f"Output returned from function: {output}")

explanation:
1.values = [10, 20, 30]
     We use this list to show how a mutable object can be changed inside a function and still affect the outside code
2.result = 0
     This variable is used to show how an immutable type behaves when we try to change it in different scopes
3.original_id = id(values)
     We store the ID to check later whether the same list object is being modified or a new one is created
4.def process_data(data, multiplier=2):
     This function is used to demonstrate how function scope and default arguments work
5.temp = data
     This line shows that Python does not create a copy; both variables point to the same list in memory
6.temp.append(40)
      We use this to show that modifying a mutable object inside a function also changes it outside
7.def inner_function():
      This nested function is used to explain how enclosing (nested) scopes work in Python
8.values = [100]
      This line shows variable shadowing, where a local variable hides an outer variable with the same name
9.nonlocal result
       We use this so we can update the variable from the enclosing function, not create a new local one
10.global result
       result updates the variable from the global scope
11.result.append(values)
       This demonstrates that Python allows dynamic typing, and lists can store different types and references

conclusion:
1.Mutability
       Lists can be modified directly, so changes affect the original object unless a copy is made
2.Scoping
        Python uses the LEGB rule, and incorrect use of global or nonlocal causes errors
3.Dynamic typing
         A variable can change its data type at runtime
4.Shadowing 
        A local variable with the same name hides an outer variable without changing it
