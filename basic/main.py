def main():
    for i in range(10):
        print('i, {0}'.format(i))
        for j in range(5):
            print('j, {0}'.format(j))
            if j==3:
                break


if __name__ == "__main__":
    main()