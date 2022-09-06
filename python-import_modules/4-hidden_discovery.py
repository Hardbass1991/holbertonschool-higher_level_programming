#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    names = [x for x in dir(hidden_4) if x[:2] != "__"]
    for name in names:
        print(name)
