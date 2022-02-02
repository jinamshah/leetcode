class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        valueDefinition = {
            3: "Fizz",
            5: "Buzz"
        }
        answer = []
        for i in range(1,n+1):
            currentString = ""
            for k,v in valueDefinition.items():
                if i % k == 0:
                    currentString+=v
            if currentString == "":
                currentString = str(i)
            answer.append(currentString)
        return answer
        # answer = []
        # for i in range(1,n+1):
        #     if i % 3 == 0 and i % 5 == 0:
        #         answer.append("FizzBuzz")
        #     elif i % 3 == 0:
        #         answer.append("Fizz")
        #     elif i % 5 == 0:
        #         answer.append("Buzz")
        #     else:
        #         answer.append(str(i))
        # return answer