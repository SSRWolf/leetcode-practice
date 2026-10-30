param([string]$Scene='all', [double]$Hold=4)
$ErrorActionPreference='Stop'
Set-Location -LiteralPath $PSScriptRoot
$env:PYTHONUTF8='1'
$env:TRACE_HOLD=[string]$Hold
$env:TRACE_PROGRESS='1'
Remove-Item Env:TRACE_LIMIT -ErrorAction SilentlyContinue
$env:TEMP=Join-Path $PSScriptRoot 'temp'
$env:TMP=$env:TEMP
New-Item -ItemType Directory -Path $env:TEMP -Force | Out-Null
$scenes=@('Opening','TreeComparison','BruteLesson','GreedyReason','GreedyLesson','DPLesson','DivideLesson','ComplexitySummary')
if ($Scene -ne 'all') { $scenes=@($Scene) }
foreach ($name in $scenes) {
    & 'D:\Python\Python312\Scripts\manimgl.exe' lesson_animation.py $name -w -r 1280x720 --fps 15 --video_dir videos --config_file custom_config.yml
    if ($LASTEXITCODE -ne 0) { throw "Render failed: $name" }
}






