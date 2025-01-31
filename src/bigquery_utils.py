import json
import logging

import boto3
import pandas as pd
from google.cloud import bigquery
from google.oauth2.service_account import Credentials

from .config import BQ_OBJECT_KEY_NAME, QUERY_PATH, ROOT_BUCKET_NAME


def initialize_bigquery_client() -> bigquery.Client | None:
    """
    BigQueryクライアントを初期化する。

    Returns:
        bigquery.Client: BigQueryクライアント
    """
    try:
        s3 = boto3.resource("s3")
        bucket = s3.Bucket(ROOT_BUCKET_NAME)
        obj = bucket.Object(BQ_OBJECT_KEY_NAME)
        bigquery_credentials = Credentials.from_service_account_info(
            json.loads(obj.get()["Body"].read().decode("utf-8")),
            scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        bigquery_client = bigquery.Client(
            credentials=bigquery_credentials,
            project=bigquery_credentials.project_id,
            location="asia-northeast1",
        )
        return bigquery_client
    except Exception as e:
        logging.error(f"BigQueryクライアントの初期化に失敗しました: {e}")
        return None


def get_matching_info(client: bigquery.Client) -> pd.DataFrame | None:
    """
    BigQueryからマッチング情報を取得する。

    Parameters:
        matching_id (str): マッチングID

    Returns:
        Tuple[str, str]: (売手企業名, 買手企業名)
    """
    try:
        with open(QUERY_PATH, "r") as file:
            query = file.read()

        df = client.query(query).result().to_dataframe()
        return df
    except Exception as e:
        logging.error(f"BigQueryのクエリでエラーが発生しました: {e}")
        return None
