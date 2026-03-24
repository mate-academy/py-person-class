class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for i in people:
        obj = Person(i["name"], i["age"])
        if "wife" in i and i["wife"] is not None:
            if i["wife"] in Person.people:
                obj.wife = Person.people[i["wife"]]
                obj.wife.husband = obj
        elif "husband" in i and i["husband"] is not None:
            if i["husband"] in Person.people:
                obj.husband = Person.people[i["husband"]]
                obj.husband.wife = obj
        result.append(obj)

    return result
