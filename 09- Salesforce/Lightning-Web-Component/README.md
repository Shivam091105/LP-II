# College Management - Salesforce Lightning Application

## Project Overview
This document contains the step-by-step declarative (point-and-click) configuration required to build the "College Management" Lightning Application in Salesforce. This is a purely configuration-based assignment—**no HTML, CSS, or Apex code is required.**

---

## Step 1: Create Custom Objects
We need two standard data tables (Objects) to store records: **Student** and **Faculty**.

1. Go to **Setup** > **Object Manager**.
2. Click **Create** > **Custom Object**.

**Student Object:**
* Label: `Student`
* Plural Label: `Students`
* Object Name: `Student`
* Record Name: `Student Name` (Type: Text)
* Click **Save**.

**Faculty Object:**
* Label: `Faculty`
* Plural Label: `Faculties`
* Object Name: `Faculty`
* Record Name: `Faculty Name` (Type: Text)
* Click **Save**.

---

## Step 2: Create Custom Tabs
*Crucial step so the objects can be added to the App Navigation.*

1. Go to **Setup** > Search **Tabs** in the Quick Find box.
2. Under **Custom Object Tabs**, click **New**.
3. Select **Student**, pick a Tab Style (icon), and click **Next** until **Save**.
4. Repeat the process for the **Faculty** object.

---

## Step 3: Create Custom Fields
Navigate to **Setup** > **Object Manager** > Select the Object > **Fields & Relationships** > **New**.

### Student Fields:
1. **Marks:** Data Type -> `Number` (Length: 3, Decimal: 0). Field Name: `Marks__c`
2. **Roll Number:** Data Type -> `Number` (Length: 10, Decimal: 0). Field Name: `Roll_Number__c`
3. **Email:** Data Type -> `Email`. Field Name: `Email__c`

### Faculty Fields:
1. **Faculty ID:** Data Type -> `Number`. Field Name: `Faculty_ID__c`. *(Note: Check the box for "Do not allow duplicate values" to enforce uniqueness).*
2. **Salary:** Data Type -> `Currency`. Field Name: `Salary__c`
3. **Department:** Data Type -> `Picklist`. Field Name: `Department__c`. (Enter values: IT, HR, Finance, etc.)
4. **Joining Date:** Data Type -> `Date`. Field Name: `Joining_Date__c`

---

## Step 4: Create Validation Rules
Navigate to **Setup** > **Object Manager** > Select the Object > **Validation Rules** > **New**.

### Student Validation Rules:
1. **Marks should be between 0 and 100:**
   * Rule Name: `Validate_Marks`
   * Formula: `OR(Marks__c < 0, Marks__c > 100)`
   * Error: "Marks must be between 0 and 100."
2. **Roll number must be greater than 0:**
   * Rule Name: `Validate_Roll_Number`
   * Formula: `Roll_Number__c <= 0`
   * Error: "Roll number must be greater than 0."
3. **Ensure the email contains @ symbol:**
   * Rule Name: `Validate_Email`
   * Formula: `NOT(CONTAINS(Email__c, "@"))`
   * Error: "Email must contain an @ symbol."
4. **Student name cannot be blank:**
   * Rule Name: `Validate_Student_Name`
   * Formula: `ISBLANK(Name)`
   * Error: "Student name cannot be blank."

### Faculty Validation Rules:
1. **Name cannot be empty and must contain at least 3 characters:**
   * Rule Name: `Validate_Faculty_Name`
   * Formula: `OR(ISBLANK(Name), LEN(Name) < 3)`
   * Error: "Faculty name cannot be empty and must be at least 3 characters long."
2. **Faculty ID must be greater than 0:**
   * Rule Name: `Validate_Faculty_ID`
   * Formula: `Faculty_ID__c <= 0`
   * Error: "Faculty ID must be greater than 0."
3. **Salary must be greater than 10,000 and less than 500,000:**
   * Rule Name: `Validate_Salary`
   * Formula: `OR(Salary__c <= 10000, Salary__c >= 500000)`
   * Error: "Salary must be strictly between 10,000 and 500,000."
4. **Department must be selected:**
   * Rule Name: `Validate_Department`
   * Formula: `ISPICKVAL(Department__c, "")`
   * Error: "Please select a department."
5. **Joining Date cannot be a future date:**
   * Rule Name: `Validate_Joining_Date`
   * Formula: `Joining_Date__c > TODAY()`
   * Error: "Joining Date cannot be a future date."

---

## Step 5: Create the Lightning Application
1. Go to **Setup** > **App Manager**.
2. Click **New Lightning App**.
3. **App Details:** Name it `College Management`. Click **Next**.
4. **App Options:** Leave as Standard Navigation. Click **Next**.
5. **Utility Items:** Skip. Click **Next**.
6. **Navigation Items:** Search for **Students** and **Faculties** in the *Available Items* list. Use the arrow to move them to the *Selected Items* list.
7. **User Profiles:** Add **System Administrator**. Click **Save & Finish**.

---
*Created as a study guide for Salesforce Practical Examinations.*
