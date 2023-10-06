```json
{
  "name": "Disney+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Disney+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(dsnp|dsny|disney|Disney\\+)\\b"
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