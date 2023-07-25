from collections import defaultdict

class Solution:
    def findRestaurant(self, list1, list2):
            res = defaultdict(list)
            for i in range(len(list1)):
                for j in range(len(list2)):
                    if list1[i] == list2[j]:
                        res[(i+j)].append(list1[i])
            return res[min(res.keys())]


list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(Solution().findRestaurant(list1, list2))

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Shogun","Burger King"]
print(Solution().findRestaurant(list1, list2))

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]
print(Solution().findRestaurant(list1, list2))
