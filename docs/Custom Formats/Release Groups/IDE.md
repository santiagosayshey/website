```json
{
  "name": "IDE",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "IDE",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])IDE\\b"
      }
    }
  ]
}
```
