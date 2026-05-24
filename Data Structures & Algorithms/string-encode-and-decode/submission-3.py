class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for s in strs: 
            l = len(s)
            encoded_string += str(l) + "#" + s
        
        return encoded_string


    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_list = []

        while i < len(s):
            num = ""
            j = i

            while s[j] != "#":
                num += s[j]
                j += 1

            num = int(num)

            sub = ""
            k = 0
            while k < num:
                sub += s[j + 1 + k]
                k += 1

            decoded_list.append(sub)

            i = j + 1 + num

        return decoded_list