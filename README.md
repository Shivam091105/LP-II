# Salesforce Assignments - Apex, Execute Anonymous and Visualforce Code

This README contains finalized Salesforce practical code assignment-wise.
all github links:
1. https://github.com/4SNA/salesforce-email-notification.git
2. https://github.com/4SNA/SecureFileSharing.git
3. https://github.com/4SNA/College-Management-Lightning-App.git
4. git@github.com:4SNA/Employee-Management----Salesforce.git
5. https://github.com/4SNA/Event-Registration_LP2.git
6. https://github.com/4SNA/Task-Manager-LP2.git
7. https://github.com/4SNA/ecommerce-app-LP2.git
8. https://github.com/4SNA/Student-Record-Management-System-LP-2.git
9. https://github.com/4SNA/Blog-app-LP-2.git
10. https://github.com/4SNA/Static-Website-EC2-apache.git
---

# Assignment 16 - Student Record Management System

## Problem Statement

Develop an application in Salesforce using Apex programming language and Visualforce page to manage student records:

- Name
- Roll No
- Class
- Mobile No

stored in a custom object.

## Custom Object

```text
Student__c
```

## Fields

| Field Label | API Name | Type |
|---|---|---|
| Student Name | Name | Standard Name Field |
| Roll No | Roll_No__c | Number |
| Class | Class__c | Text |
| Mobile No | Mobile_No__c | Phone |

## Apex Class: StudentController

```java
public class StudentController {

    public Student__c student { get; set; }

    public StudentController() {
        student = new Student__c();
    }

    public void saveStudent() {
        insert student;

        ApexPages.addMessage(
            new ApexPages.Message(
                ApexPages.Severity.CONFIRM,
                'Student Record Saved Successfully'
            )
        );

        student = new Student__c();
    }
}
```

## Visualforce Page: StudentPage

```html
<apex:page controller="StudentController">

    <apex:form>

        <apex:pageMessages />

        Name:
        <apex:inputField value="{!student.Name}" />
        <br/><br/>

        Roll No:
        <apex:inputField value="{!student.Roll_No__c}" />
        <br/><br/>

        Class:
        <apex:inputField value="{!student.Class__c}" />
        <br/><br/>

        Mobile No:
        <apex:inputField value="{!student.Mobile_No__c}" />
        <br/><br/>

        <apex:commandButton value="Save" action="{!saveStudent}" />

    </apex:form>

</apex:page>
```

## SOQL Query to Verify

```sql
SELECT Name, Roll_No__c, Class__c, Mobile_No__c
FROM Student__c
```

---

# Assignment 17 - Employee Management System

## Problem Statement

Develop a menu-driven Employee Management System that manages employee records:

- Emp ID
- Emp Name
- Email
- Birth Date
- Department

in Salesforce using console based.

## Custom Object

```text
Employee__c
```

## Fields

| Field Label | API Name | Type |
|---|---|---|
| Employee Name | Name | Standard Name Field |
| Emp ID | Emp_ID__c | Number |
| Email | Email__c | Email |
| Birth Date | Birth_Date__c | Date |
| Department | Department__c | Text |

## Apex Class: EmployeeManagement

```java
public class EmployeeManagement {

    public static void addEmployee() {

        Employee__c emp = new Employee__c();

        emp.Name = 'Sarthak';
        emp.Emp_ID__c = 101;
        emp.Email__c = 'sarthak@gmail.com';
        emp.Birth_Date__c = Date.newInstance(2005, 1, 1);
        emp.Department__c = 'IT';

        insert emp;

        System.debug('Employee Record Inserted Successfully');
    }

    public static void viewEmployees() {

        List<Employee__c> employees =
            [SELECT Name, Emp_ID__c, Email__c,
             Birth_Date__c, Department__c
             FROM Employee__c];

        for(Employee__c emp : employees) {

            System.debug(
                'Name: ' + emp.Name +
                ', Employee ID: ' + emp.Emp_ID__c +
                ', Email: ' + emp.Email__c +
                ', Birth Date: ' + emp.Birth_Date__c +
                ', Department: ' + emp.Department__c
            );
        }
    }
}
```

## Execute Anonymous Code

```java
EmployeeManagement.addEmployee();

EmployeeManagement.viewEmployees();
```

## SOQL Query to Verify

```sql
SELECT Name, Emp_ID__c, Email__c, Birth_Date__c, Department__c
FROM Employee__c
```

---

# Assignment 18 - Bank Account System

## Problem Statement

Develop a menu-driven Bank Account System that manages customer records in Salesforce using console based.

## Custom Object

```text
Bank_Customer__c
```

## Fields

| Field Label | API Name | Type |
|---|---|---|
| Customer Name | Customer_Name__c | Text |
| Customer ID | CustomerID__c | Number |
| Email | Email__c | Email |
| Birth Date | Birth_Date__c | Date |
| Branch | Branch__c | Text |

## Apex Class: BankAccountSystem

```java
public class BankAccountSystem {

    public static void addCustomer() {

        Bank_Customer__c customer = new Bank_Customer__c();

        customer.Customer_Name__c = 'Rahul Sharma';
        customer.CustomerID__c = 1001;
        customer.Email__c = 'rahul@gmail.com';
        customer.Birth_Date__c = Date.newInstance(2004, 5, 10);
        customer.Branch__c = 'Pune';

        insert customer;

        System.debug('Customer Record Inserted Successfully');
    }

    public static void viewCustomers() {

        List<Bank_Customer__c> customers =
            [SELECT Customer_Name__c,
             CustomerID__c,
             Email__c,
             Birth_Date__c,
             Branch__c
             FROM Bank_Customer__c];

        for(Bank_Customer__c customer : customers) {

            System.debug(
                'Customer Name: ' + customer.Customer_Name__c +
                ', Customer ID: ' + customer.CustomerID__c +
                ', Email: ' + customer.Email__c +
                ', Birth Date: ' + customer.Birth_Date__c +
                ', Branch: ' + customer.Branch__c
            );
        }
    }
}
```

## Execute Anonymous Code

```java
BankAccountSystem.addCustomer();

BankAccountSystem.viewCustomers();
```

## SOQL Query to Verify

```sql
SELECT Name, Customer_Name__c, CustomerID__c, Email__c, Birth_Date__c, Branch__c
FROM Bank_Customer__c
```

---

# Assignment 19 - Product Inventory Management System

## Problem Statement

Develop an application in Salesforce using Apex programming language and Visualforce page to manage product inventory records:

- Product Name
- Serial No
- Manufacture Date
- Expiry Date

stored in a custom object.

## Custom Object

```text
Product_Inventory__c
```

## Fields

| Field Label | API Name | Type |
|---|---|---|
| Product Name | Name | Standard Name Field |
| Serial No | Serial_No__c | Number |
| Manufacture Date | Manufacture_Date__c | Date |
| Expiry Date | Expiry_Date__c | Date |

## Apex Class: ProductController

```java
public class ProductController {

    public Product_Inventory__c product { get; set; }

    public ProductController() {
        product = new Product_Inventory__c();
    }

    public void saveProduct() {
        insert product;

        ApexPages.addMessage(
            new ApexPages.Message(
                ApexPages.Severity.CONFIRM,
                'Product Record Saved Successfully'
            )
        );

        product = new Product_Inventory__c();
    }
}
```

## Visualforce Page: ProductPage

```html
<apex:page controller="ProductController">

    <apex:form>

        <apex:pageMessages />

        Product Name:
        <apex:inputField value="{!product.Name}" />
        <br/><br/>

        Serial No:
        <apex:inputField value="{!product.Serial_No__c}" />
        <br/><br/>

        Manufacture Date:
        <apex:inputField value="{!product.Manufacture_Date__c}" />
        <br/><br/>

        Expiry Date:
        <apex:inputField value="{!product.Expiry_Date__c}" />
        <br/><br/>

        <apex:commandButton value="Save" action="{!saveProduct}" />

    </apex:form>

</apex:page>
```

## SOQL Query to Verify

```sql
SELECT Name, Serial_No__c, Manufacture_Date__c, Expiry_Date__c
FROM Product_Inventory__c
```

---

# Assignment 21 - Console-Based Apex Email Notification

## Problem Statement

Develop a console-based Apex program that sends an email notification to a specified email address using Salesforce email services. The program should define the recipient email, subject, and message body, and send the email using the built-in messaging class with or without attachment.

## Execute Anonymous Code Without Attachment

```java
Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

mail.setToAddresses(new String[] {'yourgmail@gmail.com'});

mail.setSubject('Salesforce Email Test');

mail.setPlainTextBody('Hello from Salesforce Apex Program');

Messaging.sendEmail(new Messaging.SingleEmailMessage[] {mail});

System.debug('Email Sent Successfully');
```

## Execute Anonymous Code With Attachment

```java
Messaging.EmailFileAttachment attachment = new Messaging.EmailFileAttachment();

attachment.setFileName('test.txt');
attachment.setBody(Blob.valueOf('Hello, this is an attachment from Salesforce Apex.'));

Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

mail.setToAddresses(new String[] {'yourgmail@gmail.com'});

mail.setSubject('Email With Attachment');

mail.setPlainTextBody('Please check the attached file.');

mail.setFileAttachments(
    new Messaging.EmailFileAttachment[] {attachment}
);

Messaging.sendEmail(new Messaging.SingleEmailMessage[] {mail});

System.debug('Email With Attachment Sent Successfully');
```

---

# Assignment 22 - Email Notification with Visualforce and Attachment

## Problem Statement

Develop an Apex program that sends an email notification to a specified email address using Salesforce email services. The program should define the recipient email, subject, and message body, and send the email with or without attachment using the built-in messaging class. Give the appropriate message on invalid email id with frontend using Visualforce pages.

## Apex Class: EmailController

```java
public class EmailController {

    public String toAddress { get; set; }
    public String subject { get; set; }
    public String body { get; set; }

    public Blob fileBody { get; set; }
    public String fileName { get; set; }

    public void sendEmail() {

        if(toAddress == null || !toAddress.contains('@')) {

            ApexPages.addMessage(
                new ApexPages.Message(
                    ApexPages.Severity.ERROR,
                    'Invalid Email Address'
                )
            );

            return;
        }

        Messaging.SingleEmailMessage mail =
            new Messaging.SingleEmailMessage();

        mail.setToAddresses(new String[] {toAddress});
        mail.setSubject(subject);
        mail.setPlainTextBody(body);

        if(fileBody != null && fileName != null) {

            Messaging.EmailFileAttachment attachment =
                new Messaging.EmailFileAttachment();

            attachment.setFileName(fileName);
            attachment.setBody(fileBody);

            mail.setFileAttachments(
                new Messaging.EmailFileAttachment[] {attachment}
            );
        }

        Messaging.sendEmail(
            new Messaging.SingleEmailMessage[] {mail}
        );

        ApexPages.addMessage(
            new ApexPages.Message(
                ApexPages.Severity.CONFIRM,
                'Email Sent Successfully'
            )
        );
    }
}
```

## Visualforce Page: EmailPage

```html
<apex:page controller="EmailController">

    <apex:form enctype="multipart/form-data">

        <apex:pageMessages />

        Email Address:
        <apex:inputText value="{!toAddress}" />
        <br/><br/>

        Subject:
        <apex:inputText value="{!subject}" />
        <br/><br/>

        Message:
        <apex:inputTextarea value="{!body}" />
        <br/><br/>

        Select Attachment:
        <apex:inputFile value="{!fileBody}" filename="{!fileName}" />
        <br/><br/>

        <apex:commandButton value="Send Email" action="{!sendEmail}" />

    </apex:form>

</apex:page>
```

---

# Common SOQL Commands

## Student

```sql
SELECT Name, Roll_No__c, Class__c, Mobile_No__c
FROM Student__c
```

## Employee

```sql
SELECT Name, Emp_ID__c, Email__c, Birth_Date__c, Department__c
FROM Employee__c
```

## Bank Customer

```sql
SELECT Name, Customer_Name__c, CustomerID__c, Email__c, Birth_Date__c, Branch__c
FROM Bank_Customer__c
```

## Product Inventory

```sql
SELECT Name, Serial_No__c, Manufacture_Date__c, Expiry_Date__c
FROM Product_Inventory__c
```

---

# Common Salesforce Concepts

## Apex

Apex is Salesforce's object-oriented programming language used to write backend logic.

## Visualforce

Visualforce is a Salesforce framework used to create custom user interface pages.

## Custom Object

Custom object is a user-defined database table in Salesforce. Custom object API names end with `__c`.

## Custom Field

Custom field is a user-defined column in a Salesforce object. Custom field API names end with `__c`.

## DML

DML means Data Manipulation Language. Common DML operations are:

- insert
- update
- delete
- upsert

## SOQL

SOQL stands for Salesforce Object Query Language. It is used to retrieve records from Salesforce objects.

## Execute Anonymous Window

Execute Anonymous Window is used to run Apex code directly without creating a Visualforce page.

---

# Important Notes

1. Always check exact API names from:

```text
Setup → Object Manager → Object → Fields & Relationships
```

2. Custom object and field API names usually end with:

```text
__c
```

3. Use Query Editor in Developer Console to verify inserted records.

4. For Visualforce file upload, form must include:

```html
enctype="multipart/form-data"
```

5. For email sending, use:

```java
Messaging.SingleEmailMessage
```

---

# Remaining Salesforce Assignments

The following assignments require Lightning Web Components and should be prepared separately:

- Assignment 20 - Employee Management Lightning Web Component
- Assignment 23 - College Management Lightning Application
