with open('/tmp/test.txt', 'w') as f:
    for i in range(10):
        f.write(f"{i} is the index of the line\n")

print("I am the new line")