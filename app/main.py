class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for i in range(len(people)):
        data = people[i]
        obj = result[i]

        for key in ["wife", "husband"]:
            if key in data and data[key] is not None:
                partner_name = data[key]
                setattr(obj, key, Person.people[partner_name])
    return result
