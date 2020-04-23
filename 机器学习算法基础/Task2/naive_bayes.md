### Naive bayes classfier

#### Introduction

It is probabilistic model based on  Bayes' rule and conditional independence between features given the value of the class variable
$$
\begin{aligned}
P\left(y | x_{1}, \ldots, x_{n}\right) &= \frac{P(y) P\left(x_{1}, \ldots x_{n} | y\right)}{P\left(x_{1}, \ldots, x_{n}\right)} \\
& = \frac{P(y) \prod_{i=1}^{n} P\left(x_{i} | y\right)}{P\left(x_{1}, \ldots, x_{n}\right)} \quad\text {    given conditional independence}
\end{aligned}
$$
since $P\left(x_{1}, \ldots, x_{n}\right)$ is constant given the input, we can use the following classification rule:
$$
P\left(y | x_{1}, \ldots, x_{n}\right) \propto P(y) \prod_{i=1}^{n} P\left(x_{i} | y\right)  \quad \text{i.e. prior $\times$ likehood}\\ \Downarrow \\
\hat{y}=\arg \max _{y} P(y) \prod_{i=1}^{n} P\left(x_{i} | y\right) \quad \text{i.e. MAP(mode of posterior density)}
$$
#### Estimation of  $P(y)$ and $P(x_i | y)$ 

​	Generally, prior $\hat{P}(y=c_k) = \frac{\sum\limits_{i=1}^N \mathbb{I}(y_i = c_k)}{N}$ (This is MLE of likehood $\prod_{k=1}^K p_k^{\sum_{i=1}^{n}\mathbf{I}(y_i = k)}$ with **constraint** $\sum_{k=1}^K p_k = 1$) or $\hat{P}(y=c_k) = \frac{\sum\limits_{i=1}^N  \mathbb{I}(y_i = c_k) + \alpha}{N + K\alpha}$ (This is posterior expectation estimator(**PEE**),i.e bayes point estimator(**BPE**) with prior $\mathbf{p} = (p_1,...,p_K) \sim Dir(\alpha,...,\alpha)$)

​	Different assumption of distribution of likelihood results in various types


-  Gaussian Naive Bayes
  
    $x_{i} | y \sim N(\mu_y, \sigma_y)$ , $\sigma_y$ and $\mu_y$  are estimated using maximum likelihood
  
- Discrete Naive Bayes

    $x_i | y \sim MN(1, p)$ , then **PEE** (avoid zero case)
    $$
    \begin{array}{c} P\left(X^{(j)}=a_{j l} | Y=c_{k}\right)=\frac{{\sum_{i=1}^{N} I\left(x_{i}^{(j)}=a_{j i}, y_{i}=c_{k}\right) + \alpha}}{{\sum_{i=1}^{N} I\left(y_{i}=c_{k}\right)}+S_j\alpha} \\ {j=1,2, \cdots, n ; \quad l=1,2, \cdots, S_{j} : k=1,2, \cdots, K}\end{array}
    $$

- Multinomial Naive Bayes(*sklearn*)

    $(x_1,...,x_n)|y \sim MN(N, p)$ ,this is assumption of joint likelihood, which means input $(x_i,...,x_n)$ must be non-negative integer, and conditional probability is estimated by **PEE**
