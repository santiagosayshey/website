```json
{
  "name": "Amazon Prime",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Amazon",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(amzn|amazon)\\b"
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
