# coding: utf-8
"""Writes django-request-flow.html next to this script."""
import os

OUT = os.path.join(os.path.dirname(__file__), 'django-request-flow.html')

parts = []

# ── PART 1: HEAD + CSS ────────────────────────────────────────────────────────
parts.append("""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Django 请求全流程</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Noto+Sans+SC:wght@300;400;600;700&display=swap');
    :root{
      --bg:#0d1117;--sf:#161b22;--sf2:#1f2937;--bd:#30363d;
      --tx:#e6edf3;--mu:#7d8590;
      --blue:#58a6ff;--green:#3fb950;--orange:#f0883e;
      --purple:#bc8cff;--red:#ff7b72;--cyan:#39d353;--yellow:#e3b341;
    }
    *{margin:0;padding:0;box-sizing:border-box}
    body{background:var(--bg);color:var(--tx);font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif;height:100vh;display:flex;flex-direction:column;overflow:hidden;}
    header{display:flex;align-items:center;justify-content:space-between;padding:.72rem 1.4rem;border-bottom:1px solid var(--bd);flex-shrink:0;gap:1rem;}
    .hl{display:flex;align-items:center;gap:.8rem;}
    .badge{font-family:'JetBrains Mono',monospace;font-size:.6rem;font-weight:700;color:var(--blue);background:rgba(88,166,255,.1);border:1px solid rgba(88,166,255,.3);padding:.18rem .48rem;border-radius:4px;letter-spacing:.07em;white-space:nowrap;}
    .htitle{font-size:.98rem;font-weight:700;line-height:1.2;}
    .hsub{font-size:.7rem;color:var(--mu);margin-top:.08rem;}
    .hurl{font-family:'JetBrains Mono',monospace;font-size:.7rem;background:var(--sf2);border:1px solid var(--bd);padding:.28rem .75rem;border-radius:6px;color:var(--cyan);display:flex;align-items:center;gap:.38rem;}
    .hurl .m{background:rgba(88,166,255,.18);color:var(--blue);font-weight:700;padding:.08rem .3rem;border-radius:3px;font-size:.62rem;}
    .layout{flex:1;display:grid;grid-template-columns:248px 1fr;overflow:hidden;}
    .sidebar{border-right:1px solid var(--bd);overflow-y:auto;padding:.9rem .7rem;display:flex;flex-direction:column;gap:.08rem;}
    .sbl{font-size:.58rem;font-weight:700;color:var(--mu);text-transform:uppercase;letter-spacing:.1em;padding:0 .38rem;margin-bottom:.5rem;}
    .srow{display:flex;align-items:flex-start;gap:.55rem;padding:.52rem .38rem;border-radius:7px;cursor:pointer;transition:background .15s;border-left:2px solid transparent;}
    .srow:hover{background:rgba(255,255,255,.04);}
    .srow.is-active{background:rgba(88,166,255,.07);}
    .srow.is-done .sdot{background:var(--green)!important;color:#000!important;box-shadow:none!important;}
    .srow.is-done .stitle{color:var(--mu);}
    .sdot{width:21px;height:21px;border-radius:50%;background:var(--bd);color:var(--mu);font-family:'JetBrains Mono',monospace;font-size:.61rem;font-weight:700;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .3s;}
    .srow.is-active .sdot{color:#000;box-shadow:0 0 9px rgba(88,166,255,.6);}
    .sinfo{flex:1;}
    .stitle{font-size:.78rem;font-weight:600;line-height:1.3;}
    .ssub{font-size:.63rem;color:var(--mu);margin-top:.1rem;font-family:'JetBrains Mono',monospace;}
    .stag{display:inline-block;font-size:.54rem;font-weight:700;padding:.07rem .3rem;border-radius:3px;margin-top:.2rem;text-transform:uppercase;letter-spacing:.04em;}
    .main{display:flex;flex-direction:column;overflow:hidden;}
    .fscroll{flex:1;overflow-y:auto;padding:1.2rem 1.6rem;}
    .fwrap{max-width:660px;margin:0 auto;display:flex;flex-direction:column;align-items:center;}
    .fnode{width:100%;background:var(--sf);border:1px solid var(--bd);border-radius:10px;padding:.85rem 1.05rem;transition:all .35s cubic-bezier(.4,0,.2,1);opacity:.26;transform:translateX(-5px);}
    .fnode.lit{opacity:1;transform:translateX(0);}
    .fnode.done{opacity:.76;transform:translateX(0);}
    .nh{display:flex;align-items:center;gap:.52rem;margin-bottom:.42rem;}
    .nicon{font-size:.98rem;}
    .ntitle{font-size:.88rem;font-weight:700;flex:1;}
    .ntag{font-family:'JetBrains Mono',monospace;font-size:.56rem;font-weight:700;padding:.12rem .42rem;border-radius:4px;text-transform:uppercase;letter-spacing:.04em;}
    .nbody{font-size:.77rem;color:var(--mu);line-height:1.65;}
    .nbody strong{color:var(--tx);}
    .nbody code{font-family:'JetBrains Mono',monospace;font-size:.72rem;background:rgba(88,166,255,.1);color:var(--blue);padding:.06rem .26rem;border-radius:3px;}
    .ncode{margin-top:.52rem;background:#010409;border:1px solid var(--bd);border-radius:6px;padding:.52rem .78rem;font-family:'JetBrains Mono',monospace;font-size:.7rem;line-height:1.72;white-space:pre;overflow-x:auto;display:none;}
    .fnode.lit .ncode,.fnode.done .ncode{display:block;}
    .ckw{color:#ff79c6;}.cfn{color:#50fa7b;}.cstr{color:#f1fa8c;}.ccm{color:#6272a4;font-style:italic;}.ccls{color:#8be9fd;}.cnum{color:#bd93f9;}
    .farrow{display:flex;flex-direction:column;align-items:center;padding:.12rem 0;}
    .aline{width:2px;height:25px;background:var(--bd);transition:background .4s;}
    .farrow.lit .aline{background:linear-gradient(to bottom,var(--green),var(--bd));}
    .ahead{width:0;height:0;border-left:5px solid transparent;border-right:5px solid transparent;border-top:7px solid var(--bd);transition:border-top-color .4s;}
    .farrow.lit .ahead{border-top-color:var(--green);}
    .alabel{font-size:.58rem;color:var(--mu);font-family:'JetBrains Mono',monospace;margin-top:.1rem;}
    .infobar{border-top:1px solid var(--bd);background:var(--sf);padding:.92rem 1.6rem;display:flex;gap:1.2rem;flex-shrink:0;min-height:128px;}
    .ibm{flex:1;}
    .ibt{font-size:.88rem;font-weight:700;display:flex;align-items:center;gap:.42rem;margin-bottom:.32rem;}
    .ibd{font-size:.77rem;color:var(--mu);line-height:1.68;max-width:490px;}
    .ibd b{color:var(--blue);}
    .ibd code{font-family:'JetBrains Mono',monospace;font-size:.71rem;background:rgba(88,166,255,.1);color:var(--blue);padding:.06rem .26rem;border-radius:3px;}
    .ibs{width:195px;flex-shrink:0;}
    .ibsl{font-size:.58rem;color:var(--mu);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.42rem;}
    .kv{display:flex;align-items:flex-start;gap:.32rem;margin-bottom:.25rem;font-size:.7rem;}
    .kv .k{color:var(--mu);font-family:'JetBrains Mono',monospace;min-width:58px;flex-shrink:0;}
    .kv .v{color:var(--tx);font-family:'JetBrains Mono',monospace;word-break:break-all;}
    .controls{border-top:1px solid var(--bd);padding:.6rem 1.6rem;display:flex;align-items:center;gap:.55rem;background:var(--bg);flex-shrink:0;}
    .btn{display:flex;align-items:center;gap:.32rem;padding:.38rem .95rem;border-radius:6px;border:1px solid var(--bd);background:var(--sf);color:var(--tx);font-size:.76rem;font-family:inherit;cursor:pointer;transition:all .18s;white-space:nowrap;}
    .btn:hover{border-color:var(--blue);color:var(--blue);}
    .btn.primary{background:var(--blue);border-color:var(--blue);color:#000;font-weight:700;}
    .btn.primary:hover{background:#79baff;}
    .btn.danger{color:var(--red);border-color:var(--red);}
    .btn.danger:hover{background:rgba(255,123,114,.08);}
    .btn:disabled{opacity:.3;cursor:not-allowed;pointer-events:none;}
    .ptrack{flex:1;height:3px;background:var(--bd);border-radius:2px;overflow:hidden;}
    .pfill{height:100%;background:linear-gradient(90deg,var(--blue),var(--green));border-radius:2px;transition:width .4s cubic-bezier(.4,0,.2,1);}
    .sctr{font-family:'JetBrains Mono',monospace;font-size:.68rem;color:var(--mu);white-space:nowrap;}
    .autobtn{color:var(--yellow);border-color:rgba(227,179,65,.4);}
    .autobtn:hover,.autobtn.on{background:rgba(227,179,65,.08);border-color:var(--yellow);color:var(--yellow);}
    .pdot{width:7px;height:7px;border-radius:50%;background:var(--green);display:none;}
    .pdot.on{display:block;animation:pdotA 1s ease-in-out infinite;}
    @keyframes pdotA{0%,100%{opacity:1}50%{opacity:.2}}
    .tc{background:rgba(188,140,255,.15);color:var(--purple);}
    .tw{background:rgba(240,136,62,.15);color:var(--orange);}
    .tu{background:rgba(88,166,255,.15);color:var(--blue);}
    .tv{background:rgba(63,185,80,.15);color:var(--green);}
    .td{background:rgba(255,123,114,.15);color:var(--red);}
    .tt{background:rgba(227,179,65,.15);color:var(--yellow);}
    .ttr{background:rgba(57,211,83,.15);color:var(--cyan);}
    .fnode.lit.nc{border-color:var(--purple);box-shadow:0 0 0 1px var(--purple),0 0 18px rgba(188,140,255,.14);}
    .fnode.lit.nw{border-color:var(--orange);box-shadow:0 0 0 1px var(--orange),0 0 18px rgba(240,136,62,.14);}
    .fnode.lit.nu{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue),0 0 18px rgba(88,166,255,.14);}
    .fnode.lit.nv{border-color:var(--green);box-shadow:0 0 0 1px var(--green),0 0 18px rgba(63,185,80,.14);}
    .fnode.lit.nd{border-color:var(--red);box-shadow:0 0 0 1px var(--red),0 0 18px rgba(255,123,114,.14);}
    .fnode.lit.nt{border-color:var(--yellow);box-shadow:0 0 0 1px var(--yellow),0 0 18px rgba(227,179,65,.14);}
    .fnode.lit.ntr{border-color:var(--cyan);box-shadow:0 0 0 1px var(--cyan),0 0 18px rgba(57,211,83,.14);}
    ::-webkit-scrollbar{width:5px;height:5px;}
    ::-webkit-scrollbar-thumb{background:var(--bd);border-radius:3px;}
    ::-webkit-scrollbar-track{background:transparent;}
  </style>
</head>
<body>
""")

# ── PART 2: HTML STRUCTURE ────────────────────────────────────────────────────
parts.append("""<header>
  <div class="hl">
    <span class="badge">DJANGO REQUEST LIFECYCLE</span>
    <div>
      <div class="htitle">HTTP 请求全流程可视化</div>
      <div class="hsub">从浏览器发出请求 → WSGI → 中间件 → URL路由 → 视图 → 数据库 → 模板 → 响应</div>
    </div>
  </div>
  <div class="hurl"><span class="m">GET</span>/blog/post/5/ HTTP/1.1</div>
</header>

<div class="layout">
  <aside class="sidebar">
    <div class="sbl">流程步骤</div>
    <div id="stepList"></div>
  </aside>
  <div class="main">
    <div class="fscroll"><div class="fwrap" id="flowWrap"></div></div>
    <div class="infobar" id="infobar">
      <div class="ibm">
        <div class="ibt" id="ibTitle">&#128100; 等待开始</div>
        <div class="ibd" id="ibDesc">点击下方「下一步」按钮，逐步追踪一次 HTTP 请求从浏览器到 Django 服务器的完整旅程。</div>
      </div>
      <div class="ibs">
        <div class="ibsl">当前层级</div>
        <div id="ibMeta"></div>
      </div>
    </div>
    <div class="controls">
      <button class="btn" id="btnPrev" disabled>&#8592; 上一步</button>
      <button class="btn primary" id="btnNext">下一步 &#8594;</button>
      <button class="btn autobtn" id="btnAuto">&#9654; 自动播放</button>
      <div class="pdot" id="pdot"></div>
      <div class="ptrack"><div class="pfill" id="pfill" style="width:0%"></div></div>
      <div class="sctr" id="sctr">0 / 8</div>
      <button class="btn danger" id="btnReset">&#8635; 重置</button>
    </div>
  </div>
</div>
""")

# ── PART 3: JS DATA + LOGIC ─────────────────────────────────────────────────
parts.append("""
<script>
const STEPS = [
  {
    id: 'client',
    icon: '🌐',
    title: '浏览器发起请求',
    sub: 'HTTP Request',
    tag: '客户端', tagCls: 'tc', nodeCls: 'nc',
    desc: '用户在浏览器输入 URL 或点击链接，浏览器构造 <b>HTTP 请求报文</b>，包含请求方法、路径、请求头（Headers）、Cookie 等，通过 TCP 连接发送到服务器。',
    meta: [['层级','客户端 Client'],['协议','HTTP/1.1'],['方法','GET'],['路径','/blog/post/5/']],
    code: `<span class="ccm"># 浏览器发出的 HTTP 请求报文</span>\nGET /blog/post/5/ HTTP/1.1\nHost: www.example.com\nAccept: text/html\nCookie: sessionid=abc123\nUser-Agent: Mozilla/5.0`
  },
  {
    id: 'wsgi',
    icon: '⚙️',
    title: 'WSGI/ASGI 接收并封装请求',
    sub: 'HttpRequest 对象',
    tag: 'Django 服务器', tagCls: 'tw', nodeCls: 'nw',
    desc: 'Django 通过 <code>WSGI</code>（同步）或 <code>ASGI</code>（异步）服务器接收原始 HTTP 请求，将其封装为 <b>HttpRequest 对象</b>，该对象携带了本次请求的全部信息。',
    meta: [['层级','WSGI/ASGI'],['对象','HttpRequest'],['文件','wsgi.py']],
    code: `<span class="ccm"># HttpRequest 核心属性</span>\nrequest.method   <span class="ccm"># 'GET' 或 'POST'</span>\nrequest.path     <span class="ccm"># '/blog/post/5/'</span>\nrequest.GET      <span class="ccm"># 查询参数 QueryDict</span>\nrequest.POST     <span class="ccm"># POST 数据</span>\nrequest.user     <span class="ccm"># 当前登录用户</span>\nrequest.COOKIES  <span class="ccm"># Cookie 字典</span>\nrequest.session  <span class="ccm"># Session 数据</span>`
  },
  {
    id: 'middleware_req',
    icon: '🔒',
    title: '中间件（请求阶段）',
    sub: 'Middleware → process_request',
    tag: '中间件', tagCls: 'tu', nodeCls: 'nu',
    desc: '请求依次经过 <code>settings.py</code> 中 <code>MIDDLEWARE</code> 列表从上到下的每个中间件。每个中间件可以拦截、修改或放行请求，执行 Session 解析、CSRF 校验、身份认证等工作。',
    meta: [['层级','Middleware'],['方向','process_request'],['文件','settings.py']],
    code: `<span class="ccm"># settings.py</span>\nMIDDLEWARE = [\n    <span class="cstr">'django.middleware.security.SecurityMiddleware'</span>,\n    <span class="cstr">'django.contrib.sessions.middleware.SessionMiddleware'</span>,\n    <span class="cstr">'django.middleware.csrf.CsrfViewMiddleware'</span>,\n    <span class="cstr">'django.contrib.auth.middleware.AuthenticationMiddleware'</span>,\n    <span class="cstr">'django.contrib.messages.middleware.MessageMiddleware'</span>,\n]`
  },
  {
    id: 'urlconf',
    icon: '🗺️',
    title: 'URL 路由匹配',
    sub: 'urls.py → URLconf',
    tag: 'URL 路由', tagCls: 'tu', nodeCls: 'nu',
    desc: 'Django 用请求路径 <code>/blog/post/5/</code> 依次匹配 <code>urls.py</code> 中的 URL 模式，找到第一个匹配项后，提取路径参数并将请求转发给对应的<b>视图函数或视图类</b>。',
    meta: [['层级','URL Dispatcher'],['路径','/blog/post/5/'],['文件','urls.py'],['参数','pk=5']],
    code: `<span class="ccm"># urls.py</span>\n<span class="ckw">from</span> django.urls <span class="ckw">import</span> path\n<span class="ckw">from</span> . <span class="ckw">import</span> views\n\nurlpatterns = [\n    path(<span class="cstr">'blog/post/&lt;int:pk&gt;/'</span>, views.post_detail, name=<span class="cstr">'post-detail'</span>),\n]`
  },
  {
    id: 'view',
    icon: '👁️',
    title: '视图处理（View）',
    sub: 'views.py → 业务逻辑',
    tag: 'View 视图', tagCls: 'tv', nodeCls: 'nv',
    desc: '视图函数/类是 Django 的<b>控制器</b>，接收 <code>request</code> 对象和 URL 参数，执行业务逻辑：查询数据库、权限验证、数据处理，然后把数据传给模板进行渲染。',
    meta: [['层级','View'],['文件','views.py'],['参数','request, pk=5']],
    code: `<span class="ccm"># views.py</span>\n<span class="ckw">from</span> django.shortcuts <span class="ckw">import</span> render, get_object_or_404\n<span class="ckw">from</span> .models <span class="ckw">import</span> Post\n\n<span class="ckw">def</span> <span class="cfn">post_detail</span>(request, pk):\n    post = get_object_or_404(<span class="ccls">Post</span>, pk=pk)\n    <span class="ckw">return</span> render(request, <span class="cstr">'blog/post_detail.html'</span>, {<span class="cstr">'post'</span>: post})`
  },
  {
    id: 'db',
    icon: '🗄️',
    title: '数据库查询（ORM）',
    sub: 'models.py → SQL → DB',
    tag: '数据库', tagCls: 'td', nodeCls: 'nd',
    desc: 'Django ORM 将 Python 的模型查询语句自动转换为 <b>SQL 语句</b>，向数据库发起查询。查询结果以 Model 实例或 QuerySet 形式返回给视图，整个过程对开发者透明。',
    meta: [['层级','ORM / DB'],['文件','models.py'],['SQL','SELECT ... WHERE id=5']],
    code: `<span class="ccm"># models.py</span>\n<span class="ckw">class</span> <span class="ccls">Post</span>(models.<span class="ccls">Model</span>):\n    title   = models.<span class="cfn">CharField</span>(max_length=<span class="cnum">200</span>)\n    content = models.<span class="cfn">TextField</span>()\n    created = models.<span class="cfn">DateTimeField</span>(auto_now_add=<span class="ckw">True</span>)\n\n<span class="ccm"># ORM 自动生成的 SQL：</span>\n<span class="ccm"># SELECT * FROM blog_post WHERE id = 5 LIMIT 1;</span>`
  },
  {
    id: 'template',
    icon: '🎨',
    title: '模板渲染（Template）',
    sub: 'templates/*.html → HTML',
    tag: '模板', tagCls: 'tt', nodeCls: 'nt',
    desc: '视图将数据传入 <b>Django 模板引擎</b>，模板文件中的变量 <code>{{ post.title }}</code> 和标签 <code>{% for %}</code> 被替换为真实数据，最终生成完整的 HTML 字符串。',
    meta: [['层级','Template'],['文件','post_detail.html'],['引擎','Django Template']],
    code: `<span class="ccm">{# templates/blog/post_detail.html #}</span>\n&lt;h1&gt;<span class="cstr">{{ post.title }}</span>&lt;/h1&gt;\n&lt;p&gt;<span class="cstr">{{ post.content }}</span>&lt;/p&gt;\n&lt;small&gt;发布于 <span class="cstr">{{ post.created|date:&quot;Y-m-d&quot; }}</span>&lt;/small&gt;`
  },
  {
    id: 'middleware_resp',
    icon: '🔁',
    title: '中间件（响应阶段）',
    sub: 'Middleware → process_response',
    tag: '中间件', tagCls: 'tu', nodeCls: 'nu',
    desc: '生成 HttpResponse 后，请求<b>反向</b>经过中间件列表（从下到上），各中间件可在响应返回客户端前对其进行处理，例如添加安全头、压缩、设置 Cookie 等。',
    meta: [['层级','Middleware'],['方向','process_response'],['顺序','逆序（从下到上）']],
    code: `<span class="ccm"># 自定义中间件示例</span>\n<span class="ckw">class</span> <span class="ccls">TimingMiddleware</span>:\n    <span class="ckw">def</span> <span class="cfn">process_response</span>(self, request, response):\n        response[<span class="cstr">'X-Process-Time'</span>] = <span class="cstr">'12ms'</span>\n        <span class="ckw">return</span> response`
  },
  {
    id: 'response',
    icon: '✅',
    title: '返回 HTTP 响应',
    sub: 'HttpResponse → 浏览器',
    tag: '响应', tagCls: 'ttr', nodeCls: 'ntr',
    desc: 'Django 将渲染好的 HTML 封装为 <b>HttpResponse 对象</b>（状态码 200、响应头、响应体），通过 WSGI/ASGI 写回 TCP 连接，浏览器接收后解析 HTML 并渲染页面，用户看到最终结果。',
    meta: [['层级','Response'],['状态码','200 OK'],['Content-Type','text/html']],
    code: `<span class="ccm"># HTTP 响应报文</span>\nHTTP/1.1 200 OK\nContent-Type: text/html; charset=utf-8\nSet-Cookie: csrftoken=xyz\nX-Frame-Options: DENY\n\n&lt;!DOCTYPE html&gt;\n&lt;html&gt;...渲染好的页面...&lt;/html&gt;`
  }
];

const ARROWS = [
  'TCP 传输',
  '封装对象',
  '请求链',
  'URL 匹配',
  'ORM 查询',
  'SQL 结果',
  '数据注入',
  '响应链',
];

let cur = -1;
let autoTimer = null;

function buildDOM() {
  const wrap = document.getElementById('flowWrap');
  const list = document.getElementById('stepList');
  wrap.innerHTML = '';
  list.innerHTML = '';

  STEPS.forEach((s, i) => {
    // flow node
    const node = document.createElement('div');
    node.className = 'fnode ' + s.nodeCls;
    node.id = 'fn' + i;
    node.innerHTML = `
      <div class="nh">
        <span class="nicon">${s.icon}</span>
        <span class="ntitle">${s.title}</span>
        <span class="ntag ${s.tagCls}">${s.tag}</span>
      </div>
      <div class="nbody">${s.desc}</div>
      <div class="ncode">${s.code}</div>
    `;
    wrap.appendChild(node);

    // arrow (not after last)
    if (i < STEPS.length - 1) {
      const arr = document.createElement('div');
      arr.className = 'farrow';
      arr.id = 'fa' + i;
      arr.innerHTML = `<div class="aline"></div><div class="ahead"></div><div class="alabel">${ARROWS[i] || ''}</div>`;
      wrap.appendChild(arr);
    }

    // sidebar row
    const row = document.createElement('div');
    row.className = 'srow';
    row.id = 'sr' + i;
    row.innerHTML = `
      <div class="sdot" style="background:none;border:1px solid var(--bd)">${i + 1}</div>
      <div class="sinfo">
        <div class="stitle">${s.title}</div>
        <div class="ssub">${s.sub}</div>
        <span class="stag ${s.tagCls}">${s.tag}</span>
      </div>
    `;
    row.addEventListener('click', () => goTo(i));
    list.appendChild(row);
  });
}

function goTo(idx) {
  if (idx < 0 || idx >= STEPS.length) return;
  const prev = cur;
  cur = idx;

  STEPS.forEach((s, i) => {
    const node = document.getElementById('fn' + i);
    const row  = document.getElementById('sr' + i);
    const sdot = row.querySelector('.sdot');
    node.classList.remove('lit', 'done');
    row.classList.remove('is-active', 'is-done');

    if (i < cur) {
      node.classList.add('done');
      row.classList.add('is-done');
      sdot.style.background = '';
      sdot.style.border = '';
    } else if (i === cur) {
      node.classList.add('lit');
      row.classList.add('is-active');
      sdot.style.background = `var(${['--purple','--orange','--blue','--blue','--green','--red','--yellow','--blue','--cyan'][i] || '--blue'})`;
      sdot.style.border = 'none';
    } else {
      sdot.style.background = 'none';
      sdot.style.border = '1px solid var(--bd)';
    }

    