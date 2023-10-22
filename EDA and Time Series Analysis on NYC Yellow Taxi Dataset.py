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
