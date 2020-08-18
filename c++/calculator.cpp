#include <iostream>

using namespace std;

int main()
{
    char play = 'y';

    while(play == 'y'){

        float num1,num2;
    char op;

    cout<<"ENTER NUMBER 1: "<<endl;
    cin>>num1;
    cout<<"ENTER NUMBER 2: "<<endl;
    cin>>num2;

    cout<<"ENTER OPERATOR, /, *, +, -  : "<<endl;
    cin>>op;

        while(op != '+' && op != '-' && op != '/' && op != '*')
    {
        cout<<"INVALID INPUT PLS ENTER A OPERATOR (+,-,*,/) "<<endl;
        cout<<"ENTER OPERATOR, /, *, +, -  : "<<endl;
        cin>>op;
        cout<<""<<endl;
    }


    switch(op){

    case '+': {
        cout<<(num1+num2)<<endl;

cout<<"DO YOU WANT TO CONTINUE OR END(y/n): "<<endl;
        cin>>play;

        break;

    }

        case '-': {
        cout<<(num1-num2)<<endl;

cout<<"DO YOU WANT TO CONTINUE OR END(y/n): "<<endl;
        cin>>play;

        break;
    }

        case '/': {
        cout<<(num1/num2)<<endl;

cout<<"DO YOU WANT TO CONTINUE OR END(y/n): "<<endl;
        cin>>play;

        break;
    }

        case '*': {
        cout<<(num1*num2)<<endl;

cout<<"DO YOU WANT TO CONTINUE OR END(y/n): "<<endl;
        cin>>play;

        break;
    }
}

   }
}
