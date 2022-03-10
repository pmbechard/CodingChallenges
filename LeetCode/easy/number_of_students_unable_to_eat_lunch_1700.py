"""
1700. Number of Students Unable to Eat Lunch
https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
"""


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while True:
            if len(set(students)) == 1 and students[0] != sandwiches[0]:
                return len(students)

            current_student = students.pop(0)
            if current_student == sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(current_student)

            if not students:
                return 0
