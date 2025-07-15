// # Sample Input

// # 3 12345678912345 a 334.23 14049.30493
// # Sample Output

// # 3
// # 12345678912345
// # a
// # 334.230
// # 14049.304930000


// # but need to write code in c++


#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int i;
    long l;
    char c;
    float f;
    double d;
    
    scanf("%d %ld %c %f %lf", &i, &l, &c, &f, &d);
    printf("%d\n%ld\n%c\n%.3f\n%.9lf", i, l, c, f,d);
    
        
    
    return 0;
}