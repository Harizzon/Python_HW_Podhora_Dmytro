from .Employee import Employee


class Candidate(Employee):
    """
    This class create a candidate
    """

    def __init__(self, name, sec_name, email, p_numb, salary, technologies, main_skill, main_skill_grade):
        super().__init__(name, sec_name, email, p_numb, salary)
        self.main_skill_grade = main_skill_grade
        self.technologies = technologies
        self.main_skill = main_skill

