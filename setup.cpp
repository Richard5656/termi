#include <iostream>
#include <fstream>

using namespace std;







void makeuser(){
 string register_username, register_password;
 cout << "Lets start setting up!\n" << ends;
 cout << "Enter a username: " << ends;
 
 
 /* Store username for later use */
 cin >> register_username;
 cout << "Enter a password: " << ends;
 cin >> register_password;
 
 /* store password for later use */
 ofstream username;
 username.open("user/username.data");
 
 /* write in the text file whatever stored in the register_username variable */
 
 username << register_username;
 
 username.close();
 ofstream password;
 password.open("user/password.data");
 
 /* write whatever stored in register_password in the txt file */
 password << register_password;
 
 password.close();
 cout << "Username and password has been created! launch the home file now! and your all set!\n" << ends;
 }



void checkuser(){
	string buffer;	// buffer for reading the file //holds the data
	
	ifstream FP_username("user/username.data"),FP_password("user/password.data"); //same thing as ofstream just that it instead reads the file 
	
	string _username, _password; // user input 
	
	cout << "Login \n";
	cout << "Lets start setting up!\n" << ends;

	cout << "Enter a username: " << ends;
	cin >> _username;
	cout << "Enter a password: " << ends;
	cin >> _password;
	

	
	
	/*
	// this is the slow comparision between the username and password
	getline(FP_username,buffer);
	
	if(buffer == _username){
		getline(FP_password,buffer);
		if(buffer == _password){
			system("./home");
		}else{
			
			cout << "Incorrect USERNAME OR PASSWORD\n";
		}
		
		
	}else{
		
		cout << "Incorrect USERNAME OR PASSWORD\n";
		
	}
	*/
	
	
	
	
	//sorry for using ints instead of bool on this one
 // you can store conditions in varibles and they will end up like this true = 1 and false =0
	//this is the fast comparrision
	getline(FP_username,buffer); //gets username into buffer
	
	int username_cond = (buffer == _username); // compares the username that was gotten to the one that was typed

	getline(FP_password,buffer);//gets password into buffer
	
	int password_cond = (buffer == _password); // compares the password that was gotten to the one that was typed
	
	int final_cond = username_cond * password_cond; // multiplies the 2 conditions together. 
 //if both of them are true it is 1*1 = 1 if 1 of them is false it would be 0*1 =0 or 1*0 = 0 if both false it would be 0*0 = 0
	
 
 //since only if both are correct it will equal 1 we can use a switch statement which is faster than using many if elses
	
	switch(final_cond){
		case 0:
			cout << "Incorrect USERNAME OR PASSWORD\n"; // if it was 0
		break;
		
		case 1:
			cout << "Launching home..." << ends; // if it is 1
			system("./home");
		break;
	}
	
	
	
	
	// choose which ever comparision method you would like to use 
	FP_username.close();
	FP_password.close();
	
	
	
}











int main()
{
 int option;
 cout << "[1] Setup\n" << ends;
 cout << "[2] I have done the setup already\n" << ends;
 cout << ">>>: " << ends;
 cin >> option;
 if(option == 1){
 makeuser();
 }
 
 if(option == 2){
checkuser();
 }

}
