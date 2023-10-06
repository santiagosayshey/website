```json
{
  "name": "EDPH",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "EDPH",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])EDPH\\b"
      }
    }
  ]
}
```
