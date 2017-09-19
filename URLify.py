
def main():
    a, length= "Mr John Smith     ", int(13)
    new_a = []
    for each in a[:length]:
        if each == ' ':
            new_a.append('%20')
        else:
            new_a.append(each)
    print (''.join(new_a))

if __name__ == '__main__':
    main()