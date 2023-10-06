```json
{
  "name": "Paramount+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Paramount+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(pmtp|Paramount Plus)\\b"
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

