```json
{
  "name": "ROKU",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "ROKU",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(roku)\\b"
      }
    },
    {
      "name": "WEBRIP",
      "implementation": "SourceSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 8
      }
    }
  ]
}
```

