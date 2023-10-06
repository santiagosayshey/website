```json
{
  "name": "BV",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "BV",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])BV\\b"
      }
    }
  ]
}
```
