class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Шаг 1: создаём все экземпляры Person
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        Person(name, age)

    # Шаг 2: устанавливаем отношения wife/husband
    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            partner_name = person_dict["wife"]
            person.wife = Person.people[partner_name]

        elif person_dict.get("husband") is not None:
            partner_name = person_dict["husband"]
            person.husband = Person.people[partner_name]

    # Возвращаем список объектов Person в том же порядке
    return [Person.people[p["name"]] for p in people]
