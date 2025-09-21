# Базовый класс
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет."


# Производный класс (наследуется от Person)
class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)  # вызываем конструктор базового класса
        self.university = university

    def introduce(self):
        # переопределяем метод базового класса
        return f"Я студент {self.university}. Меня зовут {self.name}, мне {self.age} лет."

    def study(self):
        return f"{self.name} учится в {self.university}."


# Тестовая программа
if __name__ == "__main__":
    person = Person("Анна", 30)
    student = Student("Иван", 20, "МГУ")

    print(person.introduce())   # метод базового класса
    print(student.introduce())  # переопределённый метод
    print(student.study())      # метод производного класса
