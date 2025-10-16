class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for c in s : 
            if c == " " :
                if len(word):
                    words.append(word)
                    word = ""
                continue
            word += c 
        if word != "":
            words.append(word)
        
        return " ".join(words[::-1])