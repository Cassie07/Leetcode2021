class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        res = []
        this = ''
        for char in searchWord:
            this += char
            tmp = []
            count = 1
            for word in products:
                if word.startswith(this) and count <= 3:
                    tmp.append(word)
                    count += 1
            res.append(tmp)
        return res
