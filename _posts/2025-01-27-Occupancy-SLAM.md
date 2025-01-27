---
layout: post
title: "Occupancy-SLAM论文解读"
date:   2025-01-24
tags: [SLAM, LiDAR]
comments: true
author: kwanwaipang
toc: true
---


<!-- * 目录
{:toc} -->


# 引言
Occupancy-SLAM传言可以超越Cartographer，为此对该系列工作进行解读与学习

本博客仅供本人学习记录用～

论文：

~~~
@inproceedings{wang2024grid,
  title={Grid-based Submap Joining: An Efficient Algorithm for Simultaneously Optimizing Global Occupancy Map and Local Submap Frames},
  author={Wang, Yingyu and Zhao, Liang and Huang, Shoudong},
  booktitle={2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)},
  pages={10121--10128},
  year={2024},
  organization={IEEE}
}

@article{zhao2024occupancy,
  title={Occupancy-slam: Simultaneously optimizing robot poses and continuous occupancy map},
  author={Zhao, Liang and Wang, Yingyu and Huang, Shoudong},
  journal={arXiv preprint arXiv:2405.10743},
  year={2024}
}
~~~



# 参考资料
* [超越经典Cartographer：将二维基于网格的子地图拼接问题表述为非线性最小二乘形式(IROS'24)](https://mp.weixin.qq.com/s/XqsOPfo90mGnzPtVfHlZrQ)
* [Grid-based Submap Joining: An Efficient Algorithm for Simultaneously Optimizing Global Occupancy Map and Local Submap Frames](https://arxiv.org/pdf/2501.12764)
* [Occupancy-slam: Simultaneously optimizing robot poses and continuous occupancy map](https://arxiv.org/pdf/2405.10743)