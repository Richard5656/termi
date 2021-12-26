#include <iostream>
#include <unistd.h>
using namespace std;

int main(){
 int choice;
 cout << "Your system is running linux!\n" << ends;
 cout << "More stuff will be coming soon!\n" << ends;
 cout << "[1] Yes.\n" << ends;
 cout << "[2] No exit.\n" << ends;
 cout << "Go back?\n" << ends;
 cout << ">>>: " << ends;
 cin >> choice;
 if(choice == 1){
  chdir("../");
  system("./home");
 }
 if(choice == 2){
 system("exit");
 } 
}
