def main():
    numbers = []
    prenum = None
    
    while True:

        nownum = int(input("Enter a number here:"))
        
        if prenum != None and nownum <= prenum:
            numbers.append(nownum)
            
        else:
            if prenum != None:
                break
        
    prenum = nownum

    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
