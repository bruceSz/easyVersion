

#from oslo.config import cfg
from ev import cfg
from oslo.db import options
from ev import paths
from ev import version


CONF = cfg.CONF
_DEFAULT_SQL_CONNECTION = 'sqlite:///' + paths.default_path('ev.sqlite')  

def parse_args(argv,default_config_files=None):
    options.set_defaults(CONF,connection=_DEFAULT_SQL_CONNECTION,
                        sqlite_db='ev.sqlite')
    CONF(argv[1:],
        project='ev',
        version=version.version_string(),
        default_config_files=default_config_files)
