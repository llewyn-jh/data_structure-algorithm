"""The longest palindrom"""
import time

def longest_palindrom_ver1(strs: str) -> str:
    """Dynamic programing"""
    if len(strs) < 2 or strs == strs[::-1]:
        return strs

    palins = []
    for num in range(1, len(strs)):
        for i in range(len(strs) - num):
            if strs[i:i + num + 1][::-1] == strs[i:i + num + 1]:
                palins.append(strs[i:i + num + 1])
                break
    palins.sort(key=len)
    return palins[-1]

def longest_palindrom_ver2(strs: str) -> str:
    """Use two pointer"""
    if len(strs) == 1 or strs == strs[::-1]:
        return strs

    # Expand a slicing and find a palindrome
    def expand(left: int, right: int) -> str:
        while left >=0 and right < len(strs) and strs[left] == strs[right]:
            left -= 1
            right += 1
        return strs[left + 1:right]

    # Two pointers: even and odd slicing windows
    result = ''
    for i in range(len(strs) - 1):
        result = max(result,
                    expand(i, i + 1),
                    expand(i, i + 2),
                    key=len)
    return result

if __name__ == "__main__":

    EX = "txzokgefxajgkrlhllbqmcrtbjpppdzugzketdvlaxametkejdfbcwxijjjywjzoedqduensgouechpbdthevggtdelqyejxvybvmttbkheqfyiartxmmuxbkixgslcmjondweiyuvztqntkmvkxqqlfxgotaexzejnmfrhvkgaxyxdxasxrjevzwfvwvmxqikvsfbhhznjsvrlzkwionopahxhcetbsacwrazeciknyczsrxpbblvskzfaimaoyxfcwcsfxlulcezkbiszclkcfawqefwbhalyqjtvedlwigklrkuzyfamqjgjmytxytrlwhttelgttxlizpypwccfhwhwtzyawxyjqnynfdgrqixbwfahrjvvoowehmhyllnfhnnaswfmjitjbftpyvbfgtywcvhcziempcmxlgfuktengaakiwbovlfdtkropqvntuawouofuebfqojpmbodeaaedobmpjoqfbeufouowautnvqporktdflvobwikaagnetkufglxmcpmeizchvcwytgfbvyptfbjtijmfwsannhfnllyhmhewoovvjrhafwbxiqrgdfnynqjyxwayztwhwhfccwpypzilxttgletthwlrtyxtymjgjqmafyzukrlkgiwldevtjqylahbwfeqwafcklczsibkzeclulxfscwcfxyoamiafzksvlbbpxrszcynkicezarwcasbtechxhaponoiwkzlrvsjnzhhbfsvkiqxmvwvfwzvejrxsaxdxyxagkvhrfmnjezxeatogxflqqxkvmktnqtzvuyiewdnojmclsgxikbxummxtraiyfqehkbttmvbyvxjeyqledtggvehtdbphceuogsneudqdeozjwyjjjixwcbfdjektemaxalvdtekzguzdpppjbtrcmqbllhlrkgjaxfegkozxt"
    start = time.time()
    longest_palindrom_ver1(EX)
    print(f"Dynamic programing: {time.time() - start:0.9f}")

    start = time.time()
    longest_palindrom_ver2(EX)
    print(f"Two pointer: {time.time() - start:0.9f}")
