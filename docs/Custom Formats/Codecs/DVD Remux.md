```json
{
  "name": "DVD REMUX ",
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
      "negate": false,
      "required": true,
      "fields": {
        "value": 5
      }
    }
  ]
}
```

