
def head(num):
    print(f"HEAD {num}\n")
    if(num == 1):
        return
    
    return head(num - 1)


head(10)