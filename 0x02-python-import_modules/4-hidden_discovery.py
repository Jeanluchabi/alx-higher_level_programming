#!/usr/bin/python3
if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    n = dir(hidden_4)
    for x in n:
        if x[:2] != "__":
            print(x)
