project_time = {'A':0,'B':0,'C':0}

def request_project_time():
    global project_time
    for project in project_time:
        project_time[project] = int(input(f'Report the number of days to complete the project {project}: '))
def validate_project_time():
    for project in project_time:
        if (project_time[project] < 0):
            print('The number of days can not be negative')
def main():
    request_project_time()
    validate_project_time()

if __name__ == '__main__':
    main()