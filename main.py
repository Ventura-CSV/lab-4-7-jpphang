def main():
    numbers = []
    pre_val = None
    
    while True:
        
        cur_val = int(input("Enter a number here:"))
        
        if pre_val is not None and cur_val <= pre_val:
            numbers.append(cur_val)
            
        else:
            if pre_val is not None:
                break
        pre_val = cur_val

    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
