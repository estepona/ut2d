# ut2d
__ut2d__ (unix timestamp to datetime) is a tiny command-line utility to convert unitx timestamp into human readable datetime.

If a city is specified, it will scrap the city's time zone from the Web, and calculate the time in that city of given unitx timestamp.

If you deal with unix timestamp a lot or need a tiny utility to get the time of another city that native `date` command cannot provide, `ut2d` can make your life easier.

## Installation

__Python 3.5__ or above is needed in order to install the package.

`$ pip3 install ut2d`

## Examples

### get datetime (local & GMT)
```console
$ ut2d 1547671090
Unix Timestamp: 1547671090.0
Local: Wed, Jan 16, 2019 03:38PM
GMT  : Wed, Jan 16, 2019 08:38PM
```

### get current unix timestamp and datetime (local & GMT)
```console
$ ut2d now
Unix Timestamp: 1547671189.5133939
Local: Wed, Jan 16, 2019 03:39PM
GMT  : Wed, Jan 16, 2019 08:39PM
```

### get datetime (local & GMT) and time difference
```console
$ ut2d 1547671090 -d
Unix Timestamp: 1547671090.0
Local: Wed, Jan 16, 2019 03:38PM
GMT  : Wed, Jan 16, 2019 08:38PM
Given time is 11 mins, 5 secs ago
```

### get datetime (local & GMT & given city)
This is done by scraping the cities' timezone from search engines, and calculate the datetime of the given unix timestamp of the given city.

If searching "New York"... (I'm in Boston)
```console
$ ut2d 1547671090 -d -c "New York"
Unix Timestamp: 1547671090.0
Local: Wed, Jan 16, 2019 03:38PM
GMT  : Wed, Jan 16, 2019 08:38PM
Given time is 15 mins, 42 secs ago
😛  I am finding your city on popular search engines! Plz wait a sec...
😎  I suppose the given time in New York is: Wed, Jan 16, 2019 03:38PM. I have 88% confidence with this result from search engines!
```

If searching "san babara"...
```console
$ ut2d 1547671090 -d -c "san babara"
Unix Timestamp: 1547671090.0
Local: Wed, Jan 16, 2019 03:38PM
GMT  : Wed, Jan 16, 2019 08:38PM
Given time is 17 mins, 11 secs ago
😛  I am finding your city on popular search engines! Plz wait a sec...
😎  I suppose the given time in san babara is: Wed, Jan 16, 2019 12:38PM. I have 88% confidence with this result from search engines!
```

You can search anything here! But if it cannot find on the search engines it will not print out the time.

## License

This software is distributed under the [MIT license](https://raw.github.com/soimort/you-get/master/LICENSE.txt).

## Author

Written by [Binghuan Zhang](https://github.com/estepona)
