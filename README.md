django-timedeltatemplatefilter
=====================

That is: **timedelta template filter** for Django :)

Format timedelta values nicely in your templates.

[![Build Status](https://api.travis-ci.org/frnhr/django_timedeltatemplatefilter.png)](https://travis-ci.org/frnhr/django_timedeltatemplatefilter)

v0.1.2


## What

New template filter named "timedelta"

## How

A timedelta value: `4:03:21` rendered using: `{{ dt }}`

A timedelta value with django-timedeltatemplatefilter filter:
 * `04:03:21`, rendered using:      
   `{{ dt|timedelta:"{hours2}:{minutes2}:{seconds2}" }}`
 * `04:03`, rendered using:  
   `{{ dt|timedelta:"{hours2}:{minutes2}" }}`
 * `4:3`, rendered using:  
   `{{ dt|timedelta:"{hours}:{minutes}" }}`

#### Moar!

Another timedelta value: `2620 days, 4:03:21`, rendered using: `{{ dt2 }}`

A timedelta value with django-timedeltatemplatefilter filter:
 * `2620 days, 04:03:21`, rendered using:  
   `{{ dt2|timedelta:"{days_total} days, {hours2}:{minutes2}:{seconds2}" }}`
 * `7 years, 65 days, 4 hours`, rendered using:  
   `{{ dt2|timedelta:"{years} years, {days} days, {hours} hours" }}`
 * `62884 hours`, rendered using:  
   `{{ dt2|timedelta:"{hours_total} hours" }}`

## Details

### Installation & usage

##### 1) Install the packet
    pip install django_timedeltatemplatefilter

You are hereby granted the right to do a copy and paste :)

Or you could just take the `timedeltatemplatefilter` directory and dump it next to your other apps, if you'd like.... for some reason... yeah.

##### 2) add to INSTALLED_APPS

Pretty much anywhere in your INSTALLED_APPS...

    INSTALLED_APPS = (
        # ... stuff ...
        'timedeltatemplatefilter',
        # ... stuff ---
    )

##### 3) Load in your template

In any template that you with to use this filter in, add:

    {% load timedelta_filter %}

to the top, but after `{% extends ... %}`.

##### 4) Use it

See the example at the top of this file.


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
 * `{dec_minutes}` - minutes until full hour in decimal
 * `{minutes_total}` - total number of minutes, rounded down
 * `{hours}` - number of hours until full day
 * `{hours_total}` - total number of hours, rounded down
 * `{days}` - number of days until full year*
 * `{days_total}` - total number of days, rounded down
 * `{years}` - number of years*
 * `{years_total}` - alias for {years}
 
\* Leap years are not taken into account, 1 year = 365 days


### Additional values

A few values are available in 2-digit form. Means that one-digit values are going to be padded with a `0` in front. These are:
 * `{seconds2}`
 * `{minutes2}`
 * `{dec_minutes2}`
 * `{hours2}`


### What's that `{stuff}` thing?

See python's [string format function][1].


## Todo & Ideas

 * add a template tag that provides a nice python object in template context, so that we can use it like `{{ dt.hours }}:{{ dt.minutes }}` etc.
 
[1]: https://docs.python.org/2/library/string.html#format-string-syntax
