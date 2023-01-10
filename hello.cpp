#include <iostream>
using namespace std;

int main(){
    long long range = 100000000000;
    long long total = 0;
    for (int i = 0; i <= range; i += 1){
        total += i;
    }
    cout << total;
return 0;
}