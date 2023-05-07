# Reading files ex 1
lang = open("programming.txt")
contents = lang.read()
print('Contents of programming.txt:\n')
print(contents)
lang.close()

# Reading files ex 2
lang = open("programming.txt")
lines = lang.readlines()
print('Contents of the first line: ', lines[0])
print('Contents of the first line: ', lines[1])
print('Contents of the first line: ', lines[2])
print('Contents of the first line: ', lines[3])
print('Contents of the first line: ', lines[2])
print('Contents of the first line: ', lines[1])
print('Contents of the first line: ', lines[0])


# Reading files ex 3
grades = open("grades.txt")

total = 0
count = 0

for line in grades:
    total += float(line)
    count += 1
avg = total / count
print('Average grade is: ', avg)

grades.close()


# Reading files ex 4
grades = open("grades.txt")
lines = grades.readlines()
grades.close()
print(lines[0])

total = 0
for g in lines:
    total += float(g)
avg = total / len(lines)

print('Average grade is: ', avg)

# write example ex 5
statistics = open("statistics.txt", "w")
statistics.write('Average: ' + str(avg))
print('Average grade written into statistics.txt!')
statistics.close()


# example with keyword ex 6
with open("grades.txt", "r+") as f:
    pass

# CSV ex 7
import csv
with open("studentgrades.csv", "r") as csvfile:
    grades = csv.reader(csvfile, delimiter=",")



# CSV ex 8

grades_new = [["name", "attendance", "homework","quiz","midterm","final","total"],
              ["Alic", "20","35","8","14","20","97.0"],
              ["Brad", "18","37","7","13","23","98.0"],
              ["Cathy","19","36","8","12","24","99.0"]]
with open("grades_total.csv", "w", newline="") as csvfile:

