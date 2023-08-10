class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.status = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person_data["name"],
                          person_data["age"]) for person_data in people]

    for person_data in people:
        name = person_data["name"]
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            person_instance = Person.people.get(name)
            spouse_instance = Person.people.get(spouse_name)

            if person_instance and spouse_instance:
                person_instance.wife = spouse_instance
                spouse_instance.husband = person_instance

    return result_list
