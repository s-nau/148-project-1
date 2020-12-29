"""CSC148 Assignment 1

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

=== Module Description ===

This file contains classes that describe a university course and the students
who are enrolled in these courses.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, List, Tuple, Optional, Dict
if TYPE_CHECKING:
    from survey import Answer, Survey, Question


# done
def sort_students(lst: List[Student], attribute: str) -> List[Student]:
    """
    Return a shallow copy of <lst> sorted by <attribute>

    === Precondition ===
    <attribute> is a attribute name for the Student class

    >>> s1 = Student(1, 'Misha')
    >>> s2 = Student(2, 'Diane')
    >>> s3 = Student(3, 'Mario')
    >>> sort_students([s1, s3, s2], 'id') == [s1, s2, s3]
    True
    >>> sort_students([s1, s2, s3], 'name') == [s2, s3, s1]
    True
    """
    return sorted(lst, key=lambda s: getattr(s, attribute))


class Student:
    """
    A Student who can be enrolled in a university course.

    === Public Attributes ===
    id: the id of the student
    name: the name of the student

    === Private Attributes ===
    _questions_answered: dictionary of question id to it's answer

    === Representation Invariants ===
    name is not the empty string
    """

    id: int
    name: str
    _questions_answered: Dict[int: Answer]
    # id of question to answer for question

    def __init__(self, id_: int, name: str) -> None:  # done
        """ Initialize a student with name <name> and id <id>"""
        self.id = id_
        self.name = name
        self._questions_answered = {}

    def __str__(self) -> str:  # done
        """ Return the name of this student """
        return self.name

    def has_answer(self, question: Question) -> bool:  # done
        """
        Return True iff this student has an answer for a question with the same
        id as <question> and that answer is a valid answer for <question>.
        """
        q_id = question.id
        if q_id not in self._questions_answered:
            return False
        if len(self._questions_answered) == 0:
            return False
        if self._questions_answered[q_id] == []:
            return False
        if q_id in self._questions_answered:
            # checking if the student has an answer for the question
            ans = self._questions_answered[q_id]
            # answer to question with id: q_id
            # if isinstance(ans, bool) or isinstance(ans, str) or isinstance(
            #         ans, int):
            #     # if not a list
            #     if not ans.is_valid(question):
            #         return False
            # else:
            #     for opt in ans.content:  # if a list
            if not ans.is_valid(question):
                return False
                # checking if the answer is a valid answer to question
        return True
    # will return False if it hasn't returned true

    def set_answer(self, question: Question, answer: Answer) -> None:  # done
        """
        Record this student's answer <answer> to the question <question>.
        """
        self._questions_answered[question.id] = answer
        # saving the answer to the _question_answered dict

    def get_answer(self, question: Question) -> Optional[Answer]:  # done
        """
        Return this student's answer to the question <question>. Return None if
        this student does not have an answer to <question>
        """
        if self.has_answer(question):
            return self._questions_answered[question.id]
        else:
            return None


class Course:
    """
    A University Course

    === Public Attributes ===
    name: the name of the course
    students: a list of students enrolled in the course

    === Representation Invariants ===
    - No two students in this course have the same id
    - name is not the empty string
    """

    name: str
    students: List[Student]

    def __init__(self, name: str) -> None:  # done
        """
        Initialize a course with the name of <name>.
        """
        self.name = name
        self.students = []

    def enroll_students(self, students: List[Student]) -> None:  # done
        """
        Enroll all students in <students> in this course.

        If adding any student would violate a representation invariant,
        do not add any of the students in <students> to the course.
        """
        id_to_stud = {}
        for stud in students:
            id_to_stud[stud.id] = stud
        counter = 0
        for stud in students:
            if stud.name != "":
                # checking that none of the students violate the rep invariant
                counter += 1

        if counter == len(students) and len(id_to_stud) == len(students):
            # checking that none of them violates
            # because if there are multiple students with the same id it will
            # replace them in dict and therefore there will not be as many
            # in the dict
            for stud in students:
                self.students.append(stud)

    def all_answered(self, survey: Survey) -> bool:  # done
        """
        Return True iff all the students enrolled in this course have a valid
        answer for every question in <survey>.
        """
        for stud in self.get_students():
            for q in survey.get_questions():
                if not stud.has_answer(q):
                    # if one stud does not have an answer will return false
                    return False
        return True

    def get_students(self) -> Tuple[Student, ...]:  # done
        """
        Return a tuple of all students enrolled in this course.

        The students in this tuple should be in order according to their id
        from lowest id to highest id.

        Hint: the sort_students function might be useful
        """
        students = sort_students(self.students, "id")
        # sort students returns the sorted, doesn't sort it in place
        tup = tuple()
        for stud in students:
            tup = tup + (stud,)
        return tup

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing', 'survey']})
