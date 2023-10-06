```json
{
  "name": "Hulu",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Hulu",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(hulu)\\b"
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