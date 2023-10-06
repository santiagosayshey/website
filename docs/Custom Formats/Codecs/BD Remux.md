```json
{
  "name": "REMUX",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "REMUX",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "REMUX"
      }
    },
    {
      "name": "DVD",
      "implementation": "SourceSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 5
      }
    }
  ]
}
```

