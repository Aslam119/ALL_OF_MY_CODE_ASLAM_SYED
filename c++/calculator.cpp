#include <iostream>
using namespace std;

void getDayOfWeek(int dayNum);

int main()
{
    string clues[] = {"","odd number", "prime number", "Crisriano Ronaldo number","GAME OVER HAHA YOU TOUGHT IT WAS ANOTHER CLUE"};
    cout<<"WELCOME TO GUESSING NUMBER GAME YOU WILL HAVE ONLY 3 GUESSES AND 3 CLUES"<<endl;
   
    //you can choose any secret num
    
    int secretNum = 7;
    int guess;
    int i = 0;
    int clue_Count = 0;
    int guessCount = 0;

    while(guess != secretNum){
    cout<<"GUESS A NUMBER (1 - 10): "<<endl;
    cin>>guess;

    if(guess == secretNum){
        cout<<"You guessed the number You win!!!!!"<<endl;
    }
    else{
        cout<<"Incorrect guess \n"<<endl;
        i++;
        clue_Count++;
        guessCount++;
        cout<<"CLUE "<<clueCount<<" : "<<clues[i]<<"\n"<<endl;

             if(guessCount > 3){
            cout<<"EXCEEDED GUESS LIMIT SORRY BUD YOU LOSE!"<<endl;
            return 0;
        }



    }


}
return 0;
}
