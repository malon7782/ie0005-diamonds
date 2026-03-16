# Conclusions drawn from explore.py:

## For _numeric_ values, 

price is highly(~92) correlated to carat weight;
price is also highly(~88) correlated to x, y and z.

_(Note that the correlation coefficient between x, y, z, and carat weight is close to 1;_
_This is clearly because the side length determines the volume, which in turn determines the carat weight)_

Here, we select *carat weight* as one of the predictors.

## For _non-numeric_ values,

Surprisingly, as the cut approaches 'ideal' and the color approaches 'D', the price actually decreases.

I suspect this is because diamonds with excellent cut and perfect color are typically smaller,  
so their price is lower relative to larger diamonds with poorer cut and less desirable color.
