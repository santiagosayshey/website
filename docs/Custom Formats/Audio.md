## Atmos

```json
{
  "name": "ATMOS",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bATMOS(\\b|\\d)"
      }
    }
  ]
}
```

- Missing

```json
{
  "name": "ATMOS (Missing)",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
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
      "name": "TrueHD",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD[ .-]?7\\.1"
      }
    },
    {
      "name": "Atmos",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bATMOS(\\b|\\d)"
      }
    }
  ]
}
```



## DD+

```json
{
  "name": "DD+",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Dolby Digital Plus",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bDD[P+](?!A)|\\b(e[-_. ]?ac3)\\b"
      }
    },
    {
      "name": "TrueHD",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD"
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
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    }
  ]
}
```

## DD

```json
{
  "name": "DD",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Basic Dolby Digital",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bDD[^a-z+]|(?<!e)(a(c3|ac))"
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
      "name": "Not TrueHD/ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD|\\bATMOS(\\b|\\d)"
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
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    }
  ]
}
```



## DTS-HD MA

```json
{
  "name": "DTS-HD MA",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "DTS-HD MA",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?(ma|hd([-_. ]?ma)?|xll))\\b"
      }
    },
    {
      "name": "Not TrueHD/ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD|\\bATMOS(\\b|\\d)"
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
      "name": "Not Basic Dolby Digital ",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bDD[^a-z+]|(?<!e)ac3"
      }
    },
    {
      "name": "Not DTS X",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?x)\\b(?!\\d)"
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
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    },
    {
      "name": "Not DTS-HD HRA/ES",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "dts[-. ]?(es|(hd[. ]?)?(hr|hi))"
      }
    }
  ]
}
```



## DTS-X

- HDBits labels DTS-X as DTS-HD MA 7.1 sometimes

```json
{
  "name": "DTS-X",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "DTS X",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?x)\\b(?!\\d)"
      }
    },
    {
      "name": "Not Basic DTS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "DTS[ .]?[1-9]"
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
      "name": "Not TrueHD/ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD|\\bATMOS(\\b|\\d)"
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
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    }
  ]
}
```

## DTS

```json
{
  "name": "DTS",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "Basic DTS",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bDTS(\\b|\\d)"
      }
    },
    {
      "name": "Not DTS-HD",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?(ma|hd([-_. ]?ma)?|xll))\\b"
      }
    },
    {
      "name": "Not DTS-HD HRA/ES",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "dts[-. ]?(es|(hd[. ]?)?(hr|hi))"
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
      "name": "Not TrueHD/ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD|\\bATMOS(\\b|\\d)"
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
    },
    {
      "name": "Not DTS X",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(dts[-_. ]?x)\\b(?!\\d)"
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
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    }
  ]
}
```

## FLAC

```json
{
  "name": "FLAC",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "FLAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\bFLAC(\\b|\\d)"
      }
    },
    {
      "name": "Not PCM",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(l?)PCM(\\b|\\d)"
      }
    },
    {
      "name": "Not AAC",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bAAC(\\b|\\d)"
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
      "name": "Not TrueHD/ATMOS",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "True[ .-]?HD|\\bATMOS(\\b|\\d)"
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
    },
    {
      "name": "Not Dolby Digital Plus ",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bDD[P+]|\\b(e[-_. ]?ac3)\\b"
      }
    }
  ]
}
```

## TrueHD

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



