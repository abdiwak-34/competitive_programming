class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        count = 0
        while i < len(command):
            if command[i] == "G":
                ans += "G"
                i += 1
            elif command[i] == "(":
                count += 1
                i += 1
            elif command[i] == ")":
                if count == 1:
                    ans += "o"
                else:
                    ans += "al"
                i += 1
                count = 0
            else:
                i += 1
                count += 1
        return ans