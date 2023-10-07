## Criterion



## Features

```json
{
  "name": "Extras",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Extras",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?i)(\\b|\\.)(extra[s]?|special feature[s]?)\\b"
      }
    }
  ]
}
```

## IMAX

```json
{
  "name": "IMAX",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "IMAX",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": "\\bIMAX\\b"
      }
    },
    {
      "name": "IMAX Enhanced",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": "^(?=.*(DSNP|CORE(?=[ ._-]web[ ._-]?(dl|rip)\\b)|\\bBC(?=[ ._-]web[ ._-]?(dl|rip)\\b)|IMAX[- .]Enhanced)\\b)(?=.*\\b(IMAX|IMAX[- .]Enhanced)\\b).*"
      }
    }
  ]
}
```

## SE



