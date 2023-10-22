# Databricks notebook source
# MAGIC %sql
# MAGIC -- This SQL query selects the first 10 rows from the table
# MAGIC SELECT * FROM default.yellow_taxi_nyc_trip_data_2_csv LIMIT 10;

# COMMAND ----------

# MAGIC %sql
# MAGIC DESCRIBE TABLE default.yellow_taxi_nyc_trip_data_2_csv;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Calculating Basic Statistics: Average distance, fare, and tip
# MAGIC SELECT 
# MAGIC   AVG(trip_distance) AS avg_distance, 
# MAGIC   AVG(fare_amount) AS avg_fare, 
# MAGIC   AVG(tip_amount) AS avg_tip 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv;
# MAGIC
# MAGIC -- Counting the Total Number of Rides
# MAGIC SELECT COUNT(*) AS total_rides FROM default.yellow_taxi_nyc_trip_data_2_csv;
# MAGIC
# MAGIC -- Analyzing Number of Trips per Hour (Time-Based Analysis)
# MAGIC SELECT 
# MAGIC   EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour, 
# MAGIC   COUNT(*) AS number_of_trips 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY 
# MAGIC   hour 
# MAGIC ORDER BY 
# MAGIC   hour;
# MAGIC
# MAGIC -- Identifying Most Common Pickup Locations (Location-Based Insights)
# MAGIC SELECT PULocationID, COUNT(*) AS trip_count 
# MAGIC FROM default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY PULocationID 
# MAGIC ORDER BY trip_count DESC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT PULocationID, trip_count 
# MAGIC FROM 
# MAGIC   (SELECT PULocationID, COUNT(*) AS trip_count 
# MAGIC    FROM default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC    GROUP BY PULocationID 
# MAGIC    ORDER BY trip_count DESC) AS subquery 
# MAGIC LIMIT 10;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour, 
# MAGIC   COUNT(*) AS number_of_trips 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY 
# MAGIC   hour 
# MAGIC ORDER BY 
# MAGIC   hour;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   EXTRACT(HOUR FROM tpep_pickup_datetime) AS hour, 
# MAGIC   AVG(fare_amount) AS average_fare 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY 
# MAGIC   hour 
# MAGIC ORDER BY 
# MAGIC   hour;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   passenger_count, 
# MAGIC   COUNT(*) AS number_of_trips 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY 
# MAGIC   passenger_count 
# MAGIC ORDER BY 
# MAGIC   passenger_count;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   payment_type, 
# MAGIC   COUNT(*) AS number_of_transactions 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv 
# MAGIC GROUP BY 
# MAGIC   payment_type 
# MAGIC ORDER BY 
# MAGIC   number_of_transactions DESC;
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC   MAX(trip_distance) AS longest_trip, 
# MAGIC   MIN(trip_distance) AS shortest_trip 
# MAGIC FROM 
# MAGIC   default.yellow_taxi_nyc_trip_data_2_csv;
# MAGIC

# COMMAND ----------

# MAGIC %pip install matplotlib seaborn
# MAGIC

# COMMAND ----------

import matplotlib.pyplot as plt
import seaborn as sns

# Assume 'hours' and 'number_of_trips' are lists containing the data of hours and the corresponding number of trips.
hours = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]  # example data
number_of_trips = [84969, 59799, 42040, 27438, 17835, 18011, 43860, 86877, 116865, 131111, 143666, 154157, 169858, 178739, 191604, 196424, 195977]  # example data

plt.figure(figsize=(10, 6))
sns.lineplot(x=hours, y=number_of_trips, marker='o')
plt.title('Number of Trips by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Number of Trips')
plt.grid(True)
plt.show()


# COMMAND ----------

# Assume 'average_fare' is a list containing the data of the average fare per hour.
average_fare = [19.58, 17.74, 16.73, 17.67, 22.00, 26.16, 21.95, 18.87, 17.42, 17.49, 17.54, 17.23, 17.59, 18.26, 19.49, 19.07, 19.29]  # example data

plt.figure(figsize=(10, 6))
sns.lineplot(x=hours, y=average_fare, marker='o', color='orange')
plt.title('Average Fare by Hour')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Fare ($)')
plt.grid(True)
plt.show()


# COMMAND ----------

# Assume 'locations' and 'trip_counts' are lists of the pickup locations and the number of trips from those locations.
locations = [132, 237, 236, 161, 186]  # top 5 for illustration
trip_counts = [160030, 148074, 138391, 135417, 109227]  # example data

plt.figure(figsize=(10, 6))
sns.barplot(x=locations, y=trip_counts, palette='viridis')
plt.title('Most Common Pickup Locations')
plt.xlabel('Location ID')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)  # Rotates X-axis labels for readability
plt.tight_layout()
plt.show()

