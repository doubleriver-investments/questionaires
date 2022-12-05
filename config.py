"""This module contains the configurations needed to configure AIM.

These configurations represent needed info to manage the data transfer,
local storage, push back to Bloomberg and parsing of the data files.

"""
from dataclasses import dataclass
from enum import Enum
from typing import Literal

from pydantic import BaseSettings


class BrokerNames(Enum):
    """Enum representing supported broker names."""

    NT = "NorthernTrust"
    NTTest = "NorthernTrustTest"
    BB = "Bloomberg"
    BBPort = "Bloomberg_PORT"
    IB = "InteractiveBrokers"


class FTP_Type(Enum):
    """Enum representing how FTP should happen between broker and local files."""
    SFTP = "sftp"
    FTP = "ftp"


@dataclass(frozen=True)
class AccountInfo:
    """A dataclass to hold secrets of each account

    Attributes:

    """
    user = {}
    passwd = {}
    site = {}
    port = {}
    rdir = {}
    ldir = {}
    rfile = {}
    ftptype = {}

    user[BrokerNames.NT]: str = "BLOOM91S"
    passwd[BrokerNames.NT]: str = "Uk197#68#28xY"
    site[BrokerNames.NT]: str = "secure-B2BI.ntrs.com"
    port[BrokerNames.NT]: int = 4022
    rdir[BrokerNames.NT]: int = 'OUTBOUND'
    ldir[BrokerNames.NT]: int = 'NT'
    rfile[BrokerNames.NT]: int = '*'
    ftptype[BrokerNames.NT]: FTP_Type = FTP_Type.SFTP

    user[BrokerNames.BB]: str = "T1019L1"
    passwd[BrokerNames.BB]: str = "rH9CbL129C-5Ljcp"
    site[BrokerNames.BB]: str = "sftp.bloomberg.com"
    port[BrokerNames.BB]: int = 22
    rdir[BrokerNames.BB]: int = '.'
    ldir[BrokerNames.BB]: int = 'AIM'
    rfile[BrokerNames.BB]: int = 'f*1'
    ftptype[BrokerNames.BB]: FTP_Type = FTP_Type.SFTP
    # Uploaded here to 'results' dir.
    # results/f1019upload.1667275223.rpt.221101.1

    user[BrokerNames.BBPort]: str = "u1237053220"
    passwd[BrokerNames.BBPort]: str = "O0kb6-=%j3P4}qsV[Mh]"
    site[BrokerNames.BBPort]: str = "sftp.bloomberg.com"
    port[BrokerNames.BBPort]: int = 22
    rdir[BrokerNames.BBPort]: int = 'report'
    ldir[BrokerNames.BBPort]: int = 'NTPort'
    rfile[BrokerNames.BBPort]: int = '*xls'
    ftptype[BrokerNames.BBPort]: FTP_Type = FTP_Type.SFTP
    # Upload to data directory data/nt_port_cash.csv  data/nt_port_positions.csv

    # Password does not work ...
    user[BrokerNames.NTTest]: str = "BLOOM91T"
    passwd[BrokerNames.NTTest]: str = "Uk197#68#28xY"
    site[BrokerNames.NTTest]: str = "uat-b2bi.ntrs.com"
    port[BrokerNames.NTTest]: int = 4022
    rdir[BrokerNames.NTTest]: int = '.'
    rfile[BrokerNames.NTTest]: int = 'f*'
    ftptype[BrokerNames.NTTest]: FTP_Type = FTP_Type.SFTP

    # This only works with FTP in passive mode :(
    user[BrokerNames.IB]: str = "d0ublerivergs"
    passwd[BrokerNames.IB]: str = "ma8ahdbas"
    site[BrokerNames.IB]: str = "ftp2.interactivebrokers.com"
    port[BrokerNames.IB]: int = 22
    rdir[BrokerNames.IB]: int = 'outgoing'
    rfile[BrokerNames.IB]: int = 'f*'
    ftptype[BrokerNames.IB]: FTP_Type = FTP_Type.FTP


class Settings(BaseSettings):
    """The base settings for aim, determines directories, file names, etc.  This
    allows testing into temporary locations and live runs in the production
    areas.

    These settings include all the connection strings required
    to get data along with a few configuration settings such as logging.

    Any of these defaults can be overwritten by setting an environment variable with
    an equivalent name.

    """
    brokerdir = {}
    brokerdir[BrokerNames.IB]: str = "IB"
    brokerdir[BrokerNames.NTTest]: str = "NTT"
    brokerdir[BrokerNames.NT]: str = "NT"
    brokerdir[BrokerNames.BB]: str = "BB"
    brokerdir[BrokerNames.BBPort]: str = "BB_Port"

    AIM_DATA_DOWNLOAD_DIR: str = "raw"
    AIM_DATA_PROCESS_DIR: str = "data"
    AIM_DATA_UPLOAD_DIR: str = "upload"
    AIM_DATA_ROOT_DIR: str = "/data"

    AIM_LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] = "INFO"

    # Google cloud settings, pass to Falcon
    DEFAULT_PROJECT: str = "dr-bloomberg-aim"
    MODEL_BUCKET: str = "dr-dev-us-east1-aim"
    # Bucket needs to be initialized on the cloud
    MODEL_ARTIFACT_BUCKET: str = "dr-dev-us-east1-aim-artifacts"
    PREFECT_FLOWS_BUCKET: str = "dr-dev-us-east1-aim-flows"

    # The https://www.openfigi.com/api requires a key to increase number of calls at a time.
    FIGI_API_KEY = "85e6b624-d0dc-4a40-a5cc-b56cfcb2da67"
    FIGI_API_MAX_PAYLOAD = 100


settings = Settings()
