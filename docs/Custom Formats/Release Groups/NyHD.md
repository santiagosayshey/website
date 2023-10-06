```json
{
  "name": "NyHD",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "NyHD",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])NyHD\\b"
      }
    }
  ]
}
```
