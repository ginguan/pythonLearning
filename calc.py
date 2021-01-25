import sys

#(FUNCTION EXPR EXPR)

class EXPR:
    # Pre-Calculated expressions for dynamic programming optimization
    pre_calculated = {}

    def calc(self, str_input):
        while ')' in str_input:
            # First check if already been calculated
            if str_input in self.pre_calculated:
                return self.pre_calculated[str_input]

            # Start with the first expression to close (ie. first index of ')')
            right = str_input.index(')')
            left = str_input[:right].rindex('(')

            # Note: Because we're getting the first expression to close,
            #       it is guaranteed not to have nested functions inside
            value = self._evaluate_single(str_input[left + 1:right])

            # If evaluated final function
            if left == 0:
                return value

            # Else update str_input, replacing expression with calculated value
            else:
                str_input = str_input[:left] + str(value) + str_input[right+1:]

        return int(str_input)

    # Evaluates simple expression with no nested values
    def _evaluate_single(self, str_input):
        # Check if already been calculated
        if str_input in self.pre_calculated:
            return self.pre_calculated[str_input]

        pieces = str_input.split()

        if pieces[0] == 'add':
            answer = int(pieces[1]) + int(pieces[2])

        elif pieces[0] == 'multiply':
            answer = int(pieces[1]) * int(pieces[2])

        else:
            answer = int(str_input)

        # Add to pre calculated dict
        self.pre_calculated[str_input] = answer
        return answer


def main():
    print(EXPR().calc(sys.argv[1]))


main()