```json
{
  "name": "Netflix",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Netflix",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(nf|netflix)\\b"
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