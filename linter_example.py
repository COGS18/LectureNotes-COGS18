def MyFunction(input_num):
    
    my_list = [0,1,2,3]
    if 1 in my_list: ind = 1
    else:
      ind = 0
    qq = []
    for i in my_list [ind:]:
        qq.append(input_num/i)
    return qq
