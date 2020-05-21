

def main():
    print("coding-test")

    with open("input.txt") as f:
        lines = f.read()
        lines = lines.split('\n')

    m = int(lines[-2])
    del lines[-2:]
    lines2 = []

    for l in lines:
        line = l.split(":")
        lines2.append(line)

    for n in range(0, len(lines2)-1):
        ni = int(lines2[n][0])
        if m % ni == 0:
            print(lines2[n][1])
    
    print(m)


main()