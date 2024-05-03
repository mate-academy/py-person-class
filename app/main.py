class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: str) -> None:
    person_list = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            spouse = Person.people.get(spouse_name)
            if spouse:
                if "wife" in person_data:
                    person.wife = spouse
                    spouse.husband = person
                elif "husband" in person_data:
                    person.husband = spouse
                    spouse.wife = person
        person_list.append(person)
    return person_list
