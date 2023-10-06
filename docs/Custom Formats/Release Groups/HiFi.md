```json
{
  "name": "HiFi",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "HiFi",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])HiFi\\b"
      }
    }
  ]
}
```
