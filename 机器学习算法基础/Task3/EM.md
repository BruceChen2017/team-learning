### The EM algorithm
Give data $\{x^{(1)}, ..., x^{(m)}\}$, log likelihood is 
$$\begin{aligned}
\ell(\theta) &=\sum_{i=1}^{m} \log p(x ; \theta) \\
&=\sum_{i=1}^{m} \log \sum_{z} p(x, z ; \theta)
\end{aligned}$$
where $z$ is latent unobserved variable.  
$$
\begin{aligned}
\sum_{i} \log p\left(x^{(i)} ; \theta\right) &=\sum_{i} \log \sum_{z^{(i)}} p\left(x^{(i)}, z^{(i)} ; \theta\right) \\
&=\sum_{i} \log \sum_{z^{(i)}} Q_{i}\left(z^{(i)}\right) \frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q_{i}\left(z^{(i)}\right)} \\
& \geq \sum_{i} \sum_{z^{(i)}} Q_{i}\left(z^{(i)}\right) \log \frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q_{i}\left(z^{(i)}\right)}
\end{aligned}
$$  
where $Q_i$ be some distribution over the $z$'s $\left(\sum_{z} Q_{i}(z)=1, Q_{i}(z) \geq 0\right)$  
To make the bound tight for a particular value of $\theta$, we need to make
$Q_{i}\left(z^{(i)}\right) \propto p\left(x^{(i)}, z^{(i)} ; \theta\right)$.Thus 
$$\begin{aligned}
Q_{i}\left(z^{(i)}\right) &=\frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{\sum_{z} p\left(x^{(i)}, z ; \theta\right)} \\
&=\frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{p\left(x^{(i)} ; \theta\right)} \\
&=p\left(z^{(i)} | x^{(i)} ; \theta\right)
\end{aligned}
$$  
i.e. we simply set the $Q_{i}$'s to be the **posterior** distribution of the $z^{(i)}$'s given $x^{(i)}$ and the setting of the parameters $\theta$.This is **E-step**.  
Next,for this choice of $Q_i$'s,
$$\theta:=\arg \max _{\theta} \sum_{i} \sum_{z^{(i)}} Q_{i}\left(z^{(i)}\right) \log \frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q_{i}\left(z^{(i)}\right)}$$  
This is **M-step**.  
Next, we show that EM always monotonically improves the log-likelihood.  
> Proof: Need to show $\ell\left(\theta^{(t)}\right) \leq \ell\left(\theta^{(t+1)}\right)$  
> Given $\theta^{(t)}$, by **E-step**, we set $Q_{i}^{(t+1)}\left(z^{(i)}\right):=p\left(z^{(i)} | x^{(i)} ; \theta^{(t)}\right)$  
> Then we have
> $$\begin{aligned}
\ell\left(\theta^{(t+1)}\right) & \geq \sum_{i} \sum_{z^{(i)}} Q_{i}^{(t+1)}\left(z^{(i)}\right) \log \frac{p\left(x^{(i)}, z^{(i)} ; \theta^{(t+1)}\right)}{Q_{i}^{(t+1)}\left(z^{(i)}\right)} \\
& \geq \sum_{i} \sum_{z^{(i)}} Q_{i}^{(t+1)}\left(z^{(i)}\right) \log \frac{p\left(x^{(i)}, z^{(i)} ; \theta^{(t)}\right)}{Q_{i}^{(t+1)}\left(z^{(i)}\right)} \\
&=\ell\left(\theta^{(t)}\right) \qquad Q.E.D
\end{aligned}$$
*Remark*: If we define $J(Q, \theta)=\sum_{i} \sum_{z^{(i)}} Q_{i}\left(z^{(i)}\right) \log \frac{p\left(x^{(i)}, z^{(i)} ; \theta\right)}{Q_{i}\left(z^{(i)}\right)}$, the EM can also be viewed a *coordinate ascent* on $J$.  

**Reference**:  
1. cs229-note8
