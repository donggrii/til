<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title></title>
    </head>
    <body>
        <h1>Array</h1>
        <?php
            $coworkers = array('egoing', 'leezche', 'duru', 'taeho');
            echo $coworkers[1].'<br>';     // leezche
            echo $coworkers[3].'<br>';     // taeho
            var_dump(count($coworkers));   // int(4)

            echo '<br>';
            array_push($coworkers, '동찬');
            var_dump($coworkers);          // array(5) { [0]=> string(6) "egoing" [1]=> string(7) "leezche" [2]=> string(4) "duru" [3]=> string(5) "taeho" [4]=> string(6) "동찬" }
        ?>
    </body>
</html>