class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list[dict]) -> list[Person]:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people_data]

    for person_dict in people_data:
        person_instance = Person.people[person_dict["name"]]

        spouse_name = person_dict.get("wife") or person_dict.get("husband")

        spouse_instance = spouse_name and Person.people.get(spouse_name)

        if spouse_instance:
            if person_dict.get("wife"):
                person_instance.wife = spouse_instance
            elif person_dict.get("husband"):
                person_instance.husband = spouse_instance

    return person_list
