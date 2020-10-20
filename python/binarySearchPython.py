def binary_search(numbers,number_to_find,low,high):
    
    if low > high:
        return False
    
    mid = (low + high) / 2
    mid = int(mid)

    if numbers[mid] == number_to_find:
        return True
    
    elif numbers[mid] > number_to_find:
        return binary_search(numbers,number_to_find, low, mid -1)
    else:
        return binary_search(numbers,number_to_find,mid + 1, high)

    


if __name__ == '__main__':  
    numbers = [1,3,5,6,9,10,11,25,27,28,34,36,49,51]
    
    numbers = list(map(int, numbers))
    
    number_to_find  = int(input('Type a number my valedor: '))

    result = binary_search(numbers,number_to_find,0,len(numbers)-1)

    if result is True:
        print('The number mason, is on the list')

    else:
        print('Im sorry, lo siento my valedor, that number is NOT on the list')