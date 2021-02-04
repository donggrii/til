// Pseudo-code
// <선형 검색> : 배열의 인덱스를 처음부터 끝까지 하나씩 증가시키면서 방문하여 그 값이 속하는지를 검사
//			   : 따라서, 자료가 정렬되어 있지 않거나 그 어떤 정보도 없어 하나씩 찾아야 하는 경우에 유용함(검색 전 데이터 정렬의 필요성)
/*
For i from 0 to n-1
	If i'th element is 50
		Return True
Return False
*/


//<이진 검색> : 만약 배열이 정렬되어 있다면, 배열 중간 인덱스부터 시작하여 찾고자 하는 값과 비교하며
// 그보다 작은(작은 값이 저장되어 있는) 인덱스 또는 큰 (큰 값이 저장되어 있는) 인덱스로 이동을 반복
/*
If no items                             # 아래 3가지 경우가 모두 해당되지 않을 때
	Return False
If middle item is 50
	Return True
Else if 50 < middle item
	Search left half
Else if 50 > middle item
	Search right half
*/
