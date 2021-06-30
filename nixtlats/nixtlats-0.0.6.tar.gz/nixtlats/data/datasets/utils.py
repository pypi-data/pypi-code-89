# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/data_datasets__utils.ipynb (unless otherwise specified).

__all__ = ['logger', 'download_file', 'Info', 'TimeSeriesDataclass', 'get_holiday_dates', 'holiday_kernel',
           'create_calendar_variables', 'create_us_holiday_distance_variables', 'US_FEDERAL_HOLIDAYS']

# Cell
import logging
import requests
import subprocess
import zipfile
from pathlib import Path
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from tqdm import tqdm

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cell
def download_file(directory: str, source_url: str, decompress: bool = False) -> None:
    """Download data from source_ulr inside directory.

    Parameters
    ----------
    directory: str, Path
        Custom directory where data will be downloaded.
    source_url: str
        URL where data is hosted.
    decompress: bool
        Wheter decompress downloaded file. Default False.
    """
    if isinstance(directory, str):
        directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)

    filename = source_url.split('/')[-1]
    filepath = Path(f'{directory}/{filename}')

    # Streaming, so we can iterate over the response.
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(source_url, stream=True, headers=headers)
    # Total size in bytes.
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024 #1 Kibibyte

    t = tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(filepath, 'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
            f.flush()
    t.close()

    if total_size != 0 and t.n != total_size:
        logger.error('ERROR, something went wrong downloading data')

    size = filepath.stat().st_size
    logger.info(f'Successfully downloaded {filename}, {size}, bytes.')

    if decompress:
        if '.zip' in filepath.suffix:
            logger.info('Decompressing zip file...')
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(directory)
        else:
            from patoolib import extract_archive
            extract_archive(filepath, outdir=directory)
        logger.info(f'Successfully decompressed {filepath}')

# Cell
@dataclass
class Info:
    """
    Info Dataclass of datasets.
    Args:
        groups (Tuple): Tuple of str groups
        class_groups (Tuple): Tuple of dataclasses.
    """
    groups: Tuple[str]
    class_groups: Tuple[dataclass]

    def get_group(self, group: str):
        """Gets dataclass of group."""
        if group not in self.groups:
            raise Exception(f'Unkown group {group}')

        return self.class_groups[self.groups.index(group)]

    def __getitem__(self, group: str):
        """Gets dataclass of group."""
        if group not in self.groups:
            raise Exception(f'Unkown group {group}')

        return self.class_groups[self.groups.index(group)]

    def __iter__(self):
        for group in self.groups:
            yield group, self.get_group(group)


# Cell
@dataclass
class TimeSeriesDataclass:
    """
    Args:
        S (pd.DataFrame): DataFrame of static features of shape
            (n_time_series, n_features).
        X (pd.DataFrame): DataFrame of exogenous variables of shape
            (sum n_periods_i for i=1..n_time_series, n_exogenous).
        Y (pd.DataFrame): DataFrame of target variable of shape
            (sum n_periods_i for i=1..n_time_series, 1).
        idx_categorical_static (list, optional): List of categorical indexes
            of S.
        group (str, optional): Group name if applies.
            Example: 'Yearly'
    """
    S: pd.DataFrame
    X: pd.DataFrame
    Y: pd.DataFrame
    idx_categorical_static: Optional[List] = None
    group: Union[str, List[str]] = None

# Cell
import pandas as pd
from pandas.tseries.holiday import (
    AbstractHolidayCalendar,
    Holiday,
    USMartinLutherKingJr,
    USPresidentsDay,
    USMemorialDay,
    USLaborDay,
    USColumbusDay,
    USThanksgivingDay,
    nearest_workday
)

US_FEDERAL_HOLIDAYS = {'new_year': Holiday("New Years Day", month=1, day=1, observance=nearest_workday),
                       'martin_luther_king': USMartinLutherKingJr,
                       'presidents': USPresidentsDay,
                       'memorial': USMemorialDay,
                       'independence': Holiday("July 4th", month=7, day=4, observance=nearest_workday),
                       'labor': USLaborDay,
                       'columbus': USColumbusDay,
                       'veterans': Holiday("Veterans Day", month=11, day=11, observance=nearest_workday),
                       'thanksgiving': USThanksgivingDay,
                       'christmas': Holiday("Christmas", month=12, day=25, observance=nearest_workday)}

def get_holiday_dates(holiday, dates):
    start_date = min(dates) + pd.DateOffset(days=-366)
    end_date = max(dates) + pd.DateOffset(days=366)
    holiday_calendar = AbstractHolidayCalendar(rules=[US_FEDERAL_HOLIDAYS[holiday]])
    holiday_dates = holiday_calendar.holidays(start=start_date, end=end_date)
    return np.array(holiday_dates)

def holiday_kernel(holiday, dates):
    # Get holidays around dates
    dates = pd.DatetimeIndex(dates)
    dates_np = np.array(dates).astype('datetime64[D]')
    holiday_dates = get_holiday_dates(holiday, dates)
    holiday_dates_np = np.array(pd.DatetimeIndex(holiday_dates)).astype('datetime64[D]')

    # Compute day distance to holiday
    nearest_holiday_idx = np.expand_dims(dates_np, axis=1) - np.expand_dims(holiday_dates_np, axis=0)
    nearest_holiday_idx = np.argmin(np.abs(nearest_holiday_idx), axis=1)
    nearest_holiday = pd.DatetimeIndex([holiday_dates[idx] for idx in nearest_holiday_idx])
    holiday_diff = (dates - nearest_holiday).days.values
    return holiday_diff

def create_calendar_variables(X_df: pd.DataFrame):
    X_df['day_of_year'] = X_df.ds.dt.dayofyear
    X_df['day_of_week'] = X_df.ds.dt.dayofweek
    X_df['hour'] = X_df.ds.dt.hour
    return X_df

def create_us_holiday_distance_variables(X_df: pd.DataFrame):
    dates = X_df.ds.dt.date
    for holiday in US_FEDERAL_HOLIDAYS.keys():
        X_df[f'holiday_dist_{holiday}'] = holiday_kernel(holiday=holiday,
                                                         dates=dates)
    return X_df