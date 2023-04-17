class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for persons in people:
        names = Person(persons.get("name"), persons.get("age"))
        for relation in persons:
            if relation == "wife":
                names.wife = persons.get("husband")
                # Person.people[persons.get("wife")]
            if relation == "husband":
                names.husband = persons.get("husband")
        print(names.__dict__)
        result_list.append(names)

    return result_list


people = [
        {"name": "Ross", "age": 30, "wife": "Rachel"},
        {"name": "Joey", "age": 29, "wife": None},
        {"name": "Phoebe", "age": 31, "husband": None},
        {"name": "Chandler", "age": 30, "wife": "Monica"},
        {"name": "Monica", "age": 32, "husband": "Chandler"},
        {"name": "Rachel", "age": 28, "husband": "Ross"},
    ]

create_person_list(people)