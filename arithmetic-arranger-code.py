def arithmetic_arranger(problems,rpta=False):
    operators = []
    nums1 = []
    nums2 = []
    num = ''
    if len(problems)>5:
        print('Error: Too many problems.')
        quit()
    for i in problems:
        lst = i.split()
        if len(lst[0]) > 4 or len(lst[2]) > 4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        if lst[0].isdigit():
            nums1.append(lst[0])
        else:
            print("Error: Numbers must only contain digits.")
            quit()
        if lst[1] == '+' or lst[1] == '-':
            operators.append(lst[1])
        else:
            print("Error: Operator must be '+' or '-'.")
            quit()
        if lst[2].isdigit():
            nums2.append(lst[2])
        else:
            print("Error: Numbers must only contain digits.")
            quit()
    return nums1,operators,nums2

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))