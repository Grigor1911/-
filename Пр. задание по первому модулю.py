grades_ = [[5, 3, 3, 5, 4], [2, 2, 2, 3,], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_ = {"Johnny", "Bilbo", "Steve", "Khendrik", "Aaron"}
average_grade_ = (sum(grades_[0]) / len(grades_[0]),
                 sum(grades_[1]) / len(grades_[1]),
                 sum(grades_[2]) / len(grades_[2]),
                 sum(grades_[3]) / len(grades_[3]),
                 sum(grades_[4]) / len(grades_[4]))
teachers_journal_ = dict(zip(sorted(students_),average_grade_))
print(teachers_journal_)