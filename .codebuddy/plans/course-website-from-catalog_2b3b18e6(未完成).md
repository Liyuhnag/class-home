---
name: course-website-from-catalog
overview: 基于现有《课程目录.md》构建一个简洁可导航的静态课程网站：首页展示课程目录并链接到各课程详情页，详情页提供课程资料与可下载资源入口。
design:
  architecture:
    framework: html
  styleKeywords:
    - 简洁现代
    - 高可读性
    - 卡片分组
    - 轻量动态反馈
  fontSystem:
    fontFamily: Noto Sans
    heading:
      size: 30px
      weight: 700
    subheading:
      size: 20px
      weight: 600
    body:
      size: 16px
      weight: 400
  colorSystem:
    primary:
      - "#2563EB"
      - "#1D4ED8"
    background:
      - "#F8FAFC"
      - "#FFFFFF"
    text:
      - "#0F172A"
      - "#334155"
    functional:
      - "#16A34A"
      - "#DC2626"
      - "#F59E0B"
      - "#0EA5E9"
todos:
  - id: build-course-map
    content: 解析课程目录并定义8节课页面映射
    status: pending
  - id: create-shared-assets
    content: 编写assets/css/main.css与assets/js/main.js
    status: pending
    dependencies:
      - build-course-map
  - id: implement-homepage
    content: 实现index.html课程目录展示与详情跳转
    status: pending
    dependencies:
      - create-shared-assets
  - id: implement-course-pages
    content: 批量创建courses下8个课程详情页面
    status: pending
    dependencies:
      - create-shared-assets
  - id: wire-downloads-and-verify
    content: 配置下载资源目录并逐页校验下载链接
    status: pending
    dependencies:
      - implement-homepage
      - implement-course-pages
---

## User Requirements

- 构建一个课程网站首页，展示完整课程目录并清晰列出所有课程。
- 每门课程需跳转到独立详情页，详情页展示该课程对应学习资料内容。
- 每个详情页提供可下载资源，学生点击后可直接获取文件。
- 页面结构简洁明了、导航清晰，用户可快速在首页与各课程页间切换。
- 下载功能应可用且稳定，避免出现无效链接或无法下载情况。

## Product Overview

- 网站包含一个课程总览首页和多个课程详情页面。
- 首页以分节方式展示课程列表与主题摘要，点击课程进入对应资料页。
- 详情页统一采用一致布局：课程标题、主题内容、资料下载区、返回入口。

## Core Features

- 课程目录展示与一键跳转
- 独立课程资料页展示
- 资料文件下载入口与可用性保障
- 简洁统一的导航与页面视觉层次

## Tech Stack Selection

- 前端：HTML + CSS + JavaScript（原生）
- 内容来源：`d:/class/homepage/课程目录.md`（已确认含 8 节课程）
- 资源组织：静态文件目录（课程页、样式脚本、下载资源分层）

## Implementation Approach

采用“静态多页站点 + 统一样式脚本”的方案：以首页承载课程导航，8 个课程详情页承载资料与下载入口。先根据 `课程目录.md` 建立课程编号与页面映射，再批量生成一致模板页面，最后做下载链路校验。
关键决策：

- 复用统一 CSS/JS，避免 8 个详情页重复逻辑（可维护性更高）。  
- 下载链接使用相对静态资源路径，减少运行时依赖，稳定且部署简单。  
- 目录解析与页面映射一次性完成，构建复杂度 O(n)（n 为课程条目数），无性能瓶颈。

## Implementation Notes

- 仅新增站点文件，不改动 `课程目录.md` 原始内容，降低影响面。  
- 首页与详情页均使用同一导航样式和返回入口，避免交互不一致。  
- 下载区优先使用真实文件；若暂缺文件，提供占位说明并在发布前替换。  
- 控制脚本职责：仅处理导航高亮、返回逻辑与轻量交互，避免不必要复杂度。

## Architecture Design

- 页面层：`index.html`（课程总览） + `courses/course-xx.html`（课程详情）
- 表现层：`assets/css/main.css`（全站视觉与布局）
- 交互层：`assets/js/main.js`（导航、轻交互、可用性提示）
- 资源层：`assets/downloads/...`（按课程分目录存放下载文件）

## Directory Structure

```text
d:/class/homepage/
├── 课程目录.md  # [EXISTING] 课程源数据参考文件，不改动
├── index.html  # [NEW] 首页。展示8节课目录、主题摘要与详情页跳转入口
├── assets/
│   ├── css/
│   │   └── main.css  # [NEW] 全站统一样式：布局、导航、卡片、下载按钮、响应式
│   ├── js/
│   │   └── main.js  # [NEW] 轻量交互：导航状态、返回逻辑、下载可用性提示
│   └── downloads/
│       ├── course-01/  # [NEW] 第一节课下载资源
│       ├── course-02/  # [NEW] 第二节课下载资源
│       ├── course-03/  # [NEW] 第三节课下载资源
│       ├── course-04/  # [NEW] 第四节课下载资源
│       ├── course-05/  # [NEW] 第五节课下载资源
│       ├── course-06/  # [NEW] 第六节课下载资源
│       ├── course-07/  # [NEW] 第七节课下载资源
│       └── course-08/  # [NEW] 第八节课下载资源
└── courses/
    ├── course-01.html  # [NEW] 第一节课详情与下载区
    ├── course-02.html  # [NEW] 第二节课详情与下载区
    ├── course-03.html  # [NEW] 第三节课详情与下载区
    ├── course-04.html  # [NEW] 第四节课详情与下载区
    ├── course-05.html  # [NEW] 第五节课详情与下载区
    ├── course-06.html  # [NEW] 第六节课详情与下载区
    ├── course-07.html  # [NEW] 第七节课详情与下载区
    └── course-08.html  # [NEW] 第八节课详情与下载区
```

## 设计方案

采用简洁现代的课程门户风格：首页使用清晰分组卡片展示课程与主题，详情页保持统一信息结构与下载区块。强调高可读性、低认知负担和明确导航路径；通过悬停反馈与按钮状态提升交互确定性，保证学生快速定位并下载资料。