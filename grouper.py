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
Sophia Huynh and Jaisie Sinlen(
=== Module Description ===

This file contains classes that define different algorithms for grouping
students according to chosen criteria and the group members' answers to survey
questions. This file also contain a classe that describes a group of students as
well as a grouping (a group of groups).
"""
from __future__ import annotations
import random
from typing import TYPE_CHECKING, List, Any
from course import Course, Student, sort_students
if TYPE_CHECKING:
    from survey import Survey


def slice_list(lst: List[Any], n: int) -> List[List[Any]]: # done
    """
    Return a list containing slices of <lst> in order. Each slice is a
    list of size <n> containing the next <n> elements in <lst>.

    The last slice may contain fewer than <n> elements in order to make sure
    that the returned list contains all elements in <lst>.

    === Precondition ===
    n <= len(lst)

    >>> slice_list([3, 4, 6, 2, 3], 2) == [[3, 4], [6, 2], [3]]
    True
    >>> slice_list(['a', 1, 6.0, False], 3) == [['a', 1, 6.0], [False]]
    True
    >>> slice_list([1,2,3,4], 2) == [[1,2], [3,4]]
    True
    >>> slice_list([1,2], 2) == [[1, 2]]
    True
    """
    if len(lst) == 0:
        return [[]]
    if len(lst) == n:
        to_return = [lst]
        return to_return
    empty = []
    i = 0
    while i + n < len(lst):
        end = min(len(lst), i + n)
        sublist = lst[i: end]
        empty.append(sublist)
        i += i + n

    last_in_empty = len(lst) - 1 - lst[::-1].index(empty[-1][-1])
    empty.append(lst[last_in_empty + 1:])
    return empty


def windows(lst: List[Any], n: int) -> List[List[Any]]: # done
    """
    Return a list containing windows of <lst> in order. Each window is a list
    of size <n> containing the elements with index i through index i+<n> in the
    original list where i is the index of window in the returned list.

    === Precondition ===
    n <= len(lst)

    >>> windows([3, 4, 6, 2, 3], 2) == [[3, 4], [4, 6], [6, 2], [2, 3]]
    True
    >>> windows(['a', 1, 6.0, False], 3) ==   [['a', 1, 6.0], [1, 6.0, False]]
    True
    >>> windows([3, 4, 5, 6], 2) == [[3,4], [4,5], [5,6] ]
    True
    >>> windows([], 0)
    [[]]
    >>> windows([1], 1)
    [[1]]
    """
    empty = []
    i = 0
    while i + n <= len(lst):
        empty.append(lst[i: i + n])
        i += 1
    return empty


class Grouper:
    """
    An abstract class representing a grouper used to create a grouping of
    students according to their answers to a survey.

    === Public Attributes ===
    group_size: the ideal number of students that should be in each group

    === Representation Invariants ===
    group_size > 1
    """

    group_size: int

    def __init__(self, group_size: int) -> None:  # done
        """
        Initialize a grouper that creates groups of size <group_size>

        === Precondition ===
        group_size > 1
        """
        self.group_size = group_size

    def make_grouping(self, course: Course, survey: Survey) -> Grouping:
        """ Return a grouping for all students in <course> using the questions
        in <survey> to create the grouping.
        """
        raise NotImplementedError


class AlphaGrouper(Grouper):
    """
    A grouper that groups students in a given course according to the
    alphabetical order of their names.

    === Public Attributes ===
    group_size: the ideal number of students that should be in each group

    === Representation Invariants ===
    group_size > 1
    """

    group_size: int

    # done
    def make_grouping(self, course: Course, survey: Survey) -> Grouping:
        """
        Return a grouping for all students in <course>.

        The first group should contain the students in <course> whose names come
        first when sorted alphabetically, the second group should contain the
        next students in that order, etc.

        All groups in this grouping should have exactly self.group_size members
        except for the last group which may have fewer than self.group_size
        members if that is required to make sure all students in <course> are
        members of a group.

        Hint: the sort_students function might be useful
        """
        lst = []  # list of students
        to_return = Grouping()
        for stud in course.get_students():  # shallow list of course.student
            lst.append(stud)  # the student in the course
        if len(lst) == 0:
            return to_return
        size = self.group_size
        lst = sort_students(lst, "name")  # sorting the students
        sliced_list = slice_list(lst, size)  # divided the students properly
        for sublist in sliced_list:  # need to make them all groups
            to_return.add_group(Group(sublist))  # each sublist is a group
        return to_return


class RandomGrouper(Grouper):
    """
    A grouper used to create a grouping of students by randomly assigning them
    to groups.

    === Public Attributes ===
    group_size: the ideal number of students that should be in each group

    === Representation Invariants ===
    group_size > 1
    """

    group_size: int

    # done
    def make_grouping(self, course: Course, survey: Survey) -> Grouping:
        """
        Return a grouping for all students in <course>.

        Students should be assigned to groups randomly.

        All groups in this grouping should have exactly self.group_size members
        except for one group which may have fewer than self.group_size
        members if that is required to make sure all students in <course> are
        members of a group.
        """
        to_return = Grouping()
        lst = []  # need a shallow list
        for stud in course.get_students():
            lst.append(stud)
        while len(lst) > 0:
            sublist = []
            i = 0
            while i < self.group_size and len(lst) != 0:
                # want to have n random
                ind_in_lst = random.randint(0, len(lst) - 1)
                sublist.append(lst[ind_in_lst])
                lst.pop(ind_in_lst)
                i += 1
            to_return.add_group(Group(sublist))  # need to return a grouping
            # which takes argument group
        return to_return


class GreedyGrouper(Grouper):  # done
    """
    A grouper used to create a grouping of students according to their
    answers to a survey. This grouper uses a greedy algorithm to create
    groups.

    === Public Attributes ===
    group_size: the ideal number of students that should be in each group

    === Representation Invariants ===
    group_size > 1
    """

    group_size: int

    def make_grouping(self, course: Course, survey: Survey) -> Grouping:
        """
        Return a grouping for all students in <course>.

        Starting with a tuple of all students in <course> obtained by calling
        the <course>.get_students() method, create groups of students using the
        following algorithm:

        1. select the first student in the tuple that hasn't already been put
           into a group and put this student in a new group.
        2. select the student in the tuple that hasn't already been put into a
           group that, if added to the new group, would increase the group's
           score the most (or reduce it the least), add that student to the new
           group.
           # which would make the group the best group
        3. repeat step 2 until there are N students in the new group where N is
           equal to self.group_size.
        4. repeat steps 1-3 until all students have been placed in a group.

        In step 2 above, use the <survey>.score_students method to determine
        the score of each group of students.

        The final group created may have fewer than N members if that is
        required to make sure all students in <course> are members of a group.
        """
        to_return = Grouping()
        lst_of_studs = []
        for stud in course.get_students():
            lst_of_studs.append(stud)
        if len(lst_of_studs) == 0:
            return to_return
        lst_of_studs = sort_students(lst_of_studs, "id")
        i = 0
        while i < (len(course.get_students()) - 1):
            group_lst = []
            while len(group_lst) != self.group_size and len(lst_of_studs) != 0:
                # important stopping conditions
                student1 = lst_of_studs[1]
                tups_of_scores_and_studs = []
                if len(group_lst) == 0:
                    group_lst.append(lst_of_studs[i])
                    lst_of_studs.pop(i)
                    # first student to add
                for stud in lst_of_studs:
                    tups_of_scores_and_studs.append((survey.score_students(
                        group_lst + [stud]), stud))
                    # appedning the sore of the group with the student
                lst_of_scores = []
                for tup in tups_of_scores_and_studs:
                    lst_of_scores.append(tup[0])
                ind_of_highest = lst_of_scores.index(max(lst_of_scores))
                # find the index of the tup with this score
                lst_of_studs.pop(lst_of_studs.index(
                    tups_of_scores_and_studs[ind_of_highest][1]))
                # removing the student with the highest score from lst of studs
                group_lst.append(tups_of_scores_and_studs[ind_of_highest][1])
                # adding that student to group_lst
                if student1 not in lst_of_studs:  # for starting from beggining
                    i += 1
                else:
                    i = 0
            if len(group_lst) != 0:
                group = Group(group_lst)
                to_return.add_group(group)
            if len(lst_of_studs) == 0:
                i += 1
        if len(lst_of_studs) != 0:
            lst = []
            for stud in lst_of_studs:
                lst.append(stud)
            to_return.add_group(Group(lst))
            # for dealing with the remainder
        return to_return
                    # if tup_of_studs[i] in lst_of_studs and len(group_lst) ==
        # 0:
                        # lst_of_studs.pop(i)
                        # group_lst.append(tup_of_studs[i])
                #     prev_temp_score = survey.score_student(group_lst)
                #     group_lst.append(tup_of_studs[i + 1])
                #     temp_score = survey.score_students(group_lst)
                #     if temp_score <= prev_temp_score:
                #         group_lst.pop()
                #     else:
                #         lst_of_studs.pop(i + 1)
                # group = Group(group_lst)
                # to_return.add_group(group)
        # return to_return
        # for stud in tup_of_studs:
        #     lst_of_studs.append(stud)
        # while len(lst_of_studs) != 0:
        #     for i in range(len_tup):
        #         temp_lst = []
        #         if stud in lst_of_studs:
        #             lst_of_studs.remove(stud)
        #             temp_lst.append(stud)
        #         i = 0
        #         while i < len_tup and temp_lst != N and lst_of_studs != []:
        #             temp_score = survey.score_students(temp_lst + [
        #                 tup_of_studs[i]])
        # for i in range(len(tup_of_studs)):
        #     # looping through the length to studs
        #     new_lst = []
        #     while len(new_lst) < N and len(lst_of_studs) != 0:
        #         # second condition because want to avoid the situation
        #         # in which
        #         # the end was reached
        #         new_lst.append(tup_of_studs[i])
        #         # the current student that is leading the group
        #         lst_of_studs.pop(i)
        #         # no longer being compared to so can remove him
        #         score = 0
        #         for stud in tup_of_studs:
        #             if survey.score_students(new_lst + [stud]) > score:
        #                 new_lst.append(stud)
        #                 score = survey.score_students(new_lst)
        #                 # update score
        #                 lst_of_studs.remove(stud)
        #                 # no longer want to check because we removed them
        #                 # from the group
        #     group = Group(new_lst)
            # create a list of the students which is now len(n) after
            # exiting while loop
        #     to_return.add_group(group)
        # return to_return
    # def _great_score(self, lst_of_studs: List[Student], survey: Survey, score
    # ) -> float:
    #     """returns the greatest score of between all the students in the list
    #     >>> q1 = YesNoQuestion(1, "water?")
    #     >>> YNsurvey = Survey([q1])
    #     >>> YNsurvey.set_criterion(HomogenousCriterion(, q1))
    #     True
    #     >>>stud1 = Student(1, "a")
    #     >>>stud2 = Student(2, "b")
    #     >>>stud3 = Student(2, "b")
    #     >>>stud1.set_answer(q1, True)
    #     >>> stud2.set_answer(q1, True)
    #     >>> stud3.set_answer(q1, False)
    #     >>> gg = GreedyGrouper(2)
    #     >>> gg._great_score([stud1, stud2, stud3], YNsurvey)
    #     1
    #     """
    #     for i in range(lst_of_studs)


class WindowGrouper(Grouper):  # done
    """
    A grouper used to create a grouping of students according to their
    answers to a survey. This grouper uses a window search algorithm to create
    groups.

    === Public Attributes ===
    group_size: the ideal number of students that should be in each group

    === Representation Invariants ===
    group_size > 1
    """

    group_size: int

    def make_grouping(self, course: Course, survey: Survey) -> Grouping:
        """
        Return a grouping for all students in <course>.

        Starting with a tuple of all students in <course> obtained by calling
        the <course>.get_students() method, create groups of students using the
        following algorithm:

        1. Get the windows of the list of students who have not already been
           put in a group.
        2. For each window in order, calculate the current window's score as
           well as the score of the next window in the list. If the current
           window's score is greater than or equal to the next window's score,
           make a group out of the students in current window and start again at
           step 1. If the current window is the last window, compare it to the
           first window instead.

        In step 2 above, use the <survey>.score_students to determine the score
        of each window (list of students).

        In step 1 and 2 above, use the windows function to get the windows of
        the list of students.

        If there are any remaining students who have not been put in a group
        after repeating steps 1 and 2 above, put the remaining students into a
        new group.
        """

        n = self.group_size
        tup_of_studs = course.get_students()
        lst_of_studs = []
        to_return = Grouping()
        for stud in tup_of_studs:
            lst_of_studs.append(stud)
        if len(lst_of_studs) == 0:
            return to_return
        lst_of_studs = sort_students(lst_of_studs, "id")
        lst_of_windows = windows(lst_of_studs, n)
        shallow_lst_of_windows = []
        for window in lst_of_windows:
            shallow_lst_of_windows.append(window)
        i = 0
        while i < len(shallow_lst_of_windows) - 1:
            if survey.score_students(shallow_lst_of_windows[i]) >= \
                    survey.score_students(shallow_lst_of_windows[i + 1]):
                to_return.add_group(Group(shallow_lst_of_windows[i]))
                # add group to grouping
                for stud in shallow_lst_of_windows[i]:  # this avoids repeats
                    lst_of_studs.remove(stud)
                shallow_lst_of_windows = windows(lst_of_studs, n)
                i = 0
            else:    # have to start comparing from the beggining  again
                i += 1
        if len(shallow_lst_of_windows) != 0:
            # comparing the last with the first
            if survey.score_students(shallow_lst_of_windows[-1]) >= \
                survey.score_students(shallow_lst_of_windows[0]):
                to_return.add_group(Group(shallow_lst_of_windows[-1]))
                shallow_lst_of_windows.pop(-1)
        if len(shallow_lst_of_windows) != 0:
            # if some did not get matched
            for lst in shallow_lst_of_windows:
                to_return.add_group(Group(lst))
            # want to increment
        return to_return


class Group:
    """
    A group of one or more students

    === Private Attributes ===
    _members: a list of unique students in this group

    === Representation Invariants ===
    No two students in _members have the same id
    """

    _members: List[Student]

    def __init__(self, members: List[Student]) -> None:  # tested
        """ Initialize a group with members <members> """
        self._members = members

    def __len__(self) -> int:   # done
        """ Return the number of members in this group """
        return len(self._members)

    def __contains__(self, member: Student) -> bool:  # done
        """
        Return True iff this group contains a member with the same id
        as <member>.
        """
        id_ = member.id
        for stud in self._members:
            if stud.id == id_:
                return True
        return False

    def __str__(self) -> str:  # done
        """
        Return a string containing the names of all members in this group
        on a single line.

        You can choose the precise format of this string.
        """
        i = 0
        string = ""
        for stud in self._members:
            string = string + " " + str(i) + " " + str(stud.name)
            i += 1
        return string

    def get_members(self) -> List[Student]:  # done
        """ Return a list of members in this group. This list should be a
        shallow copy of the self._members attribute.
        """
        lst = []
        for student in self._members:
            lst.append(student)
        return lst


class Grouping:
    """
    A collection of groups

    === Private Attributes ===
    _groups: a list of Groups

    === Representation Invariants ===
    No group in _groups contains zero members
    No student appears in more than one group in _groups
    """

    _groups: List[Group]

    def __init__(self) -> None:  # done
        """ Initialize a Grouping that contains zero groups """
        self._groups = []

    def __len__(self) -> int:  # done
        """ Return the number of groups in this grouping """
        return len(self._groups)

    def __str__(self) -> str:  # done
        """
        Return a multi-line string that includes the names of all of the members
        of all of the groups in <self>. Each line should contain the names
        of members for a single group.

        You can choose the precise format of this string.
        """
        string = ""
        for group in self._groups:
            string = string + str(group) + "\n"
        return string

    def add_group(self, group: Group) -> bool:  # done
        """
        Add <group> to this grouping and return True.

        Iff adding <group> to this grouping would violate a representation
        invariant don't add it and return False instead.
        """
        lst_of_studs_in_group = []
        for gr in self._groups:
            for stud in gr.get_members():
                lst_of_studs_in_group.append(stud)
        for member in group.get_members():
            if member in lst_of_studs_in_group:
                return False
        if len(group) == 0:
            return False
        self._groups.append(group)
        return True

    def get_groups(self) -> List[Group]:  # done
        """ Return a list of all groups in this grouping. 
        This list should be a shallow copy of the self._groups 
        attribute.
        """
        lst_of_groups = []
        for group in self._groups:
            lst_of_groups.append(group)
        return lst_of_groups


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={'extra-imports': ['typing',
                                                  'random',
                                                  'survey',
                                                  'course']})
