def add_binary(a: str, b: str) -> str:
    result = []
    aptr, bptr = len(a)-1, len(b)-1
    carry = 0

    while aptr >= 0 or bptr >= 0 or carry:
        sum = carry
        if aptr >= 0:
            sum += int(a[aptr])
            aptr -= 1
        if bptr >= 0:
            sum += int(b[bptr])
            bptr -= 1
        
        carry = sum // 2
        result.append(str(sum%2))

    return ''.join(reversed(result))


def main():
    a, b = "1011", "11"
    print(add_binary(a,b))

if __name__ == "__main__":
    main()