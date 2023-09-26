class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    result = [Person(human["name"], human["age"]) for human in people]

    for result_index, human in enumerate(people):
    
        wife_name = human.get("wife")
        if wife_name is not None:
            result[result_index].wife = Person.people.get(wife_name)
    
        husband_name = human.get("husband")
        if husband_name is not None:
            result[result_index].husband = Person.people.get(husband_name)


    return result
