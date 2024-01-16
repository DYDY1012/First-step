# def under_3(x):
#    return x < 3

def main():
    li = [x for x in range(1,11)]
    print(list(filter(lambda x: x < 3, li)))



if __name__ == "__main__":
    main()