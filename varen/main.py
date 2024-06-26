import logging
import os
import sys
import xml.etree.ElementTree as ET

import requests
from pydantic import BaseModel

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(os.environ.get("LOG_LEVEL", logging.INFO))


class OpenDataAPI:
    def __init__(self, api_token: str):
        self.base_url = "https://api.dataplatform.knmi.nl/open-data/v1"
        self.headers = {"Authorization": api_token}

    def __get_data(self, url, params=None):
        return requests.get(url, headers=self.headers, params=params).json()

    def list_files(self, dataset_name: str, dataset_version: str, params: dict):
        return self.__get_data(
            f"{self.base_url}/datasets/{dataset_name}/versions/{dataset_version}/files",
            params=params,
        )

    def get_file_url(self, dataset_name: str, dataset_version: str, file_name: str):
        return self.__get_data(
            f"{self.base_url}/datasets/{dataset_name}/versions/{dataset_version}/files/{file_name}/url"
        )


def download_file_from_temporary_download_url(download_url, filename):
    try:
        with requests.get(download_url, stream=True) as r:
            r.raise_for_status()
            with open(filename, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
    except Exception:
        logger.exception("Unable to download file using download URL")
        sys.exit(1)

    logger.info(f"Successfully downloaded dataset file to {filename}")


class DailyForecast(BaseModel):
    temperature: int
    precipitation: int
    sun: int


def parse_weather_forecast_xml(xml: str) -> list[DailyForecast]:
    root = ET.fromstring(xml)
    forecast = root.find("Middellange_x0020_en_x0020_lange_x0020_Termijn")
    forecast_objects = []
    for i in range(1, 7):
        try:
            daily_forecast = DailyForecast(
                temperature=int(forecast.find(f"maximumtemperatuur_max_dag{i}").text),
                precipitation=int(forecast.find(f"neerslagkans_dag{i}").text),
                sun=int(forecast.find(f"zonneschijnkans_dag{i}").text),
            )
            forecast_objects.append(daily_forecast)
        except Exception as e:
            logger.exception(f"Unable to parse data of day {i}: {e}")

    return forecast_objects


def main():
    api_key = os.environ["API_KEY"]
    dataset_name = "outlook_weather_forecast"
    dataset_version = "1.0"
    logger.info(f"Fetching latest file of {dataset_name} version {dataset_version}")

    api = OpenDataAPI(api_token=api_key)

    # sort the files in descending order and only retrieve the first file
    params = {"maxKeys": 1, "orderBy": "created", "sorting": "desc"}
    response = api.list_files(dataset_name, dataset_version, params)
    if "error" in response:
        logger.error(f"Unable to retrieve list of files: {response['error']}")
        sys.exit(1)

    latest_file = response["files"][0].get("filename")
    logger.info(f"Latest file is: {latest_file}")

    # fetch the download url and download the file
    response = api.get_file_url(dataset_name, dataset_version, latest_file)
    download_file_from_temporary_download_url(
        response["temporaryDownloadUrl"], latest_file
    )


if __name__ == "__main__":
    main()
