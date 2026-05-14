public class EmailWithAttachment {

    public static void sendEmailWithAttachment() {

        // Create Email Object
        Messaging.SingleEmailMessage mail = new Messaging.SingleEmailMessage();

        // Recipient
        mail.setToAddresses(new String[] {'receiver@example.com'});

        // Subject
        mail.setSubject('Salesforce Email With Attachment');

        // Body
        mail.setPlainTextBody('Hello User,\n\nPlease find the attachment below.\n\nThank You.');

        // Create Attachment
        Messaging.EmailFileAttachment attachment = new Messaging.EmailFileAttachment();

        attachment.setFileName('SampleFile.txt');

        attachment.setBody(Blob.valueOf('This is sample attachment content.'));

        attachment.setContentType('text/plain');

        // Attach File
        mail.setFileAttachments(
            new Messaging.EmailFileAttachment[] { attachment }
        );

        // Send Email
        Messaging.sendEmail(new Messaging.SingleEmailMessage[] { mail });

        System.debug('Email with Attachment Sent Successfully');
    }
}