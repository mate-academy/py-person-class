class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_people = [Person(p.get("name"), p.get("age")) for p in people]
    for i in range(len(new_people)):
        one_dict = people[i]
        p_obj = new_people[i]
        if one_dict.get("wife"):
            wife_name = one_dict.get("wife")
            p_obj.wife = Person.people[wife_name]

        if one_dict.get("husband"):
            husband_name = one_dict.get("husband")
            p_obj.husband = Person.people[husband_name]
    return new_people
