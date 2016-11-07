#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i;
    int a[10] = {2,4,5,6,1,3,7,8,9,0};
    insert(a);
    for(i = 0;i < 10;i++)
    {
        printf("%d ",a[i]);
    }
}

void insert(int a[10])
{
    int j,i,k;
    for(j = 1;j < 10;j++)
    {
        k = a[j];
        i = j-1;
        while((i >= 0) && (a[i] < k))
        {
            a[i+1] = a[i];
            i--;
        }
        a[i+1] = k;
    }
}
