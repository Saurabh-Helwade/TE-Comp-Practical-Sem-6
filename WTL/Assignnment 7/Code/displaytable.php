<!DOCTYPE html>
<html lang="en">
<body>
<h2 class="pull-left">Users List</h2>
<?php

    $conn = mysqli_connect('localhost', 'root', '','database');
    if(!$conn)
        {
          die('Could not Connect MySql Server:' .mysql_error());
        }
else
{
echo "connected";
}
$result = mysqli_query($conn,"SELECT * FROM contact");

if ($result->num_rows > 0)
{
?>
<table border="1">
<tr>
<td>Name</td>
<td>Email</td>
<td>Mobile</td>
<td>Message</td>
</tr>
<?php
$i=0;
while($row = mysqli_fetch_array($result)) {
?>
<tr>
<td><?php echo $row["Name"]; ?></td>
<td><?php echo $row["Email"]; ?></td>
<td><?php echo $row["Mobile"]; ?></td>
<td><?php echo $row["Message"]; ?></td>
</tr>
<?php
$i++;
}
?>
</table>
<?php
}
else{
echo "No result found";
}
?>
</body>
</html>