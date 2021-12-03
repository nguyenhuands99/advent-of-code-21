with open('input.txt', 'r') as file:
    nums = list(map(int, file.read().splitlines()))
    ## part 1
    # print(sum([1 if nums[i] > nums[i-1] else 0 for i in range(1, len(nums))]))

    ## part 2    
    context_nums = [(nums[i] + nums[i+1] + nums[i+2]) for i in range(len(nums) - 2)]
    print(sum([1 if context_nums[i] > context_nums[i-1] else 0 for i in range(1,len(context_nums))])


