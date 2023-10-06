```json
{
  "name": "Dolby Vision w/out Fallback",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Dolby Vision w/out Fallback",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "^(?!.*(HDR|HULU|REMUX))(?=.*\\b(DV|Dovi|Dolby[- .]?V(ision)?)\\b)"
      }
    }
  ]
}
```

