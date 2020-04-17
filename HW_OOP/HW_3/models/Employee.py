from datetime import date


class Employee:
    """
    This is main class for all another classes in this python package
    """
    def __init__(self, name, sec_name, email, p_numb, salary):
        self.name = name
        self.sec_name = sec_name
        self.email = email
        self.p_numb = p_numb
        self.salary = salary

    def work(self):
        """
        This method can start the work process
        :return: string
        """
        return "I come to the office."

    def check_salary(self):
        """
        This method can show you the salary for current day
        :return: integer
        """

        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [19, 20, 26, 27]
        diff = (now - month_start).days + 1
        pay_salary = diff - len(weekend)
        return pay_salary * self.salary

    def __str__(self):
        """
        This method return class name and full name of employee
        :return: string
        """
        return f"{self.__class__.__name__}: {self.name} {self.sec_name}"

    # With methods below we can compare salary
    def __lt__(self, other):
        print('LT')
        return self.salary < other.salary

    def __gt__(self, other):
        print('GT')
        return self.salary > other.salary

    def __eq__(self, other):
        print('EQ')
        return self.salary == other.salary

    def __le__(self, other):
        print('LE')
        return self.salary <= other.salary

    def __ge__(self, other):
        print('GE')
        return self.salary >= other.salary

    def __ne__(self, other):
        print('NE')
        return self.salary != other.salary
