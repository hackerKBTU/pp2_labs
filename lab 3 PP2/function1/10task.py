def uni_list():
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            unums.append(nums[i])
    print(unums)

x = int(input("Enter the number of elements: "))
nums = []
unums = []

for i in range(x):
    nums.append(int(input(f"Enter element {i+1}: ")))

uni_list()
