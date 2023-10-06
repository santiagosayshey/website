```json
{
  "name": "TBB SD",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "TBB",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])TBB\\b"
      }
    }
  ]
}
```
