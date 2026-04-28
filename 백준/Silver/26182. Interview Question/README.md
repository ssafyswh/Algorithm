# [Silver II] Interview Question - 26182 

[문제 링크](https://www.acmicpc.net/problem/26182) 

### 성능 요약

메모리: 47492 KB, 시간: 108 ms

### 분류

수학, 해 구성하기

### 제출 일자

2026년 04월 28일 09:16:43

### 문제 설명

<p><em>Fizz Buzz</em> is a party game that is often used as a programming exercise in job interviews. In the game, there are two positive integers $a$ and $b$, and the game consists of counting up through the positive integers, replacing any number by <code>Fizz</code> if it is a multiple of $a$, by <code>Buzz</code> if it is a multiple of $b$, and by <code>FizzBuzz</code> if it is a multiple of both $a$ and $b$. The most common form of the game has $a=3$ and $b=5$, but other parameters are allowed.</p>

<p>Your task here is to solve the reverse problem: given a transcript of part of the game (not necessarily starting at 1), find possible values of $a$ and $b$ that could have been used to generate it.</p>

<p>Figure I.1 shows some sample sequences for various values of $a$ and $b$.</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<td>$a=3, b=5:$</td>
			<td><code>1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz</code></td>
		</tr>
		<tr>
			<td>$a=6, b=2:$</td>
			<td><code>1 Buzz 3 Buzz 5 FizzBuzz 7 Buzz 9 Buzz 11 FizzBuzz 13</code></td>
		</tr>
		<tr>
			<td>$a=4, b=4:$</td>
			<td><code>1 2 3 FizzBuzz 5 6 7 FizzBuzz 9 10 11 FizzBuzz 13 14</code></td>
		</tr>
	</tbody>
</table>

<p style="text-align: center;">Figure I.1: Example sequences for <em>Fizz Buzz</em>.</p>

### 입력 

 <p>The input consists of:</p>

<ul>
	<li>One line with two integers $c$ and $d$ ($1 \le c \le d \le 10^5$), indicating that your transcript starts at $c$ and ends at $d$.</li>
	<li>One line with $d-c+1$ integers and strings, the contents of the transcript.</li>
</ul>

<p>It is guaranteed that the transcript is valid for some integers $a$ and $b$ with $1 \le a,b \le 10^6$, according to the rules laid out above.</p>

### 출력 

 <p>Output two positive integers $a$ and $b$ ($1 \le a,b \le 10^6$) that are consistent with the given transcript.</p>

<p>If there are multiple valid solutions, you may output any one of them.</p>

