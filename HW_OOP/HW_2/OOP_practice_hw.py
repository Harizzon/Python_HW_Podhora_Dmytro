class Employee:

    def __init__(self, name, sec_name, email, p_numb, salary):
        self.name = name
        self.sec_name = sec_name
        self.email = email
        self.p_numb = p_numb
        self.salary = salary

    def work(self):
        return "I come to the office."

    def check_salary(self):
        from datetime import date

        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [19, 20, 26, 27]
        diff = (now - month_start).days + 1
        pay_salary = diff - len(weekend)
        return pay_salary * self.salary

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} {self.sec_name}"

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


class Recruiter(Employee):

    def __init__(self, name, sec_name, email, p_numb, salary, hired_this_month=0):
        self.hired_this_month = hired_this_month
        super().__init__(name, sec_name, email, p_numb, salary)

    def work(self):
        work_str = super().work()[:-1]
        return work_str + "and start hiring"

    def hire_people(self):
        self.hired_this_month += 1
        return "Congratulation you hire a new employee"

    @property
    def hired_in_this_month(self):
        return self.hired_this_month


class Programmer(Employee):
    def __init__(self, name, sec_name, email, p_numb, salary, tech_stack, closed_this_month=0):
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month
        super().__init__(name, sec_name, email, p_numb, salary)

    def work(self):
        work_str = super().work()[:-1]
        return work_str + "and start coding"

    def close_task(self):
        self.closed_this_month += 1
        return "You've closed task. Finally"

    def check_done_tasks(self):
        return self.closed_this_month

    def add_new_tech(self, tech):
        self.tech_stack.append(tech)
        return "You've added new tech"

    @property
    def show_tech_list(self):
        return self.tech_stack

    def __add__(self, other):
        self.tech_stack += other.tech_stack
        self.closed_this_month += other.closed_this_month
        return set(self.tech_stack), self.closed_this_month

    ##################################
    # In this block located the compare between the programmers
    def __lt__(self, other):
        print('LT')
        return len(self.tech_stack) < len(other.tech_stack)

    def __gt__(self, other):
        print('GT')
        return len(self.tech_stack) > len(other.tech_stack)

    def __eq__(self, other):
        print('EQ')
        return len(self.tech_stack) == len(other.tech_stack)

    def __le__(self, other):
        print('LE')
        return len(self.tech_stack) <= len(other.tech_stack)

    def __ge__(self, other):
        print('GE')
        return len(self.tech_stack) >= len(other.tech_stack)

    def __ne__(self, other):
        print('NE')
        return len(self.salary) != len(other.salary)


def run():
    x = Employee("Ivan", "Ivanov", "Ivan@mail.com", 88005553535, 25)
    y = Recruiter("Petya", "Vasilyev", "vasil@mail.com", 99899452, 13)
    prog1 = Programmer("Bob", 'Sanders', "Sanders@com", 8787445, 45, ['java', 'css', "oracle", 'Html'], 6)
    prog2 = Programmer("Sam", "O'niel", "QWERT@com", 785455, 55, ['java', 'css', "oracle", 'Html', "Ruby"], 8)
    print(prog1 < prog2)
    print(prog1 == prog2)
    print(prog1 + prog2)
    print(prog1.check_salary())

if __name__ == '__main__':
    run()
