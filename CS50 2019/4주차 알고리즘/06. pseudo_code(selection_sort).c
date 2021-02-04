// Selection Sort pseudo-code

// Selection Sort(선택 정렬) : 배열 안의 자료 중 가장 작은 수(혹은 가장 큰 수)를 찾아 첫 번째 위치(혹은 가장 마지막 위치)의 수와 교환해주는 방식의 정렬
// --> 교환 횟수를 최소화하는 반면 각 자료를 비교하는 횟수는 증가

/*
For i from 0 to n-1
	Find smallest item between i'th item and last item
	Swap smallest item with i'th item
*/

/*
Big-O 표기 :
n + (n-1) + (n-2) + ... + 1
n(n+1)/2
(n^2 + n)/2
n^2/2 + n/2
--> O(n^2) (n^2의 영향력이 가장 크기 때문)

Ω(Omega) : Ω(n^2)
가장 최선의 상황은 "이미 정렬되어 있는 것"
하지만, 이미 정렬되어 있어도 버블 정렬의 알고리즘은 수행될 것
*/