from .Employee import Employee


class Recruiter(Employee):
    """
    This class can create   new Recruiter
    """

    def __init__(self, name, sec_name, email, p_numb, salary, hired_this_month=0):
        self.hired_this_month = hired_this_month
        super().__init__(name, sec_name, email, p_numb, salary)

    def work(self):
        """
        This method can start work process
        :return: string
        """
        work_str = super().work()[:-1]
        return work_str + "and start hiring"

    def hire_people(self):
        """
        This method can increase amount of hired people
        :return: string
        """
        self.hired_this_month += 1
        return "Congratulation you hire a new employee"

    @property
    def hired_in_this_month(self):
        """
        This method show amount of hired people
        :return: integer
        """
        return self.hired_this_month
