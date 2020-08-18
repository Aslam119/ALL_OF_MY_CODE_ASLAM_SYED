#include <iostream>
using namespace std;

void getDayOfWeek(int dayNum);

int main()
{
    getDayOfWeek(4);
    return 0;
}

//VALUE FOR EACH DAY NUMBER
void getDayOfWeek(int dayNum)
{
    switch(dayNum)
    {
    case 1:
        {
            cout<<"SUNDAY";
            break;
        }


    case 2:
        {
            cout<<"MONDAY";
            break;
        }


    case 3:
        {
            cout<<"TUESDAY";
            break;
        }

    case 4:
        {
            cout<<"WEDNESDAY";
            break;
        }

    case 5:
        {
            cout<<"THURSDAY";
            break;
        }

    case 6:
        {
            cout<<"FRIDAY";
            break;
        }

    case 7:
        {
            cout<<"SATURDAY";
            break;
        }
    }
}
