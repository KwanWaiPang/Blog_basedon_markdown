---
layout: post
title: "Hello World"
date:   2025-01-24
tags: [markdown]
comments: true
author: kwanwaipang
toc: true
---


<!-- * 目录
{:toc} -->


# 标题
基于markdown的静态博客～

配置过程都是参考[链接](https://lemonchann.github.io/blog/create_blog_with_github_pages/)


# 插入图片

<div align="center">
  <img src="../images/yijiansanlian.gif" width="60%" />
</div>

# 插入youtube视频

<div align="center">
<iframe width="560" height="315" src="https://www.youtube.com/embed/Nn40U4e5Si8?si=P_4XDu5l83VeVRQo" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

# 插入B站视频

<div align="center">
<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=983500021&bvid=BV15t4y1t7yS&cid=777013703&p=1&autoplay=0" title="Bilibili video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

# 插入代码链接
~~~
hello world
~~~

<p><br></p>

{% highlight html %}
 This is some text in a paragraph.
{% endhighlight %}

## 插入c++代码
```cpp
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```

```c++
int main() {
  int y = SOME_MACRO_REFERENCE;
  int x = 5 + 6;
  cout << "Hello World! " << x << std::endl();
}
```

## 插入python代码
```python 
print("Hello, World")
```



# 参考资料
* [lemonchann的博客](https://lemonchann.github.io/blog/create_blog_with_github_pages/)
* [为Jekyll博客添加小功能](https://blog.csdn.net/ds19991999/article/details/81293467)
* [Markdown 语法简明笔记](https://lemonchann.github.io/blog/Markdown_brief_syntactic/)