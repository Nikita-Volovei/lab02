i = 1
with open('sample.txt', 'r') as f:
    for line in f:
        print(i,": ",line.strip())
        i+=1
        