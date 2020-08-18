#include <iostream>
using namespace std;

void getDayOfWeek(int dayNum);

int main()
{
    string clues[] = {"","odd number", "prime number", "Crisriano Ronaldo number"};

    int secretNum = 7;
    int guess;
    int i = 0;
    int counnt = 0;

    while(guess != secretNum){
    cout<<"GUESS A NUMBER (1 - 10): "<<endl;
    cin>>guess;

    if(guess == secretNum){
        cout<<"You guessed the number!!!!!"<<endl;
    }
    else{
        cout<<"Incorrect guess \n"<<endl;
        i++;
        counnt++;
        cout<<"CLUE "<<counnt<<" : "<<clues[i]<<"\n"<<endl;
    }



}
return 0;
}
