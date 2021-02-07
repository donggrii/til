// Merge Sort pseudo-code

// Merge Sort(병합 정렬) : 원소가 한 개가 될 때까지 계속해서 반으로 나누다가 다시 합쳐나가며 정렬을 하는 방식
//                       : 이 과정은 재귀적으로 구현됨

/*
If only one item
	Return
Else
	Sort left half of items
	Sort right half of items
	Merge sorted halves
*/

/*
병합 정렬 실행시간의 Big-O 표기 :
--> O(n * log n) (절반으로 나누는 형태의 실행횟수는 log n)
--> 숫자들을 반으로 나누는 데는 O(log n)의 시간이 들고, 각 반으로 나눈 부분들을 다시 정렬해서 병합하는 데 각각 O(n)의 시간이 걸림

병합 정렬 Ω(Omega) : Ω(n * log n)
--> 숫자들이 이미 정렬되었는지 여부에 관계 없이 나누고 병합하는 과정이 필요함
*/

/*
<정리>
: Big-O 표기
O(n^2)     - Bubble Sort, Selection Sort
O(n log n) - Merge Sort
O(n)       - Linear Search
O(log n)   - Binary Search
O(1)

: Big-Ω 표기
Ω(n^2)     - Selection Sort
Ω(n log n) - Merge Sort
Ω(n)       - Bubble Sort
Ω(log n)
Ω(1)       - Linear Search, Binary Search

*/