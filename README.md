# 新中式电子请柬 · 婚礼 H5

面向长辈与四五十岁宾客的端庄喜庆请柬：宣纸底、朱砂囍印、细金线、中轴对称、竖向翻阅。

纯静态，双击 `index.html` 即可运行，不需要服务器、不需要联网。

---

## 1. 怎么打开

- **电脑**：双击 `index.html`（Chrome / Edge 均可）。
- **手机**：把整个文件夹拷到手机，用浏览器打开 `index.html`；或放到任意静态托管（微信里打开效果最好）。
- 微信内置浏览器、iOS Safari、Android Chrome 均可。

## 2. 交付结构

```text
D:\Codex\wedding-story-h5\
├─ index.html                  ← 全部代码（HTML + CSS + JS，单文件）
├─ assets\
│  ├─ panda-zoo.png            ← 原图（回退用）
│  ├─ universal-studios.png
│  ├─ livingroom-watermelon.png
│  ├─ cinema.png
│  ├─ night-market.png
│  ├─ panda-zoo.webp           ← 压缩版（优先加载）
│  ├─ universal-studios.webp
│  ├─ livingroom-watermelon.webp
│  ├─ cinema.webp
│  ├─ night-market.webp
│  └─ river-flows-in-you.mp3   ← 背景音乐（Yiruma，正版自备）
├─ publish\                    ← 可直接上传的发布包（含 BGM）
│  ├─ index.html
│  └─ assets\*.webp + *.mp3
└─ _legacy\                    ← 更早的旧版，原样保留
```

> 已删除 1970 复古版（`retro-70s-invite.html`）与双版本入口（`choose.html`），现仅保留主版本。

## 3. 改成你们的信息（只改一处）

打开 `index.html`，搜索 `var CONFIG`（在 `<script>` 开头），只改这一段：

```js
var CONFIG = {
  groom: '新郎',
  bride: '新娘',
  dateText: '2026.10.18',              // 显示用日期
  dateISO: '20261018',                 // 日历文件用日期（YYYYMMDD）
  dateCN: '2026年10月18日',             // 请柬正文里的中文日期
  timeText: '17:30 签到',
  venue: '湖畔礼堂 · 三楼宴会厅',
  address: '示例市示例区湖畔路 88 号',
  lng: 116.397428,
  lat: 39.90923,
  timeline: [
    { time: '17:30', title: '签到 · 迎宾', desc: '茶歇、合影与祝福' },
    { time: '18:18', title: '仪式开始', desc: '请提前十分钟入席' },
    { time: '19:00', title: '晚宴 · 敬酒', desc: '一起吃到很晚' },
    { time: '21:00', title: '送客', desc: '记得带走喜糖' }
  ]
};
```

改完保存即可，封面姓名、正文、流程、场地、按钮文案都会自动同步。

## 4. 页面结构（六段竖滑）

| 段落 | 内容 |
| --- | --- |
| 封面 | 朱砂「囍」印 + 姓名 + 日期 |
| 请柬正文 | 谨订良辰 · 敬备喜筵 · 恭候光临 |
| 时光片段 | 五张插画自动循环横滑（按住可暂停） |
| 当日流程 | 金点时间线 |
| 婚礼场地 | 日期 / 时间 / 场地 / 地址 + 导航、复制、加日历 |
| 结尾 | 「百年好合」印章 + 敬邀 |

## 5. 交互一览

| 操作 | 效果 |
| --- | --- |
| 上下滑动 | 竖向翻阅整份请柬 |
| 时光片段 | 自动循环滚动；手指按住 / 鼠标悬停暂停 |
| 点「导航到场地」 | 唤起高德地图（带经纬度） |
| 点「复制地址」 | 复制场地 + 地址 |
| 点「加入日历」 | 下载 `.ics` 日历文件 |
| 右上角音符 | 播放 / 关闭背景音乐（可选） |

背景音乐优先加载 `assets/river-flows-in-you.mp3`（River Flows in You），
没有则依次尝试 `a-thousand-years.mp3`、`bgm.mp3`；文件不存在时按钮保持静音态，不影响页面。

## 6. 技术说明

- 纯 HTML + CSS + JavaScript，单文件，无构建、无外部依赖。
- 宣纸质感用 SVG 噪声纹理，细金线双框 + 四角直角装饰，支持 `prefers-reduced-motion`。
- 图片用 `<picture>` 优先加载 `.webp`，老浏览器回退 `.png`。
- 已适配刘海屏 `safe-area-inset`、`dvh`、横竖屏。
- 底部展示备案号并链向工信部。

## 7. 设计取向（给后续改版用）

面向四五十岁宾客，取「高端酒店新中式纸质请柬」路线：

- **要**：朱砂红点缀、宣纸米白、细金线、宋体大标题、中轴对称、大留白、信息清楚
- **不要**：高饱和正红满铺、立体烫金、粗书法、迪斯科/玩具感、过度动效

色彩与字体变量都在 `:root`，改主题只动这一处。
