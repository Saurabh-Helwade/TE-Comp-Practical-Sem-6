var myApp = angular.module("myApp", []);
myApp.service("ContactService" , function(){
	var uid = 1;
	var contacts = [{
		  'id' : 0,
				'firstname' : 'Saurabh',
                                'lastname' : 'Helwade',
				'email' : 'shelwade@gmail.com',
				'password': 'Saurabh123',
				'phone' : '8888888888',
                'age' : '21'}
                ];	
	
	// Save Service for sving new contact and saving existing edited contact.
	this.save = function(contact)  
	{
		if(contact.id == null)                       
		{
			contact.id = uid++;
			contacts.push(contact);
		}
		else
		{
			for(var i in contacts)
			{
				if(contacts[i].id == contact.id)
				{
					contacts[i] = contact;
				}
			}
		}
	};
	
	// serach for a contact
	
	this.get = function(id)
	{
		for(var i in contacts )
		{
			if( contacts[i].id == id)
			{
				return contacts[i];
			}
		}
	};
	
	//Delete a contact
		
	//Show all contacts
	this.list = function()
	{
		return contacts;
	};	
});

////Controller area .....
	
myApp.controller("ContactController" , function($scope , ContactService){
    console.clear();
    
    $scope.ifSearchUser = false;
    $scope.title ="Click Here To See List of Users";
    
		$scope.contacts = ContactService.list();
		
		$scope.saveContact = function()
		{
		  console.log($scope.newcontact);
		  if($scope.newcontact == null || $scope.newcontact == angular.undefined)
		  return;
			ContactService.save($scope.newcontact);
			$scope.newcontact = {};
		};				
		$scope.searchUser = function(){
		  if($scope.title == "Click Here To See List of Users"){
		    $scope.ifSearchUser=true;
		    $scope.title = "Back";
		  }
		  else
		  {
		    $scope.ifSearchUser = false;
		    $scope.title = "Click Here To See List of Users";
		  }		  
		};
});