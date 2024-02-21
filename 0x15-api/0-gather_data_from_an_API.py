#!/usr/bin/python3
'''
This script gathers employee data from API
'''

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    # This checks if an employee is provided
    if len(sys.argv) > 1:
        # This validates the provided argument as a +pos integer
        if re.fullmatch(r'\d+', sys.argv[1]):
            # This convert the employee ID to an integer
            id = int(sys.argv[1])

            # This Fecth the user details and name
            reqs = requests.get('{}/users/{}'.format(REST_API, id)).json()
            
            #This fetch all the task in the todo list
            task_reqs = requests.get('{}/todos'.format(REST_API)).json()
            
            # This extract the employees name
            emp_name = reqs.get('name')
            
            # This filters tasks for the specified employee
            tasks = [task for task in task_reqs if task.get('userId') == id]
            #tasks = list(filter(lambda x: x.get('userId') == id, task_reqs))
            
            # This shows and filter out the employee completed tasks
            completed_tasks = [task for task in tasks if task.get('completed')]
            #completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            
            # This display the employee todo list
            print(
                'Employee {} is done with tasks({}/{}):'.format(
                    emp_name,
                    len(completed_tasks),
                    len(tasks)
                )
            )

            # This displays titles of the completed tasks
            if len(completed_tasks) > 0:
                for task in completed_tasks:
                    print('\t {}'.format(task.get('title')))