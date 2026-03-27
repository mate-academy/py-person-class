class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(item["name"], item["age"]) for item in people]
    people_dict = {person.name: person for person in result}

    for i in range(len(result)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            result[i].wife = people_dict[people[i]["wife"]]
            people_dict[people[i]["wife"]].husband = result[i]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            result[i].husband = people_dict[people[i]["husband"]]
            people_dict[people[i]["husband"]].wife = result[i]

    return result
