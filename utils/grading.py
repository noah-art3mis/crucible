from utils.my_types import Variable


def grade_response(response: str, variable: Variable, grading_type: str) -> int:
    if grading_type == "binary":
        for expected in variable.expected:
            if expected in response:
                return 1
            return 0

    if grading_type == "qualitative":
        raise NotImplementedError

    if grading_type == "out_of_ten":
        grade = 0  # out of 10

        expected = variable.expected
        possible_responses = variable.options

        for expected in variable.expected:
            if expected in response:
                grade = 10

        # penalize if it cites other possible responses
        if possible_responses:
            other_responses = set(possible_responses) - {x for x in expected}
            for other in other_responses:
                if other in response:
                    grade -= 5

        return int(max(grade, 0))
