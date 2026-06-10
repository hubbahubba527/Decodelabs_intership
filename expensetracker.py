# ================================
# Project 2 — Expense Tracker
# Intern: Hubba
# Company: Decode Labs Internship
# Date: June 2026
# Description: A console-based expense
# tracker to record and summarize
# daily expenses using Python
# ================================
expenses = []
total=0
for i in range (1,6):
    expense = int(input("enter a num :"))
    expenses.append(expense)
    total += expense
print("TOTAL EXPENSE ARE:",total)
