class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for p_dict in people:
        Person(p_dict["name"], p_dict["age"])
    result = []
    for p_dict in people:
        current_person = Person.people[p_dict["name"]]
        spouse_key = "wife" if "wife" in p_dict else "husband"
        spouse_name = p_dict.get(spouse_key)
        if spouse_name:
            setattr(current_person, spouse_key, Person.people[spouse_name])

        result.append(current_person)
    return result
