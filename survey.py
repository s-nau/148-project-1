"""CSC148 Assignment 1

=== CSC148 Winter 2020 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Misha Schwartz, Mario Badr, Christine Murad, Diane Horton, Sophia Huynh
and Jaisie Sin

All of the files in this directory and all subdirectories are:
Copyright (c) 2020 Misha Schwartz, Mario Badr, Christine Murad, Diane Horton,
Sophia Huynh and Jaisie Sin

=== Module Description ===

This file contains classes that describe a survey as well as classes that
described different types of questions that can be asked in a given survey.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, Union, Dict, List
from criterion import HomogeneousCriterion, InvalidAnswerError
if TYPE_CHECKING:
    from criterion import Criterion
    from grouper import Grouping
    from course import Student


class Question:
    """ An abstract class representing a question used in a survey

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str

    # student id to answer

    def __init__(self, id_: int, text: str) -> None:  # done
        """ Initialize a question with the text <text> """
        self.text = text

        self.id = id_

    def __str__(self) -> str:
        """
        Return a string representation of this question that contains both
        the text of this question and a description of all possible answers
        to this question.

        You can choose the precise format of this string.
        """
        raise NotImplementedError

    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer> is a valid answer to this question.
        """
        raise NotImplementedError

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """ Return a float between 0.0 and 1.0 indicating how similar two
        answers are.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        raise NotImplementedError


class MultipleChoiceQuestion(Question):
    """ A question whose answers can be one of several options

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    ===Private Attributes===
    _answer_options: list of all the answer options

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    _answer_options: List[str]

    def __init__(self, id_: int, text: str, options: List[str]) -> None:
        """
        Initialize a question with the text <text> and id <id> and
        possible answers <options>.

        === Precondition ===
        No two elements in <options> are the same string
        <options> contains at least two elements
        """
        Question.__init__(self, id_, text)
        self._answer_options = options
        # possible answers to question

    def __str__(self) -> str:  # done
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        return self.text + " Multiple Choice Question"

    def validate_answer(self, answer: Answer) -> bool:  # done
        """
        Return True iff <answer> is a valid answer to this question.

        An answer is valid if its content is one of the possible answers to this
        question.
        """
        return answer.content in self._answer_options

    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:  # done
        """
        Return 1.0 iff <answer1>.content and <answer2>.content are equal and
        0.0 otherwise.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question.
        """
        if answer1.content == answer2.content:
            return 1.0
        else:
            return 0.0


class NumericQuestion(Question):
    """ A question whose answer can be an integer between some
    minimum and maximum value (inclusive).

    ===Private Attributes===
    _answer_options: list of all the answer options

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    _answer_options: List[int]

    # done
    def __init__(self, id_: int, text: str, min_: int, max_: int) -> None:
        """
        Initialize a question with id <id_> and text <text> whose possible
        answers can be any integer between <min_> and <max_> (inclusive)

        === Precondition ===
        min_ < max_
        """
        Question.__init__(self, id_, text)
        self._answer_options = list(range(min_, max_ + 1))
        # + 1 b/c range is exclusive on upper bound

    # done
    def __str__(self) -> str:
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        return str(self.text) + " NumericQuestion"

# done
    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff the content of <answer> is an integer between the
        minimum and maximum (inclusive) possible answers to this question.
        """
        return answer.content in self._answer_options

    # done
    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return the similarity between <answer1> and <answer2> over the range
        of possible answers to this question.

        Similarity calculated by:

        1. first find the absolute difference between <answer1>.content and
           <answer2>.content.
        2. divide the value from step 1 by the difference between the maximimum
           and minimum possible answers.
        3. subtract the value from step 2 from 1.0

        Hint: this is the same calculation from the worksheet in lecture!

        For example:
        - Maximum similarity is 1.0 and occurs when <answer1> == <answer2>
        - Minimum similarity is 0.0 and occurs when <answer1> is the minimum
            possible answer and <answer2> is the maximum possible answer
            (or vice versa).

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        dif = abs(answer1.content - answer2.content)
        dif_div = dif/(self.__getitem__(-1) - self.__getitem__(0))
        # -1 and 0 are the max and min respectively
        return float(1.0 - dif_div)

    # done
    def __getitem__(self, item: int) -> int:
        """returns the item at index item in _answer_options
         >>> numq = NumericQuestion(1, "hello", 0, 10)
         >>> numq.__getitem__(1)
         1
         """
        return self._answer_options[item]


class YesNoQuestion(Question):
    """ A question whose answer is either yes (represented by True) or
    no (represented by False).

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    === Representation Invariants ===
    text is not the empty string
    """
    id: int
    text: str

# done
    def __init__(self, id_: int, text: str) -> None:
        """
        Initialize a question with the text <text> and id <id>.
        """
        Question.__init__(self, id_, text)

# done
    def __str__(self) -> str:
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        return str(self.text) + " YESNO"

# done
    def validate_answer(self, answer: Answer) -> bool:
        """
        Return True iff <answer>'s content is a boolean.
        """
        return isinstance(answer.content, bool)
# done
    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return 1.0 iff <answer1>.content is equal to <answer2>.content and
        return 0.0 otherwise.

        === Precondition ===
        <answer1> and <answer2> are both valid answers to this question
        """
        if answer1.content == answer2.content:
            return 1.0
        else:
            return 0.0


class CheckboxQuestion(Question):

    """ A question whose answers can be one or more of several options

    === Public Attributes ===
    id: the id of this question
    text: the text of this question

    ===Private Attributes===
    _answer_options: list of all the answer options

    === Representation Invariants ===
    text is not the empty string
    """

    id: int
    text: str
    _options: List[str]

    # done
    def __init__(self, id_: int, text: str, options: List[str]) -> None:
        """
        Initialize a question with the text <text> and id <id> and
        possible answers <options>.

        === Precondition ===
        No two elements in <options> are the same string
        <options> contains at least two elements
        """
        self._options = options
        Question.__init__(self, id_, text)

    def __str__(self) -> str:  # done
        """
        Return a string representation of this question including the
        text of the question and a description of the possible answers.

        You can choose the precise format of this string.
        """
        return str(self.text) + " CheckBoxQuestion"

    def validate_answer(self, answer: Answer) -> bool:  # done
        """
        Return True iff <answer> is a valid answer to this question.

        An answer is valid iff its content is a non-empty list containing
        unique possible answers to this question. # no pizza and pizza
        """
        if answer.content == []:  # if it's an empty list
            return False
        unique_list = []
        for ans in answer.content:  # because this would be a list of string
            # can iterate through the options b/c the options are a list
            if ans not in unique_list:
                # want to see what the unique answers are
                unique_list.append(ans)
        for ans in unique_list:
            # making sure that ans are options for the question
            if ans not in self._options:
                return False
        return len(unique_list) == len(answer.content)

#done
    def get_similarity(self, answer1: Answer, answer2: Answer) -> float:
        """
        Return the similarity between <answer1> and <answer2>.

        Similarity is defined as the ratio between the number of strings that
        are common to both <answer1>.content and <answer2>.content over the
        total number of unique strings that appear in both <answer1>.content and
        <answer2>.content

        For example, if <answer1>.content == ['a', 'b', 'c'] and
        <answer1>.content == ['c', 'b', 'd'], the strings that are common to
        both are ['c', 'b'] and the unique strings that appear in both are
        ['a', 'b', 'c', 'd'].

        === Precondition ===
        <answer1>and <answer2> are both valid answers to this question
        """

        union_list = list(dict.fromkeys(answer1.content + answer2.content))
        # will return the union list without duplicates
        intersection_list = sorted(list(set(answer1.content) & set(
            answer2.content)))
        # the intersection list of items in both
        try:
            return len(intersection_list) / len(union_list)
        except ZeroDivisionError:
            return 0.0


class Answer:  # done
    """ An answer to a question used in a survey

    === Public Attributes ===
    content: an answer to a single question
    """
    content: Union[str, bool, int, List[str]]

    def __init__(self,
                 content: Union[str, bool, int, List[Union[str]]]) -> None:
        """Initialize an answer with content <content>"""
        self.content = content

    def is_valid(self, question: Question) -> bool:
        """Return True iff self.content is a valid answer to <question>"""
        return question.validate_answer(self)


class Survey:
    """
    A survey containing questions as well as criteria and weights used to
    evaluate the quality of a group based on their answers to the survey
    questions.

    === Private Attributes ===
    _questions: a dictionary mapping each question's id to the question itself
    _criteria: a dictionary mapping a question's id to its associated criterion
    _weights: a dictionary mapping a question's id to a weight; an integer
              representing the importance of this criteria.
    _default_criterion: a criterion to use to evaluate a question if the
              question does not have an associated criterion in _criteria
    _default_weight: a weight to use to evaluate a question if the
              question does not have an associated weight in _weights
    _ques: the list of all the questions in the survey

    === Representation Invariants ===
    No two questions on this survey have the same id
    Each key in _questions equals the id attribute of its value
    Each key in _criteria occurs as a key in _questions
    Each key in _weights occurs as a key in _questions
    Each value in _weights is greater than 0
    _default_weight > 0
    """

    _questions: Dict[int, Question]
    _criteria: Dict[int, Criterion]
    _weights: Dict[int, int]
    _default_criterion: Criterion
    _default_weight: int
    _ques: List[Question]

    def __init__(self, questions: List[Question]) -> None:  # done
        """
        Initialize a new survey that contains every question in <questions>.
        This new survey should use a HomogeneousCriterion as a default criterion
        and should use 1 as a default weight.
        """
        self._ques = questions
        self._questions = {}  # dict of question id to question
        for quest in self._ques:
            self._questions[quest.id] = quest
        self._criteria = {}  # dict question id to criterion
        self._default_criterion = HomogeneousCriterion()
        self._default_weight = 1
        self._weights = {}  # question id to weight of question

    def __len__(self) -> int:  # done
        """ Return the number of questions in this survey """
        return len(self._ques)

    def __contains__(self, question: Question) -> bool:  # done
        """
        Return True iff there is a question in this survey with the same
        id as <question>.
        """
        return question.id in self._questions

    def __str__(self) -> str:  # done
        """
        Return a string containing the string representation of all
        questions in this survey

        You can choose the precise format of this string.
        """
        string = ""
        for question in self._ques:  # string of all the questions in the survey
            string = string + " " + str(question)
            # single string of all the lists
        return string

    def get_questions(self) -> List[Question]:  # done
        """ Return a list of all questions in this survey """
        return self._ques
        # is the list of all the questions

    def _get_criterion(self, question: Question) -> Criterion:  # done
        """
        Return the criterion associated with <question> in this survey.

        Iff <question>.id does not appear in self._criteria, return the default
        criterion for this survey instead.

        === Precondition ===
        <question>.id occurs in this survey
        """
        if question.id in self._criteria:
            return self._criteria[question.id]
        else:
            return self._default_criterion

    def _get_weight(self, question: Question) -> int:  # done
        """
        Return the weight associated with <question> in this survey.

        Iff <question>.id does not appear in self._weights, return the default
        weight for this survey instead.

        === Precondition ===
        <question>.id occurs in this survey
        """
        if question.id in self._weights:
            return self._weights[question.id]
        else:
            return self._default_weight

    def set_weight(self, weight: int, question: Question) -> bool:  # done
        """
        Set the weight associated with <question> to <weight> and return True.

        If <question>.id does not occur in this survey, do not set the <weight>
        and return False instead.
        """
        if question.id not in self._questions:
            return False  # if not in survey
        else:
            self._weights[question.id] = weight
            return True

#done
    def set_criterion(self, criterion: Criterion, question: Question) -> bool:
        """
        Set the criterion associated with <question> to <criterion> and return
        True.

        If <question>.id does not occur in this survey, do not set the <
        criterion> and return False instead.
        """
        if question.id not in self._questions:
            return False  # if not in survey
        else:
            self._criteria[question.id] = criterion
            return True

# done
    def score_students(self, students: List[Student]) -> float:
        """
        Return a quality score for <students> calculated based on their answers
        to the questions in this survey, and the associated criterion and weight
        for each question .

        This score is determined using the following algorithm:

        1. For each question in <self>, find its associated criterion, weight,
           and <students> answers to this question. Use the score_answers method
           for this criterion to calculate a quality score. Multiply this
           quality score by the associated weight.
        2. Find the average of all quality scores from step 1.

        If an InvalidAnswerError would be raised by calling this method, or if
        there are no questions in <self>, this method should return zero.

        === Precondition ===
        All students in <students> have an answer to all questions in this
            survey
        """
        if len(self) == 0:
            return 0.0
        if len(students) == 0:
            return 0.0
        q_to_crit = {}
        q_to_weight = {}
        q_to_studs_answers = {}
        lst_of_scores = []
        try:
            for q in self._ques:
                q_to_crit[q] = self._get_criterion(q)
                q_to_weight[q] = self._get_weight(q)
                q_to_studs_answers[q] = []
                # make an empty list because need to find students that have
                # answered the question
            for stud in students:
                for q in self.get_questions():
                    q_to_studs_answers[q].append(stud.get_answer(q))
            # appending all the student answers to each question
            for q in self.get_questions():
                weight = q_to_weight[q]
                crit = q_to_crit[q]
                answers = q_to_studs_answers[q]
                score = crit.score_answers(q, answers) * weight
                # deal with the added argument
                lst_of_scores.append(score)
            # finding the score for each question
            return sum(lst_of_scores) / len(lst_of_scores)
        except InvalidAnswerError:
            return 0.0

        # lst_of_scores =[]
        # dict_q_to_crit = {}
        # dict_q_to_weight ={}
        # dict_q_to_ans = {}
        # if len(self._questions) == 0:
        #     return 0.0
        # for stud in students:
        #     for q in self._ques:
        #         ans = stud.get_answer(q)
        #         if not ans.is_valid(q):
        #             return 0
        #         # checking that every answer is a valid answer
        # # for q in self._ques:  # the list of the questions
        # #     dict_q_to_crit[q] = self._get_criterion(q)
        # #     dict_q_to_weight[q] = self._get_weight(q)
        # #     dict_q_to_ans[q] =

#done
    def score_grouping(self, grouping: Grouping) -> float:
        """ Return a score for <grouping> calculated based on the answers of
        each student in each group in <grouping> to the questions in <self>.

        If there are no groups in <grouping> this score is 0.0. Otherwise, this
        score is determined using the following algorithm:

        1. For each group in <grouping>, get the score for the members of this
           group calculated based on their answers to the questions in this
           survey.
        2. Return the average of all the scores calculated in step 1.

        === Precondition ===
        All students in the groups in <grouping> have an answer to all questions
            in this survey
        """
        if len(grouping) == 0:
            return 0.0
        lst_of_group_scores = []
        for group in grouping.get_groups():
            lst_of_studs = group.get_members()
            # the students in each group
            score_of_group = self.score_students(lst_of_studs)
            # the score for the group
            lst_of_group_scores.append(score_of_group)
        try:
            return sum(lst_of_group_scores) / len(lst_of_group_scores)
        except ZeroDivisionError:
            return 0.0


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing',
                                                  'criterion',
                                                  'course',
                                                  'grouper']})
