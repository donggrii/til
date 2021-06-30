<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
    </head>
    <body>
    <!-- URL : http://127.0.0.1:8080/php/parameter.php?address=""&name="" -->
    <!-- URL에서 정보를 가져와 출력 -->
        안녕하세요. <?php echo $_GET['address']; ?>에 사시는 <?php echo $_GET['name']; ?>님
    </body>
</html>