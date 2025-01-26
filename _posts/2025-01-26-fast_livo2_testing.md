---
layout: post
title: "Fast-LIVO2测试及论文解读"
date:   2025-01-26
tags: [SLAM, LiDAR]
comments: true
author: kwanwaipang
toc: true
---

<!-- * 目录
{:toc} -->

HKU-MARSLAB的新作FAST-LIVO2终于开源了,用本博文记录下测试过程，并记录学习代码及论文的一些笔记。
本博客仅供本人学习记录用～
~~~
@article{zheng2024fast,
  title={Fast-livo2: Fast, direct lidar-inertial-visual odometry},
  author={Zheng, Chunran and Xu, Wei and Zou, Zuhao and Hua, Tong and Yuan, Chongjian and He, Dongjiao and Zhou, Bingyang and Liu, Zheng and Lin, Jiarong and Zhu, Fangcheng and others},
  journal={IEEE Transactions on Robotics},
  year={2024},
  publisher={IEEE}
}
~~~

# 代码配置
按照官方给出的[Github仓库](https://github.com/hku-mars/FAST-LIVO2) step by step配置
1. Ubuntu, ROS, Sophus都是原本系统安装好的，直接跳过。
2. Mimalloc是可选项，也跳过
3. Vikit
~~~
cd catkin_ws/src
git clone https://github.com/xuankuzcr/rpg_vikit.git
~~~
4. livox_ros_driver。
Follow [livox_ros_driver Installation](https://github.com/Livox-SDK/livox_ros_driver).
5. 下载源码
~~~
cd ~/catkin_ws/src
git clone https://github.com/hku-mars/FAST-LIVO2

#直接cm
cd ../
catkin_make
source ~/catkin_ws/devel/setup.bash
~~~
6. 出现Sophus相关的报错.在“/home/kwanwaipang/catkin_ws/src/rpg_vikit/vikit_common/CMakeLists.txt”中添加下面代码即可
~~~
#添加Sophus_LIBRARIES
SET(Sophus_LIBRARIES "/usr/local/lib/libSophus.so")
~~~

<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/fast_livo2_testing/2025-01-26 12-19-37 的屏幕截图.png" width="60%" />
<figcaption>  
编译成功
</figcaption>
</div>


# 实验测试
~~~
roslaunch fast_livo mapping_avia.launch
rosbag play YOUR_DOWNLOADED.bag
~~~
修改launch文件直接开启的时候播包会方便些，修改代码请见[link](https://github.com/KwanWaiPang/Fast-LIVO2_comment/blob/main/launch/mapping_avia.launch)

效果如下所示：









其中对于CBD_Building_02的测试发现有存在比较明显的drift的情况。如下图所示，实验人员应该是试图回到起点的，但是最终的位置与起始的位置差别较大。并且从生成的彩色点云也可以看到柱子的地方有较为明显的偏移。
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/fast_livo2_testing/2025-01-26 12-52-32 的屏幕截图.png" width="80%" />
<figcaption>  
</figcaption>
</div>
对于序列HIT_Graffiti_Wall_01，也是一个长走廊的序列，且路径比上面的序列更长，但却可以较好的回到原点，看似不是由于长走廊带来的drift吧~
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/fast_livo2_testing/2025-01-26 13-20-12 的屏幕截图.png" width="80%" />
<figcaption>  
</figcaption>
</div>
再次测试CBD_Building_02序列，又是正常的，可以回归原点～～～
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/fast_livo2_testing/2025-01-26 13-38-41 的屏幕截图.png" width="80%" />
<figcaption>  
</figcaption>
</div>


# 论文解读

<div align="center">
<iframe width="560" height="315" src="//player.bilibili.com/player.html?isOutside=true&aid=983500021&bvid=BV15t4y1t7yS&cid=777013703&p=1&autoplay=0" title="Bilibili video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>





# 代码解读
代码解读部分直接将注释添加到代码中，具体请见：[Fast-LIVO2代码解读](https://github.com/KwanWaiPang/Fast-LIVO2_comment)


# 参考资料
* [FAST-LIVO2 Github](https://github.com/hku-mars/FAST-LIVO2)
* [paper link](https://arxiv.org/pdf/2408.14035)
* [Fast-LIVO Self Comment](https://github.com/KwanWaiPang/fast_livo_comment)
* [ROS实验笔记之——FAST-LIVO](https://blog.csdn.net/gwplovekimi/article/details/127844810?spm=1001.2014.3001.5501)