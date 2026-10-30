"""Generate complete, uncached execution traces of the user's four algorithms."""
from copy import deepcopy
from pathlib import Path
import json

CODES = {
'brute': ['def integerBreak(n):','    maxmul = 0','    for i in range(1, n):','        mul = i * (n-i)','        maxmul = max(maxmul, mul)','        if n-i > 1:','            mul = i * integerBreak(n-i)','            maxmul = max(maxmul, mul)','    return maxmul'],
'greedy': ['def integerBreak(n):','    maxmul = 1','    if n <= 3:','        return n - 1','    while n > 4:','        maxmul *= 3','        n = n - 3','    return maxmul * n'],
'dp': ['def integerBreak(n):','    dp = [0] * (n + 1)','    for i in range(2, n + 1):','        for j in range(1, i):','            a = j * (i-j)','            b = j * dp[i-j]','            dp[i] = max(dp[i], a, b)','    return dp[n]'],
'divide': ['def best(x):','    if x < 4: return x','    best_mul = x','    for i in range(1, x):','        left = best(i)','        right = best(x-i)','        best_mul = max(left*right, best_mul)','    return best_mul','','def integerBreak(n):','    max_mul = 0','    for i in range(1, n):','        left = best(i)','        right = best(n-i)','        max_mul = max(max_mul, left*right)','    return max_mul']}

def traces():
    out={}
    events=[]; stack=[]
    def emit(line,msg,detail='',parts=None,values=None,dp=None,active=-1,source=-1):
        events.append(dict(line=line,msg=msg,detail=detail,parts=parts,values=values or {},stack=deepcopy(stack),dp=deepcopy(dp),active=active,source=source))
    def brute(n):
        f={'name':f'F({n})','n':n};stack.append(f);emit(0,f'调用 F({n})','新建一个调用栈帧，父调用在原位置等待')
        m=0;f['best']=m;emit(1,'初始化 maxmul = 0')
        for i in range(1,n):
            f['i']=i;emit(2,f'循环取 i = {i}',f'把 {n} 分为 {i} 和 {n-i}',[i,n-i])
            v=i*(n-i);emit(3,'先计算不继续拆分的乘积',f'{i} × {n-i} = {v}',[i,n-i],{'mul':v})
            old=m;m=max(m,v);f['best']=m;emit(4,'比较并更新 maxmul',f'max({old}, {v}) = {m}',[i,n-i],{'旧值':old,'候选':v,'新值':m})
            emit(5,f'条件 {n-i} > 1 为 {n-i>1}', '成立就继续拆右边，否则进入下一轮',[i,n-i])
            if n-i>1:
                emit(6,f'父调用 F({n}) 暂停',f'等待 F({n-i})，之后再乘左边的 {i}',[i,n-i])
                r=brute(n-i);v=i*r;emit(6,f'子调用返回 {r}',f'mul = {i} × {r} = {v}',[i,n-i],{'子结果':r,'mul':v})
                old=m;m=max(m,v);f['best']=m;emit(7,'比较递归候选',f'max({old}, {v}) = {m}',[i,n-i],{'旧值':old,'候选':v,'新值':m})
        emit(2,f'F({n}) 的循环结束',f'i 已遍历 1 到 {n-1}')
        emit(8,f'返回 F({n}) = {m}','弹出当前栈帧，回到父调用');stack.pop();return m
    assert brute(6)==9
    out['brute']=dict(title='方法一：暴力递归',intro='n = 6 · 完整展开所有重复调用',code=CODES['brute'],events=events)
    events=[];stack=[]
    for original in [6,10,2,3,4]:
        n=original;f={'name':f'输入{original}','n':n};stack.append(f);emit(0,f'输入 n = {original}','这一次从头运行贪心代码')
        m=1;f['best']=m;emit(1,'初始化 maxmul = 1')
        emit(2,f'{n} <= 3 为 {n<=3}','必须至少拆成两份，不能直接返回 n')
        if n<=3:emit(3,f'提前返回 {n-1}',f'{n} = 1 + {n-1}，乘积为 {n-1}');stack.pop();continue
        while True:
            emit(4,f'判断 {n} > 4：{n>4}','继续拆出一个 3' if n>4 else '剩余值不大于 4，退出循环')
            if n<=4:break
            old=m;m*=3;f['best']=m;emit(5,'累乘一个 3',f'maxmul = {old} × 3 = {m}',[3,n-3],{'maxmul':m,'剩余n':n})
            n-=3;f['n']=n;emit(6,'剩余整数减去 3',f'n = {n+3} - 3 = {n}',[3,n],{'maxmul':m,'剩余n':n})
        emit(7,f'返回 {m*n}',f'maxmul × n = {m} × {n} = {m*n}');stack.pop()
    out['greedy']=dict(title='方法二：贪心算法',intro='先演示 n = 6，再演示 n = 10 与边界',code=CODES['greedy'],events=events)
    events=[];stack=[];d=[0]*7
    emit(0,'输入 n = 6','dp[i] 表示 i 至少拆成两份的最大乘积')
    emit(1,'初始化 dp[0…6] = 0','dp[1] = 0，因为 1 无法继续拆分',dp=d)
    for i in range(2,7):
        emit(2,f'外层取 i = {i}',f'开始求 dp[{i}]',dp=d,active=i)
        for j in range(1,i):
            emit(3,f'内层取 j = {j}',f'{i} = {j} + {i-j}',[j,i-j],dp=d,active=i,source=i-j)
            a=j*(i-j);emit(4,'右边不继续拆分',f'a = {j} × {i-j} = {a}',[j,i-j],{'a':a},d,i,i-j)
            b=j*d[i-j];emit(5,'读取已经完成的 dp 格子',f'b = {j} × dp[{i-j}] = {j} × {d[i-j]} = {b}',[j,i-j],{'a':a,'b':b},d,i,i-j)
            old=d[i];d[i]=max(old,a,b);emit(6,f'写入 dp[{i}] = {d[i]}',f'max({old}, {a}, {b}) = {d[i]}', [j,i-j],{'旧值':old,'a':a,'b':b,'新值':d[i]},d,i,i-j)
        emit(3,f'j 循环结束，dp[{i}] 已确定',f'最终 dp[{i}] = {d[i]}',dp=d,active=i)
    emit(2,'外层循环结束','i 已遍历 2 到 6',dp=d)
    emit(7,'返回 dp[6] = 9','最优拆分：6 = 3 + 3，乘积 3 × 3 = 9',dp=d,active=6)
    out['dp']=dict(title='方法三：动态规划',intro='n = 6 · 展示每次读取、比较与写回',code=CODES['dp'],events=events)
    events=[];stack=[]
    def best(x):
        f={'name':f'B({x})','n':x};stack.append(f);emit(0,f'调用 best({x})','best 允许不拆，返回当前整数也合法')
        emit(1,f'{x} < 4 为 {x<4}','边界值直接返回 x')
        if x<4:emit(1,f'返回 best({x}) = {x}','弹出栈帧，返回父调用');stack.pop();return x
        m=x;f['best']=m;emit(2,f'初始化 best_mul = {x}','把“不拆分”纳入候选')
        for i in range(1,x):
            f['i']=i;emit(3,f'best({x}) 枚举 i = {i}',f'{x} = {i} + {x-i}',[i,x-i])
            emit(4,f'先调用左边 best({i})','父调用暂停',[i,x-i]);l=best(i);f['left']=l;emit(4,f'左边返回 left = {l}',values={'left':l})
            emit(5,f'再调用右边 best({x-i})','左边结果保存在当前栈帧',[i,x-i]);r=best(x-i);f['right']=r;emit(5,f'右边返回 right = {r}',values={'left':l,'right':r})
            old=m;m=max(l*r,m);f['best']=m;emit(6,'合并左右结果并更新',f'max({l} × {r}, {old}) = {m}',[i,x-i],{'left':l,'right':r,'新值':m})
        emit(3,f'best({x}) 枚举结束')
        emit(7,f'返回 best({x}) = {m}','本次结果不会缓存，后面可能重新计算');stack.pop();return m
    f={'name':'F(6)','n':6};stack.append(f);emit(9,'调用 integerBreak(6)','外层必须先拆一次，保证至少两份')
    m=0;f['best']=m;emit(10,'初始化 max_mul = 0')
    for i in range(1,6):
        f['i']=i;emit(11,f'外层枚举 i = {i}',f'6 = {i} + {6-i}',[i,6-i])
        emit(12,f'调用左边 best({i})','外层等待左边返回',[i,6-i]);l=best(i);f['left']=l;emit(12,f'left = {l}',values={'left':l})
        emit(13,f'调用右边 best({6-i})','外层等待右边返回',[i,6-i]);r=best(6-i);f['right']=r;emit(13,f'right = {r}',values={'left':l,'right':r})
        old=m;m=max(m,l*r);f['best']=m;emit(14,'更新外层最大乘积',f'max({old}, {l} × {r}) = {m}',[i,6-i],{'旧值':old,'新值':m})
    emit(11,'外层循环结束','所有 i = 1…5 都已经执行')
    emit(15,'返回 integerBreak(6) = 9','左右都选择 3，乘积最大');stack.pop();assert m==9
    out['divide']=dict(title='方法四：分治递归',intro='n = 6 · 左右两边全部递归，不省略重复调用',code=CODES['divide'],events=events)
    return out

if __name__=='__main__':
    data=traces()
    Path(__file__).with_name('execution_traces.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print({k:len(v['events']) for k,v in data.items()})
