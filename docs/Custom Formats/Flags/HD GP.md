```json
{
  "name": "Golden Popcorn 1080p",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "1080p Golden Popcorn",
      "implementation": "IndexerFlagSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 8
      }
    },
    {
      "name": "1080p",
      "implementation": "ResolutionSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 1080
      }
    }
  ]
}
```

```json
{
  "name": "Golden Popcorn 720p",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "720p Golden Popcorn",
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
      "negate": false,
      "required": true,
      "fields": {
        "value": 720
      }
    }
  ]
}
```