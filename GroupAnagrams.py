# -*- coding: utf-8 -*-
# @Time    : 6/12/2018 10:50 AM
# @FileName: GroupAnagrams.py
# Info: 49. Group Anagrams


# string排序，可以先将string转为list，再用list的sort()方法

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 0:
            return []
        result = []
        hashTable = dict()
        for i in range(len(strs)):
            sortedWord = ''.join(sorted(strs[i]))
            if sortedWord in hashTable:
                index = hashTable.get(sortedWord)
                result[index].append(strs[i])
            else:
                result.append([strs[i]])
                hashTable[sortedWord] = len(result)-1
        return  result


    def groupAnagrams_fromLCode(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for str in strs:
            key = "".join(sorted(str))  # "str".join(str)
            if key in dic:
                dic.get(key).append(str)    # Appending to the list value in dict
            else:
                dic[key] = [str]    # List of single item ---> [item]
        return list(dic.values())