def flatten_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)
        
flatten_sort([1,2,3,4,5])


# How does this solution ensure data immutability?
#  Yes , to ensure data immutabilty fictuin should create a new list or in immatuabler data types like string,tuples,or integers

# Is this solution a pure function?
# Yes, function does not modify the args in anyway just sorts.
# Is this solution a higher order function? Why or why not?
# NO, function only takes one argument. Bulit-in sorted function dont make it a high order function..

# Would it have been easier to solve this problem using a different programming style?
# NO, built in sorted function helps.

# Why in particular is functional programming a helpful paradigm when solving this problem?
# foucs is on what to solve in contrast to how to solve it.