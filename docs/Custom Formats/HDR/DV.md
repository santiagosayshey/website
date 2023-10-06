```json
{
  "name": "Dolby Vision",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "DV",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(dv|dovi|dolby[ .]?vision)\\b"
      }
    },
    {
      "name": "Not DV HLG",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(DV[ .]HLG)\\b"
      }
    },
    {
      "name": "Not DV SDR",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(DV[ .]SDR)\\b"
      }
    }
  ]
}
```

