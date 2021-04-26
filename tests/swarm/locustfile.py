import json

from locust import HttpUser, between, task

from tests.swarm.common import (get_rand_ymd, get_query_url, get_range_string,
                                check_zipfile)


class CdmLensUser(HttpUser):
    host = "http://localhost:5000"
    wait_time = between(1, 10)


    def _check_zip_response(self, query, func_name):
        with self.client.get(query, catch_response=True, name=func_name) as response:
            check_zipfile(response, func_name)


    @task(1)
    def marine_constraints(self):
        query = "/v1/constraints/marine"

        with self.client.get(query, catch_response=True, name="marine_constraints") as response:
            if "water_temperature" not in response.text:
                response.failure("marine_constraints: response not as expected")

    @task(1)
    def land_constraints(self):
        query = "/v1/constraints/land"

        with self.client.get(query, catch_response=True, name="land_constraints") as response:
            if "air_temperature" not in response.text:
                response.failure("land_constraints: response not as expected")

    @task(1)
    def land_1_day_sub_daily(self):
        year, month, day = get_rand_ymd()
        query = get_query_url(domain="land", frequency="sub_daily", 
                              variable="air_pressure", intended_use="non_commercial",
                              data_quality="all_data", year=year, month=month, day=day)

        self._check_zip_response(query, "land_1_day_sub_daily")

    @task(1)
    def land_1_month_monthly(self):
        year, month, _ = get_rand_ymd()
        query = get_query_url(domain="land", frequency="monthly",
                              variable="air_temperature", intended_use="non_commercial",
                              data_quality="all_data", year=year, month=month)

        self._check_zip_response(query, "land_1_month_monthly")

    @task(1)
    def land_full_month_daily(self):
        year, month, _ = get_rand_ymd()
        day = get_range_string(1, 28)
        query = get_query_url(domain="land", frequency="sub_daily",
                              variable="air_pressure", intended_use="non_commercial",
                              data_quality="all_data", year=year, month=month, day=day)

        self._check_zip_response(query, "land_full_month_daily")

