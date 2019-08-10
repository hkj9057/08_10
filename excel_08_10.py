#-*-coding:utf-8-*-
import pandas as pd
#무비파일을 가져옴
movies = pd.read_csv("movies.csv")
"""
#위에몇개만
print(movies.head())

#밑에몇개만
print(movies.tail())

#칼럼
print(movies.columns)

#통계적인 수치를 출력
print(movies.describe())

#엑셀파일에서 부분적인 칼럼 가져오기
sheet_1 = movies[['Title','Year','Country']]
print(sheet_1)

#행 범위로 부분적으로 가져 오고 싶을때
print(movies[15:20])

#열, 행 두개를 섞어서 사용하는
print(movies.loc[0:5,['Year', 'Title']])
print(movies.iloc[3:5,0:2])

#조건으로 검색하고 싶을때
print(movies[movies.Year > 2015])

#없는 데이터가 얼마만큼이나 있는지 구하는것
for col in movies.columns:
    msg = print('columns : {:<30}\t Percent of NaN value{:.2f}%'
                .format(col,100* (movies[col].isnull().sum()/movies[col].shape[0])))

#결측치를 바꿔주고 싶을때
print(movies.fillna(value=0))

#데이터의 갯수를 세고 싶을
print(movies['Year'].value_counts())

print(movies.fillna(value=0))
"""
excel_file = 'part_time.csv'
df = pd.read_csv(excel_file)

df['total_time'] = df['End_time'] - df['Start_time']

df['time_of_make'] = df['total_time'] / df['Make']

df = df.sort_values(by=['time_of_make'], ascending=False)
df.to_csv('df.csv')
