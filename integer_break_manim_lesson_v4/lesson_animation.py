"""ManimGL narrated-style lesson: ideas first, two examples, then final results."""
import sys,json,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from manimlib import *
from trace_data import CODES
from lesson_story import brute_frames,divide_frames,dp_frames,greedy_frames
FONT='Microsoft YaHei';BG='#101827';INK='#E5EDF8';BLUE='#66B3FF';GREEN='#56DEAA';ORANGE='#FFC16C';MUTED='#9CAEC8'

def text(s,size=25,color=INK,width=13):
    t=Text(str(s) or ' ',font=FONT,font_size=size).set_color(color)
    if t.get_width()>width:t.set_width(width)
    return t

def save(scene):
    folder=Path(__file__).parent/'subtitles';folder.mkdir(exist_ok=True)
    (folder/(scene.__class__.__name__+'.json')).write_text(json.dumps(scene.cues,ensure_ascii=False,indent=2),encoding='utf8')

def box(s,x,y,color=BLUE,w=1.9):
    r=RoundedRectangle(width=w,height=.72,corner_radius=.1,stroke_color=color,fill_color='#1D2D45',fill_opacity=1).move_to([x,y,0])
    return VGroup(r,text(s,21,color,w-.15).move_to(r))

def tree(nodes,edges):
    g=VGroup();positions={n[0]:np.array([n[2],n[3],0]) for n in nodes}
    for a,b in edges:
        g.add(Arrow(positions[a]+DOWN*.37,positions[b]+UP*.37,buff=.03,stroke_color=BLUE,stroke_width=2))
    for ident,s,x,y,state in nodes:g.add(box(s,x,y,{'active':ORANGE,'done':GREEN,'normal':BLUE}[state]))
    return g

def table(rows,x=3.45,y=.45,width=6.1):
    g=VGroup();cols=len(rows[0]);cw=width/cols;rh=.48
    for i,row in enumerate(rows):
        for j,s in enumerate(row):
            p=[x-width/2+cw*(j+.5),y+(len(rows)-1)*rh/2-i*rh,0]
            r=Rectangle(width=cw,height=rh,stroke_color='#35445F',fill_color='#1D2D45',fill_opacity=1).move_to(p)
            g.add(r,text(s,19,ORANGE if i==0 else INK,cw-.15).move_to(r))
    return g

class TeachingScene(Scene):
    def setup(self):
        super().setup();self.camera.background_color=BG;self.cues=[]
    def show(self,g,caption,hold=7):
        c=text(caption,24,INK,13.4).move_to([0,-3.5,0])
        start=self.time;self.play(FadeIn(g),FadeIn(c),run_time=.4)
        self.wait(max(hold,min(11,len(caption)/5)))
        self.cues.append([start,self.time,caption])
        self.play(FadeOut(g),FadeOut(c),run_time=.3)
    def cards(self,title,items):
        heading=text(title,37).move_to([0,3.35,0]);self.add(heading)
        for name,formula,caption in items:
            group=VGroup(text(name,32,ORANGE).move_to([0,1.5,0]))
            if formula:group.add(text(formula,29,GREEN).move_to([0,-.1,0]))
            self.show(group,caption,9)
        self.remove(heading)

class Opening(TeachingScene):
    def construct(self):
        self.cards('整数拆分：先看思路，再看代码',[
            ('同一道题，四种解法','6 = 3 + 3 → 最大乘积 9','题目要求至少拆成两个正整数。我们用六作主例子，看看四种方法分别怎么想。'),
            ('暴力递归：每个位置都试一试','固定左边 i；比较右边不拆和继续拆','先选出左边的数，再看右边要不要继续拆。每种选择都算一遍，最后取最大值。'),
            ('分治递归：左右分别求，再把结果乘起来','B(x) 允许保留 x；外层必须先拆一次','分治写法会处理左右两边。要注意 best 允许不拆，而最外层仍然必须拆一次。'),
            ('动态规划：把小问题的答案先存起来','dp[i] = max(dp[i], j×(i−j), j×dp[i−j])','它保留暴力方法的两种候选，但先算小的数，后面用到时直接查表，不再重复求解。'),
            ('贪心：先证明规律，再按规律选','尽量取 3；剩下 4 时保留 4','如果能证明局部选择不会吃亏，就不必枚举。这里的规律是尽量拆出三，但不要留下一个一。'),
            ('接下来的演示怎么安排','思路 → 两个具体例子 → 其余候选与最终结果','相同的枚举只展开两个例子，后面用以此类推衔接，并给出其余候选和最后答案。'),
        ]);save(self)

class TreeComparison(TeachingScene):
    def construct(self):
        title=text('暴力树里多了什么？和分治、动态规划怎么比？',32).move_to([0,3.35,0]);self.add(title)
        nodes=[('r','F(6)',0,2,'active'),('a','F(5)',-2.4,.7,'normal'),('b','F(4)',2.4,.7,'active'),('c','F(4)',-2.4,-.7,'active')]
        g=tree(nodes,[('r','a'),('r','b'),('a','c')])
        g.add(text('i=1 的路径',21,MUTED).move_to([-4,.7,0]),text('i=2 的路径',21,MUTED).move_to([4.3,.7,0]),text('这两个 F(4) 会各自再展开一遍',27,ORANGE).move_to([0,-2.1,0]))
        self.show(g,'看这两条路径：先拆出一再拆出一，或者直接拆出二，都会遇到 F(4)。',11)
        g=VGroup(text('暴力多出的部分：同一个问题的重复调用和整棵子树',29,ORANGE).move_to([0,1.7,0]),table([['重复位置','是否要重新求解'],['第一条路径中的 F(4)','原代码会计算'],['第二条路径中的 F(4)','原代码又算一遍'],['它们下面的 F(3)、F(2)','也可能跟着重复']],x=0,y=-.2,width=11))
        self.show(g,'暴力树里重复的不只是一个节点，它下面的整段计算也会重来。动态规划主要省掉的就是这些。',11)
        nodes=[('r','F(6)',0,2,'active'),('l','B(2)',-2.5,.6,'normal'),('q','B(4)',2.5,.6,'normal'),('a','B(2)',1.1,-.9,'active'),('b','B(2)',3.9,-.9,'active')]
        g=tree(nodes,[('r','l'),('r','q'),('q','a'),('q','b')]);g.add(text('这里展示 6=2+4、4=2+2 这条分支',23,MUTED).move_to([0,-2.25,0]))
        self.show(g,'分治并不自动消除重复。代码对左右都递归，同样会多次遇到 B(2) 这样的子问题。',11)
        g=VGroup(text('动态规划：按大小顺序，每个状态只求一次',30,ORANGE).move_to([0,1.9,0]))
        for i,v in enumerate([0,0,1,2,4,6,9]):
            g.add(box(f'dp[{i}]\n{v}',-5.4+i*1.8,.3,GREEN,1.55))
        g.add(text('dp[4] = 4 → 后面需要时，直接读取',30,GREEN).move_to([0,-1.5,0]))
        self.show(g,'动态规划把 dp[4] 算好后存下来，以后直接读取。',11)
        self.remove(title)
        self.cards('三个方法的关系',[
            ('F 和 dp 表示同一种状态','F(x)：必须拆；dp[x]：必须拆','所以可以把暴力递归里重复出现的 F(x)，改成表里的 dp[x]。'),
            ('B 的含义稍有不同','B(x) = max(x, F(x))，这里 x ≥ 2','B 还允许保留原来的数。比如 F(3) 是二，B(3) 是三，不能把这两个返回值混在一起。'),
        ]);save(self)

class GreedyReason(TeachingScene):
    def construct(self):
        self.cards('为什么可以尽量多取 3？',[
            ('先看不小于 4 的输入','尽量避免在拆分里留下 1','一乘其他数不会变大；把一和另一份合并，通常就能得到更大的乘积。二和三的小输入稍后单独处理。'),
            ('一份如果不小于 5，还能拆得更好','3(x−3) − x = 2x−9 > 0（x ≥ 5）','比如五可以拆成二和三，乘积从五变成六。一般地，拆出三也会让乘积变大。'),
            ('因此只需要考虑 2、3 和 4','4 可以看成 2 + 2，乘积仍然是 4','四可以不拆，也可以拆成两个二，所以接下来只需比较二和三怎样搭配。'),
            ('三个 2 可以换成两个 3','2×2×2 = 8 < 3×3 = 9','两种组合的总和都是六，但两个三的乘积更大。这就是我们优先使用三的原因。'),
            ('剩下 4 时，别再取 3','3×1 = 3 < 2×2 = 4','如果再取三，就会留下一个一，乘积反而变小。因此循环条件要写成 n 大于四。'),
            ('小输入单独处理','2 → 1+1；3 → 1+2','题目要求至少拆成两份，因此输入是二时返回一，输入是三时返回二。'),
        ]);save(self)

INTRO={
 'brute':('暴力递归的思路','固定左边，右边有两种选择','我们每次固定一个左边的数，再比较右边保持原样和继续拆分，选乘积较大的那个。'),
 'divide':('分治递归的思路','左右分别求最好结果，再相乘','最外层先拆成两份；进入 best 后，可以保留当前整数，也可以再拆开，最后取最大值。'),
 'dp':('动态规划的思路','小的先算好，大的直接查表','先确定 dp[i] 的含义，再从二开始往上填。每个位置都比较右边不拆和继续拆这两种情况。'),
 'greedy':('贪心算法的思路','大于 4 就取 3，最后乘上剩余值','刚才已经说明了为什么选三。现在我们用十作例子，完整走两轮循环。'),
}

class MethodLesson(TeachingScene):
    method='brute'
    def construct(self):
        name,idea,caption=INTRO[self.method]
        if self.method=='dp':
            self.cards('整数拆分：先看思路，再看代码',[
                ('动态规划：把小问题的答案先存起来',
                 'dp[i] = max(dp[i], j×(i−j), j×dp[i−j])',
                 '先确定 dp[i] 的含义，再从二开始往上填。右边可以保持原样，也可以使用已经算好的 dp[i−j]。')
            ])
        else:
            self.cards(name,[(idea,'',caption)])
        title=text({'brute':'方法一：暴力递归','divide':'方法四：分治递归','dp':'方法三：动态规划','greedy':'方法二：贪心算法'}[self.method],37).move_to([0,3.45,0]);self.add(title)
        sub={'brute':'F(n) = integerBreak(n)，必须至少拆成两份','divide':'F 必须拆一次；B(x) = best(x)，允许不拆','dp':'dp[i]：把 i 至少拆成两份后的最大乘积','greedy':'示例 n=10；尽量取 3，剩下 4 时保留'}[self.method]
        self.add(text(sub,22,MUTED).move_to([0,2.95,0]))
        gap=.255 if self.method=='divide' else .35;top=2.35
        for k,line in enumerate(CODES[self.method]):
            indent=len(line)-len(line.lstrip());obj=text(line.lstrip() or ' ',18 if self.method=='divide' else 20,INK,6-indent*.045)
            obj.move_to([-6.75+indent*.045,top-k*gap,0],aligned_edge=LEFT);self.add(obj)
        hi=Rectangle(width=6.25,height=gap*.94,stroke_color=ORANGE,fill_color=ORANGE,fill_opacity=.12).move_to([-3.6,top,0]);self.add(hi)
        frames={'brute':brute_frames,'divide':divide_frames,'dp':dp_frames,'greedy':greedy_frames}[self.method]()
        previous=None;last=None;history=None;finished=[]
        for index,f in enumerate(frames):
            g=VGroup()
            if 'nodes' in f:g.add(tree(f['nodes'],f['edges']))
            if 'table' in f:g.add(table(f['table'],y=.55 if self.method=='dp' else .4))
            if self.method=='dp':
                if 'table' not in f:
                    if 'source' in f:
                        s=f['source'];g.add(box(f'dp[{s}] = {f["dp"][s]}',3.4,.7,BLUE,3.0),text('读取已经算好的结果',23,BLUE).move_to([3.4,1.65,0]))
                    else:g.add(text('从小到大，只求一次',27,ORANGE,6).move_to([3.4,1.3,0]))
                for i,v in enumerate(f['dp']):
                    color=GREEN if i==f.get('active') and f.get('write') else ORANGE if i==f.get('active') else BLUE if i==f.get('source') else MUTED
                    g.add(box(v,-5.35+i*1.78,-2.35,color,1.5),text(f'dp[{i}]',18,MUTED).move_to([-5.35+i*1.78,-1.75,0]))
            if 'numbers' in f:
                count=len(f['numbers'])
                for j,v in enumerate(f['numbers']):g.add(box(v,3.4+(j-(count-1)/2)*2,.5,GREEN,1.8))
            formula_y=-.8 if self.method=='dp' else -2.35
            g.add(text(f['formula'],25,GREEN,6.3 if self.method=='dp' else 13).move_to([3.4 if self.method=='dp' else 0,formula_y,0]))
            cap=text(f['caption'],24,INK,13.4).move_to([0,-3.5,0])
            if last is not None:self.remove(last)
            start=self.time
            if self.method in ('brute','divide'):
                if self.method=='brute':
                    if index==10:finished.append('已完成：1 + 5 → 6')
                    if index==15:finished.append('已完成：2 + 4 → 8')
                else:
                    if index==10:finished.append('已完成：1 + 5 → 6')
                    if index==13:finished.append('已完成：2 + 4 → 8')
                status=text('   '.join(finished),17,MUTED,6.5).move_to([3.4,2.5,0])
                if history is not None:self.remove(history)
                self.add(status);history=status
            switching_table=previous is not None and ('table' in f or 'table' in frames[index-1])
            # Rebuilding the DP grid is much faster than morphing every cell and label.
            # Keep Transform for the two recursion trees so their branches evolve on screen.
            if previous is not None and (switching_table or self.method=='dp'):
                self.remove(previous);previous=None
            change=FadeIn(g) if previous is None else Transform(previous,g)
            self.play(hi.animate.move_to([-3.6,top-f['line']*gap,0]),change,FadeIn(cap),run_time=.6 if previous is not None else .4)
            self.wait(max(f.get('hold',6),min(11,len(f['caption'])/5)))
            self.cues.append([start,self.time,f['caption']]);previous=g if previous is None else previous;last=cap
            if index%5==0:print(f'LESSON {self.method} {index+1}/{len(frames)}',flush=True)
        self.wait(3);save(self)

class BruteLesson(MethodLesson):method='brute'
class DivideLesson(MethodLesson):method='divide'
class DPLesson(MethodLesson):method='dp'
class GreedyLesson(MethodLesson):method='greedy'

class Closing(TeachingScene):
    def construct(self):
        self.cards('最后把思路串起来',[
            ('暴力与分治：把选择展开','暴力固定左边；分治处理左右两边','两种递归都可能反复求同一个问题。树上出现相同的节点，是理解重复计算的线索。'),
            ('动态规划与贪心：用不同方式减少工作','动态规划保存答案；贪心利用已证明的选择规律','动态规划仍比较候选，但不重复求状态；贪心则根据证明，直接选择尽量多的三。'),
            ('回到这道题','n=6 的答案是 9；n=10 的答案是 36','遇到类似问题时，先说明状态和选择，再判断能否保存子问题，或者证明一个贪心规律。'),
        ]);save(self)

class ComplexitySummary(TeachingScene):
    def construct(self):
        self.cards('最后比较：哪里多算了？',[
            ('动态规划：避免重复求状态','每个 dp[i] 填好一次，后面直接读取','它仍然枚举每个 j，但同一个 dp[i-j] 不会再沿递归树重新展开。这里省掉的是重复求子问题。'),
            ('时间复杂度：按你这四份代码','暴力 O(2ⁿ)；分治 O(3ⁿ)','这两份原始递归都没有缓存。分治在每个切分处递归左右两边，所以增长更快。'),
            ('动态规划与贪心的复杂度','动态规划 O(n²)；贪心 O(n)','动态规划有两层循环；贪心每次减三。空间分别为 O(n) 与 O(1)。两种递归的调用栈都是 O(n)。'),
        ]);save(self)
