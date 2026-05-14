public class BackAccountSystem{
    public static voidmainMethod(){
        Banker__c b = new Banker__c();
        b.Emp_ID = 101;
        b.Name = "Kshitij";
        b.Email = [EMAIL_ADDRESS]";
        b.Amount = 10000;

        insert b;

        System.debug('Banker Added Successfully');

        List<Banker__c> bankerList = [SELECT Name, Emp_ID, Email, Amount FROM Banker__c];

        System.debug('Banker List: ' + bankerList);

        for(Banker__c b : bankerList){
            System.debug('Banker: ' + b.Name + ', Amount: ' + b.Amount);
            System.debug('........................................');
        }
    }
}