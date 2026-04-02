class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = [Person(item["name"], item["age"]) for item in people]
    people_dict = {person.name: person for person in result}

    for item in range(len(result)):
        if "wife" in people[item] and people[item].get("wife") is not None:
            result[item].wife = people_dict[people[item]["wife"]]
            people_dict[people[item]["wife"]].husband = result[item]
        elif ("husband" in people[item]
              and people[item].get("husband") is not None):
            result[item].husband = people_dict[people[item]["husband"]]
            people_dict[people[item]["husband"]].wife = result[item]

    return result
