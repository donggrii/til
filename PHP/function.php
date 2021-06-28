<!DOCTYPE html>
<html]>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>function</h1>
        <?php
            $str = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. 
                    Quasi maxime dolorum, obcaecati exercitationem delectus ullam voluptatibus deserunt harum cumque necessitatibus laudantium. 
                    Numquam, incidunt provident explicabo nemo veniam animi doloribus. 
                    In?";
            echo $str;           // 줄바꿈되지 않고 출력
        ?>

        <h2>strlen()</h2>
        <?php
            echo strlen($str);   // 문자열 길이 출력 함수
        ?>

        <h2>nl2br()</h2>
        <?php
            echo nl2br($str);    // 문자열에서 개행문자를 자동으로 인식하여 <br> 추가해서 출력해주는 함수
        ?>
    </body>
</html>