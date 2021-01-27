#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Input: ");
    printf("Output: ");
    for (int i = 0, n = strlen(s); i < n; i++) // i < strlen(s) 대신 s[i] != '\0'도 가능
    {
        printf("%c", s[i]);
    }
    printf("\n");
}