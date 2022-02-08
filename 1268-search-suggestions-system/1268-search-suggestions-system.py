# class Trie:
#     class Node:
#         isWord = False
#         children = [Node()] * 26
#     Root = Node()
#     curr = 0
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        list_ = []
        products.sort()
        for i, c in enumerate(searchWord):
            products = list(filter(lambda p: p[i] == c if len(p) > i else False, products))
            list_.append(products[:3])
        return list_
#         products.sort() # sorts values lexicographically
        
#         searchOrd = 0
#         answers = []
#         for index in range(len(searchWord)):
#             searchOrd += ord(searchWord[index])
#             # product_hashmap = {}
#             selected_products = []
#             for product in products:
#                 if abs(sum([ord(productChar) for productChar in product[:index+1]]) - searchOrd) == 0:
#                     if len(selected_products) < 3:
#                         selected_products.append(product)
#                     else:
#                         break
#             answers.append(selected_products)
            
        return answers