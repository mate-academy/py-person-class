class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_info in people:
        new_person = Person(person_info["name"], person_info["age"])
        person_list.append(new_person)

        spouse_name = person_info.get("wife") or person_info.get("husband")
        if spouse_name:
            spouse_instance = Person.people.get(spouse_name)
            if spouse_instance:
                if "wife" in person_info:
                    new_person.wife = spouse_instance
                    spouse_instance.husband = new_person
                elif "husband" in person_info:
                    new_person.husband = spouse_instance
                    spouse_instance.wife = new_person
    return person_list
