class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result_list = [Person(people_it["name"],
                          people_it["age"])
                   for people_it in people]
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        spouse_name = person_dict.get("wife")
        if spouse_name:
            person.wife = Person.people[person_dict["wife"]]
        spouse_name = person_dict.get("husband")
        if spouse_name:
            person.husband = Person.people[person_dict["husband"]]
    return result_list
