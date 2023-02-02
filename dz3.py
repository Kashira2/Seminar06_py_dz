def open_data(num1, my_list):
    for i in range(len(num1) - 1):
        if num1[i].isdigit():
            number = int(num1[i])
            for j in range(number):
                my_list.append(num1[i + 1])
    
    return my_list


num1 = input('Введите данные, которые необходимо сжать или восстановить: ')
if not num1[len(num1)-1] == num1[len(num1)-2]:
    temp = num1[len(num1)-1]
num1 = num1 + '1'
my_list = []
if num1[0].isdigit():
    open_data(num1, my_list)
    my_list = ''.join(my_list)
    print(my_list)
else:
    count2 = 0
    i = 1
    if num1[0] == num1[1]:    
        while count2 != len(num1)-1:           
            count = 1
            while num1[i] == num1[i-1]:
                count += 1                              
                i += 1                                     
                count2 += 1
            my_list.append(str(count))
            my_list.append(num1[count2 - 1])
            i += 1
            count2 += 1
        for item in my_list:
            my_list = ''.join(my_list)
        if not num1[len(num1)-2] == num1[len(num1)-3]:
            my_list = my_list + '00'
            my_list = my_list.replace(my_list[len(my_list)-3] +'00', temp)
    else:
        my_list.append('1')
        my_list.append(num1[0])
        while count2+1 != len(num1)-1:           
            count = 1
            while num1[i+1] == num1[i]:
                count += 1                              
                i += 1                                     
                count2 += 1
            my_list.append(str(count))
            my_list.append(num1[count2])
            i += 1
            count2 += 1
        for item in my_list:
            my_list = ''.join(my_list)
        if not num1[len(num1)-2] == num1[len(num1)-3]:
            my_list = my_list + '00'
            my_list = my_list.replace(my_list[len(my_list)-3] +'00', temp)
    print(my_list)

    
        
    

    
