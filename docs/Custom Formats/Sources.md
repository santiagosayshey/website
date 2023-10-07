## Amazon Prime

```json
{
  "name": "Amazon Prime",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Amazon",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(amzn|amazon)\\b"
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


## Apple TV+

```json
{
  "name": "Apple TV+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Apple TV+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(atvp|aptv|Apple TV\\+)\\b"
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

## Blu-Ray

```json
{
  "name": "Blu-Ray",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Blu-Ray",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 9
      }
    }
  ]
}
```

## Disney+

```json
{
  "name": "Disney+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Disney+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(dsnp|dsny|disney|Disney\\+)\\b"
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

## DVD

```json
{
  "name": "DVD",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "DVD",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": false,
      "fields": {
        "value": 5
      }
    },
    {
      "name": "DVD",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "DVD"
      }
    }
  ]
}
```

## HBOMax

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

## Hulu

```json
{
  "name": "Hulu",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Hulu",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(hulu)\\b"
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

## iTunes

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


## Movies Anywhere

Best Possible WEB source
- Prefer over Amazon for true transparent, make equal for immutable
- 4K VODS often used for Transparent 1080p encodes in place of a traditional blu-ray

```json
{
  "name": "Movies Anywhere",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Movies Anywhere",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<!dts[ .-]?hd[ .-]?)ma\\b(?=.*\\bweb[ ._-]?(dl|rip)\\b)"
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



## Netflix

```json
{
  "name": "Netflix",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Netflix",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(nf|netflix)\\b"
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

## Paramount+

```json
{
  "name": "Paramount+",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Paramount+",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(pmtp|Paramount Plus)\\b"
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



## Peacock

```json
{
  "name": "Peacock TV",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Peacock TV",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(pcok|peacock)\\b"
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


## Roku

```json
{
  "name": "ROKU",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "ROKU",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(roku)\\b"
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



## WEBRIP

```json
{
  "name": "WEBRip",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "WEBRip",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 8
      }
    }
  ]
}
```



