```json
{
  "name": "DVD",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "DVD",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": 5
      }
    },
    {
      "name": "DVD",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "DVD"
      }
    }
  ]
}
```