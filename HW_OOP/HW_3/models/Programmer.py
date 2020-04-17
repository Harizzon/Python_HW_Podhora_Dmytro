from .Employee import Employee


class Programmer(Employee):

    def __init__(self, name, sec_name, email, p_numb, salary, tech_stack, closed_this_month=0):
        self.tech_stack = tech_stack
        self.closed_this_month = closed_this_month
        super().__init__(name, sec_name, email, p_numb, salary)

    def work(self):
        """
        This method start work process
        :return: String
        """
        work_str = super().work()[:-1]
        return work_str + "and start coding"

    def close_task(self):
        """
        This method increase amount of closed tasks
        :return: string
        """
        self.closed_this_month += 1
        return "You've closed task. Finally"

    def check_done_tasks(self):
        """
        This method show amount of closed tasks
        :return: Integer
        """
        return self.closed_this_month

    def add_new_tech(self, tech):
        """
        This method adding new tech in list of tech
        :param tech: string
        :return: string
        """
        self.tech_stack.append(tech)
        return "You've added new tech"

    @property
    def show_tech_list(self):
        """
        This method show all tech list
        :return: list
        """
        return self.tech_stack

    def __add__(self, other):
        """
        This method create new ALFA programmer
        :param other: class Programmer
        :return: set and integer
        """
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