class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(each_people["name"], each_people["age"])
        for each_people in people
    ]
    len_list_people = len(people)
    for i in range(len_list_people):
        if "wife" in people[i] and people[i]["wife"] is not None:
            Person.people[people[i]["name"]].wife =\
                Person.people[people[i]["wife"]]
            Person.people[people[i]["name"]].wife.husband =\
                Person.people[people[i]["name"]]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            Person.people[people[i]["name"]].husband =\
                Person.people[people[i]["husband"]]
            Person.people[people[i]["name"]].husband.wife =\
                Person.people[people[i]["name"]]
    return person_list
