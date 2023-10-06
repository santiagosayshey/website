## GPPi: The Decision Engine

The GPPi is a calculated metric, pivotal to the "Transparent" profile's decision-making process. It's engineered to rank release groups based on their consistent delivery of 'Golden Popcorn' quality releases for a given resolution. The formula is a delicate interplay between a group's Golden Popcorn performance and their overall release activity at that resolution.

### Formula

For any given resolution *r*, the GPPi is defined as:

$$ 
GPPi_r = \frac{\left( GPE_r \right)^2}{E_r} 
$$

Where:
$$ 
\begin{align*}
GPPi_r & : \text{Golden Popcorn Performance index at resolution } r \\
GPE_r & : \text{Number of Golden Popcorn Encodes at resolution } r \\
E_r & : \text{Total encodes at resolution } r
\end{align*}
$$

- This algorithm is pretty straightforward. Essentially, it limits both metrics against one another to ensure that one metric is not more important than the other. If we were to take Golden Popcorn ratio at face value, we might incorrectly prioritise a release group who has only ever released a handful of encodes, but each of them are GPs. 