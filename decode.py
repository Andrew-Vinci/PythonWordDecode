def decode_message(message_file):
    mapWords = {}
    file = open(message_file, "r")
    for line in file:
        split_line = line.split()
        key = int(split_line[0])
        value = split_line[1]
        mapWords[key] = value
        split_line = ""
        

    file.close()
    keys = list(sorted(mapWords, key=int))
    index = 0
    numKeys = 1
    while index < len(mapWords):
        for i in range(numKeys):
            if index + i < len(mapWords):
                print(keys[index + i], end='')
            else:
                break

        print()
        index += numKeys
        numKeys += 1

    start = 1
    previous = 0
    while start < 40:
        print(mapWords[start])
        new_start = start + previous
        previous = start
        start = new_start


decode_message("words.txt")