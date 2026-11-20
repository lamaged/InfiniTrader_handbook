# -*- coding: utf-8 -*-
"""01：抓取 PythonGO v2 文档站
   首页定位 buildId -> 页面清单(buildManifest) -> 搜索索引(nextra-data) -> 逐页 HTML
用法：python scripts/01_fetch.py [--force]   (--force 强制重新下载已有页面)
"""
import io, json, os, re, sys, time, urllib.request

BASE = "https://infinitrader.quantdo.com.cn/pythongo_v2"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, "_raw")
PAGES = os.path.join(RAW, "pages")
os.makedirs(PAGES, exist_ok=True)
FORCE = "--force" in sys.argv


def http(url, retries=3, timeout=40, binary=False):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) handbook-mirror/1.0",
                "Accept": "text/html,application/xhtml+xml,application/json;q=0.9,*/*;q=0.8",
                "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            })
            with urllib.request.urlopen(req, timeout=timeout) as r:
                data = r.read()
            return data if binary else data.decode("utf-8", "replace")
        except Exception as e:
            last = e
            time.sleep(1.5 * (i + 1))
    raise last


def find_build_id():
    home = http(BASE)
    m = re.search(r"/pythongo_v2/_next/static/([^/\"']+)/_buildManifest\.js", home)
    if not m:
        raise SystemExit("未找到 buildId，站点结构可能已变化")
    return m.group(1)


def routes_from_manifest(js):
    rs = re.findall(r'"(/[^"]*)":\s*\[', js)
    seen, out = set(), []
    for r in rs:
        if r.startswith("/_") or r.endswith("/_meta") or r in seen:
            continue
        seen.add(r)
        out.append(r)
    return out


def safe_name(route):
    return "index" if route == "/" else route.strip("/").replace("/", "__")


def main():
    build_id = find_build_id()
    url = f"{BASE}/_next/static/{build_id}/_buildManifest.js"
    js = http(url)
    io.open(os.path.join(RAW, "buildManifest.js"), "w", encoding="utf-8").write(js)
    print("buildId:", build_id)

    for name in ["nextra-data-en-US.json", "nextra-data-zh-CN.json"]:
        try:
            data = http(f"{BASE}/_next/static/chunks/{name}")
            io.open(os.path.join(RAW, "nextra-data.json"), "w", encoding="utf-8").write(data)
            print("search index:", name, len(data), "bytes")
            break
        except Exception:
            continue

    routes = routes_from_manifest(js)
    print("routes:", len(routes))
    ok, fail = 0, []
    for i, r in enumerate(routes, 1):
        target = BASE + ("/" if r == "/" else r)
        dst = os.path.join(PAGES, safe_name(r) + ".html")
        if not FORCE and os.path.exists(dst) and os.path.getsize(dst) > 1000:
            ok += 1
            continue
        try:
            html = http(target)
            io.open(dst, "w", encoding="utf-8").write(html)
            ok += 1
            print(f"[{i}/{len(routes)}] {r} {len(html)//1024}KB")
        except Exception as e:
            fail.append((r, str(e)))
            print(f"[{i}/{len(routes)}] FAIL {r} {e}")
        time.sleep(0.35)
    print("OK", ok, "FAIL", len(fail))
    for r, e in fail:
        print("  ", r, e)
    json.dump([{"route": r, "file": safe_name(r) + ".html"} for r in routes],
              io.open(os.path.join(RAW, "routes.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
