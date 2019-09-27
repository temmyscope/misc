<?php
function quad($a, $b, $c){
	$x = (-$b + sqrt(($b**2) - (4 * $a * $c))) / (2 * $a);
	$y = (-$b - sqrt(($b**2) - (4 * $a * $c))) /(2 * $a);
	return[ "The first value of x is".$x,"The second value of x is".$y];
}
echo "<pre>";
print_r(quad(11, 18, 7));
echo "<pre>";