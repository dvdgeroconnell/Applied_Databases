# Applied_Databases
Final Project for the Applied Databases module

| Topic | Details |
|---------|-------------|
| **Module:**  | 8637 - Applied Databases  |
| **Lecturer:**  | Gerard Harrison  | 
| **Course:**  | Diploma in Science in Computing (Data Analytics)  |
| **Year/Semester:**  | Year 1 / Semester 1  |
| **Student Name:**  | David O'Connell  |
| **Student ID:**  | G00438912  |
| **Student Email:**  | G00438912@atu.ie  |  

## How to Use
1. Fill out *dbconfig_template* with the local access credentials and remname it to *dbconfig.py*.  
**Note** - this does not have to be done for the final project assessment, as I have provided a copy of *dbconfig.py* which should work unless the user is using different credentials to those  used through the semester.
  
2. Run *python appdb_main.py**.


## GitHub Repository   
The GitHub repository contains the files associated with the Applied Databases final project.  
  
This is the link [AppliedDatabases GitHub repository](https://github.com/dvdgeroconnell/Applied_Databases.git).  
  
It does not contain the *db_config.py* file, which has username and password information.
It instead contains a template, *db_config_template.py*, which should be filled out with the relevant information by the end user.

## Assumptions and Interpretations

For the successful use cases in the Project Specification, the screenshots show the menu following the printing out of the results, without presenting a "Press Enter to continue" prompt.  
  
Therefore, bearing in mind that we had to have the *exact* answer for the database query results, I am taking the same approach with the Python program and implementing the Specification and screenshots as exactly as possible.  
  
One other use case is the response to a request to twin with a city which is already twinned with Dublin. The screenshot in the Project Specification is "Dublin has now been twinned with XXXX" and this is the response that was implemented.

### 4.4.7.1 
In Part 2 of this section, a 'valid' city could be interpreted in 2 ways:  
  
a) Valid meaning that it is in neo4j.  
b) Valid meaning that it may not be in neo4j but is in mysql.  
  
The option implemented is a). There is no point in adding the city to neo4j if it cannot be twinned with Dublin, since that would be the reason for adding it. So, if the city is not in neo4j, the user will be returned to the main menu.

## Innovations
Just a couple of things to mention here - and these aren't really innovations, just good coding practise.
1. Separate out the credentials into a separate config file, which is included in the .gitignore file so it is not uploaded to GitHub. This was covered in the Web Services & Applications module.
2. On exiting the program I had occasionally been seeing the following message:   
*Failed to write data to connection IPv4Address(('localhost', 7687)) (ResolvedIPv4Address(('127.0.0.1', 7687)))*
I thought this may be because the connection was still open, so I changed the creation of the driver to the following, which worked.  
*with gdb.driver(uri, auth=(user,password), max_connection_lifetime=1000) as driver:*

## Deprecated Functions
The neo4j driver is outdated and functions have since been deprecated, specifically *read_transaction* and *write_transaction*. These were however retained in this project. They still work with the current version of the driver (5.2.0) but will be removed in version 6. They were tested on the VM with both neo4j driver versions 5.2.0 and the version used in the lectures, 4.4.0.  
The following warning was seen when using those functions with driver version 5.2.0.
    
  neo4jtest.py:37: DeprecationWarning: read_transaction has been renamed to execute_read
    
From [neo4j docs (Python Driver Manual 5)](https://neo4j.com/docs/python-manual/current/transactions/).  
The methods .execute_read() and .execute_write() have replaced .read_transaction() and .write_transaction(), which are deprecated in version 5.x and will be removed in version 6.0.

## Packages installed

### Key Packages
- pymysql-1.1.0  
- neo4j-5.20.0 and neo4j-4.4.dev0 - tested with both locally and on the VM  
- Visual Studio Code version 1.88.0 was used during development  
- The Python 3.11.7 kernel was used to run the code  

### Output from *pip install* (Local Environment)
Package                       Version
----------------------------- ---------------
aiobotocore                   2.7.0  
aiohttp                       3.9.0  
aioitertools                  0.7.1  
aiosignal                     1.2.0  
alabaster                     0.7.12  
anaconda-anon-usage           0.4.2  
anaconda-catalogs             0.2.0  
anaconda-client               1.12.1  
anaconda-cloud-auth           0.1.4  
anaconda-navigator            2.5.0  
anaconda-project              0.11.1  
anyio                         3.5.0  
appdirs                       1.4.4  
archspec                      0.2.1  
argon2-cffi                   21.3.0  
argon2-cffi-bindings          21.2.0  
arrow                         1.2.3  
astroid                       2.14.2  
astropy                       5.3.4  
asttokens                     2.0.5  
async-lru                     2.0.4  
atomicwrites                  1.4.0  
attrs                         23.1.0  
Automat                       20.2.0  
autopep8                      1.6.0  
Babel                         2.11.0  
backports.functools-lru-cache 1.6.4  
backports.tempfile            1.0  
backports.weakref             1.0.post1  
bcrypt                        3.2.0  
beautifulsoup4                4.12.2  
binaryornot                   0.4.4  
black                         23.11.0  
bleach                        4.1.0  
bokeh                         3.3.0  
boltons                       23.0.0  
boto3                         1.28.64  
botocore                      1.31.64  
Bottleneck                    1.3.5  
Brotli                        1.0.9  
certifi                       2023.11.17  
cffi                          1.16.0  
chardet                       4.0.0  
charset-normalizer            2.0.4  
click                         8.1.7  
cloudpickle                   2.2.1  
clyent                        1.2.2  
colorama                      0.4.6  
colorcet                      3.0.1  
comm                          0.1.2  
conda                         23.11.0  
conda-build                   3.28.4  
conda-content-trust           0.2.0  
conda_index                   0.3.0  
conda-libmamba-solver         23.12.0  
conda-pack                    0.6.0  
conda-package-handling        2.2.0  
conda_package_streaming       0.9.0  
conda-repo-cli                1.0.75  
conda-token                   0.4.0  
conda-verify                  3.4.2  
constantly                    23.10.4  
contourpy                     1.2.0  
cookiecutter                  2.5.0  
cryptography                  41.0.7  
cssselect                     1.1.0  
cycler                        0.11.0  
cytoolz                       0.12.2  
daal4py                       2023.1.1  
dask                          2023.11.0  
datashader                    0.16.0  
debugpy                       1.6.7  
decorator                     5.1.1  
defusedxml                    0.7.1  
diff-match-patch              20200713  
dill                          0.3.7  
distributed                   2023.11.0  
distro                        1.8.0  
docstring-to-markdown         0.11  
docutils                      0.18.1  
entrypoints                   0.4  
et-xmlfile                    1.1.0  
executing                     0.8.3  
fastjsonschema                2.16.2  
filelock                      3.13.1  
flake8                        6.0.0  
Flask                         2.2.5  
fonttools                     4.25.0  
frozenlist                    1.4.0  
fsspec                        2023.10.0  
future                        0.18.3  
gensim                        4.3.0  
gmpy2                         2.1.2  
greenlet                      3.0.1  
h5py                          3.9.0  
HeapDict                      1.0.1  
holoviews                     1.18.1  
hvplot                        0.9.1  
hyperlink                     21.0.0  
idna                          3.4  
imagecodecs                   2023.1.23  
imageio                       2.31.4  
imagesize                     1.4.1  
imbalanced-learn              0.11.0  
importlib-metadata            7.0.1  
incremental                   21.3.0  
inflection                    0.5.1  
iniconfig                     1.1.1  
intake                        0.6.8  
intervaltree                  3.1.0  
ipykernel                     6.25.0  
ipython                       8.20.0  
ipython-genutils              0.2.0  
ipywidgets                    8.0.4  
isort                         5.9.3  
itemadapter                   0.3.0  
itemloaders                   1.0.4  
itsdangerous                  2.0.1  
jaraco.classes                3.2.1  
jedi                          0.18.1  
jellyfish                     1.0.1  
Jinja2                        3.1.2  
jmespath                      1.0.1  
joblib                        1.2.0  
json5                         0.9.6  
jsonpatch                     1.32  
jsonpointer                   2.1  
jsonschema                    4.19.2  
jsonschema-specifications     2023.7.1  
jupyter                       1.0.0  
jupyter_client                8.6.0  
jupyter-console               6.6.3  
jupyter_core                  5.5.0  
jupyter-events                0.8.0  
jupyter-lsp                   2.2.0  
jupyter_server                2.10.0  
jupyter_server_terminals      0.4.4  
jupyterlab                    4.0.8  
jupyterlab-pygments           0.1.2  
jupyterlab_server             2.25.1  
jupyterlab-widgets            3.0.9  
kaleido                       0.2.1  
keyring                       23.13.1  
kiwisolver                    1.4.4  
lazy_loader                   0.3  
lazy-object-proxy             1.6.0  
libarchive-c                  2.9  
libmambapy                    1.5.6  
linkify-it-py                 2.0.0  
llvmlite                      0.41.0  
lmdb                          1.4.1  
locket                        1.0.0  
lxml                          4.9.3  
lz4                           4.3.2  
Markdown                      3.4.1  
markdown-it-py                2.2.0  
MarkupSafe                    2.1.3  
matplotlib                    3.8.0  
matplotlib-inline             0.1.6  
mccabe                        0.7.0  
mdit-py-plugins               0.3.0  
mdurl                         0.1.0  
menuinst                      1.4.19  
mistune                       2.0.4  
mkl-fft                       1.3.8  
mkl-random                    1.2.4  
mkl-service                   2.4.0  
more-itertools                10.1.0  
mpmath                        1.3.0  
msgpack                       1.0.3  
multidict                     6.0.4  
multipledispatch              0.6.0  
munkres                       1.1.4  
mypy-extensions               1.0.0  
navigator-updater             0.4.0  
nbclient                      0.8.0  
nbconvert                     7.10.0  
nbformat                      5.9.2  
nest-asyncio                  1.5.6  
networkx                      3.1  
nltk                          3.8.1  
notebook                      7.0.6  
notebook_shim                 0.2.3  
numba                         0.58.1  
numexpr                       2.8.7  
numpy                         1.26.3  
numpydoc                      1.5.0  
openpyxl                      3.0.10  
overrides                     7.4.0  
packaging                     23.1  
pandas                        2.1.4  
pandocfilters                 1.5.0  
panel                         1.3.1  
param                         2.0.1  
paramiko                      2.8.1  
parsel                        1.6.0  
parso                         0.8.3  
partd                         1.4.1  
pathlib                       1.0.1  
pathspec                      0.10.3  
patsy                         0.5.3  
pep8                          1.7.1  
pexpect                       4.8.0  
pickleshare                   0.7.5  
Pillow                        10.0.1  
pip                           23.2.1  
pkce                          1.0.3  
pkginfo                       1.9.6  
platformdirs                  3.10.0  
plotly                        5.9.0  
pluggy                        1.0.0  
ply                           3.11  
prometheus-client             0.14.1  
prompt-toolkit                3.0.43  
Protego                       0.1.16  
psutil                        5.9.0  
ptyprocess                    0.7.0  
pure-eval                     0.2.2  
py-cpuinfo                    9.0.0  
pyarrow                       11.0.0  
pyasn1                        0.4.8  
pyasn1-modules                0.2.8  
pycodestyle                   2.10.0  
pycosat                       0.6.6  
pycparser                     2.21  
pyct                          0.5.0  
pycurl                        7.45.2  
pydantic                      1.10.12  
PyDispatcher                  2.0.5  
pydocstyle                    6.3.0  
pyerfa                        2.0.0  
pyflakes                      3.0.1  
Pygments                      2.15.1  
PyJWT                         2.4.0  
pylint                        2.16.2  
pylint-venv                   2.3.0  
pyls-spyder                   0.4.0  
PyNaCl                        1.5.0  
pyodbc                        5.0.1  
pyOpenSSL                     23.2.0  
pyparsing                     3.0.9  
PyQt5                         5.15.10  
PyQt5-sip                     12.13.0  
PyQtWebEngine                 5.15.6  
PySocks                       1.7.1  
pytest                        7.4.0  
python-dateutil               2.8.2  
python-dotenv                 0.21.0  
python-json-logger            2.0.7  
python-lsp-black              1.2.1  
python-lsp-jsonrpc            1.0.0  
python-lsp-server             1.7.2  
python-slugify                5.0.2  
python-snappy                 0.6.1  
pytoolconfig                  1.2.6  
pytz                          2023.3.post1  
pyviz_comms                   3.0.0  
pywavelets                    1.5.0  
pywin32                       305.1  
pywin32-ctypes                0.2.0  
pywinpty                      2.0.10  
PyYAML                        6.0.1  
pyzmq                         25.1.2  
QDarkStyle                    3.0.2  
qstylizer                     0.2.2  
QtAwesome                     1.2.2  
qtconsole                     5.4.2  
QtPy                          2.4.1  
queuelib                      1.6.2  
referencing                   0.30.2  
regex                         2023.10.3  
requests                      2.31.0  
requests-file                 1.5.1  
requests-toolbelt             1.0.0  
rfc3339-validator             0.1.4  
rfc3986-validator             0.1.1  
rich                          13.3.5  
rope                          1.7.0  
rpds-py                       0.10.6  
Rtree                         1.0.1  
ruamel.yaml                   0.17.21  
ruamel-yaml-conda             0.17.21  
s3fs                          2023.10.0  
s3transfer                    0.7.0  
sacremoses                    0.0.43  
scikit-image                  0.20.0  
scikit-learn                  1.2.2  
scikit-learn-intelex          20230426.121932  
scipy                         1.11.4  
Scrapy                        2.8.0  
seaborn                       0.12.2  
semver                        2.13.0  
Send2Trash                    1.8.2  
service-identity              18.1.0  
setuptools                    68.0.0  
sip                           6.7.12  
six                           1.16.0  
smart-open                    5.2.1  
sniffio                       1.3.0  
snowballstemmer               2.2.0  
sortedcontainers              2.4.0  
soupsieve                     2.5  
Sphinx                        5.0.2  
sphinxcontrib-applehelp       1.0.2  
sphinxcontrib-devhelp         1.0.2  
sphinxcontrib-htmlhelp        2.0.0  
sphinxcontrib-jsmath          1.0.1  
sphinxcontrib-qthelp          1.0.3  
sphinxcontrib-serializinghtml 1.1.5  
spyder                        5.4.3  
spyder-kernels                2.4.4  
SQLAlchemy                    2.0.25  
stack-data                    0.2.0  
statsmodels                   0.14.0  
sympy                         1.12  
tables                        3.8.0  
tabulate                      0.9.0  
TBB                           0.2  
tblib                         1.7.0  
tenacity                      8.2.2  
terminado                     0.17.1  
text-unidecode                1.3  
textdistance                  4.2.1  
threadpoolctl                 2.2.0  
three-merge                   0.1.1  
tifffile                      2023.4.12  
tinycss2                      1.2.1  
tldextract                    3.2.0  
toml                          0.10.2  
tomlkit                       0.11.1  
toolz                         0.12.0  
tornado                       6.3.3  
tqdm                          4.65.0  
traitlets                     5.7.1  
transformers                  2.1.1  
truststore                    0.8.0  
Twisted                       22.10.0  
twisted-iocpsupport           1.0.2  
typing_extensions             4.9.0  
tzdata                        2023.3  
uc-micro-py                   1.0.1  
ujson                         5.4.0  
Unidecode                     1.2.0  
urllib3                       1.26.18  
w3lib                         1.21.0  
watchdog                      2.1.6  
wcwidth                       0.2.5  
webencodings                  0.5.1  
websocket-client              0.58.0  
Werkzeug                      2.2.3  
whatthepatch                  1.0.2  
wheel                         0.38.4  
widgetsnbextension            4.0.5  
win-inet-pton                 1.1.0  
wrapt                         1.14.1  
xarray                        2023.6.0  
xlwings                       0.29.1  
xyzservices                   2022.9.0  
yapf                          0.31.0  
yarl                          1.9.3  
zict                          3.0.0  
zipp                          3.17.0  
zope.interface                5.4.0  
zstandard                     0.19.0  
  
  ***** 
  #### End