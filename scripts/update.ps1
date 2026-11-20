# PythonGO 手册：一键更新
# 用法：  powershell -ExecutionPolicy Bypass -File scripts\update.ps1           # 增量：只抓新页面
#         powershell -ExecutionPolicy Bypass -File scripts\update.ps1 -Force  # 全量：重新抓取所有页面
param([switch]$Force)

$ErrorActionPreference = "Stop"
$env:PYTHONUTF8 = "1"          # Python 输入输出统一 UTF-8，避免中文乱码
$env:PYTHONIOENCODING = "utf-8"
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
    $py = "python"
    $args1 = @()
    if ($Force) { $args1 += "--force" }

    Write-Host "== 1/5 抓取站点" -ForegroundColor Cyan
    & $py "scripts\01_fetch.py" @args1
    if ($LASTEXITCODE -ne 0) { throw "抓取失败" }

    Write-Host "== 2/5 生成整页 Markdown (docs/)" -ForegroundColor Cyan
    & $py "scripts\02_docs.py"
    if ($LASTEXITCODE -ne 0) { throw "生成 docs 失败" }

    Write-Host "== 3/5 拆分 API 速查卡 (api/)" -ForegroundColor Cyan
    & $py "scripts\03_api.py"
    if ($LASTEXITCODE -ne 0) { throw "生成 api 失败" }

    Write-Host "== 4/5 生成索引 (index/)" -ForegroundColor Cyan
    & $py "scripts\04_index.py"
    if ($LASTEXITCODE -ne 0) { throw "生成索引失败" }

    Write-Host "== 5/5 校验链接与锚点" -ForegroundColor Cyan
    & $py "scripts\05_check.py"
    if ($LASTEXITCODE -ne 0) { throw "校验失败" }

    Write-Host "完成。直接问 AI 即可，或看 README.md" -ForegroundColor Green
}
finally {
    Pop-Location
}
