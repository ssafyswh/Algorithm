# [Silver I] Painting the Wall - 16256 

[문제 링크](https://www.acmicpc.net/problem/16256) 

### 성능 요약

메모리: 32412 KB, 시간: 80 ms

### 분류

해 구성하기

### 제출 일자

2026년 04월 28일 09:16:43

### 문제 설명

<p>Little girl Masha is looking at the wall in her room. The wall is tiled with square tiles, but some of the tiles are replaced with lamps. So it is possible to consider the wall to be a rectangle of n × m, some cells contain tiles, other cells contain lamps.</p>

<p>Masha has paints of k different colors. Consider continuous vertical or horizontal segments of tiles, having an edge of the wall or a lamp at each of its ends. Masha wants to paint all tiles in such way, that any such segment has all tiles painted in different colors. Masha will not paint lamps. She doesn't have to use all the colors.</p>

<p>Help Masha to paint the wall.</p>

### 입력 

 <p>Input contains several test cases. The first line contains the number of test cases t.</p>

<p>Each test case is described by several lines. The first line contains three integers: n, m, k (1 ≤ n, m ≤ 100, 1 ≤ k ≤ max(n, m)) — the size of the wall and the number of paints Masha has.</p>

<p>The following n lines contain m integers a<sub>ij</sub> each:</p>

<ul>
	<li>a<sub>ij</sub> = 0 means that the position (i, j) contains the lamp;</li>
	<li>a<sub>ij</sub> = 1 means that the position (i, j) contains the tile.</li>
</ul>

<p>The total number of tiles and lamps in all test cases of one input doesn't exceed 10<sup>5</sup>.</p>

### 출력 

 <p>For each test case first print the answer:</p>

<ul>
	<li>NO, if there is no way to paint the wall.</li>
	<li>YES, if there is at least one way to paint the wall. In this case the following n lines must contain m integers b<sub>ij</sub> each — the color of the tile at position (i, j), or 0, if there is a lamp at this position. If there are several ways to paint the wall, you can output any one.</li>
</ul>

