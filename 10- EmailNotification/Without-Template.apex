public class EmailNotification {

    public static void sendEmail() {

        // Create email message object
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

        // Recipient Email Address
        String[] toAddresses = new String[] {'okkutsu08@gmail.com'};

        // Set recipient
        mail.setToAddresses(toAddresses);

        // Set subject
        mail.setSubject('Salesforce Email Notification');

        // Set email body
        mail.setPlainTextBody('Hello User,\n\nThis is a test email sent using Apex in Salesforce.\n\nThank You.');

        // Send Email
        Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

        System.debug('Email Sent Successfully');
    }