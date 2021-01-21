#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int i = 5;                                   // 재고량
    int order = get_int("How many orders?: ");   // 주문량 사용자 입력
    int price = 10000;                           // 물품 가격
    int tax = price * 0.1;                       // 부가세
    int sales = order * (price + tax);           // 매출액

    printf("주문건수 : %i건\n", order);
    printf("기존 재고량 : %i개\n", i);
    printf("남은 재고량 : %i개\n", i - order);
    printf("매출액(부가세포함) : %i원\n", sales);
}
