with open('copy.txt', 'w') as f:
    with open('sample.txt', 'r') as g:
        for line in g:
            f.write(line)