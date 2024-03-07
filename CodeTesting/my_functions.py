def divide_neighbors(in_list):    
    output = []
    
    for el1, el2 in zip(in_list[1:], in_list):
        output.append(el1 / el2)
    
    return output


def sum_list(input_list):
    """add all values in a list - return sum"""
    
    output = 0
    
    for val in input_list:
        output += val
        
    return output