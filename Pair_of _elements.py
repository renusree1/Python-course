class pair_elements:
    def twosums(self, nums, target):
        lookup= {}
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num]= i
value= int(input("Enter number to search its sum pair: "))
print("index1=%d, index2=%d"%pair_elements().twosums([10, 20, 10, 40, 50, 60, 70], value))