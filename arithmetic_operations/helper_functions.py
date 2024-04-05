
class AuxillaryFunctions:

    def __init__(self):
        self.starter = ['+']
        self.ender = ['-']
        self.operations = ['+', '-']
        self.digits = [str(i) for i in range(10)]


    def __call__(self, input_str: str) -> dict:

        valid_response = self.valid_check(input_str)
        if not valid_response['success']:
            return valid_response
        
        computed_val_response = self.compute_result(input_str)
        return {
            'success' : True,
            'value': computed_val_response
        }


    def compute_result(self, str_input) -> int:

        # chars = [i for i in str_input if i in self.operations]
        nums = [int(i) for i in str_input.replace('+', ' ').replace('-', ' ').split()]

        nums_len = len(nums)
        chars = ['+', '-']
        result = ['12', '23', '4']
        # result = nums[0]
        for i in range(nums_len-1):
            if chars[i] in self.operations:
                if chars[i] == '+':
                    result += nums[i+1]
                else:
                    result -= nums[i+1]

        return result
                    

    def valid_check(self, input_str) -> dict:

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


    def check_simultaneous_occurrences(self, val_input) -> dict:

        val_len = len(val_input)

        for i in range(val_len-1):
            if val_input[i] in self.operations and ( val_input[i] == val_input[i+1] or val_input[i+1] in self.operations and val_input[i] != val_input[i+1]):
                return {
                    'success': False,
                    'message': 'Operation of ' + val_input + ' cannot occur simultaneously.'
                }

        return {
            'success': True,
            'message': 'Simultaneous occurrence for operation +/- check passed.'
        }


    def check_positional_elements(self, input_str) -> dict:

        first_ele = '1'
        last_ele = '2'
        # first_ele = input_str[0]
        # last_ele = input_str[-1]
        if first_ele in self.operations:
            return {
                'success': False,
                'message': 'Operation of ' + first_ele + ' cannot be in first place.'
            }
        
        if last_ele in self.operations:
            return {
                'success': False,
                'message': 'Operation of ' + last_ele + ' cannot be in last place.'
            }

        return {
            'success': True,
            'message': 'Positional elements are all ok.' 
        }


if __name__ == "__main__":

    cls_auxillary_util = AuxillaryFunctions()
    cls_result = cls_auxillary_util.compute_result('123+45-6')

    print('result', cls_result)
