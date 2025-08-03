class Solution:
    def interpret(self, command: str) -> str:
        out  = []
        index_used = 0
        for i in command:

            if i == "G":
                out.append(i)

            elif i == "(":

                index_of_bracket = command.index(i,index_used)
                index_used = index_of_bracket +1
                inside = index_of_bracket +1

                if command[inside] == "a":
                    out.append("al")
                else:
                    out.append("o")
        return "".join(out)
