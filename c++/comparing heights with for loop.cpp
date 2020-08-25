#include <iostream>

using namespace std;

int main()
{
int num = 0;
    int heights[] = {81,180,130,140,156,190,100,83};
    int heightsSize = sizeof(heights)/sizeof(heights[0]);
    for(int i = 0; i < heightsSize  ;i++){
            int height = heights[i];
        if (height > 160)
        {
            num += 1;
        }
    }
    cout<<num<<endl;
    return 0;
}
