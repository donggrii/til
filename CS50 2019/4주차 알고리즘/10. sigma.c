#include <stdio.h>

// 반복문을 활용한 일반적인 Sigma 함수
int sigma(int n)
{
    if (n < 1)
    {
        return 0;
    }
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        sum += i;
    }
    return sum;
}

// 재귀를 활용한 Sigma 함수(반복문 X)
int sigma(int n)
{
    if (n <= 0)
    {
        return 0;
    }
    else
    {
        return (n + sigma(n-1));
    }
}

/*
재귀 함수에서 동일한 함수를 계속해서 호출할 때마다 함수를 위한 메모리가 계속해서 할당되는데,
여기서 함수가 호출될 때마다 사용되는 메모리를 "스택"이라고 함.
--> 재귀를 사용할 때는 과도하게 스택 메모리가 사용되지 않도록 주의해야 함.
*/
