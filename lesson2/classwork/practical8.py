#practical 8
def practical8(arr):
    num = 0
    for x in arr:
        if num < x < max(arr):
            num = x
        else :
            num = 0.5
    return num
if __name__ == "__main__":
    print(practical8([5, 5, 5]))


#Done