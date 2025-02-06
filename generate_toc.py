import os
import re
import urllib.parse

markdown_dir = '_posts'  # 你的markdown文件夹名
target_file = 'README.md'  # 目标文件（当前目录的.md文件）

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
