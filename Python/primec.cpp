#include<iostream>
using namespace std;

void primeChecker( int a)
{
    if(a>1)
    {
        for(int i=2;i<a;i++)
        {
            if(a%i==0){
                cout<<a<<"is not a prime no";
            }
            else{
                cout<<a<<"is a primr no.";
            }
            break;
        }
    }
    else{
            cout<<a<<"is not a prime no.";
        }
}




int main()
{
    int a;
    cout<<"Enter a prime no";
    cin>>a;
    primeChecker(a);
    return 0;
}