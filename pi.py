import findspark
findspark.init()
findspark.find()
import pyspark
findspark.find()
from pyspark import SparkContext
from time import time
import numpy as np
from random import random
from operator import add

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('CalculatePi').getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("ERROR")
n = 10000000

def is_point_inside_unit_circle(p):
    x, y = random(), random()
    return 1 if x*x + y*y < 1 else 0


t_0 = time()

count = sc.parallelize(range(0, n)) \
             .map(is_point_inside_unit_circle).reduce(add)

# or count.map(is_point_inside_unit_circle)

print(np.round(time()-t_0, 3), " Temps pour n=", n)

print("{0} ={1}".format ("Pi",(4.0 * count / n)))


