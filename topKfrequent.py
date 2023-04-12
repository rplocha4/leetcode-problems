def topKFrequent(nums, k):
    count = {}

    for num in nums:
        if count.get(num) is not None:
            count[num] += 1
        else:
            count[num] = 1

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in sorted_count[:k]]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
