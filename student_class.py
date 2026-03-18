class Student:
    def __init__(self, name, num_scores):
        self.name = name
        self.test_scores = [0] * num_scores

    def getName(self):
        return self.name

    def getScore(self, position):
        if 1 <= position <= len(self.test_scores):
            return self.test_scores[position - 1]
        else:
            raise IndexError("Score position out of range.")

    def setScore(self, position, value):
        if 1 <= position <= len(self.test_scores):
            self.test_scores[position - 1] = value
        else:
            raise IndexError("Score position out of range.")

    def getHighestScore(self):
        if not self.test_scores:
            return 0
        return max(self.test_scores)

    def getAverageScore(self):
        if not self.test_scores:
            return 0
        return sum(self.test_scores) / len(self.test_scores)

    def __str__(self):
        return f"Student: {self.name} | Scores: {self.test_scores} | Average: {self.getAverageScore():.2f}"

student1 = Student("Alice", 3)

print(student1)

student1.setScore(1, 85)
student1.setScore(2, 92)
student1.setScore(3, 88)

print(f"Name: {student1.getName()}")
print(f"Score on test 2: {student1.getScore(2)}")
print(f"Highest Score: {student1.getHighestScore()}")
print(f"Average Score: {student1.getAverageScore()}")

print(student1)
