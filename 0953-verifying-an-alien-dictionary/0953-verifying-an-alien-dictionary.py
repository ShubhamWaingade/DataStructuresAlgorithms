class Solution:
    def isAlienSorted(self, words: List, order: str) -> bool:
     
        order_dict = {}


        for index in range(len(order)):
            order_dict[order[index]] = order_dict.get(order[index], index+1)

        for ind in range(0, len(words)-1):
            current_sorted = True
            for inner_ind in range(len(words[ind])):
                if inner_ind >= len(words[ind+1]):
                    return False
                if order_dict[words[ind+1][inner_ind]] > order_dict[words[ind][inner_ind]]:
                    current_sorted = True
                    break
                elif order_dict[words[ind+1][inner_ind]] < order_dict[words[ind][inner_ind]]:
                    return False
                
        return True