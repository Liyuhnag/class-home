# coding: utf-8
import pathlib, textwrap

HTML = """\
<!DOCTYPE html>
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
    body{
      background:var(--bg);color:var(--tx);
      font-family:'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif;
      height:100vh;display:flex;flex-direction:column;overflow:hidden;
    }
    header{
      display:flex;align-items:center;justify-content:space-between;
      padding:.72rem 1.4rem;border-bottom:1px solid var(--bd);flex-shrink:0;gap:1rem;
    }
    .hl{display:flex;align-items:center;gap:.8rem;}
    .badge{
      font-family:'JetBrains Mono',monospace;font-size:.6rem;font-weight:700;
      color:var(--blue);background:rgba(88,166,255,.1);border:1px solid rgba(88,166,255,.3);
      padding:.18rem .48rem;border-radius:4px;letter-spacing:.07em;white-space:nowrap;
    }
    .htitle{font-size:.98rem;font-weight:700;line-height:1.2;}
    .hsub{font-size:.7rem;color:var(--mu);margin-top:.08rem;}
    .hurl{
      font-family:'JetBrains Mono',monospace;font-size:.7rem;
      background:var(--sf2);border:1px solid var(--bd);
      padding:.28rem .75rem;border-radius:6px;color:var(--cyan);
      display:flex;align-items:center;gap:.38rem;
    }
    .hurl .m{
      background:rgba(88,166,255,.18);color:var(--blue);font-weight:700;
      padding:.08rem .3rem;border-radius:3px;font-size:.62rem;
    }
    .layout{flex:1;display:grid;grid-template-columns:248px 1fr;overflow:hidden;}
    .sidebar{
      border-right:1px solid var(--bd);overflow-y:auto;
      padding:.9rem .7rem;display:flex;flex-direction:column;gap:.08rem;
    }
    .sbl{
      font-size:.58rem;font-weight:700;color:var(--mu);
      text-transform:uppercase;letter-spacing:.1em;
      padding:0 .38rem;margin-bottom:.5rem;
    }
    .srow{
      display:flex;align-items:flex-start;gap:.55rem;
      padding:.52rem .38rem;border-radius:7px;
      cursor:pointer;transition:background .15s;
      border-left:2px solid transparent;
    }
    .srow:hover{background:rgba(255,255,255,.04);}
    .srow.is-active{background:rgba(88,166,255,.07);}
    .srow.is-done .sdot{background:var(--green)!important;color:#000!important;box-shadow:none!important;}
    .srow.is-done .stitle{color:var(--mu);}
    .sdot{
      width:21px;height:21px;border-radius:50%;background:var(--bd);color:var(--mu);
      font-family:'JetBrains Mono',monospace;font-size:.61rem;font-weight:700;
      display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:all .3s;
    }
    .srow.is-active .sdot{color:#000;box-shadow:0 0 9px rgba(88,166,255,.6);}
    .sinfo{flex:1;}
    .stitle{font-size:.78rem;font-weight:600;line-height:1.3;}
    .ssub{font-size:.63rem;color:var(--mu);margin-top:.1rem;font-family:'JetBrains Mono',monospace;}
    .stag{
      display:inline-block;font-size:.54rem;font-weight:700;
      padding:.07rem .3rem;border-radius:3px;margin-top:.2rem;
      text-transform:uppercase;letter-spacing:.04em;
    }
    .main{display:flex;flex-direction:column;overflow:hidden;}
    .fscroll{flex:1;overflow-y:auto;padding:1.2rem 1.6rem;}
    .fwrap{max-width:660px;margin:0 auto;display:flex;flex-direction:column;align-items:center;}
    .fnode{
      width:100%;background:var(--sf);border:1px solid var(--bd);
      border-radius:10px;padding:.85rem 1.05rem;
      transition:all .35s cubic-bezier(.4,0,.2,1);
      opacity:.26;transform:translateX(-5px);
    }
    .fnode.lit{opacity:1;transform:translateX(0);}
    .fnode.done{opacity:.76;transform:translateX(0);}
    .nh{display:flex;align-items:center;gap:.52rem;margin-bottom:.42rem;}
    .nicon{font-size:.98rem;}
    .ntitle{font-size:.88rem;font-weight:700;flex:1;}
    .ntag{
      font-family:'JetBrains Mono',monospace;font-size:.56rem;font-weight:700;
      padding:.12rem .42rem;border-radius:4px;text-transform:uppercase;letter-spacing:.04em;
    }
    .nbody{font-size:.77rem;color:var(--mu);line-height:1.65;}
    .nbody strong{color:var(--tx);}
    .nbody code{
      font-family:'JetBrains Mono',monospace;font-size:.72rem;
      background:rgba(88,166,255,.1);color:var(--blue);
      padding:.06rem .26rem;border-radius:3px;
    }
    .ncode{
      margin-top:.52rem;background:#010409;border:1px solid var(--bd);
      border-radius:6px;padding:.52rem .78rem;
      font-family:'JetBrains Mono',monospace;font-size:.7rem;
      line-height:1.72;white-space:pre;overflow-x:auto;display:none;
    }
    .fnode.lit .ncode,.fnode.done .ncode{display:block;}
    .ckw{color:#ff79c6;}.cfn{color:#50fa7b;}.cstr{color:#f1fa8c;}
    .ccm{color:#6272a4;font-style:italic;}.ccls{color:#8be9fd;}.cnum{color:#bd93f9;}
    .farrow{display:flex;flex-direction:column;align-items:center;padding:.12rem 0;}
    .aline{width:2px;height:25px;background:var(--bd);transition:background .4s;}
    .farrow.lit .aline{background:linear-gradient(to bottom,var(--green),var(--bd));}
    .ahead{
      width:0;height:0;
      border-left:5px solid transparent;border-right:5px solid transparent;
      border-top:7px solid var(--bd);transition:border-top-color .4s;
    }
    .farrow.lit .ahead{border-top-color:var(--green);}
    .alabel{font-size:.58rem;color:var(--mu);font-family:'JetBrains Mono',monospace;margin-top:.1rem;}
    .infobar{
      border-top:1px solid var(--bd);background:var(--sf);
      padding:.92rem 1.6rem;display:flex;gap:1.2rem;
      flex-shrink:0;min-height:128px;
    }
    .ibm{flex:1;}
    .ibt{
      font-size:.88rem;font-weight:700;
      display:flex;align-items:center;gap:.42rem;margin-bottom:.32rem;
    }
    .ibd{font-size:.77rem;color:var(--mu);line-height:1.68;max-width:490px;}
    .ibd b{color:var(--blue);}
    .ibd code{
      font-family:'JetBrains Mono',monospace;font-size:.71rem;
      background:rgba(88,166,255,.1);color:var(--blue);
      padding:.06rem .26rem;border-radius:3px;
    }
    .ibs{width:195px;flex-shrink:0;}
    .ibsl{font-size:.58rem;color:var(--mu);text-transform:uppercase;letter-spacing:.08em;margin-bottom:.42rem;}
    .kv{display:flex;align-items:flex-start;gap:.32rem;margin-bottom:.25rem;font-size:.7rem;}
    .kv .k{color:var(--mu);font-family:'JetBrains Mono',monospace;min-width:58px;flex-shrink:0;}
    .kv .v{color:var(--tx);font-family:'JetBrains Mono',monospace;word-break:break-all;}
    .controls{
      border-top:1px solid var(--bd);padding:.6rem 1.6rem;
      display:flex;align-items:center;gap:.55rem;
      background:var(--bg);flex-shrink:0;
    }
    .btn{
      display:flex;align-items:center;gap:.32rem;
      padding:.38rem .95rem;border-radius:6px;border:1px solid var(--bd);
      background:var(--sf);color:var(--tx);font-size:.76rem;
      font-family:inherit;cursor:pointer;transition:all .18s;white-space:nowrap;
    }
    .btn:hover{border-color:var(--blue);color:var(--blue);}
    .btn.primary{background:var(--blue);border-color:var(--blue);color:#000;font-weight:700;}
    .btn.primary:hover{background:#79baff;}
    .btn.danger{color:var(--red);border-color:var(--red);}
    .btn.danger:hover{background:rgba(255,123,114,.08);}
    .btn:disabled{opacity:.3;cursor:not-allowed;pointer-events:none;}
    .ptrack{flex:1;height:3px;background:var(--bd);border-radius:2px;overflow:hidden;}
    .pfill{
      height:100%;background:linear-gradient(90deg,var(--blue),var(--green));
      border-radius:2px;transition:width .4s cubic-bezier(.4,0,.2,1);
    }
    .sctr{font-family:'JetBrains Mono',monospace;font-size:.68rem;color:var(--mu);white-space:nowrap;}
    .autobtn{color:var(--yellow);border-color:rgba(227,179,65,.4);}
    .autobtn:hover{background:rgba(227,179,65,.08);border-color:var(--yellow);color:var(--yellow);}
    .autobtn.on{background:rgba(227,179,65,.1);}
    .pdot{width:7px;height:7px;border-radius:50%;background:var(--green);display:none;}
    .pdot.on{display:block;animation:pdotA 1s ease-in-out infinite;}
    @keyframes pdotA{0%,100%{opacity:1}50%{opacity:.2}}
    .tc{background:rgba(188,140,255,.15);color:var(--purple);}
    .tw{background:rgba(240,136,62,.15);color:var(--orange);}
    .tu{background:rgba(88,166,255,.15);color:var(--blue);}
    .tv{background:rgba(63,185,80,.15);color:var(--green);}
    .td{background:rgba(255,123,114,.15);color:var(--red);}
    .tt{background:rgba(227,179,65,.15);color:var(--yellow);}
    .tr{background:rgba(57,211,83,.15);color:var(--cyan);}
    .fnode.lit.nc{border-color:var(--purple);box-shadow:0 0 0 1px var(--purple),0 0 18px rgba(188,140,255,.14);}
    .fnode.lit.nw{border-color:var(--orange);box-shadow:0 0 0 1px var(--orange),0 0 18px rgba(240,136,62,.14);}
    .fnode.lit.nu{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue),0 0 18px rgba(88,166,255,.14);}
    .fnode.lit.nv{border-color:var(--green);box-shadow:0 0 0 1px var(--green),0 0 18px rgba(63,185,80,.14);}
    .fnode.lit.nd{border-color:var(--red);box-shadow:0 0 0 1px var(--red),0 0 18px rgba(255,123,114,.14);}
    .fnode.lit.nt{border-color:var(--yellow);box-shadow:0 0 0 1px var(--yellow),0 0 18px rgba(227,179,65,.14);}
    .fnode.lit.nr{border-color:var(--cyan);box-shadow:0 0 0 1px var(--cyan),0 0 18px rgba(57,211,83,.14);}
    ::-webkit-scrollbar{width:5px;height:5px;}
    ::-webkit-scrollbar-thumb{background:var(--bd);border-radius:3px;}
    ::-webkit-scrollbar-track{background:transparent;}
  </style>
</head>
<body>

<header>
  <div class="hl">
    <span class="badge">DJANGO REQUEST LIFECYCLE</span>
    <div>
      <div class="htitle">HTTP 请求全流程可视化</div>
      <div 