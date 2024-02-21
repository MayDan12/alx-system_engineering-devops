#!/usr/bin/python3
"""
 This python script a rest api for a given emplyee ID, and returns his informations
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
  """
  This retrieve and display employee todo list progress.
  :param employee_id: Representing Integer
  """
  api_endpoint = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

  try:
    # This fetch todo list for the given employee ID
    res = requests.get(api_endpoint)
    res.raise_for_status()

    todo_lists = res.json()

    # this checks if there is todolist
    if not todo_lists:
      print(f"No TODO lists found for employee {employee_id}")
      return

    # This extract employee name
    employee_name = todo_lists[0].get('userId')

    #completed count and total tasks
    complete_task = sum(task.get('completed', False) for task in todo_lists)
    task_total = len(todo_lists)

    # This displays employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({complete_task}/{task_total}):")

    #display titles of completed tasks
    for task in todo_lists:
      if task.get('completed', False):
        print(f"\t{task['title']}")

  except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    sys.exit(1)

if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

  try:
    employee_id = int(sys.argv[1])
  
  except ValueError:
    print("Error: Employee ID must be an integer.")
    sys.exit(1)
  
  get_employee_todo_progress(employee_id)