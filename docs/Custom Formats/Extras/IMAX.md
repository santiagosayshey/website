```json
{
  "name": "IMAX",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "IMAX",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": "\\bIMAX\\b"
      }
    },
    {
      "name": "IMAX Enhanced",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": "^(?=.*(DSNP|CORE(?=[ ._-]web[ ._-]?(dl|rip)\\b)|\\bBC(?=[ ._-]web[ ._-]?(dl|rip)\\b)|IMAX[- .]Enhanced)\\b)(?=.*\\b(IMAX|IMAX[- .]Enhanced)\\b).*"
      }
    }
  ]
}
```