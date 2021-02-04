#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[4] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "EMMA") == 0)
        {
            printf("Found\n");
            return 0;   // 결과가 성공이었다면 0을 반환하는 게 관행
        }
    }
    printf("Not found\n");
    return 1;   // 결과가 실패였다면 1을 반환하는 게 관행
}