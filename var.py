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

result=[output]
result.append(values)
print("Final:",result)
