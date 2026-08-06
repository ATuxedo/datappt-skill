# 大壮的 PPT Skill

这是一个 Codex skill，用来把营销比稿、品牌策略、年度规划、前策分析整理成数据驱动的咨询风格 PPT。

## 安装

把这个仓库安装为 Codex skill 后，在对话里输入：

```text
$dazhuang-ppt-skill
```

常见用法：

```text
$dazhuang-ppt-skill 帮我把这份营销策略大纲做成麦肯锡风格的 10 页 PPT
```

## 包含内容

- `SKILL.md`：核心工作流和输出规则
- `references/`：PPT 逻辑框架和制作检查清单
- `scripts/fix_ppt_font_normalize.py`：修复中文 PPT 字体兼容和乱码问题
- `agents/openai.yaml`：默认调用提示
