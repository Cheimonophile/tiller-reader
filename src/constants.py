import pathlib as pl

# paths
CWD = pl.Path(__file__).parent.parent
PROJECT_DIR = CWD.parent
TILLER_PATH = PROJECT_DIR / 'Tiller.xlsx'
DB_PATH = PROJECT_DIR / 'banking-data.sqlite'
TILLER_LOGS_DIR = PROJECT_DIR / 'tiller-logs'


