import random
from zipfile import ZipFile
from io import BytesIO


def get_padded_int(start, end, padding=2):
    i = random.randint(start, end)
    return f"{i:0{padding}}"


def get_range_string(start, end, padding=2):
    return ",".join([f"{i:0{padding}}" for i in range(start, end+1)])


def get_rand_ymd():
    year = get_padded_int(1760, 1890, 4)
    month = get_padded_int(1, 12, 2)
    day = get_padded_int(1, 28, 2)

    return year, month, day


def get_query_url(domain="land", frequency="sub_daily", variable="air_pressure", 
                  intended_use="non_commercial", data_quality="all_data", 
                  year="1900", month="01", day=None):
    day_string = ""
    if day:
        day_string = f"&day={day}"
 
    return (f"/v1/select/?domain={domain}&frequency={frequency}&variable={variable}&"
            f"intended_use={intended_use}&data_quality={data_quality}&"
            f"year={year}&month={month}{day_string}&"
            f"column_selection=detailed_metadata&compress=true")


def check_zipfile(response, func_name):
    z = ZipFile(BytesIO(response.content))

    if len(z.namelist()) != 2:
        response.failure(f"{func_name}: expected 2 files in zip but not")

