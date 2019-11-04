<div style="margin: 0px auto; padding: 20px; min-width: 200px; max-width: 760px; font-family: Nunito, HelveticaNeue-Light, " helvetica="" neue="" light",="" "helvetica="" neue",="" helvetica,="" arial,="" sans-serif;="" font-weight:="" 300;="" font-size:="" 14px;="" background-color:="" rgb(255,="" 255,="" 255);="" color:="" rgb(51,="" 51,="" 51);="" background-position:="" initial="" initial;="" background-repeat:="" initial;"=""><div style="margin: 0px; padding: 0px; line-height: 1.5em; font-size: 1.3em; text-align: left; border: none;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="markdown-body-wrap"></a>
<div style="padding: 0px; margin: 0px;"><h2 style="margin: 30px 0px 0px; padding: 0px; font-size: 1.3em; font-weight: bold; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(221, 221, 221); position: relative; color: rgb(51, 51, 51); line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_0"></a>亮点</h2>

<p style="margin: 10px 0px 0px; padding: 0px;">一个学习时间动态的模型。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">视频超分辨率（SR）旨在从本地时间窗口中的多个低分辨率（LR）帧生成高分辨率（HR）帧。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">用于视频SR的关系有两种类型：帧内空间关系和帧间时间关系。为了解决这个问题，帧间时间关系与帧内空间关系同样重要。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">如何有效地利用时间信息,从两个方面解决:</p>

<ul style="margin: 20px 0px 0px 20px; padding: 0px;">
<li style="margin: 0px; padding: 0px;">提出了一种时间自适应神经网络，它可以自适应地确定时间依赖性的最佳尺度。在将各种时间尺度上的滤波器自适应地聚合之前，将其应用于输入LR序列</li>
<li style="margin: 0px; padding: 0px;">使用空间对齐网络减少了相邻帧之间运动的复杂性，该网络比竞争对齐方法更坚固，更有效，并且可以以端到端的方式与时间自适应网络共同训练。</li>
</ul>

<h2 style="margin: 30px 0px 0px; padding: 0px; font-size: 1.3em; font-weight: bold; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(221, 221, 221); position: relative; color: rgb(51, 51, 51); line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_1"></a>1. 介绍</h2>

<p style="margin: 10px 0px 0px; padding: 0px;">在Image SR上，已经成功地证明了神经网络捕获空间关系能力极强[ 4，30，5，14，15，26，6 ]<br style="margin: 0px; padding: 0px;" />
与帧内空间关系相比，帧间时间关系对于视频SR更重要，因为视觉系统的研究表明，人类视觉系统对运动更敏感[ 7]</p>

<p style="margin: 10px 0px 0px; padding: 0px;">因此，对于视频SR算法而言，捕获运动信息对视觉感知的影响并对其建模至关重要。为了满足这种需求，提出了许多视频SR算法[ 8，28，2，20，23，17 ]</p>

<h2 style="margin: 30px 0px 0px; padding: 0px; font-size: 1.3em; font-weight: bold; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(221, 221, 221); position: relative; color: rgb(51, 51, 51); line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_2"></a>2. VSR 相关工作</h2>

<p style="margin: 10px 0px 0px; padding: 0px;">VSR的深度学习。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">首先在不同的参数设置下通过运动补偿生成一组SR草稿，然后使用CNN从所有草稿中重建HR帧。[ 17 ]</p>

<p style="margin: 10px 0px 0px; padding: 0px;">通过沿时间维度扩展单个图像SR的SRCNN来避免显式的运动估计，从而形成一个递归卷积网络以捕获长期的时间依赖性。[ 9 ]</p>

<p style="margin: 10px 0px 0px; padding: 0px;">在固定的时间尺度上扩展SRCNN并从光学流信息中对齐的帧中提取特征。[12]</p>

<h2 style="margin: 30px 0px 0px; padding: 0px; font-size: 1.3em; font-weight: bold; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(221, 221, 221); position: relative; color: rgb(51, 51, 51); line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_3"></a>3. 方法-Temporal Adaptive Neural Network</h2>

<h3 style="margin: 20px 0px 0px; padding: 0px; font-size: 1.3em; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_4"></a>3.1 方法总览</h3>

<p style="margin: 10px 0px 0px; padding: 0px;">对于LR视频序列，我们的模型旨在从一组本地LR帧估计HR帧。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">视频SR的主要挑战在于正确利用时间信息来处理各种类型的运动。为了解决这个问题，我们设计了一个神经网络来自适应地为视频SR选择最佳的时间尺度。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">网络具有许多SR推理分支。</p>

<p style="margin: 10px 0px 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?%5Cleft%5C%7BB_%7Bi%7D%5Cright%5C%7D_%7Bi=1%7D%5E%7BN%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<p style="margin: 10px 0px 0px; padding: 0px;">每个<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />在不同的时间尺度i上工作，并使用其对尺度的时间依赖性来预测HR估计值。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">我们设计了一个额外的时间调制分支T，以确定最佳的时间尺度，并基于运动信息在像素级别自适应地组合了所有HR估计。所有SR推理分支和时间调制分支都合并并在一个统一网络中共同学习。最终估计的HR帧是从所有SR推理分支的估计值中汇总的，其中考虑了各种时间尺度上的运动信息。时间自适应网络的概述如图1所示<br style="margin: 0px; padding: 0px;" />
<img src="https://aigroupz-1258285787.cos.ap-shanghai.myqcloud.com/2019/11/04/15721015787753.jpg" alt="" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<h3 style="margin: 20px 0px 0px; padding: 0px; font-size: 1.3em; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_5"></a>3.2 网络架构</h3>

<h4 style="margin: 20px 0px 0px; padding: 0px; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_6"></a>SR推理分支</h4>

<p style="margin: 10px 0px 0px; padding: 0px;">基于ESPCN [ 26 ]的SR模型，并在每个SR信息中使用了它。为什么用ESPCN？因为它的SR准确性高且计算成本低。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">SR推理分支<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />在<img src="https://latex.codecogs.com/svg.latex?2i-1" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />个连续的LR帧上工作。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">c表示每个输入LR帧的通道数。第一层SR推理分支<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />的滤波器的时间长度为<img src="https://latex.codecogs.com/svg.latex?2i-1" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />，第一层的卷积滤波器被定制为具有<img src="https://latex.codecogs.com/svg.latex?%EF%BC%882i%20-%201%EF%BC%89%C3%97%20c" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />个通道。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">选定的线性单位（ReLU）[ 24 ]作为第一层和第二层的激活函数。(可以试试gelu？)</p>

<p style="margin: 10px 0px 0px; padding: 0px;">SR推理分支不局限于使用ESPCN，基于SR的模型都可以，比如换成SRCNN等。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">输出：<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />为最后的HR帧。</p>

<h4 style="margin: 20px 0px 0px; padding: 0px; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_7"></a>时间调制分支T</h4>

<p style="margin: 10px 0px 0px; padding: 0px;">该分支的原理是根据运动信息学习模型在不同时间尺度上的选择性。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">作者建议在每个HR估计值上分配像素级聚合权重，实际上，该分支应用于最大的时间尺度。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">即对于N个 SR推理分支的模型，时间调制分支将2 N - 1个连续帧作为输入。</p>

<h4 style="margin: 20px 0px 0px; padding: 0px; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_8"></a>聚合</h4>

<p style="margin: 10px 0px 0px; padding: 0px;">每个SR推理分支的输出都与时间调制分支中的相应权重图进行逐像素乘积，然后求和以形成最终估计的HR帧。</p>

<h3 style="margin: 20px 0px 0px; padding: 0px; font-size: 1.3em; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_9"></a>3.3 训练目标</h3>

<p style="margin: 10px 0px 0px; padding: 0px;">在target HR帧和预测输出之间求loss：</p>

<p style="margin: 10px 0px 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?%5Cmin%20_%7B%5CTheta%7D%20%5Csum_%7Bj%7D%5Cleft%5C%7CF%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5CTheta%5Cright)-%5Cmathbf%7Bx%7D%5E%7B(j)%7D%5Cright%5C%7C_%7B2%7D%5E%7B2%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<ul style="margin: 20px 0px 0px 20px; padding: 0px;">
<li style="margin: 0px; padding: 0px;">其中<img src="https://latex.codecogs.com/svg.latex?F%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5CTheta%5Cright)" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />是网络输出</li>
<li style="margin: 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?x%5E%7B(j)%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />是j-th HR帧</li>
<li style="margin: 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?y%5E%7B(j)%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />是j-th 所有相关的LR帧。</li>
<li style="margin: 0px; padding: 0px;"> <img src="https://latex.codecogs.com/svg.latex?%CE%98" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /> 是模型参数。</li>
</ul>

<p style="margin: 10px 0px 0px; padding: 0px;">更进一步，如果用额外的参数<img src="https://latex.codecogs.com/svg.latex?%5Ctheta_%7Bw%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /> ，函数 <img src="https://latex.codecogs.com/svg.latex?W%5Cleft(%5Cmathbf%7By%7D%20;%20%5Ctheta_%7Bw%7D%5Cright)" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /> 表示时间调制分支，损失函数为：</p>

<p style="margin: 10px 0px 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?%0A%5Cmin%20_%7B%5Ctheta_%7Bw%7D,%5Cleft%5C%7B%5Ctheta_%7BB_%7Bi%7D%7D%5Cright%5C%7D_%7Bi=1%7D%5E%7BN%7D%7D%20%5Csum_%7Bj%7D%5Cleft%5C%7C%5Csum_%7Bi=1%7D%5E%7BN%7D%20W_%7Bi%7D%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5Ctheta_%7Bw%7D%5Cright)%20%5Codot%20F_%7BB_%7Bi%7D%7D%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5Ctheta_%7BB_%7Bi%7D%7D%5Cright)-%5Cmathbf%7Bx%7D%5E%7B(j)%7D%5Cright%5C%7C_%7B2%7D%5E%7B2%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<ul style="margin: 20px 0px 0px 20px; padding: 0px;">
<li style="margin: 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?F_%7BB_%7Bi%7D%7D%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5Ctheta_%7BB_%7Bi%7D%7D%5Cright)" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />是SR推理链<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />的输出</li>
</ul>

<p style="margin: 10px 0px 0px; padding: 0px;">作者在实践中，首先使用与训练目标相同的HR帧，像Loss（1）一样分别训练每个SR推理分支<img src="https://latex.codecogs.com/svg.latex?B_i" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" />，得到模型A。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">然后在使用Loss（2）训练时间自适应网络（temporal adaptive<br style="margin: 0px; padding: 0px;" />
network）时，使用A初始化SR推理分支。这种训练策略在不牺牲SR的预测准确性的情况下，极大地加快了收敛速度。</p>

<h2 style="margin: 30px 0px 0px; padding: 0px; font-size: 1.3em; font-weight: bold; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: rgb(221, 221, 221); position: relative; color: rgb(51, 51, 51); line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_10"></a>4. 空间对齐方法</h2>

<p style="margin: 10px 0px 0px; padding: 0px;">对于视频SR，人们通常在空间上对准相邻帧以增加时间相干性，并且图像对齐作为预处理步骤已被证明对模型有好处[ 17，12 ]。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">因此，作者研究了几种图像对齐方法，以便为时间自适应网络提供更好的运动补偿帧。</p>

<h3 style="margin: 20px 0px 0px; padding: 0px; font-size: 1.3em; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_11"></a>4.1 纠正光流对准（Rectified Optical Flow Alignment）</h3>

<p style="margin: 10px 0px 0px; padding: 0px;">由于复杂的运动很难建模，基于常规光流的图像对齐使用错误的运动估算可能会引入伪影，会传播到以后的SR步骤并对其产生不利影响。 </p>

<p style="margin: 10px 0px 0px; padding: 0px;">作者尝试将补丁级别的运动简化为整数转换，以避免插值可能会导致模糊或混叠。 给定补丁及其光流，我们估计整数平移沿水平和垂直方向取整<br style="margin: 0px; padding: 0px;" />
所有像素的平均水平和垂直位移在此补丁中。 该方案称为纠正光流对准，被证明对以下方面更有利SR比传统的基于光流的图像对齐。</p>

<h3 style="margin: 20px 0px 0px; padding: 0px; font-size: 1.3em; line-height: 1.2em;"><a style="background: transparent; color: #1980e6; text-decoration: none;" name="toc_12"></a>4.2 空间对齐网络 （Spatial Alignment Network）</h3>

<p style="margin: 10px 0px 0px; padding: 0px;"><img src="https://aigroupz-1258285787.cos.ap-shanghai.myqcloud.com/2019/11/04/15721612969360.jpg" alt="" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<p style="margin: 10px 0px 0px; padding: 0px;">每次空间对准网络将一个LR参考帧和一个LR相邻帧（作为源帧）作为输入，并生成该相邻帧的对准版本作为输出。</p>

<p style="margin: 10px 0px 0px; padding: 0px;">最后loss为：</p>

<p style="margin: 10px 0px 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?%5Cmin%20_%7B%5Cleft%5C%7B%5CTheta,%20%5Ctheta_%7BL%7D%5Cright%5C%7D%7D%20%5Csum_%7Bj%7D%5Cleft%5C%7CF%5Cleft(%5Cmathbf%7By%7D%5E%7B(j)%7D%20;%20%5Cmathbf%7B%5CTheta%7D%5Cright)-%5Cmathbf%7Bx%7D%5E%7B(j)%7D%5Cright%5C%7C_%7B2%7D%5E%7B2%7D+%5Clambda%20%5Csum_%7Bj%7D%20%5Csum_%7Bk%20%5Cin%20%5Cmathcal%7BN%7D_%7Bj%7D%7D%5Cleft%5C%7C%5Chat%7B%5Ctheta%7D_%7BS%20T%7D%5E%7B(k)%7D-%5Ctheta_%7BS%20T%7D%5E%7B(k)%7D%5Cright%5C%7C_%7B2%7D%5E%7B2%7D" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></p>

<ul style="margin: 20px 0px 0px 20px; padding: 0px;">
<li style="margin: 0px; padding: 0px;"><img src="https://latex.codecogs.com/svg.latex?%5Cmathcal%7BN%7D_%7Bj%7D:%20LR%E5%B8%A7%E9%9B%86%E5%90%88%E5%85%B3%E8%81%94%E7%9A%84j-th%20HR%E5%B8%A7" style="margin: 0px; padding: 0px; max-width: 100%; height: auto;" /></li>
</ul>
</div>
</div>


</div>
