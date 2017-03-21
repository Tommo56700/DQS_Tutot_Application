class Student:
	def __init__(self, studentId, course, fName, sName, Tutor, acadYear, uniEmail): #create student
		self.studentId = studentId
		self.course = course
		self.fName = fName
		self.sName = sName
		self.Tutor = Tutor
		self.acadYear = acadYear
		self.uniEmail = uniEmail
		
	def output(self): #print outputs for debug
		print(self.studentId)
		print(self.course)
		print(self.fName)
		print(self.sName)
		print(self.Tutor.fName + " " + self.Tutor.sName)
		print(self.acadYear)
		print(self.uniEmail)
		
	def deleteStudent(self): #deletion of student from tutor database
		self.Tutor.Students.remove(self)
		
	def getId(self): #retrieval functions
		return(self.studentId)
	def getCourse(self):
		return(self.course)
	def getFName(self):
		return(self.fName)
	def getSName(self):
		return(self.sName)
	def getTutor(self):
		return(self.Tutor)
	def getAcadYear(self):
		return(self.acadYear)
	def getEmail(self):
		return(self.uniEmail)
	def getFullName(self):
		return(self.fName + " " + self.sName)
		
class Tutor:
	def __init__(self, staffId, course, fName, sName, uniEmail, admin, studentNum):#create Tutor
		self.staffId = staffId
		self.course = course
		self.fName = fName
		self.sName = sName
		self.Students = []
		self.uniEmail = uniEmail
		self.admin = admin
		self.studentNum = studentNum
	
	def displayStudents(self): #debug print of students
		for student in self.Students:
			print(student.fName + " " + student.sName)
		
	def output(self): #print outputs for debug
		print(self.staffId)
		print(self.course)
		print(self.fName)
		print(self.sName)
		print(self.uniEmail)
		print(self.admin)
		print(self.studentNum)
		self.displayStudents()
		
	def addStudent(self, Student): #Add a student to the Students list if not full
		if(len(self.Students) >= self.studentNum):
			ValueError
		else:
			self.Students.append(Student)
			
	def listStudentNames(self): #return the list of students (names only)
		studentList = []
	
		for student in self.Students:
			studentList.append(student.fName + " " + student.sName)
		
		return(studentList)
	
	def getId(self): #retrieval functions
		return(self.staffId)
	def getCourse(self):
		return(self.course)
	def getFName(self):
		return(self.fName)
	def getSName(self):
		return(self.sName)
	def getStudentNum(self):
		return(self.studentNum)
	def getAdmin(self):
		return(self.admin)
	def getEmail(self):
		return(self.uniEmail)
	def getStudents(self):
		return(self.Students)
	def getFullName(self):
		return(self.fName + " " + self.sName)

#--Debug Outputs--
#testTutor = Tutor(12, "CM101", "Hailey", "Smiths", "hsmiths@uni.co.uk", True, 10)
#testStudent = Student(1, "CM101", "Fred", "Jones", testTutor, "2014/15", "fjones@uni.co.uk")

#testTutor.addStudent(testStudent)

#print("Test Student: ")
#testStudent.output()
#print("")
#print("Test Tutor: ")
#testTutor.output()
