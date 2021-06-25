<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <h1>Cross site scription</h1>
    <?php
        echo htmlspecialchars('<script>alert("babo");</script>');   // htmlspecialchars() 함수를 이용해 보안 설정(Cross site scription 방지; script 태그 기능 X)
    ?>
</body>
</html>