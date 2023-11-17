def decomposition_Y(Y):
    arr = []
    for i in range(2,Y+1):
        arr.append(i)
    print(arr)
    return arr

# def find_multipliers_Y(arr):
#     n_arr = []
#     for x,y in arr:
#         if x*y==arr[-1]:
#             arr.append(x)
#     print(n_arr)

def find_multipliers_Y(arr):
    new_arr = []
    inx = 0
    Y = arr[-1]
    while arr != []:
        for el in arr:
            if arr[inx]*el==Y:
                new_arr.append(arr[inx])
                new_arr.append(el)
        arr.pop(0)
    new_arr.sort()
    print(new_arr)
    return new_arr

def delete_double_x(arr):
    new_arr = []
    for i in arr:
        if i not in new_arr:
            new_arr.append(i)
    print(new_arr)
    return new_arr
    
def find_just_x_in_arr(arr):
    answer_arr = []
    for x in arr:
        k=0
        for i in range(2,(x//2)+1):
            if x % i == 0:
                k += 1
        if k <= 0:
            answer_arr.append(x)
    if len(answer_arr) > 0:   
        print(f'Ответ: {answer_arr}')
    else: print('У этого числа нет простых множителей кроме, возможно, самого числа')


# mul(decomposition_Y(40))
# find_multipliers_Y(decomposition_Y(40))
# Y = int(input())
find_just_x_in_arr(delete_double_x(find_multipliers_Y(decomposition_Y(int(input())))))




