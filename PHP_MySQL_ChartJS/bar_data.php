<?php
header('Content-Type: application/json');

$conn = mysqli_connect("localhost", "user_name", "password", "database_name");

// $year = date('y');
// $month = date('m');
$sqlQuery = "SELECT input FROM input_noun";

$result = mysqli_query($conn, $sqlQuery);

$total = '';
foreach ($result as $row) {
    $total .= $row['input'].' ';    
}

// print_r(array_count_values(preg_split('/\s+/', $total)));    // 정규표현식으로 문자열 나누는 preg_split 함수

$data = array_count_values(preg_split('/\s+/', $total));       // 배열 안의 각 단어들의 빈도 수 계산해주는 array_count_values 함수
arsort($data);                                                 // 내림차순 정렬
mysqli_close($conn);
    
echo json_encode($data, JSON_UNESCAPED_UNICODE);               // 한글 인코딩 깨짐 해결
?>