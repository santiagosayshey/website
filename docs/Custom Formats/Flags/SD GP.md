```json
{
  "name": "Golden Popcorn SD",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "SD Golden Popcorn",
      "implementation": "IndexerFlagSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 8
      }
    },
    {
      "name": "720p",
      "implementation": "ResolutionSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 720
      }
    },
    {
      "name": "1080p",
      "implementation": "ResolutionSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 1080
      }
    }
  ]
}
```

