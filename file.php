<?php
function calculate_pi($iterations) {
    $pi = 0;
    $sign = 1;
    $denominator = 1;

    for ($i = 0; $i < $iterations; $i++) {
        $term = 4 * $sign / $denominator;
        $pi += $term;
        $sign *= -1;
        $denominator += 2;
    }

    return $pi;
}

$iterations = readline("Enter the number of iterations: ");
$result = calculate_pi($iterations);
echo "The value of PI: " . $result;
?>