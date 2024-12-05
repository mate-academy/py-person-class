class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self

    @classmethod
    def get_instance(cls, name: str) -> str:
        return cls.people.get(name, None)


def create_person_list(people: list) -> list:
    result_list = []
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)

        if person_dict.get("wife"):
            wife = person_dict["wife"]
            person.wife = Person.get_instance(wife)
            if person.wife:
                person.wife.husband = person

        elif person_dict.get("husband"):
            husband = person_dict["husband"]
            person.husband = Person.get_instance(husband)
            if person.husband:
                person.husband.wife = person

        result_list.append(person)

    return result_list
