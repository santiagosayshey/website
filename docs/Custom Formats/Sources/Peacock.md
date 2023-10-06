```json
{
  "name": "Peacock TV",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Peacock TV",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(pcok|peacock)\\b"
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
