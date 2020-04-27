### Spatial Filtering

#### Introduction

Two component:  
- a neighborhood (or Mask of size $m*n$, typically, $m = n$ and $m$ is odd)
- an operation  

i.e. $dst(x,y) = T(\{src(x', y')\})$ where $(x', y')$ belong to neighborhood

A *filtered* image is generated as the **center** of the mask moves to *every* pixel in the *input* image

- choose mask weights: typically, sampling certain function
- we need to handle pixels close to boundaries(e.g. zero padding)

#### Linear vs Non-Linear 

- A filtering method is linear when the output is a weighted sum of the input pixels
- Otherwise, methods are called non-linear(e.g. median filter)

##### Linear Spatial Filtering Methods  

- Correlation
- Convolution(== flipped correlation mask)

#### Smoothing vs Sharpening

##### Smoothing Filter

- Useful for reducing noise and eliminating small details  
- The elements of the mask are non-negative 
- Sum of mask elements is 1 (after normalization) 

e.g. Mean filter, Guassian blur, Median filter(non-linear),etc

##### Sharpening Filters

- Useful for highlighting fine details  
- The elements of the mask contain both positive and negative weights  
- Sum of mask elements is 0

e.g. Unsharp masking, High Boost filter, Gradient (1st derivative), Laplacian (2nd derivative) 

TODO: add details and example code

