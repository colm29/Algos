def find_first_non_repeated(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for key in d:
        if d[key] == 1:
            return key

def find_first_repeated(s):
    d = {}
    for c in s:
        if c in d:
            return c
        d[c] = 1

def find_most_repeated(input):
    dct = {}
    tot = 0
    for n in input:
        if n in dct:
            dct[n] += 1
        else:
            dct[n] = 1

    for key in dct:
        if dct[key] > tot:
            tot = dct[key]
            res = key
    
    return res

def count_unique_pairs_with_diff(input, diff):
    dct = {}
    for el in input:
        if el in dct:
            pass
        else:
            if el + diff in input:
                dct[el] = el + diff
    return len(dct)

def two_sum_indices(input, target):
    for el in input:
        if el > target:
            pass
        else:
            newtarget = target - el
            if newtarget in input[input.index(el)+ 1:]:
                return (input.index(el), input.index(newtarget))
    return f'There are no values that add to {target}'

def two_sum_indices_dict(input, target):
    dct = {}
    for i in range(0,len(input)):
        dct[input[i]] = i

    for i in range(0,len(input)):
        complement = target - input[i]
        if complement in dct and dct[complement] != i:
            return (i, dct[complement])

    return f'There are no values that add to {target}'

def two_sum_indices_dict_one_pass(input, target):
    dct = {}
    for i in range(0,len(input)):
        dct[input[i]] = i
        complement = target - input[i]
        if complement in dct and dct[complement] != i:
            return (i, dct[complement])

    return f'There are no values that add to {target}'



print(find_first_non_repeated('a green apple'))
print(find_first_repeated('green apple'))
print(find_most_repeated([1,2,2,3,3,3,4]))
print(count_unique_pairs_with_diff([1, 7, 5, 9, 2, 12, 3],2))
print(two_sum_indices([2,7,11,15], 14))
print(two_sum_indices_dict([2,7,11,15], 18))
print(two_sum_indices_dict_one_pass([2,7,11,15], 26))
