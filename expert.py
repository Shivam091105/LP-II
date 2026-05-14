import random

knowledge_base = {
    "login_issue": {
        "problem": "Login Issue",
        "solution": "Reset your password or check your username and password.",
        "priority": "Low"
    },
    "internet_issue": {
        "problem": "Internet Issue",
        "solution": "Restart the router and check network cable or Wi-Fi connection.",
        "priority": "High"
    },
    "printer_issue": {
        "problem": "Printer Issue",
        "solution": "Check printer power, paper tray, ink level, and printer drivers.",
        "priority": "Medium"
    },
    "software_issue": {
        "problem": "Software Issue",
        "solution": "Restart the application or reinstall the software.",
        "priority": "Medium"
    },
    "hardware_issue": {
        "problem": "Hardware Issue",
        "solution": "Check cables, keyboard, mouse, or contact hardware support.",
        "priority": "High"
    },
    "email_issue": {
        "problem": "Email Issue",
        "solution": "Check email credentials, internet connection, and mail server settings.",
        "priority": "High"
    }
}


def ask_question(question):
    answer = input(question + " (y/n): ").lower().strip()
    return answer == "y"


def diagnose_login_issue():
    return ask_question("Are you unable to login?") or ask_question("Did you forget your password?")


def diagnose_internet_issue():
    return ask_question("Is your internet not working?") or ask_question("Is Wi-Fi disconnected?")


def diagnose_printer_issue():
    return ask_question("Is the printer not printing?") or ask_question("Is the printer showing an error?")


def diagnose_software_issue():
    return ask_question("Is any software not opening?") or ask_question("Is the application crashing?")


def diagnose_hardware_issue():
    return ask_question("Is your keyboard or mouse not working?") or ask_question("Is there a hardware connection issue?")


def diagnose_email_issue():
    return ask_question("Are you unable to send or receive emails?") or ask_question("Are you unable to login to email?")


def display_solution(issue_key):
    ticket_id = random.randint(1000, 9999)
    issue = knowledge_base[issue_key]

    print("\n----- Support Ticket Generated -----")
    print("Ticket ID: HD", ticket_id)
    print("Problem Detected:", issue["problem"])
    print("Priority Level:", issue["priority"])
    print("Recommended Solution:", issue["solution"])

    if issue["priority"] == "High":
        print("Escalation: Please contact technical support immediately.")
    else:
        print("Escalation: Try the solution first. Contact support if problem continues.")


print("===== Help Desk Expert System =====")
print("Answer the following questions with y or n\n")

found = False

if diagnose_login_issue():
    display_solution("login_issue")
    found = True

if diagnose_internet_issue():
    display_solution("internet_issue")
    found = True

if diagnose_printer_issue():
    display_solution("printer_issue")
    found = True

if diagnose_software_issue():
    display_solution("software_issue")
    found = True

if diagnose_hardware_issue():
    display_solution("hardware_issue")
    found = True

if diagnose_email_issue():
    display_solution("email_issue")
    found = True

if not found:
    print("\nNo exact issue found in knowledge base.")
    print("Ticket ID: HD", random.randint(1000, 9999))
    print("Priority Level: Medium")
    print("Please contact technical support.")