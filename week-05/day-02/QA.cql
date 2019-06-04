describe table isd_weather_data.weather_station;

Where is this weather station?

cqlsh> select country_code from isd_weather_data.weather_station where id = '724940:23234';

 country_code
--------------
           US

(1 rows)
cqlsh>
Show the temperature for June 1st, 2008.
 select temperature from isd_weather_data.raw_weather_data
                    ... where wsid = '724940:23234' and year = 2008 and month = 6 and day = 1;

 temperature
-------------
          15
          15
        15.6
          15
          15
        14.4
        13.3
        12.2
        11.7
        10.6
          10
          10
        10.6
        11.1
        11.1
           0
        11.7
        11.7
        11.7
        11.7
        11.7
        12.2
        12.8
        13.3

(24 rows)

Show the temperatures for June 1st, 2008 from 9AM to 3PM.
cqlsh:isd_weather_data> select temperature from isd_weather_data.raw_weather_data
                    ... where wsid = '724940:23234' and year = 2008 and month = 6 and day
                    ... = 1 and hour > 9 and hour < 15;

 temperature
-------------
        10.6
          10
          10
        10.6
        11.1

What is the average elevation of the weather stations in Indiana?

CREATE CUSTOM INDEX E_ID ON isd_weather_data.weather_station(name) USING 'org.apache.cassandra.index.sasi.SASIIndex' WITH OPTIONS = {'analyzer_class': 'org.apache.cassandra.index.sasi.analyzer.StandardAnalyzer', 'case_sensitive': 'false'};

select avg(elevation) from isd_weather_data.weather_station where name like 'INDIANA%';

 system.avg(elevation)
-----------------------
             305.76667

(1 rows)

What is the latitude of the northest weather station in Texas?
cqlsh:isd_weather_data> select max(long) from weather_station where state_code = 'TX' allow filtering;

 system.max(long)
------------------
           -93.75

(1 rows)

Fill the daily_aggregate_temperature table.

