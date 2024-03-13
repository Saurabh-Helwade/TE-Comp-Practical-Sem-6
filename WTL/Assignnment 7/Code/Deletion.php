<html>
    <body>
<?php
    $con = mysqli_connect("localhost","root","","database");
    if($con){
        $id = $_POST['Name'];
        $sql = "delete from contact where Name='$id'";
        $rs = mysqli_query($con,$sql);
        if($rs){
            ?>
            <div>"Deletion Successful"</div>
            <?php
        }
        else{
            ?>
            <div>"Deletion UnSuccessful"</div>
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