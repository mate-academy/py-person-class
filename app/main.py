class Person:
    people = {}

    def __init__(self, name: str, age: int, ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    add_family = {}
    result = []

    for man in people:
        name, age = man["name"], man["age"]
        result.append(Person(name, age))
        add_family[name] = man.popitem()

    for man in people:
        name = man["name"]
        sex, pair_name = add_family[name]
        found_person = Person.people.get(name)
        pair = Person.people.get(pair_name)

        if pair_name:
            if sex == "wife":
                found_person.wife = pair
            else:
                found_person.husband = pair
        else:
            found_person.husband = None

    return result
