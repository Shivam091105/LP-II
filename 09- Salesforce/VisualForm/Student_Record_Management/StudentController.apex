public class StudentController {

    // Create student object
    public Student__c stu {get; set;}

    // List to store all students
    public List<Student__c> stuList {get; set;}

    // Constructor
    public StudentController() {

        // Empty student object
        stu = new Student__c();

        // Fetch all student records
        stuList = [SELECT Name, Roll_No__c, Class__c, Mobile_No__c
                   FROM Student__c];
    }

    // Save student record
    public void saveStudent() {

        insert stu;

        // Clear form
        stu = new Student__c();

        // Refresh list
        stuList = [SELECT Name, Roll_No__c, Class__c, Mobile_No__c
                   FROM Student__c];
    }
}