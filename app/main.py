class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for human_being in people:
        adding_person = Person(human_being["name"], human_being["age"])
        result_list.append(adding_person)

    print(f"Return list: {result_list}")

    for i in range(len(people)):

        ind_wife = people[i].get("wife")
        ind_husband = people[i].get("husband")

        if ind_wife is not None and (people[i]["wife"]) is not None:
            result_list[i].wife = Person.people[people[i]["wife"]]
        if ind_husband is not None and (people[i]["husband"]) is not None:
            result_list[i].husband = Person.people[people[i]["husband"]]

    return result_list
