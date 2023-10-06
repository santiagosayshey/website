```json
{
  "name": "TrueHD",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "TrueHD",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD"
      }
    },
    {
      "name": "Not Dolby Digital Plus",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bDD[P+]|\\b(e[-_. ]?ac3)\\b"
      }
    },
    {
      "name": "Not DTS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bDTS(\\b|\\d)"
      }
    },
    {
      "name": "Not FLAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bFLAC(\\b|\\d)"
      }
    },
    {
      "name": "Not Basic Dolby Digital",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bDD[^a-z+]|(?<!e)ac3"
      }
    }
  ]
}
```

- Missing

```json
{
  "name": "TrueHD (Missing)",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "RlsGrp (Missing TrueHD)",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?<=^|[\\s.-])TRiToN|EPSiLON|NoGroup\\b"
      }
    },
    {
      "name": "2160p",
      "implementation": "ResolutionSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 2160
      }
    },
    {
      "name": "Remux",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "Remux"
      }
    },
    {
      "name": "DTS: Not DTS-HD",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?(ma|hd([-_. ]?ma)?|xll))\\b"
      }
    },
    {
      "name": "DTS: Not DTS X",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?x)\\b(?!\\d)"
      }
    },
    {
      "name": "TrueHD: Not TrueHD",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD"
      }
    },
    {
      "name": "FLAC: Not FLAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bFLAC(\\b|\\d)"
      }
    }
  ]
}
```

