```json
{
  "name": "playHD",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "playHD",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])playHD\\b"
      }
    }
  ]
}
```
