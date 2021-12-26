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
 username << register_username << ends;
 username.close();
 ofstream password;
 password.open("user/password.data");
 /* write whatever stored in register_password in the txt file */
 password << register_password << ends;
 password.close();
 cout << "Username and password has been created! launch the home file now! and your all set!\n" << ends;
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
  cout << "Launching home..." << ends;
  system("./home");
 }

}
