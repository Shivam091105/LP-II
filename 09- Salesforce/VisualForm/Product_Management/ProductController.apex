public productController{
    public Product__c pro {get; set;}
    public List<Product__c> proList {get; set;}

    public productController(){
        pro = new Product__c();
        proList = [SELECT Name, Sr_No__c, Mf_Date__c, Exp_Date FROM Product__c];
    }

    public void saveProduct(){
        insert pro;
        proList = [SELECT Name, Sr_No__c, Mf_Date__c, Exp_Date FROM Product__c];
        pro = new Product__c();
    }
    
}