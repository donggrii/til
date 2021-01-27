#include <stdio.h>
#include <cs50.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("missing command-line argument\n");
        return 1;
    }
    printf("hello, %s\n", argv[1]);
    return 0;
}
// argv[] : 그 입력이 포함되어 있는 배열
// argc : main 함수가 받게 될 입력의 개수

// argv[0] : ./exit (= 프로그램의 이름)
// argv[1] : David (= 추가적인 입력)