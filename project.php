<?php
    $Name    = $_POST['Name'];
    $Product = $_POST['Product'];
    
    //Database connection
    $conn = new mysqli('localhost','root','','orderform');
    if($conn->connect_error){
        die('connection Failed : ' .$conn->connect_error);
    }else{
        $stmt = $conn->prepare("insert into orderdetails(Name,Product)
        values(?,?)");
        $stmt->bind_param("ss",$Name,$Product);
        $stmt->execute();
        echo "Thank You For Ordering...";
        $stmt->Close();
        $conn->Close();
    }
