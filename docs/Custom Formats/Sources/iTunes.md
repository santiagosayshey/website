```json
{
  "name": "iTunes",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "iTunes",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(it|itunes)\\b(?=[ ._-]web[ ._-]?(dl|rip)\\b)"
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
    },
    {
      "name": "WEBDL",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 7
      }
    }
  ]
}
```

- Missing

```json
{
  "name": "iTunes (Missing)",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "WEBRIP",
      "implementation": "SourceSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 8
      }
    },
    {
      "name": "Amazon Prime: Amazon",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(amzn|amazon)\\b"
      }
    },
    {
      "name": "Movies Anywhere: Movies Anywhere",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?<!dts[ .-]?hd[ .-]?)ma\\b(?=.*\\bweb[ ._-]?(dl|rip)\\b)"
      }
    },
    {
      "name": "Apple TV+: Apple TV+",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(atvp|aptv|Apple TV\\+)\\b"
      }
    },
    {
      "name": "Disney+: Disney+",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dsnp|dsny|disney|Disney\\+)\\b"
      }
    },
    {
      "name": "HBO Max: HBO Max",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(hmax|hbom|hbo[ ._-]max)\\b(?=[ ._-]web[ ._-]?(dl|rip)\\b)"
      }
    },
    {
      "name": "Netflix: Netflix",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(nf|netflix)\\b"
      }
    },
    {
      "name": "Peacock TV: Peacock TV",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(pcok|peacock)\\b"
      }
    },
    {
      "name": "Paramount+: Paramount+",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(pmtp|Paramount Plus)\\b"
      }
    },
    {
      "name": "WEBDL",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 7
      }
    },
    {
      "name": "ROKU: ROKU",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(roku)\\b"
      }
    },
    {
      "name": "IPT ",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])EVO|CMRG\\b"
      }
    },
    {
      "name": "Hulu: Hulu",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(hulu)\\b"
      }
    },
    {
      "name": "iTunes",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(it|itunes)\\b(?=[ ._-]web[ ._-]?(dl|rip)\\b)"
      }
    }
  ]
}
```
