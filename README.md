# ut2d
__ut2d__ (unix timestamp to datetime) is a tiny command-line utility to convert unix timestamp into human readable datetime.

If a city name is given, it will scrap the city's time zone from the Web, and calculate the time in that city of given unix timestamp.

If you work with unix timestamp a lot or need a tiny utility to get the time of another city that native `date` command cannot provide, `ut2d` can make your life a little bit easier.

## Installation

__Python 3.5__ or above is needed in order to install the package

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
This is done by scraping the city's timezone from search engines, and calculate the datetime of the given unix timestamp of the given city.

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

You can use `now` with the `-c` flag to get the local time of any city, and you can even use other languages. e.g. 北京 is Beijing, and Montreuil-Juigné is a city in France.
```console
ut2d now -c "北京"
Unix Timestamp: 1547673691.203567
Local: Wed, Jan 16, 2019 04:21PM
GMT  : Wed, Jan 16, 2019 09:21PM
😛  I am finding your city on popular search engines! Plz wait a sec...
😎  I suppose the given time in 北京 is: Thu, Jan 17, 2019 05:21AM. I have 88% confidence with this result from search engines!

$ ut2d now -c "Montreuil-Juigné"
Unix Timestamp: 1547673563.7226071
Local: Wed, Jan 16, 2019 04:19PM
GMT  : Wed, Jan 16, 2019 09:19PM
😛  I am finding your city on popular search engines! Plz wait a sec...
😎  I suppose the given time in Montreuil-Juigné is: Wed, Jan 16, 2019 10:19PM. I have 88% confidence with this result from search engines!
```

You can search anything here! But if it cannot find on the search engines it will not print out the time.

## License

This software is distributed under the [MIT license](https://raw.github.com/soimort/you-get/master/LICENSE.txt).

## Author

Written by [Binghuan Zhang](https://github.com/estepona)
