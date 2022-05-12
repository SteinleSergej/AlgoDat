def tail(num):
    if (num == 0):
        return
    else:
        tail(num - 1)
        print(f"TAIL {num}")


tail(10)