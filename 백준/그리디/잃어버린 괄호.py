import sys
input = sys.stdin.readline

numbs = input().strip()
m_parse = numbs.split("-")
ans = 0

## 마이너스 부분
for j in range(1, len(m_parse)):
    m_lists = map(int,m_parse[j].split("+"))
    ans -= sum(m_lists)
## 플러스 부분 (제일 앞)
if m_parse[0] == '':
    m_parse = m_parse[1:]
else:
    p_lists = map(int, m_parse[0].split("+"))
    ans += sum(p_lists)
print(ans)

