```json
{
  "name": "Apple TV+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Apple TV+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(atvp|aptv|Apple TV\\+)\\b"
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