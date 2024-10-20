from typing import List, Tuple
import ast

def fns(d: List[List[Tuple[int, int, int]]]) -> List[List[Tuple[int, int, int]]]:
    def ic(exam1: Tuple[int, int, int], exam2: Tuple[int, int, int]) -> bool:
        return max(exam1[1], exam2[1]) < min(exam1[2], exam2[2])

    def back(i: int, cs: List[Tuple[int, int, int]]) -> None:
        if i == len(d):
            vs.append(cs[:])
            return

        for exam in d[i]:
            if all(not ic(exam, scheduled_exam) for scheduled_exam in cs):
                cs.append(exam)
                back(i + 1, cs)
                cs.pop()

    vs = []
    back(0, [])
    return vs


input_str = input().strip()
d = ast.literal_eval(input_str)


result = fns(d)
print(result)
