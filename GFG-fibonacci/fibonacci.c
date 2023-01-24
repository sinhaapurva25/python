#include<stdio.h>

int main()
{
    int a, b, n, c, s;
    a = -1;
    b = 1;
    s = 0;
    printf("enter n: ");
    scanf("%d",&n);
    
    while (s!=n)
    {
        c = a+b;
        printf("%d\n",c);
        a = b;
        b = c;
        s++;
    }
    return 0;
}
