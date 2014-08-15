django-timedeltatemplatefilter
=====================

That is: timedelta template filter for Django :)

Format timedelta values nicely in your templates.

## What

New filter named "timedelta"

## How

A timedelta value: 4:03:21 `{{ dt }}`

A timedelta value with django-timedeltatemplatefilter_demo filter:
 * 04:03:21 `{{ dt|timedelta:"{hours2}:{minutes2}:{seconds2}" }}`
 * 04:03 `{{ dt|timedelta:{hours2}:{minutes2}" }}`
 * 4:3 `{{ dt|timedelta:{hours}:{minutes}" }}`

## Moar

Another timedelta value: 2620 days, 4:03:21 `{{ dt2 }}`

A timedelta value with django-timedeltatemplatefilter_demo filter:
 * 2620 days, 04:03:21 `{{ dt2|timedelta:"{days_total} days, {hours2}:{minutes2}:{seconds2}" }}`
 * 7 years, 65 days, 4 hours `{{ dt2|timedelta:{years} years, {days} days, {hours} hours" }}`
 * 62884 hours `{{ dt2|timedelta:{hours_total} hours" }}`

## Details

### Supported units

 * seconds
 * minutes
 * hours
 * days
 * years

### Available values

 * `{seconds}` - number of seconds until full minute
 * `{seconds_total}` - total number of seconds
 * `{minutes}` - number of minutes until full hour
 * `{minutes_total}` - total number of minutes, rounded down
 * `{hours}` - number of hours until full day
 * `{hours_total}` - total number of hours, rounded down
 * `{days}` - number of days until full year*
 * `{days_total}` - total number of days, rounded down
 * `{years}` - number of years*
 * `{years_total}` - alias for {years}
 
\* Leap years are not taken into account, 1 year = 365 days


## Todo & Ideas

 * add a template tag that provides a nice python object in template context, so that we can use it like `{{ dt.hours }}:{{ dt.minutes }}` etc.
