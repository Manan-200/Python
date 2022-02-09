array = [1, "+", 2, "-", 3, "*", 4, "/", 5]

class ReverseArray:
    def __init__(self, array):
        self.array = array
        self.reveresed_array = []
    def reverse(self):
        for i in range(len(self.array)):
            num = (i + 1) * -1
            self.reveresed_array.append(self.array[num])
        print(self.array)
        print(self.reveresed_array)
    
array = ReverseArray(array)
array.reverse()