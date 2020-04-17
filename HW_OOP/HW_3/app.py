from .models import Recruiter
from .models import Programmer
from .models import Candidate as cand
from .models import Vacancy as v


def run():
    recruiter_1 = Recruiter.Recruiter("John", "Dow", "dow@mail.com", 88005553535, 32, 2)
    programmer_1 = Programmer.Programmer("Alex", "Johns", "Johns@mail.com", 78787454, 45, ["JS", "Ruby", "DB"], 13)
    programmer_2 = Programmer.Programmer("Jane", "Dow", "Jdow@mail.com", 1316131, 55, ["JS", "Ruby", "DB", "Angular",
                                                                                       "HTML"], 23)
    candidate_1 = cand.Candidate("Sam", "Winchester", "Sam$Dean@mail.com", 878784855, 15, ["html", "css", "JS"],
                                 ["mathematical skills", "communication skills", "writing skills"],
                                 {"mathematical skills": 5, "communication skills": 3, "writing skills": 5})
    candidate_2 = cand.Candidate("Dean", "Winchester", "Dean$Sam@mail.com", 878784856, 20, ["html", "css", "JS"],
                                 ["mathematical skills", "communication skills", "writing skills"],
                                 {"mathematical skills": 7, "communication skills": 8, "writing skills": 8})
    candidate_3 = cand.Candidate("Bobby", "Imlazytofindsecondname", "random@mail.com", 8787542, 10, ["html", "JS"],
                                 ["mathematical skills", "communication skills"],
                                 {"mathematical skills": 2, "communication skills": 3})
    vacancy_1 = v.Vacancy("Programmer", ["mathematical skills", "writing skills"], {"mathematical skills": 1,
                                                                                    "communication skills": 1})
    vacancy_2 = v.Vacancy("Recruiter", ["writing skills", "writing skills"], {"writing skills": 1,
                                                                              "communication skills": 2})


if __name__ == '__main__':
    run()
