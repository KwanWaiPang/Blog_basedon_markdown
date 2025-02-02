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
* [website](https://airimu.github.io/)

## 理论解读

<div align="center">
  <img src="../images/微信截图_20250202193858.png" width="80%" />
<figcaption>  
</figcaption>
</div>


Inertial odometry(IO)中对于IMU的建模可以分为两种：kinematic motion model-based （也就是传统的使用基于kinematics模型的IMU预积分<sup>[paper](https://infoscience.epfl.ch/server/api/core/bitstreams/e23a9898-f5a4-44ce-bbb0-e70854b170d2/content)</sup>） 和 data-driven method（也就是基于learning的）。
而本文则是提出混合两者的方法，用data-driven methods来估算不确定性（特别是 non-deterministic errors），而model-based methods可以提升系统的泛化能力（就是结合版）。
如下图所示。通过利用data-driven method对非确定性噪声和运动模型进行建模，以确保在新环境中的泛化能力。
为了使AirIMU能够学习不确定性和噪声模型，构建了一个可微IMU积分器（differentiable IMU integrator）和一个可微分协方差传播器（differentiable covariance propagator）。
可以预测长时间IMU预积分的累积协方差。
此外，通过将不确定性模块（uncertainty module）与噪声校正模块（ noise correction module）联合训练，可以捕获更好的IMU特征，并使两项任务都受益。
<div align="center">
  <img src="../images/微信截图_20250202195327.png" width="60%" />
<figcaption>  
</figcaption>
</div>

论文的贡献点如下：

1. the first to train a deep neural network that models IMU sensor uncertainty through differentiable covariance propagation。也就是网络可以预测IMU的不确定性（协方差）
2. kinematic motion model-based 和 data-driven method混合imu-建模；
3. 将不确定性模块（uncertainty module）与噪声校正模块（ noise correction module）联合训练

### Data-driven module
如上面图(Fig. 4)中所示。采用encoder-decoder网络结构处理原始的IMU数据（加速度和角速度）。
网络输出加速度和角速度的校正，此外，也输出对应的uncertainty。

对于```encoder network```首先采用 1D CNN network来学习lower-level features,然后通过一个 gated recurrent unit (GRU)来学习时间维度的关联。
两个task都（correction和uncertainty）采用相同的encoder网络（shared encoder network）来处理原始的IMU。

对于```decoder network```,如下：
<div align="center">
  <img src="../images/微信截图_20250202203945.png" width="60%" />
<figcaption>  
</figcaption>
</div>

最终的网络输出的IMU观测量可以表达如下：
<div align="center">
  <img src="../images/微信截图_20250202204045.png" width="60%" />
<figcaption>  
</figcaption>
</div>

### Differentiable Integration and Covariance Module

基于获得的网络输出的IMU数据，再采用IMU kinematic model（也就是IMU预积分）来估算系统的状态：
<!-- <div align="center">
  <table style="background-color: transparent;">
    <tr>
      <td style="border: none; background-color: transparent;">
        <img src="../images/微信截图_20250202204226.png" width="100%" />
      </td>
      <td style="border: none; background-color: transparent;">
        <img src="../images/微信截图_20250202204755.png" width="100%" />
      </td>
    </tr>
  </table>
  <figcaption>
  积分传播模型与协方差传播模型
  </figcaption>
</div> -->
<div align="center">
  <table style="background-color: transparent;">
    <tr>
      <td style="width: 50%; border: none; padding: 0.001; background-color: transparent; vertical-align: middle;">
        <img src="../images/微信截图_20250202204226.png" style="width: 100%" />
      </td>
      <td style="width: 50%; border: none; padding: 0.001; background-color: transparent; vertical-align: middle;">
        <img src="../images/微信截图_20250202204755.png" style="width: 100%" />
      </td>
    </tr>
  </table>
  <figcaption>
  积分传播模型与协方差传播模型
  </figcaption>
</div>

并基于预积分的结果来supervise data-driven module而不是对上面的IMU原始输出做监督，也就是Differentiable Integration and Covariance Module（其实跟DPVO和Droid-SLAM中的Differentiable BA的概念是很像的~）



最终refined的状态及协方差则跟GPS一起通过pose graph optimization来进行融合。如下图所示
<div align="center">
  <img src="../images/微信截图_20250202202738.png" width="60%" />
<figcaption>  
</figcaption>
</div>

## 代码复现


<!-- # 参考资料 -->
