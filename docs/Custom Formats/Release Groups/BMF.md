```json
{
  "name": "BMF",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "BMF",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])BMF\\b"
      }
    }
  ]
}
```
