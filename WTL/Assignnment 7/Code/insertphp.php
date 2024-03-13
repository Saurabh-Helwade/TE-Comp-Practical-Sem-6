<?php
if(isset($_POST['txtName']))
{
$con = mysqli_connect('localhost', 'root', '','database');
$txtName = $_POST['txtName'];
$txtEmail = $_POST['txtEmail'];
$txtPhone = $_POST['txtPhone'];
$txtMessage = $_POST['txtMessage'];
$sql = "INSERT INTO contact (Name, Email, Mobile, Message) VALUES ('$txtName', '$txtEmail', '$txtPhone', '$txtMessage')";
$rs = mysqli_query($con, $sql);
if($rs)
{
	echo "Contact Records Inserted";
}
}
else
{
	echo "Contact Records failed to insert";
}?>v 