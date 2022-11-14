# Introduction to Algorithms
links to tasks list at yandex.contest.ru:

[trial algorithms tasks](https://contest.yandex.ru/contest/26365/problems/)

[introduction to algorithms](https://contest.yandex.ru/contest/23389/problems/)

_________________________________________________

<details>
<summary>
Zipper (<a href="2_zipper.py">2_zipper.py</a>) 
</summary>
Algorithm to zip two arrays into one, in which the numbers from the input arrays alternate.

Input example:
|Input|Description|
|:-|:-|
|`3`|n - length of each array|
|`1 2 3`|first array|
|`4 5 6`|second array|
|`1 4 2 5 3 6`|output|

</details>

_________________________________________________

<details>
<summary>
Moving average (<a href="3_moving_average.py">3_moving_average.py</a>) 
</summary>
Moving average is a function whose values at each point of definition are equal to some average value of the original function for the previous period

Input example:
|Input|Description|
|:-|:-|
|`7`|n - length array|
|`1 2 3 4 5 6 7`|input array|
|`4`|smoothing window|
|`2.5 3.5 4.5 5.5`|output|

</details>

_________________________________________________

<details>
<summary>
Two chips (<a href="4_twosum.py">4_twosum.py</a>) 
</summary>
Choose two chips, the sum of points on which is equal to a given number. If there are no such pairs, then output "None".

Input example:
|Input|Description|
|:-|:-|
|`6`|n - length array|
|`-1 -1 -9 -7 3 -6`|input array|
|`2`|given number|
|`-1 3`|output|

</details>

_________________________________________________

<details>
<summary>
Two chips 2 (<a href="4_twosum_2.py">4_twosum_2.py</a>) 
</summary>
Choose two chips, the sum of points on which is equal to a given number. If there are no such pairs, then output "None".

Input example:
|Input|Description|
|:-|:-|
|`8`|n - length array|
|`-3 1 1 2 6 6 8 10`|input array|
|`100`|given number|
|`None`|output|

</details>

_________________________________________________

<details>
<summary>
Function values (<a href="5_quadro_func.py">5_quadro_func.py</a>) 
</summary>
Function y = ax^2 + bx + c. Write a program that will use the coefficients a, b, c and the number x to display the value of the function at the point x.

Input example:
|Input|Description|
|:-|:-|
|`-8 -5 -2 7`|a, x, b, c respectively|
|`-183`|output|

</details>

_________________________________________________

<details>
<summary>
Even and odd numbers (<a href="6_even_and_odd.py">6_even_and_odd.py</a>) 
</summary>
Write a program that determines if all three numbers have the same parity.

Input example:
|Input|Description|
|:-|:-|
|`1 2 -3`|input numbers|
|`FAIL`|output|
|||
|`7 11 7`|input numbers|
|`WIN`|output|

</details>

_________________________________________________

<details>
<summary>
Neighbours (<a href="7_matrix_neighbours.py">7_matrix_neighbours.py</a>) 
</summary>
Given a matrix. You need to write a function that for an element returns all of its neighbors.

Input example:
|Input|Description|
|:-|:-|
|`4`|number of matrix rows|
|`3`|number of matrix columns|
|`1 2 3`|input numbers|
|`0 2 6`|input numbers|
|`7 4 1`|input numbers|
|`2 7 0`|input numbers|
|`3`|row number for a given element|
|`0`|column number for a given element|
|`7 7`|output|

</details>

_________________________________________________

<details>
<summary>
Weather chaoticness (<a href="8_weather_chaos.py">8_weather_chaos.py</a>) 
</summary>
The chaoticness of the weather over several days means the number of days in which the temperature is strictly greater than the day before (if any) and the day after (if any). For example, if over 5 days the elevated air temperature varies [1, 2, 5, 4, 8] degrees, then the chaoticness for this period is 2: the described conditions were fulfilled on the 3rd and 5th days.

Input example:
|Input|Description|
|:-|:-|
|`7`|number of measurements|
|`-1 -10 -8 0 2 0 5`|measured numbers|
|`3`|output|

</details>

_________________________________________________

<details>
<summary>
Longest word (<a href="9_longest_word.py">9_longest_word.py</a>) 
</summary>
Find the longest word in a given string. If there are several suitable words, print the one that occurs first.

Input example:
|Input|Description|
|:-|:-|
|`19`|lenght of a string|
|`i love segment tree`|a string|
|`segment`|output|
|`7`|output|

</details>

_________________________________________________

<details>
<summary>
Palindrome (<a href="10_is_palindrome.py">10_is_palindrome.py</a>) 
</summary>
Print "True" if the phrase is a palindrome, and "False" if it is not.

Input example:
|Input|Description|
|:-|:-|
|`A man, a plan, a canal: Panama`|input string|
|`True`|output|
|||
|`zo`|input string|
|`False`|output|

</details>

_________________________________________________

<details>
<summary>
Work from home (<a href="11_decimal_to_binary.py">11_decimal_to_binary.py</a>) 
</summary>
Write a function that converts an integer from decimal to binary without using the language's built-in means of converting numbers to binary representation.

Input example:
|Input|Description|
|:-|:-|
|`5`|input number|
|`101`|output|
|||
|`14`|input number|
|`1110`|output|

</details>

_________________________________________________

<details>
<summary>
Binary system (<a href="12_binary_sum.py">12_binary_sum.py</a>) 
</summary>
Write a function that returns the sum of two numbers in binary without using the language's built-in methods.

Input example:
|Input|Description|
|:-|:-|
|`1010`|first input number|
|`1011`|second input number|
|`10101`|output|
|||
|`1`|first input number|
|`1`|second input number|
|`10`|output|

</details>

_________________________________________________

<details>
<summary>
Power of four (<a href="13_fourth_power.py">13_fourth_power.py</a>) 
</summary>
Write a program that determines whether a positive integer is a power of four.

Input example:
|Input|Description|
|:-|:-|
|`15`|input number|
|`False`|output|
|||
|`16`| input number|
|`True`|output|

</details>

_________________________________________________

<details>
<summary>
Factorization (<a href="14_factorization.py">14_factorization.py</a>) 
</summary>
Factoring a number into prime factors is called factoring a number.
Write a program that factorizes the given number.

Input example:
|Input|Description|
|:-|:-|
|`8`|input number|
|`2 2 2`|output|
|||
|`13`| input number|
|`13`|output|
|||
|`100`| input number|
|`2 2 5 5`|output|

</details>

_________________________________________________

<details>
<summary>
List form (<a href="15_list_form.py">15_list_form.py</a>) 
</summary>
For a non-negative integer X, the list form is an array of its digits from left to right. For example, for 1231 the list form would be [1,2,3,1]. The input is the number of digits of the number X, the list form of the non-negative number X and the non-negative number K.
We need to return the list form of the number X + K.

Input example:
|Input|Description|
|:-|:-|
|`4`|lenght of list form|
|`1 2 0 0`|list form of X number|
|`34`|K number|
|`1 2 3 4`|output|
|||
|`2`|lenght of list form|
|`9 5`|list form of X number|
|`17`|K number|
|`1 1 2`|output|

</details>

_________________________________________________

<details>
<summary>
Extra letter (<a href="16_extra_char.py">16_extra_char.py</a>) 
</summary>
There are 2 strings s and t, consisting only of lowercase letters. The string t is obtained by mixing the letters of the string s and adding 1 letter at a random position. You need to find the added letter.

Input example:
|Input|Description|
|:-|:-|
|`abcd`|string s|
|`abcde`|string t|
|`e`|output|
|||
|`xtkpx`|string s|
|`xkctpx`|string t|
|`c`|output|

</details>