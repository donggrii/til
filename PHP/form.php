<?php
    // form.html에서 title과 description을 POST 방식으로 전송하면 파일로 저장하는 form.php 코드
    file_put_contents('data/'.$_POST['title'], $_POST['description']);     // 파일을 저장하는 file_put_contents 함수
    echo "<p>title : ".$_POST['title']."</p>";
    echo "<p>description : ".$_POST['description']."</p>";
?>