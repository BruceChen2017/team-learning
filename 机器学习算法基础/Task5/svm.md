### SVM

##### 动机

对于线性可分数据，感知机有无穷多解（超平面），我们需要通过某个标准来找到最优的超平面，这个标准是最大化数据集到超平面的（几何）距离。

##### 目标函数


$$
\max _{\gamma, w, b} \quad \gamma \\
\begin{array}{ll}
\text { s.t. } & \frac{y^{(i)}\left(w^{T} x^{(i)}+b\right)}{||w||} \geq \gamma, \quad i=1, \ldots, m \\
\end{array}
$$
等价地，
$$
\max _{\gamma, w, b} \quad \frac{\hat{\gamma}}{||w||} \\
\begin{array}{ll}
\text { s.t. } & {y^{(i)}\left(w^{T} x^{(i)}+b\right)} \geq \hat{\gamma}, \quad i=1, \ldots, m \\
\end{array}
$$
等价地
$$
\min _{\gamma, w, b} \quad \frac{1}{2}\|w\|^{2} \\
\begin{array}{ll}
\text { s.t. } & {y^{(i)}\left(w^{T} x^{(i)}+b\right)} \geq 1, \quad i=1, \ldots, m \\
\end{array}
$$
这是QP问题，现有软件能解决。

##### 拉格朗日对偶

尽管QP问题能够有效解决，但带约束优化问题的对偶形式可能更好解。

Primal optimization problem  

$$
\begin{array}{ll}
\min _{w} & f(w) \\
\text { s.t. } & g_{i}(w) \leq 0, \quad i=1, \ldots, k \\
& h_{i}(w)=0, \quad i=1, \ldots, l
\end{array}
$$

the generalized Lagrangian :

$$
\mathcal{L}(w, \alpha, \beta)=f(w)+\sum_{i=1}^{k} \alpha_{i} g_{i}(w)+\sum_{i=1}^{l} \beta_{i} h_{i}(w)
$$

Dual optimization problem

$$
\max _{\alpha, \beta: \alpha_{i} \geq 0} \theta_{\mathcal{D}}(\alpha, \beta)=\max _{\alpha, \beta: \alpha_{i} \geq 0} \min _{w} \mathcal{L}(w, \alpha, \beta)
$$

易知

$$
d^{*}=\max _{\alpha, \beta: \alpha_{i} \geq 0} \min _{w} \mathcal{L}(w, \alpha, \beta) \leq \min _{w} \max _{\alpha, \beta: \alpha_{i} \geq 0} \mathcal{L}(w, \alpha, \beta)=p^{*}
$$

在满足一些条件下 $d^{*}=p^{*}$

SVM的原始最优化问题满足强对偶条件，所有我们通过求解对偶问题来得到最优解。

##### SVM的对偶形式

$$
\begin{aligned}
&\max _{\alpha} \quad W(\alpha)=\sum_{i=1}^{m} \alpha_{i}-\frac{1}{2} \sum_{i, j=1}^{m} y^{(i)} y^{(j)} \alpha_{i} \alpha_{j}\left\langle x^{(i)}, x^{(j)}\right\rangle\\
&\text { s.t. } \quad \alpha_{i} \geq 0, \quad i=1, \ldots, m\\
&\sum_{i=1}^{m} \alpha_{i} y^{(i)}=0
\end{aligned}
$$

##### 正则化的SVM

对于由于异常点带来的线性不可分性，我们引入允许部分点的函数间隔小于1，但会给予相应的惩罚

$$
\begin{aligned}
&\min _{\gamma, w, b} \frac{1}{2}\|w\|^{2}+C \sum_{i=1}^{m} \xi_{i}\\
&\text { s.t. } \quad y^{(i)}\left(w^{T} x^{(i)}+b\right) \geq 1-\xi_{i}, \quad i=1, \ldots, m\\
&\xi_{i} \geq 0, \quad i=1, \ldots, m
\end{aligned}
$$
对偶形式：
$$
\begin{aligned}
&\max _{\alpha} \quad W(\alpha)=\sum_{i=1}^{m} \alpha_{i}-\frac{1}{2} \sum_{i, j=1}^{m} y^{(i)} y^{(j)} \alpha_{i} \alpha_{j}\left\langle x^{(i)}, x^{(j)}\right\rangle\\
&\text { s.t. } \quad 0 \leq \alpha_{i} \leq C, \quad i=1, \ldots, m\\
&\sum_{i=1}^{m} \alpha_{i} y^{(i)}=0
\end{aligned}
$$
注：正则化的SVM的原始形式等价于
$$
\min_{w,b} \sum_{i=1}^m [1-y^{(i)}(w^Tx^{(i)}+b)]_{+} + \frac{1}{2C}||w||^2
$$


##### 线性不可分下的SVM

对于上诉两个对偶形式，可以发现，对于数据的特征部分$x^{(i)}$，目标函数均可表达为数据特征向量的内积形式。对于线性不可分数据，我们认为把原始特征映射到更高维的特征空间后，数据就很可能是线性可分的。其中特征映射为$\phi(x)$,核为$K(x, z)=\phi(x)^{T} \phi(z)$。

根据对偶形式，我们不需要具体的求出$\phi(x)$,我们只需要内积即可，把上诉对偶形式中的内积替换成核就行。

##### SMO

TODO

