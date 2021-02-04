// Bubble Sort pseudo-code

// Bubble Sort(버블 정렬) : 두 개의 인접한 자료 값을 비교하면서 위치를 교환하는 방식으로 정렬하는 방법
//                        : 마치 거품이(비교 및 교환이) 터지면서 위로 올라오는(배열의 옆으로 이동하는) 방식

/*
Repeat n-1 times (--> Repeat until no swaps : Ω(n))
    For i from 0 to n-2
        If i'th and i+1'th elements out of order
            Swap them
*/

/*
버블 정렬 실행시간의 Big-O 표기 :
(n-1) * (n-1) = n^2 -2n +1
--> O(n^2) (n^2의 영향력이 가장 크기 때문)

버블 정렬 Ω(Omega) : Ω(n^2)
가장 최선의 상황은 "이미 정렬되어 있는 것"
하지만, 이미 정렬되어 있어도 버블 정렬의 알고리즘은 수행될 것
*/

