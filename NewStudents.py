from Classes import *

Students = []
Tutors = []

def csv_import(filename1, filename2, header=True):
	import csv
	global Students
	global Tutors

	with open(filename1) as csvfile:
			rdr = csv.reader(csvfile)
			next(csvfile)
			for row in rdr:
				Students.append(Student(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	with open(filename2) as csvfile:
			rdr = csv.reader(csvfile)
			next(csvfile)
			for row in rdr:
				Tutors.append(Tutor(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

	assign_students(Students, Tutors)

def assign_students(students, tutors):
	for tutor in Tutors:
		for student in students:
			if student.getCourse() == tutor.getCourse():
				tutor.addStudent(student)
				break