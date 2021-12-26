#include <iostream>
#include <unistd.h>
/* enable namespace std  Don't remove otherwise you may have to change some source code.*/
using namespace std;
/* Helloworld function */
void helloworld(){
 cout << "Hello World!" << ends;
}


int main(){
 int choice;
 cout << "Checking username or password will come later as a update. \n" << ends;
 cout << "Welcome!\n" << ends;
 cout << "[1] Systeminfo\n" << ends;
 cout << "[2] Exit safley\n" << ends;
 cout << "[3] cmatrix\n" << ends;
 cout << "[4] Reboot computer\n" << ends;
 cout << "[5] Print hello world!\n" << ends;
 cout << "[6] Browser | Not out yet! \n" << ends;
 cout << "[?]\n" << ends;
 cout << ">>>: " << ends;
 cin >> choice;
 if(choice == 1){
 chdir("services");
 system("./home");
 }

 if(choice == 2){
 system("exit");		 
 }
 
 if(choice == 3){
 /* Ignore the system code. It just adds install commands.
  Depending on what linux distro you are on  */
 system("sudo pacman -S cmatrix");
 system("sudo apt-get install cmatrix");
 system("sudo emerge --ask cmatrix");
 system("cmatrix");

 if(choice == 4){
  system("reboot");
 }
 if(choice == 5){
 cout << "Hello World!\n" << ends;
 }
 if(choice == 6){
  cout << "Coming soon!" << ends;
  system("exit"); 
 }
 
 }
 return 0;
}
