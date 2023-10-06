```json
{
  "name": "HBO Max",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "HBO Max",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(hmax|hbom|hbo[ ._-]max)\\b(?=[ ._-]web[ ._-]?(dl|rip)\\b)"
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