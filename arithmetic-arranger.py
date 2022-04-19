def arithmetic_arranger(problems,rpta=False):
    operators = []
    nums1 = []
    nums2 = []
    if len(problems)>5:
        return 'Error: Too many problems.'
    for i in problems:
        lst = i.split()
        if len(lst[0]) > 4 or len(lst[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        if lst[0].isdigit():
            nums1.append(lst[0])
        else:
            return "Error: Numbers must only contain digits."
        if lst[1] == '+' or lst[1] == '-':
            operators.append(lst[1])
        else:
            return "Error: Operator must be '+' or '-'."
        if lst[2].isdigit():
            nums2.append(lst[2])
        else:
            return "Error: Numbers must only contain digits."
    
    rptas = [] # Lista de longitud 0
    
    if rpta == True: # Return problems and their answers
        for i in range(len(operators)):
            if operators[i] == '+':
                rptas.append(str(int(nums1[i]) + int(nums2[i])))
            else:
                rptas.append(str(int(nums1[i]) - int(nums2[i])))
    
    arranged1 = ''
    arranged2 = ''
    arranged3 = ''
    arranged4 = ''
    
    for i in range(len(nums1)):
        spaces = len(nums1[i])
        if spaces < len(nums2[i]):
            spaces = len(nums2[i])
        arranged1 = arranged1 + (spaces + 2 - len(nums1[i]))*' ' + nums1[i] + 4*' '
        arranged2 = arranged2 + operators[i] + ' ' + (spaces - len(nums2[i]))*' ' + nums2[i] + 4*' '
        arranged3 = arranged3 + (spaces + 2)*'-' + 4*' '
        if rpta == True:
            arranged4 = arranged4 + (spaces + 2 - len(rptas[i]))*' ' + rptas[i] + 4*' '
    
    arranged = arranged1 + '\n' + arranged2 + '\n' + arranged3
    if rpta == True:
        arranged = arranged + '\n' + arranged4
    
    return arranged

print('Test two problems arrangement')
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print('Test four problems arrangement')
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print('Test five problems arrangement')
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print('Test too many problems')
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']))
print('Test incorrect operator')
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print('Test too many digits')
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print('Test only digits')
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print('Test two problems with solutions')
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print('Test five problems with solutions')
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
