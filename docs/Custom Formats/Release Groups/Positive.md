```json
{
  "name": "Positive",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Positive",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])Positive\\b"
      }
    }
  ]
}
```
