def main():
    total = 0
    tempfile = open('numbers.txt', 'r')
    num_line = tempfile.readline()
    while num_line != '':
        num_line = int(num_line.rstrip('\n'))
        total += num_line
        num_line = tempfile.readline()
    print(f'sum of all the numbers is {total}')

main()
