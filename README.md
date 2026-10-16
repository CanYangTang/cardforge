# CardForge

CardForge 是一个由 AI 全程协作管理的 Agent 学习项目，目标是掌握 Agent 的工作原理，并完成一个万智牌 DIY 助手 Demo。

第一阶段只聚焦于“卡牌创意助手”：

```text
自然语言描述卡牌
        ↓
Agent 提取设计意图
        ↓
生成结构化卡牌
        ↓
执行字段、规则和基础强度检查
        ↓
给出修改建议并生成卡牌预览
```

## 学习方式

- 每次学习都必须对应一个可运行的实验或代码产出。
- 先理解 Agent 原理，再使用框架封装。
- 每个任务都定义验收标准。
- 每次实验记录输入、工具调用、结果和问题。
- 使用 Git 记录代码、文档和学习进度。
- AI 负责项目经理、导师、结对开发者和 Reviewer 的角色。

## 当前里程碑

| 里程碑 | 目标 | 状态 |
|---|---|---|
| M0 | 建立项目底座和可追踪学习流程 | 进行中 |
| M1 | 实现最小 Agent Loop 和工具调用 | 未开始 |
| M2 | 完成卡牌 DIY Agent | 未开始 |
| M3 | 完成可演示的网页 Demo | 未开始 |

详细路线见 [ROADMAP.md](ROADMAP.md)，当前任务见 [tasks/current.md](tasks/current.md)。

## 项目结构

```text
.
├── app/
│   ├── agent/          # Agent 循环、状态和工具编排
│   ├── domain/         # 卡牌等领域模型
│   └── tools/          # Agent 可调用的工具
├── docs/
│   ├── architecture/   # 架构和设计决策
│   ├── experiments/    # Agent 实验记录
│   ├── learning/       # 概念学习笔记
│   ├── daily/          # 每日学习记录
│   └── weekly/         # 每周复盘
├── tasks/              # 任务状态和待办
├── tests/              # 自动化测试
├── ROADMAP.md          # 总路线图
├── STATUS.md           # 当前进度快照
└── pyproject.toml      # Python 项目配置
```

## 本地启动

当前 M0 不依赖第三方库，使用 Python 3.11+ 即可：

```bash
python3 -m app
```

运行测试：

```bash
python3 -m unittest discover -s tests -v
```

后续接入模型时，复制环境变量模板：

```bash
cp .env.example .env
```

## 每日 AI 工作流

1. 查看 `STATUS.md` 和 `tasks/current.md`。
2. 选择一个当天的核心任务。
3. 先确认学习目标和验收标准。
4. 学习必要概念并完成最小代码任务。
5. 运行测试和实验。
6. 记录到 `docs/daily/` 或 `docs/experiments/`。
7. 让 AI Review 代码和学习记录。
8. 更新任务状态、`STATUS.md` 和 `CHANGELOG.md`。
9. 提交当天成果。

