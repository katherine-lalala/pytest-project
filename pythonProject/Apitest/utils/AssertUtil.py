import jsonpath


class AssertUtil:

    def contains(self, actual_value, expect_value):
        assert expect_value in actual_value, f'{expect_value} in {actual_value}'

    def extract_by_json(self, extract_value: dict, extract_expression: str):
        """
        根据jsonpath获取值
        :param extract_value: res.json()
        :param extract_expression: $.token
        :return:
        """
        extract_value = jsonpath.jsonpath(extract_value, extract_expression)

        if not extract_value:
            return
        elif len(extract_value) == 1:
            return extract_value[0]
        else:
            return extract_value

    def validate_response(self, response, validate_check):
        """校验注释"""
        for check_type, check_value in validate_check.items():
            #实际结果
            actual_value = self.extract_by_json(response, check_value[0])
            ##预期结果
            expect_value = check_value[1]
            if check_type in ['contains', 'con']:
                self.contains(actual_value, expect_value)
