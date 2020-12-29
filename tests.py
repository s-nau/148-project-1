

from survey import Answer
from grouper import slice_list, windows
import course
import survey
import criterion
import grouper
import pytest
from typing import List, Set, FrozenSet
@pytest.fixture
def GreedyGrouper2():
    return grouper.GreedyGrouper(3)

@pytest.fixture
def GreedyGrouper1():
    return grouper.GreedyGrouper(2)

@pytest.fixture
def group1(students):
    return grouper.Group([students[1] , students[0]])


@pytest.fixture
def group2(students):
    return grouper.Group([students[2], students[3]])


@pytest.fixture
def Alpha1():
    return grouper.AlphaGrouper(1)


@pytest.fixture
def Alpha_size2():
    return grouper.AlphaGrouper(2)


@pytest.fixture
def empty_grouping():
    return grouper.Grouping()


@pytest.fixture
def homo():
    return criterion.HomogeneousCriterion()


@pytest.fixture
def hetero():
    return criterion.HeterogeneousCriterion()


@pytest.fixture
def lonely():
    return criterion.LonelyMemberCriterion()


@pytest.fixture
def AlphaGrouping_odd_len(student_odd_len):
    gr1 = grouper.Group([student_odd_len[1], student_odd_len[2]])
    gr2 = grouper.Group([student_odd_len[4], student_odd_len[3]])
    gr3 = grouper.Group([student_odd_len[0]])
    to_return = grouper.Grouping()
    lst = [gr1, gr2, gr3]
    for group in lst:
        to_return.add_group(group)
    return to_return


@pytest.fixture
def student_odd_len(students):
    stud_5 = course.Student(5, "Shimmy")
    return students + [stud_5]


@pytest.fixture
def student_odd_ans(student_odd_len, NumQ, NUMQans):
    for student in student_odd_len:
        student.set_answer(NumQ, NUMQans)
    return student_odd_len


@pytest.fixture
def course_with_student_odd(student_odd_ans):
    cor = course.Course("math")
    cor.enroll_students(student_odd_ans)
    return cor


@pytest.fixture
def survey_with_NUMq(NumQ):
    return survey.Survey([NumQ])


@pytest.fixture
def lst_of_YN_ans():
    t = survey.Answer(True)
    f = survey.Answer(False)
    return [t, t, f, f]


@pytest.fixture
def lst_of_YN_ans_last_false():
    t = survey.Answer(True)
    f = survey.Answer(False)
    return [t, t, t, f]


@pytest.fixture
def survey_0():
    return survey.Survey([])


@pytest.fixture
def stud():
    return course.Student(1, "shimmy")


@pytest.fixture
def empty_ans():
    return survey.Answer([])

@pytest.fixture
def MCQuestion():
    return survey.MultipleChoiceQuestion(1 , "dinner", ["a", "b"])


@pytest.fixture
def MCQAns():
    return survey.Answer("a")


@pytest.fixture
def NumQ():
    return survey.NumericQuestion(1, "how much", 1, 10)


@pytest.fixture
def NumQ_1():
    return survey.NumericQuestion(10, "how much", 1, 2)


@pytest.fixture
def NUMQans():
    return survey.Answer(1)


@pytest.fixture
def empty_list_ans():
    return survey.Answer([])


@pytest.fixture
def lst_of_studs_with_answers_to_yn(students, YNQuestions):
    true = survey.Answer(True)
    false = survey.Answer(False)
    for q in YNQuestions:
        students[0].set_answer(q, true)
        student[1].set_answer(q, false)
        student[2].set_answer(q, true)
        student[4].set_answer(q, false)
    return students


@pytest.fixture
def YNq():
    return survey.YesNoQuestion(1, "water?")


@pytest.fixture
def YNqnas():
    return survey.Answer(True)


@pytest.fixture
def CheckQuestion():
    return survey.CheckboxQuestion(1, "hello", ["a", "b"])


@pytest.fixture
def Checkboxq_ans():
    return survey.Answer(["a"])


@pytest.fixture
def CheckQuestion2():
    return survey.CheckboxQuestion(100, "hello", ["a", 'b', 'c', 'd'])



@pytest.fixture
def lst_MCQ_ans():
    ans1 = Answer("a")
    ans2 = Answer("b")
    ans3 = Answer("a")
    ans4 = Answer("b")
    return [ ans1, ans2, ans3, ans4]


@pytest.fixture
def lst_NumQ_ans():
    ans1 = Answer(1)
    ans2 = Answer(2)
    ans3 = Answer(3)
    ans4 = Answer(4)
    return list(ans1, ans2, ans3, ans4)


@pytest.fixture
def Check_ans_lst():
    ans1 = Answer(["a","b"])
    ans2 = Answer(["c", "b"])
    ans3 = Answer(["a", "d"])
    ans4 = Answer(["d"])
    return [ans1, ans2, ans3, ans4]


@pytest.fixture
def Checkboxq2():
    return survey.CheckboxQuestion(2, "hello", ["a", "b", "c", "d", "e"])


@pytest.fixture
def checkboxq_ans_long_a():
    return survey.Answer(["a", "b", "c"])


@pytest.fixture
def checkboxq_ans_long_b():
    return survey.Answer(["c", "d", "e"])


@pytest.fixture
def empty_course() -> course.Course:
    return course.Course('csc148')


@pytest.fixture
def students() -> List[course.Student]:
    return [course.Student(1, 'Zoro'),
            course.Student(2, 'Aaron'),
            course.Student(3, 'Gertrude'),
            course.Student(4, 'Yvette')]


@pytest.fixture
def students_out_of_order():
        return [course.Student(2, 'Zoro'),
                course.Student(3, 'Aaron'),
                course.Student(1, 'Gertrude'),
                course.Student(4, 'Yvette')]


@pytest.fixture
def YNQuestions():
    return [survey.YesNoQuestion(1, "water?"),
            survey.YesNoQuestion(2, "water?"),
            survey.YesNoQuestion(3, "water?")]


@pytest.fixture
def survey_with_YN_question(YNQuestions):
    return survey.Survey(YNQuestions)


@pytest.fixture
def studs_with_ans_besides_one_for_YN(students, YNQuestions):
     for i in range(len(students) - 1):
         students[i].set_answer(YNQuestions[i], survey.Answer(True))
     return students


@pytest.fixture
def course_with_studs_all_but_one_ans(
        studs_with_ans_besides_one_for_YN,empty_course):
    empty_course.enroll_students(studs_with_ans_besides_one_for_YN)
    return empty_course


@pytest.fixture
def students_short():
    return [course.Student(1, "a")]


@pytest.fixture
def studs_violates() -> List[course.Student]:
        return [course.Student(1, 'Zoro'),
                course.Student(2, 'Aaron'),
                course.Student(3, 'Gertrude'),
                course.Student(4, '')]


@pytest.fixture
def alpha_grouping(students_with_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_answers[0],
                                      students_with_answers[3]]))
    grouping.add_group(grouper.Group([students_with_answers[1],
                                      students_with_answers[2]]))
    return grouping


@pytest.fixture
def greedy_grouping(students_with_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_answers[1],
                                      students_with_answers[3]]))
    grouping.add_group(grouper.Group([students_with_answers[0],
                                      students_with_answers[2]]))
    return grouping


@pytest.fixture
def window_grouping(students_with_answers) -> grouper.Grouping:
    grouping = grouper.Grouping()
    grouping.add_group(grouper.Group([students_with_answers[0],
                                      students_with_answers[1]]))
    grouping.add_group(grouper.Group([students_with_answers[2],
                                      students_with_answers[3]]))
    return grouping


@pytest.fixture
def questions() -> List[survey.Question]:
    return [survey.MultipleChoiceQuestion(1, 'why?', ['a', 'b']),
            survey.NumericQuestion(2, 'what?', -2, 4),
            survey.YesNoQuestion(3, 'really?'),
            survey.CheckboxQuestion(4, 'how?', ['a', 'b', 'c'])]


@pytest.fixture
def criteria(answers) -> List[criterion.Criterion]:
    return [criterion.HomogeneousCriterion(),
            criterion.HeterogeneousCriterion(),
            criterion.LonelyMemberCriterion()]


@pytest.fixture()
def weights() -> List[int]:
    return [2, 5, 7]


@pytest.fixture
def answers() -> List[List[survey.Answer]]:
    return [[survey.Answer('a'), survey.Answer('b'),
             survey.Answer('a'), survey.Answer('b')],
            [survey.Answer(0), survey.Answer(4),
             survey.Answer(-1), survey.Answer(1)],
            [survey.Answer(True), survey.Answer(False),
             survey.Answer(True), survey.Answer(True)],
            [survey.Answer(['a', 'b']), survey.Answer(['a', 'b']),
             survey.Answer(['a']), survey.Answer(['b'])]]


@pytest.fixture
def students_with_answers(students, questions, answers) -> List[course.Student]:
    for i, student in enumerate(students):
        for j, question in enumerate(questions):
            student.set_answer(question, answers[j][i])
    return students


@pytest.fixture
def course_with_students(empty_course, students) -> course.Course:
    empty_course.enroll_students(students)
    return empty_course


@pytest.fixture
def course_with_studs_out_of_order(empty_course, students_out_of_order):
    empty_course.enroll_students(students_out_of_order)
    return empty_course


@pytest.fixture
def course_with_students_with_answers(empty_course,
                                      students_with_answers) -> course.Course:
    empty_course.enroll_students(students_with_answers)
    return empty_course


@pytest.fixture
def survey_(questions, criteria, weights) -> survey.Survey:
    s = survey.Survey(questions)
    for i, question in enumerate(questions):
        if i:
            s.set_weight(weights[i-1], question)
        if len(questions)-1 != i:
            s.set_criterion(criteria[i], question)
    return s


@pytest.fixture
def group(students) -> grouper.Group:
    return grouper.Group(students)


def get_member_ids(grouping: grouper.Grouping) -> Set[FrozenSet[int]]:
    member_ids = set()
    for group in grouping.get_groups():
        ids = []
        for member in group.get_members():
            ids.append(member.id)
        member_ids.add(frozenset(ids))
    return member_ids


def compare_groupings(grouping1: grouper.Grouping,
                      grouping2: grouper.Grouping) -> None:
    assert get_member_ids(grouping1) == get_member_ids(grouping2)


@pytest.fixture
def RandomGrouper1():
    return grouper.RandomGrouper(2)


@pytest.fixture
def WindowGrouper1():
    return grouper.WindowGrouper(2)


class TestCourse:
    def test_course_init(self, empty_course):
        assert empty_course.name == 'csc148'
        assert empty_course.students == []

    def test_enroll_studs(self, empty_course, students):
        empty_course.enroll_students(students)
        for stud in empty_course.students:
            assert stud in students

    def test_enroll_empty(self, empty_course):
        empty_course.enroll_students([])
        assert empty_course.students == []

    def test_enroll_short(self, empty_course, students_short):
        empty_course.enroll_students(students_short)
        assert students_short[0] in empty_course.students

    def test_enroll_violate(self,empty_course,studs_violates):
        empty_course.enroll_students(studs_violates)
        assert empty_course.students == []

    def test_all_answered(self, course_with_students_with_answers, survey_):
        assert course_with_students_with_answers.all_answered(survey_)

    def test_all_answered_false(self, course_with_students, survey_):
        assert course_with_students.all_answered(survey_) == False
        
    def test_all_answered_except_one(self, course_with_studs_all_but_one_ans,
                                     survey_with_YN_question):
        assert course_with_studs_all_but_one_ans.all_answered(survey_with_YN_question)  == False

    def test_get_students_empty(self, empty_course):
        assert empty_course.get_students() == tuple()

    def test_enroll_empty(self, empty_course):
        empty_course.enroll_students([])
        assert empty_course.students == []

    def test_get_student(self, empty_course, students_out_of_order, students):
        students1 = course.sort_students(students_out_of_order, "id")
        empty_course.enroll_students(students1)
        funct = empty_course.get_students()
        test = tuple(students)
        for i in range(len(funct)):
            assert funct[i].id == test[i].id


class TestStudent:
    def test_init(self, stud):
        assert stud.id == 1
        assert stud.name == "shimmy"
        assert stud._questions_answered == {}

    def test_str(self, stud):
        assert str(stud) == "shimmy"
        
    def test_has_answer(self, stud, MCQuestion):
        assert stud.has_answer(MCQuestion) == False

    def test_has_answer_and_set_answer(self, stud, YNq):
        ans = survey.Answer(True)
        stud.set_answer(YNq, ans)
        assert stud._questions_answered[1] == ans
        assert stud.has_answer(YNq)

    def test_get_answer(self, stud, YNq):
        assert stud.get_answer(YNq) is None
        stud.set_answer(YNq, survey.Answer(True))
        assert stud.get_answer(YNq) == stud._questions_answered[1]

    def test_has_answer_but_invalid_ans(self, stud, YNq):
        stud.set_answer(YNq, survey.Answer(1))
        assert stud.has_answer(YNq) == False


# test sort_stud
def test_sort_stud(students, students_out_of_order):
    new = course.sort_students(students_out_of_order, "id")
    for i in range(len(new)):
        assert new[i].id == students[i].id

class TestQuestion:
    def test_init(self):
        q = survey.Question(1, "hello")
        assert q.id == 1
        assert q.text == "hello"


class TestMultipleChoiceQuestion:
    def test_init(self, MCQuestion):  # done
        assert MCQuestion.id == 1
        assert MCQuestion.text == "dinner"
        assert MCQuestion._answer_options == ["a", "b"]

    def test_str(self, MCQuestion):
        assert "dinner" in str(MCQuestion)

    def test_validate_answer(self, MCQuestion, MCQAns, NUMQans):
        assert MCQuestion.validate_answer(MCQAns)
        assert MCQuestion.validate_answer(NUMQans) == False

    def test_get_similarity(self, MCQAns, MCQuestion):
        assert pytest.approx(MCQuestion.get_similarity(MCQAns, MCQAns)) == 1.0

    def test_get_similarity_not_similar(self, MCQuestion, MCQAns):
        assert pytest.approx(MCQuestion.get_similarity(MCQAns, survey.Answer("b"))) == 0.0

# numeric questions
def test_init(NumQ):
    assert NumQ.id == 1
    assert NumQ.text == "how much"
    assert NumQ._answer_options == [1,2,3,4,5,6,7,8,9,10]


def test_str1(NumQ):
    assert NumQ.text in str(NumQ)


def test_validate_answer(NumQ, NUMQans):
    assert NumQ.validate_answer(NUMQans)
    invalid_ans = survey.Answer(0)
    assert NumQ.validate_answer(invalid_ans) == False


def test_get_similarity(NumQ):
    ans1 = survey.Answer(1)
    ans2 = survey.Answer(2)
    dif = abs(1-2)
    dif_div = dif / (10 - 1)
    one_dif = 1.0 - dif_div
    assert NumQ.get_similarity(ans1, ans2) == one_dif
    ans10 = survey.Answer(10)
    assert NumQ.get_similarity(ans1, ans10) == 0.0
    assert NumQ.get_similarity(ans1, ans1) == 1.0


def test_get_item(NumQ):
    assert NumQ.__getitem__(0) == 1

 # yes no questions
def test_init_YNQ(YNq):
    assert YNq.id == 1
    assert YNq.text == "water?"


def test_str(YNq):
    assert "water?" in str(YNq)


def test_validate_ans1(YNq, YNqnas, MCQAns):
    assert YNq.validate_answer(YNqnas)
    assert YNq.validate_answer(MCQAns) == False


def test_get_similarity1(YNq, YNqnas):
    ans1 = survey.Answer(False)
    assert YNq.get_similarity(ans1, YNqnas) == 0.0
    assert YNq.get_similarity(ans1, ans1) == 1.0


class TestCheckBoxQuestion:
    def test_init(self, CheckQuestion):
        assert CheckQuestion._options == ["a", "b"]
        assert CheckQuestion.id == 1
        assert CheckQuestion.text == "hello"

    def test_str(self, CheckQuestion):
        assert "hello" in str(CheckQuestion)

    def test_validate_answer(self, CheckQuestion, Checkboxq_ans):
        assert CheckQuestion.validate_answer(Checkboxq_ans)
        assert CheckQuestion.validate_answer(survey.Answer([])) == False
        invalid_ans = survey.Answer(["c"])
        assert CheckQuestion.validate_answer(invalid_ans) == False
        invalid_ans_non_unique = survey.Answer(["a", "a"])
        assert CheckQuestion.validate_answer(invalid_ans_non_unique) == False

    def test_get_similarity(self, Checkboxq2, checkboxq_ans_long_a,
                            checkboxq_ans_long_b):
        assert Checkboxq2.get_similarity(checkboxq_ans_long_b,
                                         checkboxq_ans_long_a) == 1/5

    def test_get_similarity_zero(self, Checkboxq2, empty_list_ans):
        assert Checkboxq2.get_similarity(empty_list_ans, empty_list_ans) == 0.0


class TestAnswer:
    def test_init(self, NUMQans):
        assert NUMQans.content == 1

    def test_is_valid_Num(self, NUMQans, NumQ):
        assert NUMQans.is_valid(NumQ)

    def test_is_valid_MC(self, MCQuestion, MCQAns):
        assert MCQAns.is_valid(MCQuestion)

    def test_is_valid_yn(self, YNq, YNqnas):
        assert YNqnas.is_valid(YNq)

    def test_is_valid_check(self, CheckQuestion, Checkboxq_ans):
        assert Checkboxq_ans.is_valid(CheckQuestion)


class TestSurvey:
    def test_init(self, survey_with_YN_question, YNQuestions):
        assert survey_with_YN_question._ques == YNQuestions
        dict_build = {}
        for q in YNQuestions:
            dict_build[q.id] = q
        assert survey_with_YN_question._questions == dict_build
        assert survey_with_YN_question._criteria == {}
        assert survey_with_YN_question._default_weight == 1
        assert survey_with_YN_question._weights == {}

    def test_len(self, survey_with_YN_question):
        assert len(survey_with_YN_question) == 3

    def test_contains(self, survey_with_YN_question):
        q1 = survey.YesNoQuestion(1, "water?")
        assert q1 in survey_with_YN_question
        q2 = survey.YesNoQuestion(5, "water?")
        assert q2 not in survey_with_YN_question

    def test_str(self, survey_with_YN_question):
        for q in survey_with_YN_question._ques:
            assert str(q) in str(
                survey_with_YN_question)

    def test_get_question(self, survey_with_YN_question, YNQuestions):
        assert survey_with_YN_question.get_questions() == YNQuestions

    def test_set_criterion_and_get_crit(self, survey_with_YN_question):
        crit = criterion.HeterogeneousCriterion
        for q in survey_with_YN_question._ques:
            assert survey_with_YN_question.set_criterion(crit, q)
        q_not_in_survey = survey.CheckboxQuestion(10, "hello", ["a"])
        assert survey_with_YN_question.set_criterion(crit, q_not_in_survey) == False
        for q in survey_with_YN_question._ques:
            assert survey_with_YN_question._get_criterion(q) == crit

    def test_set_weight_and_get_weight(self, survey_with_YN_question):
        for q in survey_with_YN_question._ques:
            assert survey_with_YN_question.set_weight(0.1, q)
        for q in survey_with_YN_question._ques:
            assert survey_with_YN_question._get_weight(q) == 0.1
        q_not_in_survey = survey.CheckboxQuestion(10, "hello", ["a"])
        assert survey_with_YN_question.set_weight(0.1, q_not_in_survey) == False
        assert survey_with_YN_question._get_criterion(q_not_in_survey) == \
               survey_with_YN_question._default_criterion

    def test_score_studs_empty(self, survey_0, students):
        assert pytest.approx(survey_0.score_students(students)) == 0.0

    def test_score_studs_hetero(self, survey_with_YN_question , students, YNQuestions):
        crit = criterion.HeterogeneousCriterion()
        for q in YNQuestions:
            for stud in students:
                ans = survey.Answer(False)
                stud.set_answer(q, ans)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_criterion(crit, q)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_weight(0.5, q)
        assert pytest.approx(survey_with_YN_question.score_students(students)) == 0.0

    def test_score_studs_homog(self, survey_with_YN_question, students, YNQuestions ):
        crit = criterion.HomogeneousCriterion()
        for q in YNQuestions:
            for stud in students:
                ans = survey.Answer(False)
                stud.set_answer(q, ans)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_criterion(crit, q)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_weight(0.5, q)
        assert pytest.approx(
            survey_with_YN_question.score_students(students)) == 0.5

    def test_score_studs_lonely(self, survey_with_YN_question, students, YNQuestions ):
        crit = criterion.LonelyMemberCriterion()
        for q in YNQuestions:
            for stud in students:
                ans = survey.Answer(False)
                stud.set_answer(q, ans)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_criterion(crit, q)
        for q in survey_with_YN_question._ques:
            survey_with_YN_question.set_weight(0.5, q)
        assert pytest.approx(
            survey_with_YN_question.score_students(students)) == 0.5

    def test_score_studs(self, survey_with_NUMq, NumQ, student_odd_ans):
        assert survey_with_NUMq.set_criterion(criterion.HeterogeneousCriterion(), NumQ)
        assert survey_with_NUMq.set_weight(1, NumQ)
        assert survey_with_NUMq.score_students(student_odd_ans) == 0.0

    def test_score_grouping(self, survey_with_NUMq):
        grouping = grouper.Grouping()
        assert survey_with_NUMq.score_grouping(grouping) == 0.0

    def test_score_grouping2(self, survey_with_NUMq, student_odd_ans, NumQ):
        gr1 = grouper.Group([student_odd_ans[1], student_odd_ans[2]])
        gr2 = grouper.Group([student_odd_ans[0], student_odd_ans[3]])
        gr3 = grouper.Group([student_odd_ans[4]])
        grouping = grouper.Grouping()
        assert grouping.add_group(gr1)
        assert grouping.add_group(gr2)
        assert grouping.add_group(gr3)
        assert survey_with_NUMq.set_criterion(criterion.HeterogeneousCriterion(), NumQ)
        assert survey_with_NUMq.set_weight(0.5, NumQ)
        score_gr1 = survey_with_NUMq.score_students(gr1.get_members())
        score_gr2 = survey_with_NUMq.score_students(gr2.get_members())
        score_gr3 = survey_with_NUMq.score_students(gr3.get_members())
        avg = sum([score_gr1, score_gr2, score_gr3]) / 3
        assert survey_with_NUMq.score_grouping(grouping) == avg



class TestHomoCrit:

    def test_score_ans_YN(self, YNq, lst_of_YN_ans):
        assert pytest.approx(
            criterion.HomogeneousCriterion().score_answers(YNq, lst_of_YN_ans)) == 0.5

    def test_score_ans_YN_raise_error(self, YNq, lst_of_YN_ans):
        with pytest.raises(criterion.InvalidAnswerError):
            invalid_ans = survey.Answer(1)
            criterion.HomogeneousCriterion().score_answers(YNq, lst_of_YN_ans + [invalid_ans])

    def test_score_ans_check_box(self, Checkboxq2, Check_ans_lst):
        assert pytest.approx(criterion.HomogeneousCriterion().score_answers(
            Checkboxq2, Check_ans_lst)) == 7/36


class TestHeterogenousCriterious:
    def test_score_ans_YN(self, YNq, lst_of_YN_ans, hetero):
        assert pytest.approx(hetero.score_answers(YNq, lst_of_YN_ans)) == 0.5

    def test_score_ans(self, YNq, lst_of_YN_ans, hetero ):
         with pytest.raises(criterion.InvalidAnswerError):
             invalid_ans = survey.Answer(1)
             hetero.score_answers(YNq,
                                                            lst_of_YN_ans + [
                                                                invalid_ans])

    def test_score_ans_check_box(self, Checkboxq2, Check_ans_lst, hetero):
        assert pytest.approx(hetero.score_answers(
            Checkboxq2, Check_ans_lst)) ==  (1- 7 / 36)


class TestLonelyMemberCriterion:
    def test_lonely_score_ans_check_box(self, Checkboxq2, Check_ans_lst, lonely):
        assert lonely.score_answers(Checkboxq2, Check_ans_lst) == 0.0

    def test_lonely_score_ans_YN(self,YNq, lst_of_YN_ans, lonely):
        assert lonely.score_answers(YNq, lst_of_YN_ans) == 1.0

    def test_lonely_score_ans_YN_last_false(self,YNq, lst_of_YN_ans_last_false, lonely):
        assert lonely.score_answers(YNq, lst_of_YN_ans_last_false) == 0.0


class Testfunct:
    def test_slice(self):
        lst = list(range(10))
        assert slice_list(lst, 5) == [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
    def test_slice_empty(self):
        lst = []
        assert slice_list(lst, 0) == [[]]

    def test_windwos_empty(self):
        lst =[]
        assert windows(lst, 0) == [[]]

    def test_single_window(self):
        lst = [1]
        assert windows(lst, 1) == [[1]]


class TestGrouper:
    def test_init(self):
        group = grouper.Grouper(5)
        assert group.group_size == 5


class TestGroup:

    def test_init(self, group, students):
        assert group._members == students

    def test_len(self, group, students):
        assert len(group) == len(students)

    def test_contains(self, group, students):
        assert students[1] in group
        assert course.Student(100, "a") not in group

    def test_str(self, group, students):
        for stud in students:
            assert str(stud) in str(group)

    def test_get_members(self, group, students):
        assert group.get_members() == students
        assert group.get_members() is not group._members


class TestGrouping:
    def test_init(self, empty_grouping):
        assert empty_grouping._groups == []

    def test_len(self, empty_grouping):
        assert len(empty_grouping) == 0

    def test_str(self, empty_grouping):
        assert str(empty_grouping) == ""

    def test_len_longer_and_add_group(self, empty_grouping, group1):
        assert empty_grouping.add_group(group1)
        assert empty_grouping.add_group(group1) == False
        assert empty_grouping.add_group(grouper.Group([])) == False
        assert len(empty_grouping) == 1

    def test_get_groups(self, empty_grouping, group1, group2):
        lst = empty_grouping._groups
        assert empty_grouping.add_group(group1)
        assert empty_grouping.add_group(group2)
        assert empty_grouping.get_groups() == lst
        assert empty_grouping.get_groups() is not lst


class TestAlphaGrouper:
    def test_init(self, Alpha1):
        assert Alpha1.group_size == 1

    def test_make_grouping(self, alpha_grouping, course_with_students_with_answers, survey_, Alpha_size2):
        this = Alpha_size2.make_grouping(course_with_students_with_answers, survey_)
        assert len(this) == len(alpha_grouping)
        compare_groupings(this, alpha_grouping)

    def test_make_grouping_uneven(self, AlphaGrouping_odd_len, course_with_student_odd, survey_with_YN_question, Alpha_size2):
        this = Alpha_size2.make_grouping(course_with_student_odd, survey_with_YN_question)
        compare_groupings(this, AlphaGrouping_odd_len)


class TestRandomGrouper:
    def test_make_grouping(self, RandomGrouper1, survey_, students, course_with_students_with_answers):
        gr1 = grouper.Group([students[0], students[1]])
        gr2 = grouper.Group([students[2], students[3]])
        grouping = grouper.Grouping()
        grouping.add_group(gr1)
        grouping.add_group(gr2)
        assert len(grouping) == len(
            RandomGrouper1.make_grouping(course_with_students_with_answers, survey_))

    def test_make_grouping1(self, RandomGrouper1, survey_with_NUMq, student_odd_ans, course_with_student_odd):
        gr1 = grouper.Group([student_odd_ans[0], student_odd_ans[1]])
        gr2 = grouper.Group([student_odd_ans[2], student_odd_ans[3]])
        gr3 = grouper.Group([student_odd_ans[4]])
        grouping = grouper.Grouping()
        grouping.add_group(gr1)
        grouping.add_group(gr2)
        grouping.add_group(gr3)
        assert len(grouping) == len(RandomGrouper1.make_grouping(course_with_student_odd, survey_with_NUMq))


class TestWindowGrouper:
    def test_make_grouping(self, course_with_students_with_answers, survey_, WindowGrouper1, students):
        gr1 = grouper.Group([students[0], students[1]])
        gr2 = grouper.Group([students[2], students[3]])
        grouping = grouper.Grouping()
        assert grouping.add_group(gr1)
        assert grouping.add_group(gr2)
        funct = WindowGrouper1.make_grouping(course_with_students_with_answers, survey_)
        compare_groupings(grouping, funct)


class TestGreedyGrouper:
    def test_init(self, GreedyGrouper1):
        assert GreedyGrouper1.group_size == 2

    def test_make_grouping(self,student_odd_ans, course_with_student_odd, GreedyGrouper1, survey_with_NUMq, NumQ):
        survey_with_NUMq.set_weight(0.5, NumQ)
        survey_with_NUMq.set_criterion(criterion.HomogeneousCriterion(), NumQ)
        gr1 = grouper.Group([student_odd_ans[0], student_odd_ans[1]])
        gr2 = grouper.Group([student_odd_ans[2], student_odd_ans[3]])
        gr3 = grouper.Group([student_odd_ans[4]])
        grouping = grouper.Grouping()
        grouping.add_group(gr1)
        grouping.add_group(gr2)
        grouping.add_group(gr3)
        compare_groupings(grouping, GreedyGrouper1.make_grouping(course_with_student_odd, survey_with_NUMq))

    def test_make_grouping(self, student_odd_ans, course_with_student_odd,
                           GreedyGrouper2, survey_with_NUMq, NumQ):
        survey_with_NUMq.set_weight(0.5, NumQ)
        survey_with_NUMq.set_criterion(criterion.HomogeneousCriterion(), NumQ)
        gr1 = grouper.Group([student_odd_ans[0], student_odd_ans[1], student_odd_ans[2]])
        gr2 = grouper.Group([student_odd_ans[3], student_odd_ans[4]])
        grouping = grouper.Grouping()
        grouping.add_group(gr1)
        grouping.add_group(gr2)
        compare_groupings(grouping,
                          GreedyGrouper2.make_grouping(course_with_student_odd,
                                                       survey_with_NUMq))


if __name__ == '__main__':
    import pytest
    pytest.main(['prep6_sample_test.py'])
    pytest.main(['test_divider.py'])
