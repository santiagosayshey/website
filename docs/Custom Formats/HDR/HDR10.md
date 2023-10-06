```json
{
  "name": "HDR10",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "HDR10",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "HDR"
      }
    },
    {
      "name": "Not HDR10+",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bHDR10(\\+|P(lus)?\\b)"
      }
    },
    {
      "name": "Not HLG",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bHLG(\\b|\\d)"
      }
    },
    {
      "name": "Not PQ",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\b(PQ)\\b"
      }
    },
    {
      "name": "Not SDR",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bSDR(\\b|\\d)"
      }
    }
  ]
}
```

- Missing

```json
{
  "name": "HDR10 (Missing)",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "RlsGrp (Missing HDR)",
      "implementation": "ReleaseGroupSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "\\b(FraMeSToR|HQMUX|SiCFoI|playBD|RYU|ElNeekster|CiNEPHiLES|3L|EDV|Kenobi|TRiToN|HDH)\\b"
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
      "name": "Not SDR",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bSDR(\\b|\\d)"
      }
    },
    {
      "name": "Not HDR10+",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "\\bHDR10(\\+|P(lus)?\\b)"
      }
    },
    {
      "name": "HDR",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "HDR"
      }
    }
  ]
}
```

