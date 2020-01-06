from darksky.api import DarkSky, DarkSkyAsync
from darksky.types import languages, units, weather


API_KEY = '96df4121f48572f1743ad4a782a0713e'

# Synchronous way
darksky = DarkSky(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`,
    timezone='UTC' # default None - will be set by DarkSky API automatically
)

# Asynchronous way
# NOTE! On Mac os you will have problem with ssl checking https://github.com/aio-libs/aiohttp/issues/2822
# So you need to create your own session with disabled ssl verify and pass it into the DarkSkyAsync
# session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False))
# darksky = DarkSkyAsync(API_KEY, client_session=session)

darksky = DarkSkyAsync(API_KEY)

latitude = 42.3601
longitude = -71.0589
forecast = await darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS], # default `[]`
    timezone='UTC' # default None - will be set by DarkSky API automatically
)

# Final wrapper identical for both ways
forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be found at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be found at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be found at darksky/forecast.py
forecast.daily # DailyForecast. Can be found at darksky/forecast.py
forecast.alerts # [Alert]. Can be found at darksky/forecast.py
