"""Authored teaching storyboard; abbreviated examples retain all final candidates."""
from functools import lru_cache

@lru_cache(None)
def F(n):
    return max((max(i*(n-i),i*F(n-i) if n-i>1 else 0) for i in range(1,n)),default=0)

@lru_cache(None)
def B(n):
    return max(n,F(n))

# These helpers calculate storyboard labels only. The displayed user algorithms
# remain uncached; visual omission does not turn them into memoized algorithms.
def tree(left='1（固定）',right='F(5)',root='F(6)',gl=None,gr=None,done=False):
    nodes=[('p',root,3.5,1.7,'active'),('l',left,1.65,.25,'done' if '固定' in left or done else 'normal'),('r',right,5.3,.25,'done' if done else 'active')]
    edges=[('p','l'),('p','r')]
    if gl is not None:
        nodes.extend([('a',gl,4.1,-1.15,'done'),('b',gr,5.95,-1.15,'done')]);edges.extend([('r','a'),('r','b')])
    return dict(nodes=nodes,edges=edges)

def frame(line,caption,formula='',**kw):
    return dict(line=line,caption=caption,formula=formula,**kw)

def brute_frames():
    t=tree
    out=[
        frame(0,'我们用六来演示。F(6) 要把六拆开，不能直接把六当作答案。','目标：至少拆成两份，让乘积最大',**t()),
        frame(2,'先试第一种分法：左边取一，右边剩五。','6 = 1 + 5',**t()),
        frame(3,'先让右边的五保持原样，这个候选乘积是一乘五，等于五。','不继续拆右边：1 × 5 = 5',**t()),
        frame(4,'目前找到的最大乘积是五，先把它记下来。','maxmul：0 → 5',**t(root='F(6)\n当前最大 5')),
        frame(6,'接着试试把五继续拆开。先进入 F(5)，上面的 F(6) 暂时等待。','继续拆右边：1 × F(5)',**t(root='F(6)\n等待',gl='1（固定）',gr='F(4)')),
        frame(3,'在 F(5) 里面，第一种分法是一加四，直接相乘得到四。','第一种：1 × 4 = 4',**t(root='F(6)\n等待',gl='1（固定）',gr='F(4)')),
        frame(6,'如果四也继续拆，F(4) 的结果是四，所以这一项仍然得到四。','1 × F(4) = 1 × 4 = 4',**t(gl='1（固定）',gr='F(4) = 4')),
        frame(3,'再看 F(5) 的第二种分法：二加三，直接相乘得到六。','第二种：2 × 3 = 6',**t(gl='2（固定）',gr='F(3) = 2')),
        frame(7,'把右边的三继续拆，只能得到二；二乘二是四，比刚才的六小。','max(已有 4，直接 6，继续拆 4) = 6',**t(gl='2（固定）',gr='F(3) = 2')),
        frame(8,'其余分法以此类推。比较完下面这些候选值，F(5) 的结果就是六。','F(5)：取最大值 6',table=[['左边 i','右边不拆','右边继续拆'],['1','4','4'],['2','6','4'],['3','6','3'],['4','4','—']],hold=9),
        frame(6,'回到最外层，把左边的一乘上返回的六，这个分支得到六。','1 × F(5) = 1 × 6 = 6',**t(right='F(5) = 6',done=True)),
        frame(7,'把这个结果和原来的五比较，最大值更新为六。','maxmul：max(5, 6) = 6',**t(right='F(5) = 6',root='F(6)\n当前最大 6',done=True)),
        frame(2,'现在看最外层的第二种分法：左边取二，右边剩四。','6 = 2 + 4',**t(left='2（固定）',right='F(4)')),
        frame(3,'先不拆右边的四，二乘四得到八。','不继续拆右边：2 × 4 = 8',**t(left='2（固定）',right='F(4)')),
        frame(6,'F(4) 前面已经演示过，结果是四。这里省略重复画面，直接带回结果。','继续拆右边：2 × F(4) = 8',**t(left='2（固定）',right='F(4) = 4',done=True)),
        frame(7,'这两种选择都得到八，因此当前最大值更新为八。','maxmul：max(6, 8, 8) = 8',**t(left='2（固定）',right='F(4) = 4',root='F(6)\n当前最大 8',done=True)),
        frame(8,'剩下的分法以此类推。三加三得到九，比其他候选值都大。','最终答案：3 × 3 = 9',table=[['左边 i','右边不拆','右边继续拆'],['1','5','6'],['2','8','8'],['3','9','6'],['4','8','4'],['5','5','—']],hold=10),
        frame(8,'所以 F(6) 返回九。刚才省略的是重复画面，原代码依然会重复计算。','F(6) = 9',**t(left='3',right='3',root='返回 9',done=True)),
    ]
    return out

def divide_frames():
    t=tree
    return [
        frame(9,'分治还是先把六拆成两份，但这一次，左右两边都交给 best 来处理。','F(6)：先拆一次，再处理左右两边',**t(left='B(1)',right='B(5)')),
        frame(0,'这里把 best(x) 简写成 B(x)。它可以继续拆，也可以保留原来的 x。','B(3) = 3；但 F(3) = 2',**t(left='B(1)',right='B(5)')),
        frame(11,'先看第一种分法：一加五。我们分别计算 B(1) 和 B(5)。','6 = 1 + 5',**t(left='B(1)',right='B(5)')),
        frame(12,'一小于四，直接返回一。接下来计算右边的 B(5)。','left = B(1) = 1',**t(left='B(1) = 1',right='B(5)')),
        frame(2,'进入 B(5) 后，先把不拆分的五作为当前最好结果。','best_mul = 5',**t(left='B(1) = 1',right='B(5)\n当前最大 5')),
        frame(4,'B(5) 的第一种分法是一加四，左右分别调用 B(1) 和 B(4)。','第一种：B(1) × B(4)',**t(left='B(1) = 1',right='B(5)',gl='B(1) = 1',gr='B(4)')),
        frame(6,'B(4) 的结果是四。这一项只有一乘四，不如直接保留五。','max(5, 1 × 4) = 5',**t(left='B(1) = 1',right='B(5)',gl='B(1) = 1',gr='B(4) = 4')),
        frame(4,'B(5) 的第二种分法是二加三，左右两边都可以直接返回。','第二种：B(2) × B(3)',**t(left='B(1) = 1',right='B(5)',gl='B(2) = 2',gr='B(3) = 3')),
        frame(6,'二乘三得到六，比原来的五大，把最好结果更新为六。','best_mul：max(5, 2 × 3) = 6',**t(left='B(1) = 1',right='B(5) = 6',gl='B(2) = 2',gr='B(3) = 3')),
        frame(7,'其余分法以此类推。连同不拆分的五一起比较，B(5) 最终返回六。','B(5) = max(5, 4, 6, 6, 4) = 6',table=[['选择','乘积'],['不拆分','5'],['1 + 4','4'],['2 + 3','6'],['3 + 2','6'],['4 + 1','4']],hold=9),
        frame(14,'回到最外层，左右结果是一和六，所以第一种分法得到六。','max_mul = 1 × 6 = 6',**t(left='B(1) = 1',right='B(5) = 6',done=True)),
        frame(11,'再看第二种分法：二加四，分别计算 B(2) 和 B(4)。','6 = 2 + 4',**t(left='B(2)',right='B(4)')),
        frame(12,'左边 B(2) 返回二。右边 B(4) 已经出现过，这里直接展示它的结果四。','left = 2；right = 4',**t(left='B(2) = 2',right='B(4) = 4',done=True)),
        frame(14,'把左右结果相乘得到八，比前一个分支的六更大。','max_mul：max(6, 2 × 4) = 8',**t(left='B(2) = 2',right='B(4) = 4',root='F(6)\n当前最大 8',done=True)),
        frame(15,'剩下的分法以此类推。表里最大的乘积是九，对应三加三。','最终答案：B(3) × B(3) = 9',table=[['拆分','左右结果相乘'],['1 + 5','1 × 6 = 6'],['2 + 4','2 × 4 = 8'],['3 + 3','3 × 3 = 9'],['4 + 2','4 × 2 = 8'],['5 + 1','6 × 1 = 6']],hold=10),
        frame(15,'外层已经拆成两份，所以两个 B(3) 都可以保留三，最终返回九。','F(6) = 9',**t(left='B(3) = 3',right='B(3) = 3',root='返回 9',done=True)),
    ]

def dp_frames():
    d=[0]*7
    out=[frame(0,'我们用 dp[i] 记录：把 i 至少拆成两份后，能得到的最大乘积。','状态定义：dp[i] = F(i)',dp=d[:]),frame(1,'先把表初始化为零。dp[1] 为零，因为一不能再拆成两个正整数。','dp = [0, 0, 0, 0, 0, 0, 0]',dp=d[:])]
    for i in range(2,7):
        out.append(frame(2,f'现在来算 dp[{i}]。比它小的那些格子，我们已经准备好了。',f'当前目标：dp[{i}]',dp=d[:],active=i))
        for j in range(1,min(i,3)):
            a=j*(i-j);b=j*d[i-j]
            out.append(frame(4,f'第{j}种分法是{j}加{i-j}。先不拆右边，直接相乘得到{a}。',f'a = {j} × {i-j} = {a}',dp=d[:],active=i,source=i-j))
            out.append(frame(5,f'如果右边继续拆，就读取 dp[{i-j}] 中的{d[i-j]}，再乘以{j}，得到{b}。',f'b = {j} × dp[{i-j}] = {b}',dp=d[:],active=i,source=i-j))
            old=d[i];d[i]=max(old,a,b)
            out.append(frame(6,f'把原来的{old}和这两个候选值比较，当前最大值是{d[i]}，写回表格。',f'dp[{i}] = max({old}, {a}, {b}) = {d[i]}',dp=d[:],active=i,write=True))
        if i>3:
            rows=[['剩余 j','不再拆 a','继续拆 b']]
            for j in range(3,i):
                a=j*(i-j);b=j*d[i-j];rows.append([str(j),str(a),str(b)]);d[i]=max(d[i],a,b)
            out.append(frame(6,f'剩下的拆分位置以此类推。把表里的候选值也比较完，dp[{i}] 最终是{d[i]}。',f'其余候选也参与比较 → dp[{i}] = {d[i]}',dp=d[:],active=i,write=True,table=rows,hold=9))
        out.append(frame(2,f'dp[{i}] 已经确定为{d[i]}，后面遇到同一个问题，直接读这个格子。',f'dp[{i}] = {d[i]}，计算一次，多次使用',dp=d[:],active=i))
    out.append(frame(7,'最后读取 dp[6]，答案是九。整张表只计算了五个需要求解的状态。','dp = [0, 0, 1, 2, 4, 6, 9]',dp=d[:],active=6,hold=8))
    assert d==[0,0,1,2,4,6,9]
    return out

def greedy_frames():
    return [
        frame(0,'用十来演示贪心。我们不枚举所有分法，而是按照刚才证明的规则取三。','n = 10；目标是最大乘积',numbers=['10']),
        frame(1,'先把累计乘积设为一，接下来每取出一个三，就把它乘进去。','maxmul = 1',numbers=['10']),
        frame(4,'第一次判断：十比四大，可以取出一个三。','10 = 3 + 7',numbers=['3','7']),
        frame(5,'先把这个三乘进累计乘积，现在累计乘积是三。','maxmul = 1 × 3 = 3',numbers=['3','7']),
        frame(6,'再把剩余的数改成七，继续处理这七。','n = 10 − 3 = 7',numbers=['3','7']),
        frame(4,'第二次判断：七仍然比四大，再取出一个三。','7 = 3 + 4',numbers=['3','3','4']),
        frame(5,'累计乘积再乘一个三，从三变成九。','maxmul = 3 × 3 = 9',numbers=['3','3','4']),
        frame(6,'现在剩下四。我们保留这个四，不把它拆成三和一。','n = 7 − 3 = 4',numbers=['3','3','4']),
        frame(4,'四不大于四，循环结束。若输入更大，前面的两步就以此类推。','while n > 4：条件不成立',numbers=['3','3','4']),
        frame(7,'最后把累计乘积九乘上剩下的四，得到三十六。','9 × 4 = 36',numbers=['3','3','4']),
        frame(3,'再补上小输入：二必须拆成一加一，三必须拆成一加二。','n = 2 返回 1；n = 3 返回 2',numbers=['1 + 1','1 + 2'],hold=8),
    ]

for n in range(2,7):
    assert F(n)==[1,2,4,6,9][n-2]
