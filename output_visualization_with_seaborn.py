# Output:
Dataset
   Age  Salary  Experience  PerformanceScore
0   25   45000           2                78
1   30   52000           5                88
2   28   48000           3                82
3   35   65000           8                91
4   40   80000          12                95
5   27   50000           4                85
6   32   58000           6                89
7   29   62000           5                92
8   31   72000           9                90
9   26   54000           3                84

First 5 Rows
   Age  Salary  Experience  PerformanceScore
0   25   45000           2                78
1   30   52000           5                88
2   28   48000           3                82
3   35   65000           8                91
4   40   80000          12                95

Dataset Information
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 4 columns):
 #   Column            Non-Null Count  Dtype
---  ------            --------------  -----
 0   Age               10 non-null     int64
 1   Salary            10 non-null     int64
 2   Experience        10 non-null     int64
 3   PerformanceScore  10 non-null     int64
dtypes: int64(4)
memory usage: 392.0 bytes
None

Dataset Shape
(10, 4)

Missing Values
Age                 0
Salary              0
Experience          0
PerformanceScore    0
dtype: int64

Data Types
Age                 int64
Salary              int64
Experience          int64
PerformanceScore    int64
dtype: object

Summary Statistics
             Age       Salary  Experience  PerformanceScore
count  10.000000     10.00000    10.00000         10.000000
mean   30.300000  58600.00000     5.70000         87.400000
std     4.522782  11187.29438     3.12872          5.125102
min    25.000000  45000.00000     2.00000         78.000000
25%    27.250000  50500.00000     3.25000         84.250000
50%    29.500000  56000.00000     5.00000         88.500000
75%    31.750000  64250.00000     7.50000         90.750000
max    40.000000  80000.00000    12.00000         95.000000

Correlation Matrix
                       Age    Salary  Experience  PerformanceScore
Age               1.000000  0.852476    0.933613          0.833104
Salary            0.852476  1.000000    0.958043          0.877091
Experience        0.933613  0.958043    1.000000          0.860617
PerformanceScore  0.833104  0.877091    0.860617          1.000000

===== Correlation Matrix Output =====
Correlation Matrix displayed successfully.

===== Heatmap Output =====
Heatmap displayed successfully.

Insights
1. Age and Salary show a positive relationship.
2. Experience and Salary are positively correlated.
3. Performance Score tends to increase with Experience.
4. Correlation Matrix helps measure relationships between variables.
5. Heatmap provides a visual representation of correlations.
