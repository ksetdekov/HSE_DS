from scipy.stats import norm
print(f'{norm.cdf(2)-norm.cdf(-2):.4f}')
print(f'{norm.cdf(3)-norm.cdf(-3):.4f}')
