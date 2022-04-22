<?php
    $fp = fopen ( "Attendance - 31-03-2022.csv" , "r" );
    while (( $data = fgetcsv ( $fp , 1000 , "," )) !== FALSE ) {
        $i = 0;
        foreach($data as $row) {
           echo $data ;
           $i++ ;
        }
    }
    fclose ( $fp );
?>