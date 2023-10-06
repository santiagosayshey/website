```json
{
  "name": "ATMOS",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bATMOS(\\b|\\d)"
      }
    }
  ]
}
```

- Missing

```json
{
  "name": "ATMOS (Missing)",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "2160p",
      "implementation": "ResolutionSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 2160
      }
    },
    {
      "name": "TrueHD",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD[ .-]?7\\.1"
      }
    },
    {
      "name": "Atmos",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bATMOS(\\b|\\d)"
      }
    }
  ]
}
```

