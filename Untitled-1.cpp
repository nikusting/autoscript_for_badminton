#include<stdlib.h>
#include<iostream>
usingnamespace std;

int getMaxOrMin(int *arr, intcount, boolisMax)
{
    int temp = arr[0];
    for(int i = 1; i <count; i++)
    {
        if(isMax)
        {
            if( temp <arr[i])
            {
                temp = arr[i];
            }
        }
        else
        {
            if(temp >arr[i])
            {
                temp = arr[i];
            }
        }

    }
    return temp;
}

int main()
{
    int arr1[4] = {3,2,5,8};
    bool isMax = false;
    cin >> isMax;   //输入cin和输出cout在iostream头文件中，所以要在程序的开始将这个头文件包含进来，同时还要加上命名空间std
    cout << getMaxOrMin (arr1, 4, isMax) << endl;
    system("pause");//system在stdlib.h头文件中，所以要在程序的开始将这个头文件包含进来
    return 0;
}