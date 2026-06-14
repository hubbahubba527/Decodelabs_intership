# ================================
# Project 1 — To Do List
# Intern: Hubba
# Company: Decode Labs Internship
# Date: June 2026
# Description: A console-based to-do
# list app to add, view and delete
# daily tasks using Python
# ================================
my_tasks = []
for i in range(1,3):
 task = input("Enter your task here")
 my_tasks.append(task)
for i,task in enumerate(my_tasks , start =0):
 print( i ,task)
