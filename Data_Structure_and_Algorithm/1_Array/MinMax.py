class pair:
    def __init__(self):
        self.max=0
        self.min=0
        
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()
    
    if n == 0:
        return minmax
    
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.min = arr[0]
        minmax.max = arr[1]
    
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
            
    return minmax

if __name__ == "__main__":
    arr = [3, 5, 4, 1, 2, 9]
    arr_size = 1
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)