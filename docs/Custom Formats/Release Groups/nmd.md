```json
{
  "name": "nmd",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "nmd",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])nmd\\b"
      }
    }
  ]
}
```
