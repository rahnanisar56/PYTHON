students_python= {"Arya","Ardra","Akash"}
students_datascience= {"Akash","Rahna","Soorya"}
students_python.add("Athul")
students_datascience.remove("Rahna")
print(students_python & students_datascience)
print(students_python - students_datascience)
print(students_python.union(students_datascience))
students_course= {
    "Python":len(students_python),
    "Data Science":len(students_datascience)
}
print(students_course)
for course,count in 