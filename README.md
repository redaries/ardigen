### install

```
$ virtualenv -p $(which python3) venv
$ source venv/bin/activate
$ pip install git+git://github.com/redaries/ardigen.git#egg=ardigen
```

download data

```
$ mkdir data
$ wget -O data/currency.csv https://raw.githubusercontent.com/redaries/ardigen/master/data/currency.csv
$ wget -O data/data.csv https://raw.githubusercontent.com/redaries/ardigen/master/data/data.csv
$ wget -O data/matching.csv https://raw.githubusercontent.com/redaries/ardigen/master/data/matching.csv
```

### usage

```
$ fizzbuzz -n 1 -m 100
```

or

```
$ valuation
```
