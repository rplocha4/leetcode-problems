def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    res = {}
    for str in strs:
        letters = [0] * 26
        for l in str:
            letters[ord(l) - ord("a")] += 1
        if res.get(tuple(letters)) is not None:

            res[tuple(letters)].append(str)
        else:
            res[tuple(letters)] = [str]

    return res.values()
