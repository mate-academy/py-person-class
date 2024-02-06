class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self

    @classmethod
    def get_person(cls, name: str) -> str:
        return cls.people.get(name)

    def set_wife(self, spouse: "Person") -> None:
        if isinstance(spouse, Person):
            self.wife = spouse

    def set_husband(self, spouse: "Person") -> None:
        if isinstance(spouse, Person):
            self.husband = spouse

    def remove_spouse(self) -> None:
        if hasattr(self, "wife"):
            del self.wife
        if hasattr(self, "husband"):
            del self.husband


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
        person_list.append(person)

    for person_data in people:
        person = Person.get_person(person_data["name"])
        spouse_name = person_data.get("wife") or person_data.get("husband")
        if spouse_name:
            spouse = Person.get_person(spouse_name)
            if spouse:
                if "wife" in person_data:
                    person.set_wife(spouse)
                else:
                    person.set_husband(spouse)

    return person_list
