from pathlib import Path
import av,json,subprocess
ROOT=Path('E:/postgraduate/leetCode/integer_break_manim_lesson_v4')
video=ROOT/'videos';sub=ROOT/'subtitles'
names=['Opening','BruteLesson','GreedyReason','GreedyLesson','DPLesson','DivideLesson','TreeComparison','ComplexitySummary']
titles=['四种算法概览','暴力递归：思路与两个例子','贪心：证明取3','贪心：思路与两轮循环','动态规划：思路、两例与每行结果','分治递归：思路与两个例子','结尾对比：重复子树与状态保存','结尾对比：时间复杂度']
durations={}
for name in names:
    with av.open(str(video/(name+'.mp4'))) as c:durations[name]=c.duration/1e6
assert sum(durations.values())<1200
def timestamp(t):
    m=round(t*1000);h,m=divmod(m,3600000);minute,m=divmod(m,60000);s,m=divmod(m,1000)
    return f'{h:02}:{minute:02}:{s:02},{m:03}'
def write_srt(name,cues):
    (sub/(name+'.srt')).write_text('\n\n'.join(f'{i}\n{timestamp(a)} --> {timestamp(b)}\n{caption}' for i,(a,b,caption) in enumerate(cues,1))+'\n',encoding='utf-8-sig')
offset=0;all_cues=[];chapters=[];script=['# LeetCode 343 配音稿\n\n时间对应完整视频；每条字幕是一句可直接朗读的提示。\n']
for name,title in zip(names,titles):
    cues=json.loads((sub/(name+'.json')).read_text(encoding='utf8'))
    assert all(0<=a<b<=durations[name]+.1 for a,b,t in cues)
    assert all('\n' not in t for a,b,t in cues)
    write_srt(name,cues)
    all_cues.extend([[a+offset,b+offset,t] for a,b,t in cues])
    chapters.append(f'- {int(offset)//60:02}:{int(offset)%60:02} {title}')
    script.append('\n## '+title+'\n')
    script.extend(f'\n**{timestamp(a+offset)[:-4]}** {t}\n' for a,b,t in cues)
    offset+=durations[name]
write_srt('343_lesson_v4_full',all_cues)
(ROOT/'配音稿.md').write_text(''.join(script),encoding='utf8')
(video/'lesson_concat.txt').write_text(''.join(f"file '{name}.mp4'\n" for name in names),encoding='ascii')
ffmpeg=r'D:\视频下载器\4K Video Downloader Subscribe\ffmpeg-x64.exe'
subprocess.run([ffmpeg,'-y','-hide_banner','-loglevel','error','-f','concat','-safe','0','-i','lesson_concat.txt','-c','copy','-movflags','+faststart','343_lesson_v4_full.mp4'],cwd=video,check=True)
chapters='\n'.join(chapters)
(ROOT/'README.md').write_text(f'''# LeetCode 343 思路与两例讲解版

完整视频：videos/343_lesson_v4_full.mp4

时长：{int(offset)//60} 分 {round(offset)%60} 秒，低于 20 分钟。

{chapters}

## 本版内容

每种算法在代码演示前先说明思路。视频结尾用重复 F(4) 的路径说明暴力树多出了哪些重复计算。
分治左右都递归，也会重复；动态规划把每个状态计算一次并保存。
F(x) 必须拆分，B(x) 允许不拆；暴力画面只解释 F。

暴力和分治的重点枚举只详细演示两个分法，其他分法以此类推，用候选表给出最终结果。
动态规划每一行最多详细演示两个 j，剩余候选显示在小表中，并更新该行最终值。
两段递归树在每一步连续变形，已完成分支的结果保留在画面上。结尾在时间复杂度分析后结束。省略画面是教学剪辑，不代表原递归算法使用了缓存。结尾给出四种方法的时间复杂度。

字幕采用单行口语讲解，直接显示在画面中；没有步数、配音或音乐。
每幅主要画面保留约 6—11 秒，便于理解和后期配音。

## 修改位置

- lesson_story.py：各个具体操作的讲解、数值、候选表和树节点。
- lesson_animation.py：开头思路、对比图、贪心证明，以及字幕布局和停留时间。
- subtitles：独立场景和完整版的 SRT 字幕。
- 配音稿.md：按完整视频时间排列的配音提示。
- render.ps1：重新生成独立场景。重渲染后需重新合成完整版。

视频主例子为 n=6；贪心使用 n=10 展示两轮循环。
''',encoding='utf8')
print(json.dumps(durations,ensure_ascii=False));print('TOTAL',offset)



