<!-- Generator: Widdershins v4.0.1 -->

<h1 id=""> v</h1>

> Scroll down for code samples, example requests and responses. Select a language for code samples from the tabs above or the mobile navigation menu.

<h1 id="-liquids">liquids</h1>

## listLiquids

<a id="opIdlistLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /liquids/ \
  -H 'Accept: application/json'

```

`GET /liquids/`

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "name": "string",
    "description": "string",
    "density": 0
  }
]
```

<h3 id="listliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="listliquids-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Liquids](#schemaliquids)]|false|none|none|
|» id|integer|false|read-only|none|
|» name|string|true|none|none|
|» description|string|true|none|none|
|» density|number|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## createLiquids

<a id="opIdcreateLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /liquids/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /liquids/`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "density": 0
}
```

```yaml
name: string
description: string
density: 0

```

<h3 id="createliquids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Liquids](#schemaliquids)|false|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "density": 0
}
```

<h3 id="createliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Liquids](#schemaliquids)|

<aside class="success">
This operation does not require authentication
</aside>

## retrieveLiquids

<a id="opIdretrieveLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /liquids/{id}/ \
  -H 'Accept: application/json'

```

`GET /liquids/{id}/`

<h3 id="retrieveliquids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this liquids.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "density": 0
}
```

<h3 id="retrieveliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Liquids](#schemaliquids)|

<aside class="success">
This operation does not require authentication
</aside>

## updateLiquids

<a id="opIdupdateLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /liquids/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`PUT /liquids/{id}/`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "density": 0
}
```

```yaml
name: string
description: string
density: 0

```

<h3 id="updateliquids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this liquids.|
|body|body|[Liquids](#schemaliquids)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "density": 0
}
```

<h3 id="updateliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Liquids](#schemaliquids)|

<aside class="success">
This operation does not require authentication
</aside>

## partialUpdateLiquids

<a id="opIdpartialUpdateLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /liquids/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`PATCH /liquids/{id}/`

> Body parameter

```json
{
  "name": "string",
  "description": "string",
  "density": 0
}
```

```yaml
name: string
description: string
density: 0

```

<h3 id="partialupdateliquids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this liquids.|
|body|body|[Liquids](#schemaliquids)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "density": 0
}
```

<h3 id="partialupdateliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Liquids](#schemaliquids)|

<aside class="success">
This operation does not require authentication
</aside>

## destroyLiquids

<a id="opIddestroyLiquids"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /liquids/{id}/

```

`DELETE /liquids/{id}/`

<h3 id="destroyliquids-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this liquids.|

<h3 id="destroyliquids-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-zones">zones</h1>

## listZones

<a id="opIdlistZones"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /zones/ \
  -H 'Accept: application/json'

```

`GET /zones/`

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "name": "string",
    "latitude": 0,
    "longitude": 0
  }
]
```

<h3 id="listzones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="listzones-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Zones](#schemazones)]|false|none|none|
|» id|integer|false|read-only|none|
|» name|string|true|none|none|
|» latitude|number|true|none|none|
|» longitude|number|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## createZones

<a id="opIdcreateZones"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /zones/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /zones/`

> Body parameter

```json
{
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

```yaml
name: string
latitude: 0
longitude: 0

```

<h3 id="createzones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Zones](#schemazones)|false|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

<h3 id="createzones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Zones](#schemazones)|

<aside class="success">
This operation does not require authentication
</aside>

## retrieveZones

<a id="opIdretrieveZones"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /zones/{id}/ \
  -H 'Accept: application/json'

```

`GET /zones/{id}/`

<h3 id="retrievezones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this zones.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

<h3 id="retrievezones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Zones](#schemazones)|

<aside class="success">
This operation does not require authentication
</aside>

## updateZones

<a id="opIdupdateZones"></a>

> Code samples

```shell
# You can also use wget
curl -X PUT /zones/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`PUT /zones/{id}/`

> Body parameter

```json
{
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

```yaml
name: string
latitude: 0
longitude: 0

```

<h3 id="updatezones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this zones.|
|body|body|[Zones](#schemazones)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

<h3 id="updatezones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Zones](#schemazones)|

<aside class="success">
This operation does not require authentication
</aside>

## partialUpdateZones

<a id="opIdpartialUpdateZones"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /zones/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`PATCH /zones/{id}/`

> Body parameter

```json
{
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

```yaml
name: string
latitude: 0
longitude: 0

```

<h3 id="partialupdatezones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this zones.|
|body|body|[Zones](#schemazones)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "name": "string",
  "latitude": 0,
  "longitude": 0
}
```

<h3 id="partialupdatezones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Zones](#schemazones)|

<aside class="success">
This operation does not require authentication
</aside>

## destroyZones

<a id="opIddestroyZones"></a>

> Code samples

```shell
# You can also use wget
curl -X DELETE /zones/{id}/

```

`DELETE /zones/{id}/`

<h3 id="destroyzones-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this zones.|

<h3 id="destroyzones-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|204|[No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)|none|None|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-silos">silos</h1>

## listSilos

<a id="opIdlistSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /silos/ \
  -H 'Accept: application/json'

```

`GET /silos/`

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "height": 0,
    "diameter": 0,
    "zone": {
      "id": 0,
      "name": "string",
      "latitude": 0,
      "longitude": 0
    },
    "liquid": {
      "id": 0,
      "name": "string",
      "description": "string",
      "density": 0
    },
    "actions": [
      {
        "id": 0,
        "action": "string",
        "description": "string",
        "time": "2019-08-24T14:15:22Z"
      }
    ],
    "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
]
```

<h3 id="listsilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="listsilos-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Silos](#schemasilos)]|false|none|none|
|» id|integer|false|read-only|none|
|» height|number|true|none|none|
|» diameter|number|true|none|none|
|» zone|object|false|read-only|none|
|»» id|integer|false|read-only|none|
|»» name|string|true|none|none|
|»» latitude|number|true|none|none|
|»» longitude|number|true|none|none|
|» liquid|object|false|read-only|none|
|»» id|integer|false|read-only|none|
|»» name|string|true|none|none|
|»» description|string|true|none|none|
|»» density|number|true|none|none|
|» actions|[object]|false|read-only|none|
|»» id|integer|false|read-only|none|
|»» action|string|true|none|none|
|»» description|string|true|none|none|
|»» time|string(date-time)|true|none|none|
|» lastmeasurement|string|false|read-only|none|

<aside class="success">
This operation does not require authentication
</aside>

## createSilos

<a id="opIdcreateSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /silos/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /silos/`

> Body parameter

```json
{
  "height": 0,
  "diameter": 0
}
```

```yaml
height: 0
diameter: 0

```

<h3 id="createsilos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Silos](#schemasilos)|false|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "height": 0,
  "diameter": 0,
  "zone": {
    "id": 0,
    "name": "string",
    "latitude": 0,
    "longitude": 0
  },
  "liquid": {
    "id": 0,
    "name": "string",
    "description": "string",
    "density": 0
  },
  "actions": [
    {
      "id": 0,
      "action": "string",
      "description": "string",
      "time": "2019-08-24T14:15:22Z"
    }
  ],
  "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
}
```

<h3 id="createsilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Silos](#schemasilos)|

<aside class="success">
This operation does not require authentication
</aside>

## retrieveSilos

<a id="opIdretrieveSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /silos/{id}/ \
  -H 'Accept: application/json'

```

`GET /silos/{id}/`

<h3 id="retrievesilos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this silos.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "height": 0,
  "diameter": 0,
  "zone": {
    "id": 0,
    "name": "string",
    "latitude": 0,
    "longitude": 0
  },
  "liquid": {
    "id": 0,
    "name": "string",
    "description": "string",
    "density": 0
  },
  "actions": [
    {
      "id": 0,
      "action": "string",
      "description": "string",
      "time": "2019-08-24T14:15:22Z"
    }
  ],
  "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
}
```

<h3 id="retrievesilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Silos](#schemasilos)|

<aside class="success">
This operation does not require authentication
</aside>

## partialUpdateSilos

<a id="opIdpartialUpdateSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X PATCH /silos/{id}/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`PATCH /silos/{id}/`

> Body parameter

```json
{
  "height": 0,
  "diameter": 0
}
```

```yaml
height: 0
diameter: 0

```

<h3 id="partialupdatesilos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this silos.|
|body|body|[Silos](#schemasilos)|false|none|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "height": 0,
  "diameter": 0,
  "zone": {
    "id": 0,
    "name": "string",
    "latitude": 0,
    "longitude": 0
  },
  "liquid": {
    "id": 0,
    "name": "string",
    "description": "string",
    "density": 0
  },
  "actions": [
    {
      "id": 0,
      "action": "string",
      "description": "string",
      "time": "2019-08-24T14:15:22Z"
    }
  ],
  "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
}
```

<h3 id="partialupdatesilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Silos](#schemasilos)|

<aside class="success">
This operation does not require authentication
</aside>

## allMeasurementsSilos

<a id="opIdallMeasurementsSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /silos/{id}/all_measurements/ \
  -H 'Accept: application/json'

```

`GET /silos/{id}/all_measurements/`

<h3 id="allmeasurementssilos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this silos.|

> Example responses

> 200 Response

```json
{
  "measurements": [
      {
        "ext_humidity": 0.0,
        "ext_temp": 0.0,
        "int_humidity": 0.0,
        "int_pression": 0.0,
        "int_temp": 0.0,
        "ph": 0.0,
        "sensor_1": 0.0,
        "sensor_2": 0.0,
        "sensor_3": 0.0,
        "temp": 0.0,
        "time": "1668782400.238529",
        "level": 0.0,
        "level_percentage": 0.0,
        "volume": 0.0,
        "weight": 0.0
    }
  ]
}
```

<h3 id="allmeasurementssilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Silos](#schemasilos)|

<aside class="success">
This operation does not require authentication
</aside>

## lastMeasurementSilos

<a id="opIdlastMeasurementSilos"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /silos/{id}/last_measurement/ \
  -H 'Accept: application/json'

```

`GET /silos/{id}/last_measurement/`

<h3 id="lastmeasurementsilos-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this silos.|

> Example responses

> 200 Response

```json
{
  "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
}
```

<h3 id="lastmeasurementsilos-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Silos](#schemasilos)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-actions">actions</h1>

## listActions

<a id="opIdlistActions"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /actions/ \
  -H 'Accept: application/json'

```

`GET /actions/`

> Example responses

> 200 Response

```json
[
  {
    "id": 0,
    "action": "string",
    "description": "string",
    "time": "2019-08-24T14:15:22Z"
  }
]
```

<h3 id="listactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|Inline|

<h3 id="listactions-responseschema">Response Schema</h3>

Status Code **200**

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|*anonymous*|[[Actions](#schemaactions)]|false|none|none|
|» id|integer|false|read-only|none|
|» action|string|true|none|none|
|» description|string|true|none|none|
|» time|string(date-time)|true|none|none|

<aside class="success">
This operation does not require authentication
</aside>

## createActions

<a id="opIdcreateActions"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /actions/ \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /actions/`

> Body parameter

```json
{
  "action": "string",
  "description": "string",
  "time": "2019-08-24T14:15:22Z"
}
```

```yaml
action: string
description: string
time: 2019-08-24T14:15:22Z

```

<h3 id="createactions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Actions](#schemaactions)|false|none|

> Example responses

> 201 Response

```json
{
  "id": 0,
  "action": "string",
  "description": "string",
  "time": "2019-08-24T14:15:22Z"
}
```

<h3 id="createactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[Actions](#schemaactions)|

<aside class="success">
This operation does not require authentication
</aside>

## retrieveActions

<a id="opIdretrieveActions"></a>

> Code samples

```shell
# You can also use wget
curl -X GET /actions/{id}/ \
  -H 'Accept: application/json'

```

`GET /actions/{id}/`

<h3 id="retrieveactions-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|id|path|string|true|A unique integer value identifying this actions.|

> Example responses

> 200 Response

```json
{
  "id": 0,
  "action": "string",
  "description": "string",
  "time": "2019-08-24T14:15:22Z"
}
```

<h3 id="retrieveactions-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|none|[Actions](#schemaactions)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-auth">auth</h1>

## createAuthToken

<a id="opIdcreateAuthToken"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /auth/ \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Accept: application/json'

```

`POST /auth/`

> Body parameter

```json
{
  "username": "string",
  "password": "string"
}
```

```yaml
username: string
password: string

```

<h3 id="createauthtoken-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[AuthToken](#schemaauthtoken)|false|none|

> Example responses

> 201 Response

```json
{
  "token": "string"
}
```

<h3 id="createauthtoken-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|[AuthToken](#schemaauthtoken)|

<aside class="success">
This operation does not require authentication
</aside>

<h1 id="-emqx-webhook">emqx-webhook</h1>

## createEmqxWebhoox

<a id="opIdcreateEmqxWebhoox"></a>

> Code samples

```shell
# You can also use wget
curl -X POST /emqx_webhook \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json'

```

`POST /emqx_webhook`

> Body parameter

```json
null
```

```yaml
null

```

<h3 id="createemqxwebhoox-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|any|false|none|

> Example responses

> 201 Response

```json
null
```

<h3 id="createemqxwebhoox-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|201|[Created](https://tools.ietf.org/html/rfc7231#section-6.3.2)|none|Inline|

<h3 id="createemqxwebhoox-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

<h2 id="tocS_Liquids">Liquids</h2>
<!-- backwards compatibility -->
<a id="schemaliquids"></a>
<a id="schema_Liquids"></a>
<a id="tocSliquids"></a>
<a id="tocsliquids"></a>

```json
{
  "id": 0,
  "name": "string",
  "description": "string",
  "density": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|name|string|true|none|none|
|description|string|true|none|none|
|density|number|true|none|none|

<h2 id="tocS_Zones">Zones</h2>
<!-- backwards compatibility -->
<a id="schemazones"></a>
<a id="schema_Zones"></a>
<a id="tocSzones"></a>
<a id="tocszones"></a>

```json
{
  "id": 0,
  "name": "string",
  "latitude": 0,
  "longitude": 0
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|name|string|true|none|none|
|latitude|number|true|none|none|
|longitude|number|true|none|none|

<h2 id="tocS_Silos">Silos</h2>
<!-- backwards compatibility -->
<a id="schemasilos"></a>
<a id="schema_Silos"></a>
<a id="tocSsilos"></a>
<a id="tocssilos"></a>

```json
{
  "id": 0,
  "height": 0,
  "diameter": 0,
  "zone": {
    "id": 0,
    "name": "string",
    "latitude": 0,
    "longitude": 0
  },
  "liquid": {
    "id": 0,
    "name": "string",
    "description": "string",
    "density": 0
  },
  "actions": [
    {
      "id": 0,
      "action": "string",
      "description": "string",
      "time": "2019-08-24T14:15:22Z"
    }
  ],
  "lastmeasurement": {
    "ext_humidity": 0.0,
    "ext_temp": 0.0,
    "int_humidity": 0.0,
    "int_pression": 0.0,
    "int_temp": 0.0,
    "ph": 0.0,
    "sensor_1": 0.0,
    "sensor_2": 0.0,
    "sensor_3": 0.0,
    "temp": 0.0,
    "time": "1668782400.238529",
    "level": 0.0,
    "level_percentage": 0.0,
    "volume": 0.0,
    "weight": 0.0
  }
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|height|number|true|none|none|
|diameter|number|true|none|none|
|zone|object|false|read-only|none|
|» id|integer|false|read-only|none|
|» name|string|true|none|none|
|» latitude|number|true|none|none|
|» longitude|number|true|none|none|
|liquid|object|false|read-only|none|
|» id|integer|false|read-only|none|
|» name|string|true|none|none|
|» description|string|true|none|none|
|» density|number|true|none|none|
|actions|[object]|false|read-only|none|
|» id|integer|false|read-only|none|
|» action|string|true|none|none|
|» description|string|true|none|none|
|» time|string(date-time)|true|none|none|
|lastmeasurement|string|false|read-only|none|

<h2 id="tocS_Actions">Actions</h2>
<!-- backwards compatibility -->
<a id="schemaactions"></a>
<a id="schema_Actions"></a>
<a id="tocSactions"></a>
<a id="tocsactions"></a>

```json
{
  "id": 0,
  "action": "string",
  "description": "string",
  "time": "2019-08-24T14:15:22Z"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|id|integer|false|read-only|none|
|action|string|true|none|none|
|description|string|true|none|none|
|time|string(date-time)|true|none|none|

<h2 id="tocS_AuthToken">AuthToken</h2>
<!-- backwards compatibility -->
<a id="schemaauthtoken"></a>
<a id="schema_AuthToken"></a>
<a id="tocSauthtoken"></a>
<a id="tocsauthtoken"></a>

```json
{
  "username": "string",
  "password": "string",
  "token": "string"
}

```

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|write-only|none|
|password|string|true|write-only|none|
|token|string|false|read-only|none|

