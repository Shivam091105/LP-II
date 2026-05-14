# Student Record Management System (Salesforce)

## Project Overview

This project is a simple Student Record Management System developed using Salesforce, Apex Programming Language, and Visualforce Page.

The application stores and manages student records using a custom object.

---

# Features

- Add Student Records
- Store Data in Salesforce
- Display Student List
- Simple and Beginner-Friendly UI

---

# Technologies Used

| Technology | Purpose |
|------------|----------|
| Salesforce | Platform |
| Apex | Backend Logic |
| Visualforce | Frontend UI |
| Custom Object | Database Storage |

---

# Student Details Stored

The system stores:

- Student Name
- Roll Number
- Class
- Mobile Number

---

# Step 1 — Create Salesforce Developer Account

Open the Salesforce Developer signup page and create a free account.

After login:

Setup → Object Manager

---

# Step 2 — Create Custom Object

Create a custom object with the following details:

| Property | Value |
|----------|-------|
| Label | Student |
| Plural Label | Students |
| Object Name | Student |

Click Save.

---

# Step 3 — Create Custom Fields

## 1. Roll Number Field

| Property | Value |
|----------|-------|
| Data Type | Number |
| Field Label | Roll No |
| Length | 5 |

---

## 2. Class Field

| Property | Value |
|----------|-------|
| Data Type | Text |
| Field Label | Class |
| Length | 20 |

---

## 3. Mobile Number Field

| Property | Value |
|----------|-------|
| Data Type | Phone |
| Field Label | Mobile No |

---

# Step 4 — Create Apex Controller

Go to:

Setup → Apex Classes → New

Paste the following code:

```java
public class StudentController {

    public Student__c stu {get; set;}

    public List<Student__c> stuList {get; set;}

    // Constructor
    public StudentController() {

        stu = new Student__c();

        stuList = [
            SELECT Name, Roll_No__c, Class__c, Mobile_No__c
            FROM Student__c
        ];
    }

    // Save Student
    public void saveStudent() {

        insert stu;

        // Clear form
        stu = new Student__c();

        // Refresh list
        stuList = [
            SELECT Name, Roll_No__c, Class__c, Mobile_No__c
            FROM Student__c
        ];
    }
}
```

---

# Step 5 — Create Visualforce Page

Go to:

Setup → Visualforce Pages → New

Page Name:

StudentPage

Paste the following code:

```html
<apex:page controller="StudentController">

    <apex:form>

        <h1>Student Record Management</h1>

        <apex:pageBlock title="Add Student">

            <apex:pageBlockSection columns="1">

                <apex:inputField value="{!stu.Name}" />

                <apex:inputField value="{!stu.Roll_No__c}" />

                <apex:inputField value="{!stu.Class__c}" />

                <apex:inputField value="{!stu.Mobile_No__c}" />

            </apex:pageBlockSection>

            <apex:commandButton value="Save"
                                action="{!saveStudent}" />

        </apex:pageBlock>

        <br/>

        <apex:pageBlock title="Student Records">

            <apex:pageBlockTable value="{!stuList}" var="s">

                <apex:column value="{!s.Name}" />

                <apex:column value="{!s.Roll_No__c}" />

                <apex:column value="{!s.Class__c}" />

                <apex:column value="{!s.Mobile_No__c}" />

            </apex:pageBlockTable>

        </apex:pageBlock>

    </apex:form>

</apex:page>
```

---

# Step 6 — Run the Application

Open the following URL in Salesforce:

```text
/apex/StudentPage
```

---

# Working Flow

1. User enters student details.
2. Visualforce page sends data to Apex Controller.
3. Apex Controller stores data into Salesforce database.
4. Records are displayed on the page.

---

# Important Concepts

| Concept | Description |
|----------|-------------|
| Apex | Salesforce backend language |
| Visualforce | Salesforce frontend page |
| SOQL | Salesforce query language |
| Custom Object | Database table |
| Fields | Table columns |

---

# Sample SOQL Query

```sql
SELECT Name FROM Student__c
```

---

# Project Output

The system allows users to:

- Add Student Records
- Store Student Data
- View Student Records

---

# Conclusion

This project demonstrates the basics of Salesforce development using:

- Custom Objects
- Apex Classes
- Visualforce Pages

It is a beginner-friendly project for learning Salesforce application development.
