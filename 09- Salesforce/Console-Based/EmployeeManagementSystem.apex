public class EmployeeManagementSystem {

    public static void mainMethod() {

        // Add Employee
        Employee__c emp = new Employee__c();

        emp.Emp_ID__c = 101;
        emp.Emp_Name__c = 'Rahul';

        emp.Email__c = 'rahul@gmail.com';

        emp.Birth_Date__c = Date.newInstance(2000, 5, 10);

        emp.Department__c = 'IT';

        insert emp;

        System.debug('Employee Added Successfully');



        // Display Employees

        List<Employee__c> empList = [
            SELECT Emp_ID__c,
                   Emp_Name__c,
                   Email__c,
                   Birth_Date__c,
                   Department__c
            FROM Employee__c
        ];



        System.debug('Employee Records');



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