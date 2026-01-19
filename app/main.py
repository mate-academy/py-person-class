class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(p["name"], p["age"]) for p in people]

    for i in range(len(people)):
        data = people[i]
        obj = result[i]

        for key in ["wife", "husband"]:
            partner_name = data.get(key)
            if partner_name:
                partner_obj = Person.people[partner_name]
                setattr(obj, key, partner_obj)

    return result
