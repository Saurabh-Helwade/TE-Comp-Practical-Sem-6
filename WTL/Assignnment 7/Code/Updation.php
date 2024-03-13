<html>
    <body>
<?php
    $con = mysqli_connect("localhost","root","","database");
    if($con){
        $n = $_POST['txtN1'];
        $n1 = $_POST['Name'];
        $e1 = $_POST["Email"];
        $p1 = $_POST["Mobile"];
        $m1 = $_POST["Message"];
        $sql = "update contact set Name='$n1',Email='$e1',Mobile ='$p1',Message='$m1' where Name='$n' ";
        $rs = mysqli_query($con,$sql);

        if($rs){
            ?>
            <div>"Updation Successful"</div>
            <?php
        }
        else{
            ?>
            <div>"Updation UnSuccessful"</div>
            </script>
<?php
        }
        mysqli_close($con);
    }
    else{
        echo "Connection unsuccessful";
    }
    ?>
    <br>
    <br>
    <a href="index.html"><button>Show Menu</button></a>
</body>
</html>