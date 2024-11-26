from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("MoviesAnalysis").getOrCreate()

# Load JSON dataset
movies_df = spark.read.json("/Users/hunjunsin/Desktop/box/Introduction_DMB/Assignment/Assignment5/movies.json")


# This exercise uses a dataset of movies released worldwide, focusing on various aspects of film production and performance. Load the movies.json file into Spark and answer the following questions:
# 1. Show the total number of movies in each genre with (a) the DataFrame API, (b) Spark SQL, and (c) RDD operations. Identify the most efficient method.
# 2. Find the directors who directed the highest number of movies.
# 3. Determine the genres with the highest average IMDb rating (use the imdb.rating field).
# 4. Find the month with the most movie releases based on the released date.
# 5. Identify the top 5 movies with the longest runtime in each genre.
# 6. Find the top 10 actors who appeared in the most movies. For each actor, list the number of movies and their average IMDb rating.
# 7. Plot a bar chart with the number of movies released each year.

# 1. Total number of Movies by Genre

from pyspark.sql.functions import explode, col, avg, month, col

# genre_count_df = movies_df.select(explode(col("genres")).alias("genre")).groupBy('genre').count()

# genre_count_df.show()


# # Register DataFrame as a SQL temporary view
# movies_df.createOrReplaceTempView("movies")

# # Execute SQL query
# genre_count_sql = spark.sql("""
#     SELECT genre, COUNT(*) as count 
#     FROM (SELECT EXPLODE(genres) AS genre FROM movies) 
#     GROUP BY genre
# """)
# genre_count_sql.show()


# genre_count_rdd = movies_df.select("genres").rdd.\
#     filter(lambda row: row["genres"] is not None).\
#         flatMap(lambda row: row["genres"]).\
#         map(lambda genre: (genre, 1)) .reduceByKey(lambda a, b: a + b)

# print(genre_count_rdd.collect())


# director_count_df = movies_df.filter(movies_df.directors.isNotNull()) \
#                              .groupBy("directors").count() \
#                              .orderBy("count", ascending=False)

# director_count_df.show(1)

# 임시 뷰로 등록 후 SQL 쿼리 실행
# # Register DataFrame as a SQL temporary view
# movies_df.createOrReplaceTempView("movies")

# # Execute SQL query
# average_rating_sql = spark.sql("""
#     SELECT genre, AVG(CAST(imdb.rating.$numberDouble AS DOUBLE)) AS avg_rating
#     FROM (SELECT EXPLODE(genres) AS genre, imdb.rating AS rating FROM movies) 
#     GROUP BY genre
# """)
# average_rating_sql.show()

# movies_df.printSchema()

# from pyspark.sql.functions import explode, col, avg

# average_rating_df = movies_df \
#     .withColumn("genre", explode("genres")) \
#     .withColumn("rating", col("imdb.rating.$numberDouble").cast("double")) \
#     .groupBy("genre") \
#     .agg(avg("rating").alias("avg_rating"))\
#     .orderBy('avg_rating', ascending= False)

# average_rating_df.show(1)


# from pyspark.sql.functions import to_date, month, col

# # "released" 컬럼이 구조체 타입이기 때문에, 이를 문자열로 변환하여 사용할 수 있도록 처리합니다.
# movies_df = movies_df.withColumn("release_date", to_date(col("released.$date.$numberLong").cast("long") / 1000))

# # release_date에서 month를 추출하여 release_month 컬럼을 생성합니다.
# movies_df = movies_df.withColumn("release_month", month("release_date"))

# # 월별 영화 개수 계산
# month_count_df = movies_df.where(col("release_date").isNotNull())\
#                           .groupBy("release_month")\
#                           .count() \
#                           .orderBy("count", ascending=False)

# # 가장 많은 개봉작이 있는 월 출력
# month_count_df.show(1)

# from pyspark.sql.functions import to_date, month, col


# movies_df = movies_df.withColumn("release_date", to_date((col("released.$date.$numberLong").cast("long") / 1000).cast("timestamp")))


# movies_df = movies_df.withColumn("release_month", month("release_date"))


# month_count_df = movies_df.where(col("release_date").isNotNull()) \
#                           .groupBy("release_month") \
#                           .count() \
#                           .orderBy("count", ascending=False)


# month_count_df.show(1)


# movies_df = movies_df.withColumn("genre", explode("genres"))
# movies_df.createOrReplaceTempView("movies")

# query = """
# SELECT genre, title, runtime
# FROM (
#     SELECT genre, title, runtime,
#            ROW_NUMBER() OVER (PARTITION BY genre ORDER BY runtime DESC) as rank
#     FROM movies
# ) ranked_movies
# WHERE rank <= 5
# ORDER BY genre, rank
# """

# top_5_movies_by_genre = spark.sql(query)
# top_5_movies_by_genre.show()


# from pyspark.sql.functions import explode, avg, count

# movies_df = movies_df.withColumn("rating_float", col("imdb.rating.$numberDouble").cast("double"))
# movies_df = movies_df.withColumn("actor", explode("cast"))
# result_df = movies_df.groupBy("actor")\
#     .agg(count("title").alias("movie_count"), avg("rating_float").alias("avg_rating"))\
#     .orderBy(col("movie_count").desc())
    
# # top_10 = result_df.limit(10)
# # top_10.show()
# import matplotlib.pyplot as plt
# import pyspark.sql.functions as F
# from pyspark.sql import SparkSession

# # Try to cast the year column to integer and filter out any rows with null years
# movies_df = movies_df.withColumn("year", F.col("year").cast("int"))
# movies_df = movies_df.filter(F.col("year").isNotNull())

# # Debug: Check the first few rows after casting and filtering
# print("Movies DataFrame after casting 'year' to int and filtering nulls:")
# movies_df.show(5)

# # Group by year and count the number of movies released each year
# movies_by_year = movies_df.groupBy("year").agg(F.count("title").alias("movie_count"))

# # Debug: Show the first few rows of movies_by_year
# print("Movies grouped by year:")
# movies_by_year.show(5)

# # Convert to Pandas DataFrame for plotting
# movies_by_year_pd = movies_by_year.toPandas()

# # Debug: Check if movies_by_year_pd has data
# print("Data for plotting:")
# print(movies_by_year_pd.head())

# # If there is data, proceed with plotting
# if not movies_by_year_pd.empty:
#     # Sort by year in ascending order
#     movies_by_year_pd = movies_by_year_pd.sort_values(by="year")

#     # Plot the number of movies released each year as a bar chart
#     plt.figure(figsize=(12, 6))
#     plt.bar(movies_by_year_pd["year"], movies_by_year_pd["movie_count"])
#     plt.xlabel("Year")
#     plt.ylabel("Number of Movies Released")
#     plt.title("Number of Movies Released Each Year")

#     # Set x-axis ticks for every 5 years to avoid clutter
#     plt.xticks(movies_by_year_pd["year"][::5], rotation=45)

#     plt.tight_layout()
#     plt.show()
# else:
#     print("No data available for plotting.")


# # Print the schema to see the structure of `year`
# movies_df.printSchema()

# # Show a few rows with the `year` column to inspect its raw format
# movies_df.select("year").show(5, truncate=False)


from pyspark.sql import functions as F

movies_df = movies_df.withColumn("year", F.regexp_extract("year", r'"(\d+)"', 1).cast("int"))
movies_df = movies_df.filter(F.col("year").isNotNull())
movies_by_year = movies_df.groupBy("year").agg(F.count("title").alias("movie_count"))
movies_by_year_pd = movies_by_year.orderBy("year").toPandas()

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(movies_by_year_pd["year"], movies_by_year_pd["movie_count"])
plt.xlabel("Year")
plt.ylabel("Number of Movies Released")
plt.title("Number of Movies Released Each Year")
plt.xticks(rotation=45)
plt.show()