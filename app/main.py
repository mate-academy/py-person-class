class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, spouse_name: str, gender: str) -> None:
        spouse = Person.people.get(spouse_name)

        if gender == "male" and spouse:
            self.husband = spouse
            spouse.wife = self
        elif gender == "female" and spouse:
            self.wife = spouse
            spouse.husband = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        # Create a new Person instance
        person = Person(name, age)

        # Determine the spouse and gender
        spouse_name = (
                person_data.get("wife") or person_data.get("husband")
        )

        gender = "male" if "husband" in person_data else "female"
        if spouse_name:
            person.set_spouse(
                spouse_name,
                gender
            )

        person_list.append(person)

    return person_list
