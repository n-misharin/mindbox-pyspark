from typing import Union

from pyspark.sql import DataFrame, Column

from schemas.schemas import PRODUCTS_TABLE_SCHEMA, CATEGORIES_TABLE_SCHEMA, PRODUCTS_CATEGORIES_TABLE_SCHEMA
from utils.load_dataframe import load_dataframe


def get_categories_for_all_products(
        products: DataFrame,
        categories: DataFrame,
        products_categories: DataFrame,
        columns: Union[list[Column], list[str]]
) -> DataFrame:
    return products_categories. \
        join(products, products_categories.product_id == products.id, "rightouter"). \
        join(categories, products_categories.category_id == categories.id, "leftouter"). \
        select(columns)


if __name__ == "__main__":
    products_df = load_dataframe("data/products.csv", PRODUCTS_TABLE_SCHEMA)
    categories_df = load_dataframe("data/categories.csv", CATEGORIES_TABLE_SCHEMA)
    pc_df = load_dataframe("data/pc.csv", PRODUCTS_CATEGORIES_TABLE_SCHEMA)

    # products_df.show()
    # categories_df.show()
    # pc_df.show()

    get_categories_for_all_products(
        products_df,
        categories_df,
        pc_df,
        ["name", "title"]
    ).show()
