---
layout: post
title: "利用 GitHub Actions 为 Markdown 项目自动添加目录"
date:   2025-02-06
tags: [coding]
comments: true
author: kwanwaipang
toc: true
---


<!-- * 目录
{:toc} -->


<!-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -->
# 引言
对于习惯用markdown写文档的朋友，整理文档是非常繁琐的。当然类似也可以搭建Jekyll静态博客，这样可以很简单的自动生成博客目录。但是对于仅仅管理markdown文档却要重新搭建Jekyll，未免过于繁琐，为此写下本博客，利用GitHub Actions来自动生成目录。
效果如下下图所示

本博客以[我的一个github仓库](https://github.com/KwanWaiPang/Blog_basedon_markdown)为例子。（注意不仅仅适用于公开仓库，私密仓库也是适合的）

1. 首先在需要生成目录的地方添加以下内容(以```readme.md```为例)：
   
```markdown
## 自动生成md.文件的目录
### list
<!-- AUTO_GENERATED_TOC_START -->

<!-- AUTO_GENERATED_TOC_END -->
```

2. 然后在相同目录下创建```generate_toc.py```文件：
```python
import os
import re
import urllib.parse

markdown_dir = '_posts'  # 你的markdown文件夹名
target_file = 'readme.md'  # 目标文件（当前目录的.md文件）

# 获取所有.md文件，并按文件名排序
try:
    files = sorted([f for f in os.listdir(markdown_dir) if f.endswith('.md')])
except Exception as e:
    print(f"Error reading markdown directory: {e}")
    raise

# 打印文件列表，用于调试
print("Markdown files found:", files)

# 生成目录内容
toc_lines = []
for file in files:
    try:
        name = os.path.splitext(file)[0]
        # 使用 urllib.parse.quote 来处理文件名中的空格
        link = f"- [{name}](./{markdown_dir}/{urllib.parse.quote(file)})"
        toc_lines.append(link)
    except Exception as e:
        print(f"Error processing file {file}: {e}")
        continue

toc_content = "<!-- AUTO_GENERATED_TOC_START -->\n" + "\n".join(toc_lines) + "\n<!-- AUTO_GENERATED_TOC_END -->"

# 读取目标文件内容
try:
    with open(target_file, 'r') as f:
        content = f.read()
except Exception as e:
    print(f"Error reading {target_file}: {e}")
    raise

# 使用正则表达式替换占位符中的内容
try:
    new_content = re.sub(
        r'<!-- AUTO_GENERATED_TOC_START -->.*?<!-- AUTO_GENERATED_TOC_END -->',
        toc_content,
        content,
        flags=re.DOTALL
    )
except Exception as e:
    print(f"Error replacing TOC content: {e}")
    raise

# 将更新后的内容写回目标文件
try:
    with open(target_file, 'w') as f:
        f.write(new_content)
    print("TOC updated successfully!")
except Exception as e:
    print(f"Error writing {target_file}: {e}")
    raise

```