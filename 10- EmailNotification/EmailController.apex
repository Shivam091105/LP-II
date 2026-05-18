public class EmailController {

    // Variables
    public String toAddress {get; set;}
    public String subject {get; set;}
    public String body {get; set;}

    // Method to send email
    public PageReference sendEmail() {

        // Email Validation
        if(toAddress == null || 
           !Pattern.matches('^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$', toAddress)) {

            ApexPages.addMessage(
                new ApexPages.Message(
                    ApexPages.Severity.ERROR,
                    'Invalid Email Address!'
                )
            );

            return null;
        }

        try {

            // Create Email Object
            Messaging.SingleEmailMessage mail =
                new Messaging.SingleEmailMessage();

            // Set Email Address
            mail.setToAddresses(new String[] {toAddress});

            // Set Subject
            mail.setSubject(subject);

            // Set Body
            mail.setPlainTextBody(body);

            // OPTIONAL ATTACHMENT
            Messaging.EmailFileAttachment attachment =
                new Messaging.EmailFileAttachment();

            attachment.setFileName('Sample.txt');

            attachment.setBody(
                Blob.valueOf('This is sample attachment content.')
            );

            attachment.setContentType('text/plain');

            mail.setFileAttachments(
                new Messaging.EmailFileAttachment[] {attachment}
            );

            // Send Email
            Messaging.sendEmail(
                new Messaging.SingleEmailMessage[] {mail}
            );

            ApexPages.addMessage(
                new ApexPages.Message(
                    ApexPages.Severity.CONFIRM,
                    'Email Sent Successfully!'
                )
            );

        }
        catch(Exception e) {

            ApexPages.addMessage(
                new ApexPages.Message(
                    ApexPages.Severity.ERROR,
                    'Error: ' + e.getMessage()
                )
            );
        }

        return null;
    }
}