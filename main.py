def main():
    numbers = []
    pre_val = None
    
    while True:
        cur_val = int(input("Enter a number here: "))
        
        if pre_val is None or cur_val <= pre_val:
            numbers.append(cur_val)
        else:
            break

        pre_val = cur_val

    print("Collected numbers:", *numbers)
    return numbers

if __name__ == '__main__':
    main()
