with open('testing.log') as f:
    print(1 if 'Fail' in f.read() else 0)