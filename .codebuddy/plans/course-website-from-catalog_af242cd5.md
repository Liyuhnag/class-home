---
name: course-website-from-catalog
overview: 基于《课程目录.md》构建淡色调风格的静态课程网站：首页展示课程目录并链接到各课程详情页，详情页提供课程资料与可下载资源入口。
design:
  architecture:
    framework: html
  styleKeywords:
    - 淡色调
    - 简洁现代
    - 高可读性
    - 轻量交互
  fontSystem:
    fontFamily: PingFang SC
    heading:
      size: 30px
      weight: 600
    subheading:
      size: 20px
      weight: 500
    body:
      size: 16px
      weight: 400
  colorSystem:
    primary:
      - "#7AA2E3"
      - "#8EC5FC"
      - "#A7D8F0"
    background:
      - "#F7FAFF"
      - "#FFFFFF"
      - "#EEF4FF"
    text:
      - "#1F2937"
      - "#4B5563"
      - "#6B7280"
    functional:
      - "#22C55E"
      - "#F59E0B"
      - "#EF4444"
      - "#3B82F6"
todos:
  - id: parse-catalog-map
    content: 解析课程目录并建立8节课页面映射
    status: completed
  - id: build-shared-assets
    content: 创建淡色主题样式与通用交互脚本
    status: completed
    dependencies:
      - parse-catalog-map
  - id: implement-homepage
    content: 实现首页课程目录展示与详情跳转
    status: completed
    dependencies:
      - build-shared-assets
  - id: implement-course-pages
    content: 批量创建8个课程详情页与统一导航
    status: completed
    dependencies:
      - build-shared-assets
  - id: add-downloads-and-verify
    content: Use [subagent:code-explorer] 校验下载链接与页面互链
    status: completed
    dependencies:
      - implement-homepage
      - implement-course-pages
---

## User Requirements

- 基于现有 `课程目录.md` 创建一个课程网站。
- 首页展示全部课程目录，并可进入每节课的独立详情页。
- 每个详情页需展示该课程的详细资料，并提供可点击下载的资源文件。
- 页面设计保持淡色调、简洁清晰、导航直观，确保下载功能可正常使用。

## Product Overview

- 网站由一个课程总览首页和多个课程详情页组成。
- 用户可从首页快速浏览课程并跳转到对应详情页。
- 在详情页中可查看课程主题、资料说明，并通过下载按钮获取文件。

## Core Features

- 首页课程卡片/列表展示与跳转。
- 8个独立课程详情页面的结构化内容展示。
- 每节课独立下载资源入口（支持浏览器下载）。
- 统一淡色视觉风格与清晰导航（首页返回、上一页/下一页或面包屑）。

## Tech Stack Selection

- **前端**：HTML5 + CSS3 + 原生 JavaScript
- **组织方式**：静态多页面结构，共享一套样式与脚本
- **数据来源**：`d:/class/homepage/课程目录.md`（已确认包含8节课内容）

## Implementation Approach

采用“**共享模板 + 独立页面**”策略：先建立统一样式与交互脚本，再实现首页目录渲染与8个详情页，最后接入下载文件并完成全站链接校验。
关键决策：

- 复用 `assets/css/main.css` 与 `assets/js/main.js`，避免重复代码，便于后续扩展课程。
- 课程页使用统一HTML骨架，仅替换课程内容与下载链接，降低维护成本。
- 下载使用标准 `<a download>` + 本地静态资源路径，保证兼容与可用性。  
性能与可靠性：
- 首页渲染复杂度 **O(n)**（n=8），无重计算热点。
- 静态资源按需加载，JS仅处理轻量导航与状态高亮，减少阻塞。
- 下载前统一校验资源路径，避免404与无效按钮。

## Implementation Notes (Execution Details)

- 优先复用共享样式类与布局容器，避免每页内联样式膨胀。
- 链接路径统一使用相对层级规范（首页到课程页、课程页回首页、课程页到下载目录）。
- 下载文件名采用稳定命名（如 `course-01-notes.pdf`），避免中文路径兼容问题。
- 控制变更范围仅限站点新增文件，不改动 `课程目录.md` 原始内容。

## Architecture Design

- 页面层：`index.html`（课程入口） + `courses/course-01~08.html`（详情页）。
- 资源层：`assets/css`（统一视觉）、`assets/js`（导航与交互）、`assets/downloads`（可下载文件）。
- 数据映射：按“第X节课 → course-0X.html → downloads/course-0X/*”固定映射，便于增量扩展。

## Directory Structure

## Directory Structure Summary

本实现为现有目录新增静态站点文件，形成“首页 + 8详情页 + 共享资源 + 下载资源”结构。

```text
d:/class/homepage/
├── 课程目录.md                           # [MODIFY] 不修改内容，仅作为课程信息来源参考
├── index.html                           # [NEW] 首页。展示课程目录、课程简介、跳转到各详情页；需包含统一导航与淡色布局
├── courses/
│   ├── course-01.html                   # [NEW] 第一节课详情页。展示课程要点与下载入口
│   ├── course-02.html                   # [NEW] 第二节课详情页。展示课程要点与下载入口
│   ├── course-03.html                   # [NEW] 第三节课详情页。展示课程要点与下载入口
│   ├── course-04.html                   # [NEW] 第四节课详情页。展示课程要点与下载入口
│   ├── course-05.html                   # [NEW] 第五节课详情页。展示课程要点与下载入口
│   ├── course-06.html                   # [NEW] 第六节课详情页。展示课程要点与下载入口
│   ├── course-07.html                   # [NEW] 第七节课详情页。展示课程要点与下载入口
│   └── course-08.html                   # [NEW] 第八节课详情页。展示课程要点与下载入口
└── assets/
    ├── css/
    │   └── main.css                     # [NEW] 全站样式。淡色主题、版式、卡片、按钮、响应式与可读性规范
    ├── js/
    │   └── main.js                      # [NEW] 轻量交互。导航高亮、返回逻辑、可访问性增强
    └── downloads/
        ├── course-01/                   # [NEW] 第一节课下载文件目录（至少1个文件）
        ├── course-02/                   # [NEW] 第二节课下载文件目录（至少1个文件）
        ├── course-03/                   # [NEW] 第三节课下载文件目录（至少1个文件）
        ├── course-04/                   # [NEW] 第四节课下载文件目录（至少1个文件）
        ├── course-05/                   # [NEW] 第五节课下载文件目录（至少1个文件）
        ├── course-06/                   # [NEW] 第六节课下载文件目录（至少1个文件）
        ├── course-07/                   # [NEW] 第七节课下载文件目录（至少1个文件）
        └── course-08/                   # [NEW] 第八节课下载文件目录（至少1个文件）
```

采用淡色现代风格：浅背景、低饱和主色、柔和阴影与清晰层级。首页以课程卡片栅格展示；详情页采用“课程标题-知识点-资料下载”纵向布局。全站统一顶部导航与底部信息区，交互反馈轻量（悬停高亮、按钮过渡），确保阅读舒适与操作直观。

## Agent Extensions

### SubAgent

- **code-explorer**
- Purpose: 在后续实现前快速核对新增文件与链接结构一致性
- Expected outcome: 输出可验证的文件与引用清单，降低漏链和错链风险