import sys

class SegmentTree:
    
    def __init__(self, data):
        self.n = len(data)
        # 트리의 크기는 보통 원본 배열 크기의 4배로 설정합니다.
        self.tree = [0] * (4 * self.n)
        self.data = data
        # 세그먼트 트리를 구축합니다.
        self._build(1, 0, self.n - 1)
    
    # ------------------
    # 2. 트리 구축 (Build)
    # ------------------
    def _build(self, node, start, end):
        if start == end:
            # 리프 노드: 원본 배열의 값을 저장
            self.tree[node] = self.data[start]
            return
        
        mid = (start + end) // 2
        
        # 왼쪽 자식 노드는 2*node, 오른쪽 자식 노드는 2*node + 1
        self._build(2 * node, start, mid)
        self._build(2 * node + 1, mid + 1, end)
        
        # 내부 노드: 자식 노드의 값들의 연산 결과(여기서는 합)를 저장
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]
    
    # ------------------
    # 3. 범위 합 계산 (Query)
    # ------------------
    def query(self, l, r):
        return self._query_recursive(1, 0, self.n - 1, l, r)
    
    def _query_recursive(self, node, start, end, l, r):
        # Case 1: 현재 노드의 범위가 원하는 범위 [l, r]를 완전히 벗어난 경우 -> 0 반환
        if r < start or end < l:
            return 0
        
        # Case 2: 현재 노드의 범위가 원하는 범위 [l, r]에 완전히 포함되는 경우 -> 현재 노드의 값 반환
        if l <= start and end <= r:
            return self.tree[node]
        
        # Case 3: 현재 노드의 범위가 원하는 범위 [l, r]에 일부만 걸쳐 있는 경우 -> 자식 노드로 재귀 호출
        mid = (start + end) // 2
        sum_left = self._query_recursive(2 * node, start, mid, l, r)
        sum_right = self._query_recursive(2 * node + 1, mid + 1, end, l, r)
        return sum_left + sum_right
    
    # ------------------
    # 4. 값 갱신 (Update)
    # ------------------
    def update(self, index, new_value):
        diff = new_value - self.data[index]
        self.data[index] = new_value
        self._update_recursive(1, 0, self.n - 1, index, diff)
    
    def _update_recursive(self, node, start, end, index, diff):
        # 갱신할 index가 현재 노드의 범위를 벗어난 경우
        if index < start or end < index:
            return
        
        # 현재 노드의 값을 diff만큼 변경
        self.tree[node] += diff
        
        # 리프 노드가 아니면 자식 노드로 재귀 호출
        if start != end:
            mid = (start + end) // 2
            self._update_recursive(2 * node, start, mid, index, diff)
            self._update_recursive(2 * node + 1, mid + 1, end, index, diff)

N, M, K = map(int, input().split())
data = [0]
for _ in range(N):
    data.append(int(sys.stdin.readline()))
st = SegmentTree(data)
for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        st.update(b, c)
    else:
        print(st.query(b, c))