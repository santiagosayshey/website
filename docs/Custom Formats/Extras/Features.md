```json
{
  "name": "Extras",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Extras",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?i)(\\b|\\.)(extra[s]?|special feature[s]?)\\b"
      }
    }
  ]
}
```