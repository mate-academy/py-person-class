class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    persons = [Person(people_item["name"], people_item["age"])
               for people_item in people_list]

    for people_item in people_list:

        if people_item.get("wife") and people_item.get("wife") is not None:
            Person.people.get(people_item["name"]).wife \
                = Person.people.get(people_item["wife"])

        elif people_item.get("husband") and \
                people_item.get("husband") is not None:
            Person.people.get(people_item["name"]).husband \
                = Person.people.get(people_item["husband"])

    return persons
