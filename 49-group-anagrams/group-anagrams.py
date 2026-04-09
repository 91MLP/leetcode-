class Solution(object):
    def groupAnagrams(self, strs):
        hash_map={}
        for str in strs:
            key = ""+join(sorted(str))
            if key not in hash_map:
                hash_map[key] = []
            hash_map[key].append(str)
        return list(hash_map.values())
        