from pyspark.shell import spark
from pyspark.sql import DataFrame
from pyspark.sql.types import StructType


def load_dataframe(csv_filename: str, schema: StructType) -> DataFrame:
    return spark.read.csv(
        csv_filename,
        header=True,
        schema=schema,
        # encoding="cp1251"
    )
