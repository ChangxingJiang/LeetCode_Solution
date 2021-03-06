from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        codes = set()
        for word in words:
            code = ""
            for c in word.lower():
                code += morse[ord(c) - 97]
            codes.add(code)

        return len(codes)


if __name__ == "__main__":
    print(Solution().uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"]))  # 2
