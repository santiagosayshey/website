## 480p

```json
{
  "name": "480p",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "360p",
      "implementation": "ResolutionSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": 360
      }
    },
    {
      "name": "480p",
      "implementation": "ResolutionSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": 480
      }
    }
  ]
}
```

## 720p

```json
{
  "name": "720p",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "720p",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?(720p)"
      }
    },
    {
      "name": "1080p: 1080p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?1080p"
      }
    },
    {
      "name": "2160p: 2160p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])2160p\\b"
      }
    },
    {
      "name": "480p: 480p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])480p|360p|576p|540p\\b"
      }
    }
  ]
}
```

## 1080p

```json
{
  "name": "1080p",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "1080p",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?1080p"
      }
    },
    {
      "name": "2160p: 2160p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])2160p\\b"
      }
    },
    {
      "name": "720p: 720p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?(720p)"
      }
    },
    {
      "name": "720p: 480p: 480p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])480p|360p|576p|540p\\b"
      }
    }
  ]
}
```

## 2160p

```json
{
  "name": "2160p",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "2160p",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.\\-(])(2160p|UHD)\\b"
      }
    },
    {
      "name": "1080p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?1080p"
      }
    },
    {
      "name": "720p: 720p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "[.\\- (\\[]?(720p)"
      }
    },
    {
      "name": "720p: 480p: 480p",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])480p|360p|576p|540p\\b"
      }
    }
  ]
}
```
