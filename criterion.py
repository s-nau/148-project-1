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

This file contains classes that describe different types of criteria used to
evaluate a group of answers to a survey question.
"""
from __future__ import annotations
from typing import TYPE_CHECKING, List
if TYPE_CHECKING:
    from survey import Question, Answer


class InvalidAnswerError(Exception):
    """
    Error that should be raised when an answer is invalid for a given question.
    """


class Criterion:
    """
    An abstract class representing a criterion used to evaluate the quality of
    a group based on the group members' answers for a given question.
    """

    def score_answers(self, question: Question, answers: List[Answer]) -> float:
        """
        Return score between 0.0 and 1.0 indicating the quality of the group of
        <answers> to the question <question>.

        Raise InvalidAnswerError if any answer in <answers> is not a valid
        answer to <question>.

        Each implementation of this abstract class will measure quality
        differently.
        """
        raise NotImplementedError

#done
class HomogeneousCriterion(Criterion):

    """
    A criterion used to evaluate the quality of a group based on the group
    members' answers for a given question.

    This criterion gives a higher score to answers that are more similar.
    """

    def score_answers(self, question: Question, answers: List[Answer]) -> float:
        """
        Return a score between 0.0 and 1.0 indicating how similar the answers in
        <answers> are.

        This score is calculated by finding the similarity of every
        combination of two answers in <answers> and taking the average of all
        of these similarity scores.

        If there is only one answer in <answers> and it is valid return 1.0
        since a single answer is always identical to itself.

        Raise InvalidAnswerError if any answer in <answers> is not a valid
        answer to <question>.

        === Precondition ===
        len(answers) > 0
        """

        for ans in answers:  # checking if any answer in not valid
            if not ans.is_valid(question):
                raise InvalidAnswerError
        if len(answers) == 1:
            return 1.0
        lst_score = []
        for opt in answers:  # looping through to get the combination
            ind = answers.index(opt)
            for other_opt in answers[ind + 1:]:
                # to not include the current option
                # checking for indexing errors
                similarity = question.get_similarity(opt, other_opt)
                lst_score.append(similarity)
                # similarity of the two answers
        average = sum(lst_score) / len(lst_score)
        # sum of all the score divided by number of scores
        return average


class HeterogeneousCriterion(Criterion):  # done
    """ A criterion used to evaluate the quality of a group based on the group
    members' answers for a given question.

    This criterion gives a higher score to answers that are more different.
    """

    def score_answers(self, question: Question, answers: List[Answer]) -> float:
        """
        Return a score between 0.0 and 1.0 indicating how similar the answers in
        <answers> are.

        This score is calculated by finding the similarity of every
        combination of two answers in <answers>, finding the average of all
        of these similarity scores, and then subtracting this average from 1.0

        If there is only one answer in <answers> and it is valid, return 0.0
        since a single answer is never identical to itself.

        Raise InvalidAnswerError if any answer in <answers> is not a valid
        answer to <question>.

        === Precondition ===
        len(answers) > 0
        """
        for answer in answers:
            if not answer.is_valid(question):
                raise InvalidAnswerError
        if len(answers) == 1:
            return 0.0
        lst_of_similarity = []
        for opt1 in answers:
            index = answers.index(opt1)
            for opt2 in answers[index + 1:]:
                # after the opt index, check the end
                similarity = question.get_similarity(opt1, opt2)
                lst_of_similarity.append(similarity)
        average = sum(lst_of_similarity) / len(lst_of_similarity)
        # average value
        return float(1.0 - average)


class LonelyMemberCriterion(Criterion): # done
    """ A criterion used to measure the quality of a group of students
    according to the group members' answers to a question. This criterion
    assumes that a group is of high quality if no member of the group gives
    a unique answer to a question.
    """
    def score_answers(self, question: Question, answers: List[Answer]) -> float:
        """
        Return score between 0.0 and 1.0 indicating the quality of the group of
        <answers> to the question <question>.

        The score returned will be zero iff there are any unique answers in
        <answers> and will be 1.0 otherwise.

        An answer is not unique if there is at least one other answer in
        <answers> with identical content.

        Raise InvalidAnswerError if any answer in <answers> is not a valid
        answer to <question>.

        === Precondition ===
        len(answers) > 0
        """
        for answer in answers:
            if not answer.is_valid(question):
                # checking that every answer is valid
                raise InvalidAnswerError
        lst_similar = []
        lst_contents = []
        for answer in answers:
            if not isinstance(answer, list):
                # if each answer is in answers is a list would need to treat
                # differently
                lst_contents.append(answer.content)
            else:
                lst_contents.append(set(answer.content))
        i = 0
        if len(answers) == 0 or len(answers) == 1:
            return 0.0
        while i < len(lst_contents) - 1:
            if not lst_contents[i] in lst_similar:
                # checking to see if there is one before it that
                # already has been compared to it
                if lst_contents[i] in lst_contents[i + 1:]:
                    # don't want to include the current one in checking
                    # membership
                    lst_similar.append(lst_contents[i])
                else:
                    return 0.0
                    # one that doesn't have similarity will return 0.0
            i += 1
        if lst_contents[-1] in lst_similar:
            # checking if the last member has a common element
            return 1.0
        else:
            return 0.0


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing',
                                                  'survey']})
