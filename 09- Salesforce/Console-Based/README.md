# Employee Management System (Salesforce Console Based)

## Project Overview

This project is a simple console-based Employee Management System developed using Salesforce and Apex Programming Language.

The system manages employee records such as:

- Employee ID
- Employee Name
- Email
- Birth Date
- Department

The project uses a custom object in Salesforce and displays output using `System.debug()` in logs.

---

# Features

- Add Employee Records
- Store Employee Data in Salesforce
- Display Employee Records
- Console-Based Output
- Beginner-Friendly Apex Code

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Salesforce | Platform |
| Apex | Backend Programming |
| Custom Object | Database Storage |
| SOQL | Query Language |

---

# Step 1 — Create Salesforce Developer Account

Create a free Salesforce Developer account.

After login:

Go to:

Setup → Object Manager

---

# Step 2 — Create Custom Object

Create a custom object with the following details:

| Property | Value |
|----------|-------|
| Label | Employee |
| Plural Label | Employees |
| Object Name | Employee |

Click Save.

---

# Step 3 — Create Custom Fields

## 1. Employee ID Field

| Property | Value |
|----------|-------|
| Data Type | Number |
| Field Label | Emp ID |

---

## 2. Employee Name Field

| Property | Value |
|----------|-------|
| Data Type | Text |
| Field Label | Emp Name |

---

## 3. Email Field

| Property | Value |
|----------|-------|
| Data Type | Email |
| Field Label | Email |

---

## 4. Birth Date Field

| Property | Value |
|----------|-------|
| Data Type | Date |
| Field Label | Birth Date |

---

## 5. Department Field

| Property | Value |
|----------|-------|
| Data Type | Text |
| Field Label | Department |

---

# Step 4 — Create Apex Class

Go to:

Setup → Apex Classes → New

Paste the following code:

```java
public class EmployeeManagementSystem {

    public static void mainMethod() {

        // Create Employee Object
        Employee__c emp = new Employee__c();

        // Assign Values
        emp.Emp_ID__c = 101;

        emp.Emp_Name__c = 'Rahul';

        emp.Email__c = 'rahul@gmail.com';

        emp.Birth_Date__c = Date.newInstance(2000, 5, 10);

        emp.Department__c = 'IT';

        // Insert Record
        insert emp;

        System.debug('Employee Added Successfully');



        // Fetch Employee Records
        List<Employee__c> empList = [

            SELECT Emp_ID__c,
                   Emp_Name__c,
                   Email__c,
                   Birth_Date__c,
                   Department__c

            FROM Employee__c
        ];



        // Display Records
        for(Employee__c e : empList) {

            System.debug('Employee ID: ' + e.Emp_ID__c);

            System.debug('Employee Name: ' + e.Emp_Name__c);

            System.debug('Email: ' + e.Email__c);

            System.debug('Birth Date: ' + e.Birth_Date__c);

            System.debug('Department: ' + e.Department__c);

            System.debug('-------------------');
        }
    }
}
```

---

# Step 5 — Execute the Program

Open:

Developer Console

Go to:

Debug → Open Execute Anonymous Window

Paste:

```java
EmployeeManagementSystem.mainMethod();
```

Click:

Execute

---

# Step 6 — View Output

Go to the bottom panel:

Logs

Single click the latest log.

Open the:

Execution Log

Search for:

```text
USER_DEBUG
```

You will see output like:

```text
Employee Added Successfully

Employee ID: 101
Employee Name: Rahul
Email: rahul@gmail.com
Birth Date: 2000-05-10
Department: IT
```

---

# Working Flow

```text
Create Employee Object
        ↓
Assign Values
        ↓
Insert Record into Salesforce
        ↓
Fetch Employee Records
        ↓
Display Output in Logs
```

---

# Important Concepts

| Concept | Description |
|----------|-------------|
| Apex | Salesforce backend programming language |
| SOQL | Salesforce query language |
| System.debug() | Used to display output in logs |
| Custom Object | Database table in Salesforce |
| Fields | Columns inside object |

---

# Sample SOQL Query

```sql
SELECT Emp_Name__c FROM Employee__c
```

---

# Viva Questions

## What is Apex?

Apex is a backend programming language used in Salesforce.

---

## What is SOQL?

SOQL is Salesforce Object Query Language used to fetch records.

---

## What does `insert` do?

It stores records into Salesforce database.

Example:

```java
insert emp;
```

---

## What does `System.debug()` do?

It displays output in execution logs.

---

# Project Output

The system allows users to:

- Add Employee Records
- Store Employee Data
- Display Employee Details in Logs

---

# Conclusion

This project demonstrates a simple Employee Management System using Salesforce Apex.

It helps beginners understand:

- Custom Objects
- Apex Classes
- SOQL Queries
- Console-Based Execution
- Salesforce Logs