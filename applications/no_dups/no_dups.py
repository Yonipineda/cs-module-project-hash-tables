def no_dups(s):
    # Your code here
    output = ''
    cache = []
    for word in s.split():
        if word in cache:
            pass
        else:
            output += word + ' '
            cache.append(word)

    return output.strip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))