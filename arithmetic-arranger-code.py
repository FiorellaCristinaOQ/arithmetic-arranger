def arithmetic_arranger(problems,rpta=False):
    operators = []
    nums1 = []
    nums2 = []
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

print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49','888 + 40', '653 + 87']))