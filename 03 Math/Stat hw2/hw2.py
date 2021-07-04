from scipy.stats import norm
import numpy as np

print(f'{norm.cdf(2)-norm.cdf(-2):.4f}')
print(f'{norm.cdf(3)-norm.cdf(-3):.4f}')


# Параметры для бутстрэпа

sample1 = np.random.normal(14,1,size=50) 

def ci_param_bootstrap(data, alpha=0.05, number_of_bootstrap_samples=10, size_of_bootstrap_samples=20 ):
    """параметрический бутстрэп

    Args:
        data (array like): данные для оценки среднего
        alpha (float, optional): увроень доверия. Defaults to 0.05.
        number_of_bootstrap_samples (int, optional): сколько сэмплов для бутстрэпа делать. Defaults to 10.
        size_of_bootstrap_samples (int, optional): сколько наблюдений делать в каждый сэмпл. Defaults to 20.
    """
    # Оцениваем неизвестный параметр theta 
    sample_mean = np.mean(data) 
    sample_std = np.std(data, ddof=1)
    # print(sample_mean, sample_std)

    # Генерируем выборку из распределения N(sample_mean, sigma)
    bootstrap_samples = np.random.normal(sample_mean,sample_std,size=[number_of_bootstrap_samples,size_of_bootstrap_samples]) 

    #  Считаем среднее для каждой выборки 
    bootstrap_estimates = np.apply_along_axis(np.mean, 1, bootstrap_samples)

    # Вычисляем параметрический бутстрэп доверительный интервал
    CI_Bootstrap_Parametric = (np.quantile(bootstrap_estimates,alpha/2), np.quantile(bootstrap_estimates,1-alpha/2))

    return(CI_Bootstrap_Parametric)

print(ci_param_bootstrap(sample1))

def ci_non_param_bootstrap(data, alpha=0.05, number_of_bootstrap_samples=10, size_of_bootstrap_samples=20 ):
    """непараметрический бутстрэп

    Args:
        data (array like): данные для оценки среднего
        alpha (float, optional): увроень доверия. Defaults to 0.05.
        number_of_bootstrap_samples (int, optional): сколько сэмплов для бутстрэпа делать. Defaults to 10.
        size_of_bootstrap_samples (int, optional): сколько наблюдений делать в каждый сэмпл. Defaults to 20.
    """

    # Генерируем выборку из исходного распределения
    bootstrap_samples = np.random.choice(data,size=[number_of_bootstrap_samples,size_of_bootstrap_samples]) 

    #  Считаем среднее для каждой выборки 
    bootstrap_estimates = np.apply_along_axis(np.mean, 1, bootstrap_samples)

    # Вычисляем параметрический бутстрэп доверительный интервал
    CI_Bootstrap_Parametric = (np.quantile(bootstrap_estimates,alpha/2), np.quantile(bootstrap_estimates,1-alpha/2))

    return(CI_Bootstrap_Parametric)

print(ci_non_param_bootstrap(sample1))

