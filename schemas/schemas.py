from pyspark.sql.types import StructType, IntegerType, StructField, StringType


PRODUCTS_TABLE_SCHEMA = StructType([
    StructField("id", IntegerType(), False),
    StructField("name", StringType(), False)
])

CATEGORIES_TABLE_SCHEMA = StructType([
    StructField("id", IntegerType(), False),
    StructField("title", StringType(), False)
])

PRODUCTS_CATEGORIES_TABLE_SCHEMA = StructType([
    StructField("id", IntegerType(), False),
    StructField("product_id", StringType(), False),
    StructField("category_id", StringType(), False),
])
