import os, math
grade_a = 0
grade_b = 0
grade_c = 0

def request_grades():
    global grade_a, grade_b, grade_c

    grade_a = int(input('Type the grade of the first assesment: '))
    grade_b = int(input('Type the grade of the first assesment: '))
    grade_c = int(input('Type the grade of the first assesment: '))

def calculate_average(grade_a,grade_b,grade_c):
    try:
        grades_tuple = (grade_a,grade_b,grade_c)
        return int(sum(grades_tuple) / len(grades_tuple))
    except Exception as e:
        print(f'An error occurred {e}')

def define_student_situation(grade):
    try:
        if(grade < 5):
            print(f'The final grade is {grade}, the student had failed in classes.')
        elif(5 <= grade <= 7):
            print(f'The final grade is {grade}, the student is in remedial classes.')
        else:
            print('The student is approved.')
    except Exception as e:
        print(f'An error occurred {e}')

def main():
    os.system('cls')
    request_grades()
    define_student_situation(calculate_average(grade_a,grade_b,grade_c))

if __name__ == '__main__':
    main()