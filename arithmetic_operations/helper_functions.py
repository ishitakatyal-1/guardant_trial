
EMPTY_VALS_CHECK = ['', ' ', "", " ", None, [], {}]


class HelperClass:

    def __init__(self):
        self.allowedOperations = ['+', '-']
        self.allowedDigits = [str(i) for i in range(10)]

    def __call__(self, input_str: str) -> dict:

        if input_str in EMPTY_VALS_CHECK:
            return {
                'success': False,
                'message': 'Enter a valid arithmetical expression'
            }

        valid_response = self.valid_check(input_str)
        if not valid_response['success']:
            return valid_response

        computed_val_response = self.compute_result(input_str)
        return {
            'success': True,
            'value': computed_val_response
        }

    @classmethod
    def compute_result(self, str_input) -> int:
        """
        input: str_input: str
        description: compute expression for valid input
        output: result: int
        """

        # separating arithmetical expressions in input string - O(n)
        operators_list = [i for i in str_input if i in self.allowedOperations]

        # separating numbers in input string - O(n)
        nums_list = [int(i) for i in str_input.replace(
            '+', ' ').replace('-', ' ').split()]

        nums_len = len(nums_list)
        result = nums_list[0]
        for i in range(nums_len-1):
            if operators_list[i] in self.allowedOperations:
                # actual computation
                match operators_list[i]:
                    case '+':
                        result += nums_list[i+1]
                    case '-':
                        result -= nums_list[i+1]

        return result

    @classmethod
    def valid_check(self, input_str) -> dict:
        """
        input: str_input: str
        description: check for valid string
        output: {'success': True/False, 'message': ''} 
        """

        # check for valid characters
        valid_chars_msg = self.check_for_valid_chars(input_str)
        if not valid_chars_msg['success']:
            return valid_chars_msg

        # check for first and last element
        positional_msg = self.check_positional_elements(input_str)
        if not positional_msg['success']:
            return {
                'success': False,
                'message': positional_msg['message']
            }

        # check for simultaneous arithmetic signs of +/-, +/+, -/-, -/+
        occurrence_msg = self.check_simultaneous_occurrences(input_str)
        if not occurrence_msg['success']:
            return {
                'success': False,
                'message': occurrence_msg['message']
            }

        return {
            'success': True,
            'message': 'Valid input string.'
        }

    @classmethod
    def check_for_valid_chars(self, val_input) -> dict:
        """
        input: val_input: str
        description: check for valid chars - [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, +, - ]
        output: {'success': True/False, 'message': ''} 
        """

        for i in val_input:
            if str(i) not in self.allowedOperations and str(i) not in self.allowedDigits:
                return {
                    'success': False,
                    'message': 'Invalid characters sent. Only +/- and digits 0-9 are allowed.'
                }

        return {
            'success': True,
            'message': 'All characters are valid.'
        }

    @classmethod
    def check_simultaneous_occurrences(self, val_input) -> dict:
        """
        input: val_input: str
        description: check simultaneous occurrences - [++, --, +-, -+]
        output: {'success': True/False, 'message': ''} 
        """

        val_len = len(val_input)

        for i in range(val_len-1):
            if val_input[i] in self.allowedOperations and (val_input[i] == val_input[i+1] or val_input[i+1] in self.allowedOperations and val_input[i] != val_input[i+1]):
                return {
                    'success': False,
                    'message': 'Arithmetical operations: ' + val_input + ' cannot occur simultaneously.'
                }

        return {
            'success': True,
            'message': 'Simultaneous occurrence for operation +/- check passed.'
        }

    @classmethod
    def check_positional_elements(self, input_str) -> dict:
        """
        input: input_str: str
        description: check first and last element which cannot be a mathematical expression [+, -]
        output: {'success': True/False, 'message': ''} 
        """

        first_ele = input_str[0]
        last_ele = input_str[-1]
        if first_ele in self.allowedOperations:
            return {
                'success': False,
                'message': 'Operation of ' + first_ele + ' cannot be in first place.'
            }

        if last_ele in self.allowedOperations:
            return {
                'success': False,
                'message': 'Operation of ' + last_ele + ' cannot be in last place.'
            }

        return {
            'success': True,
            'message': 'Positional elements are all ok.'
        }


if __name__ == "__main__":

    cls_auxillary_util = HelperClass()
    cls_result = cls_auxillary_util.compute_result('123+45-6')

    print('result', cls_result)
