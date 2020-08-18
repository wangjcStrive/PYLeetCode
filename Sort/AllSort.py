class AllSort:
    def bubble(self, input:str) -> str:
        if len(input) == 0:
            return
        for i in range(len(input)):
            for j in range(len(input)-i-1):
                if input[j] > input[j+1]:
                    tempVal = input[j]
                    input[j] = input[j+1]
                    input[j+1] = tempVal
        return

    def selectionSort(self, input: str) -> str:
        if len(input) == 0:
            return
        minVal = input[0]
        for i in range(len(input)):
            minIndex = i
            minVal = input[i]
            for j in range(i, len(input)):
                if input[j] < minVal:
                    minVal = input[j]
                    minIndex = j
            tempVal = minVal
            input[minIndex] = input[i]
            input[i] = tempVal
        return

    def insertSort(self, input:str) -> str:
        # for i in range(len(input)):
        pass

                    

if __name__ == '__main__':
    ins = AllSort()
    input = [5, 3, 7, 2, 8, 1, 1, 9]
    #ins.bubble(input)
    ins.selectionSort(input)
    print(input)