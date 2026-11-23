---
name: weather-lookup
description: Get the current weather and a 3-day forecast for a city.
---


# Weather lookup

Uses the free Open-Meteo API. No key is needed.

1. Geocode the city: `https://geocoding-api.open-meteo.com/v1/search?name=<city>&count=1`
2. Fetch the forecast: `https://api.open-meteo.com/v1/forecast?latitude=<lat>&longitude=<lon>&daily=temperature_2m_max,temperature_2m_min&forecast_days=3`

Report the current temperature and the three daily highs and lows.
