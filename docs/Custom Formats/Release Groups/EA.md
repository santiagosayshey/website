```json
{
  "name": "EA",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "EA",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])EA\\b"
      }
    }
  ]
}
```
