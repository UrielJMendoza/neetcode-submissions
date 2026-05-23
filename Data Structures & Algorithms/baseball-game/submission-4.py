class Solution:
    def calPoints(self, operations: List[str]) -> int:

        # c removes prevous element so pop

        # d 
        scores = [] 
        sums = 0



        for i in range(len(operations)):


            if operations[i].lstrip('-').isdigit():
                scores.append(operations[i])


            elif operations[i] == "+":
                scores.append(int(scores[len(scores)-1])+ int(scores[len(scores)-2]))


            elif operations[i] == "C":
                scores.pop()


            elif operations[i] == "D":
                scores.append(int(scores[len(scores)-1]) * 2)

        for i in range(len(scores)):
            sums += int(scores[i])
        return sums