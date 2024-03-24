import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

def task():
    housing_data = pd.read_csv('housing.csv')
 
    low_price, high_price = SplitDataset(housing_data)
    
    #1
    #Density(housing_data, 'population')
    
    #ShowHist(low_price, high_price)
    #2 #4
    #CalcMedian(housing_data, low_price, high_price, 'population')

    #3 #4
    #CalcMedian(housing_data, low_price, high_price, 'total_rooms')
    
    #5
    #Scatter(housing_data, 'total_rooms', 'population')
    #Box(housing_data, 'population')
    #
    

    #6
    #print('All data')
    #calculate_average_value_and_standard_deviation(housing_data, 'total_rooms')
    #print('Low price')
    #calculate_average_value_and_standard_deviation(low_price, 'total_rooms')
    #print('High pricez')
    #calculate_average_value_and_standard_deviation(high_price, 'total_rooms')

    #7 #8
    evaluate_class_differences(low_price, high_price, 'housing_median_age')
    #evaluate_class_differences(low_price, high_price, 'median_house_value')

def CalcMedian(data, low_price, high_price, param_name):   
    median_n_all = data[param_name].median()
    print("TOAL median for param", param_name, ":", median_n_all)
    
    median_n_low_price = low_price[param_name].median()
    median_n_high_price = high_price[param_name].median()
    
    print("Low Price class median for for param", param_name, ":", median_n_low_price)
    print("High Price class median for for param", param_name, ":", median_n_high_price)  

    above_median = data[data[param_name] >= median_n_all]
    below_median = data[data[param_name] < median_n_all]
    
    plt.figure(figsize=(10, 6))

    sns.distplot(above_median[param_name], color='blue', label='Above Median')
    sns.distplot(below_median[param_name], color='red', label='Below Median')

    plt.xlabel(param_name)
    plt.ylabel('Frequency')
    plt.title('Distribution')
    plt.legend()
    plt.grid(True)

    plt.show()

def SplitDataset(data):
    median_price = data['median_house_value'].median()
    high_price = data[data['median_house_value'] >= median_price]
    low_price = data[data['median_house_value'] < median_price]
    data['price_class'] = data['median_house_value'].apply(lambda x: 1 if x >= median_price else 0)
    return low_price, high_price

def Density(data, param_name):
    plt.figure(figsize=(12, 8))
    sns.distplot(data[param_name], color='blue', label=param_name)

    plt.xlabel(param_name)
    plt.ylabel('Density')
    plt.title('Density Plot')
    plt.legend()

    plt.grid(True)
    plt.show()

def ShowHist(low_price, high_price):   
    plt.figure(figsize=(12, 8))
    plt.hist(high_price['median_house_value'], bins=30, color='blue', alpha=0.5, label='High Price')
    plt.hist(low_price['median_house_value'], bins=30, color='red', alpha=0.5, label='Low Price')
    plt.xlabel('Median House Value')
    plt.ylabel('Frequency')
    plt.title('Distribution of Median House Value')
    plt.legend()
    plt.grid(True)
    plt.show()
    return low_price, high_price

def ShowScatter(df, parameter_x, parameter_y):
    sns.scatterplot(x=parameter_x, y=parameter_y, data=df, color='blue', alpha=0.5, label=parameter_x)
    plt.xlabel(parameter_x)
    plt.ylabel(parameter_y)
    plt.title('Scatter Plot')
    plt.grid(True)
    plt.legend()
    plt.show()

def ShowBoxPlot(df, parameter):
    sns.boxplot(y=parameter, data=df)

    plt.xlabel(parameter)
    plt.title('Box Plot')
    plt.grid(True)
    plt.legend()
    plt.show()

def Scatter(data, param_name1, param_name2):
    med1 = data[param_name1].median()
    above_median1 = data[data[param_name1] >= med1]
    below_median1 = data[data[param_name1] < med1]
  
    med2 = data[param_name2].median()
    above_median2 = data[data[param_name2] >= med2]
    below_median2 = data[data[param_name2] < med2]

    ShowScatter(above_median1, param_name1, param_name2)
    ShowScatter(below_median1, param_name1, param_name2)
    ShowScatter(above_median2, param_name1, param_name2)
    ShowScatter(below_median2, param_name1, param_name2)

def Box(data, param_name):
    med1 = data[param_name].median()
    above_median1 = data[data[param_name] >= med1]
    below_median1 = data[data[param_name] < med1]
    ShowBoxPlot(above_median1, param_name)
    ShowBoxPlot(below_median1, param_name)


def calculate_average_value_and_standard_deviation(df, parameter_name):
    average_value = df[parameter_name].mean()
    standard_deviation = df[parameter_name].std()
    print(f'average_value {parameter_name} = {average_value}')
    print(f'standard_deviation {parameter_name} = {standard_deviation}')
    print('\n')

def evaluate_class_differences(above_median, below_median, parameter_name):
    t_statistic, p_value = ttest_ind(above_median[parameter_name], below_median[parameter_name])

    print("t_statistic value:", t_statistic)
    print("p-value:", p_value)
    alpha = 0.05
    if p_value < alpha:
        print(f"Differnve by {parameter_name} stattistically valueable.")
    else:
        print(f"Differnve by {parameter_name} not valuable.")
    print('\n')

if __name__ == "__main__":
    task()