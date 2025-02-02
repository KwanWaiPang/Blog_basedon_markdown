---
layout: post
title: "Paper Survey之——Deep IMU-Bias Inference"
date:   2025-02-02
tags: [SLAM, Deep Learning]
comments: true
author: kwanwaipang
toc: false
---


# 引言

对于IMU-based odometry，或者说所有包含IMU的framework，如LIO或VIO，IMU的bias建模是重中之重。
特别是VIO，标定及sensor modeling是影响系统性能最关键的部分。一般传统的方法都是把IMU的bias建模为additive Gaussian noise + random walk.
得益于深度学习强大的性能，基于learning的IMU bias建模也将具备很大的发展潜力。

之前[博客](https://kwanwaipang.github.io/File/Blogs/Poster/Learning_based_VO.html)已经较为系统的介绍了基于learning的VO以及VIO工作。
但是对于使用learning的方法来handle IMU bias仍然没有调研。
为此，写下本博客，作为本人学习相关工作的学习笔记。
本博客仅供本人学习记录用~




* 目录
{:toc}



<!-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -->
# Deep IMU Bias Inference for Robust Visual-Inertial Odometry with Factor Graphs
* [RAL 2022](https://arxiv.org/pdf/2211.04517)

低成本、小型化的微机电系统（MEMS）惯性测量单元（IMU）已在机器人学和行人追踪领域得到广泛应用。
然而，单纯依赖IMU的状态估计会受到严重漂移影响。
这种漂移源于IMU积分过程中各类误差的累积，这些误差通常被统一建模为additive Gaussian noise + random walk。
由于漂移的累积，仅通过IMU测量积分进行状态估计的有效时间窗口通常不超过数秒。

该工作实现以及对比了 LSTMs 和 Transformers两个模型对IMU bias的推断性能。
网络不是学习运动模型，而是显示地学习IMU bias，这样也可以使得模型可以泛化到训练中没见过的运行模式。
下图展示了，如果模型只是学习运动的模型，当泛化到不同的环境（比如从行人手持到四足机器人，或者平地走训练的模型用到上下楼梯的场景）就会导致发散。
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202160846.png" width="60%" />
<figcaption>  
</figcaption>
</div>

论文的主要贡献点如下:
1. 设计一个神经网络可以从历史的IMU测量及bias中推断出IMU的bias
2. 对比了LSTMs 和 Transformers两个模型，并且将他们融入VIO的因子图中

论文的基于NN估算IMU-bias的VIO图优化的framework如下：
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202161751.png" width="60%" />
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202161803.png" width="60%" />
<figcaption>  
</figcaption>
</div>

而所谓的可以从历史的IMU测量及bias中推断出IMU的bias的神经网络则是如下表示：
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202162236.png" width="60%" />
<figcaption>  
</figcaption>
</div>
此外设计了IMU-bias的因子如下：
<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202162735.png" width="60%" />
<figcaption>  
注意，此处的方差给定的是常数，当然也可以通过网络来估算uncertainty
</figcaption>
</div>

至于network的结构，论文中设计了两个结构并且进行了对比
<div align="center">
  <table style="background-color: transparent;">
    <tr>
      <td style="border: none; background-color: transparent;">
        <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202155453.png" width="100%" />
      </td>
      <td style="border: none; background-color: transparent;">
        <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202155520.png" width="100%" />
      </td>
    </tr>
  </table>
  <figcaption>
  基于LSTM以及Transformer的IMU-bias Interference结构
  </figcaption>
</div>

作者测试了多种场景，包括手持、四足、飞机。
但可惜的是既没有开源代码，似乎也没有说baseline VIO指的是哪个具体算法

<div align="center">
  <table style="background-color: transparent;">
    <tr>
      <td style="border: none; background-color: transparent;">
        <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202163309.png" width="100%" />
      </td>
      <td style="border: none; background-color: transparent;">
        <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202163500.png" width="100%" />
      </td>
    </tr>
  </table>
  <figcaption>
手持实验（Newer College Multi-Camera Dataset(NCD-Multi)）
  </figcaption>
</div>


<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202163627.png" width="60%" />
<figcaption>  
在四足上的测试效果（网络都是用手持的数据进行训练的，也没有进行fine-tuning）
</figcaption>
</div>

<div align="center">
  <img src="https://kwanwaipang.github.io/ubuntu_md_blog/images/微信截图_20250202163831.png" width="60%" />
<figcaption>  
Euroc飞行数据集（平移和旋转误差）
</figcaption>
</div>




<!-- !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -->
# AirIMU: Learning uncertainty propagation for inertial odometry
* [code](https://github.com/haleqiu/AirIMU)
* [paper](https://arxiv.org/pdf/2310.04874)



<!-- # 参考资料 -->
