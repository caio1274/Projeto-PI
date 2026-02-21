<?php
    $db_host = "localhost";
    $db_user = "root";
    $db_password = "";
    $db_name = "Calmind";

    $conexao = new mysqli($db_host, $db_user, $db_password, $db_name);
    /*if ($conexao->connect_error) {
        echo "erro";
        }
    else {
        echo "conexão bem sucedida";
    }*/
?>