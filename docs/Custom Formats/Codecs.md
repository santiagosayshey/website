## BD Remux

```json
{
  "name": "REMUX",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "REMUX",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "REMUX"
      }
    },
    {
      "name": "DVD",
      "implementation": "SourceSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 5
      }
    }
  ]
}
```



## Disc

```json
{
  "name": "Disc ",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Disc",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "^(?!.*\\b((?<!HD[._ -]|HD)DVD|BDRip|MKV|XviD|WMV|d3g|BDREMUX|REMUX|^(?=.*1080p)(?=.*HEVC)|[xh][-_. ]?26[45]|German.*DL|((?<=\\d{4}).*German.*(DL)?)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2)\\b))\\b)(((?=.*\\b(Blu[-_. ]?ray|BD|HD[-_. ]?DVD)\\b)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2|BDMV|ISO)\\b))|^((?=.*\\b(^((?=.*\\b((.*_)?COMPLETE.*|Dis[ck])\\b)(?=.*(Blu[-_. ]?ray|HD[-_. ]?DVD)))|3D[-_. ]?BD|BR[-_. ]?DISK|Full[-_. ]?Blu[-_. ]?ray|^((?=.*((BD|UHD)[-_. ]?(25|50|66|100|ISO)))))))).*|(?i)(DVD9|DVD5|NTSC|PAL|VOB IFO|VC-1|AVC|MPEG-2|\\bCOMPLETE[-.\\s]?(?:UHD[-.\\s])?BLU[-.\\s]?RAY\\b|\\bCOMPLETE BLURAY\\b|\\bBR-Disk\\b)"
      }
    },
    {
      "name": "Remux / Encode",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?i)(REMUX|DVDRip)"
      }
    }
  ]
}
```


## DVD Remux

```json
{
  "name": "DVD REMUX ",
  "includeCustomFormatWhenRenaming": true,
  "specifications": [
    {
      "name": "REMUX",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "REMUX"
      }
    },
    {
      "name": "DVD",
      "implementation": "SourceSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": 5
      }
    }
  ]
}
```



## x264

```json
{
  "name": "x264",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "x264",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "^(?!.*(?i:remux)).*([xh](%5C%5C.?264)|DVDRip)"
      }
    },
    {
      "name": "Xvid",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?i)[-. ]Xvid"
      }
    },
    {
      "name": "Disc",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "^(?!.*\\b((?<!HD[._ -]|HD)DVD|BDRip|MKV|XviD|WMV|d3g|BDREMUX|REMUX|^(?=.*1080p)(?=.*HEVC)|[xh][-_. ]?26[45]|German.*DL|((?<=\\d{4}).*German.*(DL)?)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2)\\b))\\b)(((?=.*\\b(Blu[-_. ]?ray|BD|HD[-_. ]?DVD)\\b)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2|BDMV|ISO)\\b))|^((?=.*\\b(^((?=.*\\b((.*_)?COMPLETE.*|Dis[ck])\\b)(?=.*(Blu[-_. ]?ray|HD[-_. ]?DVD)))|3D[-_. ]?BD|BR[-_. ]?DISK|Full[-_. ]?Blu[-_. ]?ray|^((?=.*((BD|UHD)[-_. ]?(25|50|66|100|ISO)))))))).*|(?i)(DVD9|DVD5|NTSC|PAL|VOB IFO|VC-1|AVC|MPEG-2|\\bCOMPLETE[-.\\s]?(?:UHD[-.\\s])?BLU[-.\\s]?RAY\\b|\\bCOMPLETE BLURAY\\b|\\bBR-Disk\\b)"
      }
    },
    {
      "name": "Remux",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?i)(REMUX)"
      }
    },
    {
      "name": "WEB",
      "implementation": "SourceSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": 7
      }
    }
  ]
}
```


## x265

```json
{
  "name": "x265",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "x265",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "^(?!.*(?i:remux)).*([xh](%5C%5C.?265)|HEVC)"
      }
    },
    {
      "name": "Disc",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "^(?!.*\\b((?<!HD[._ -]|HD)DVD|BDRip|MKV|XviD|WMV|d3g|BDREMUX|REMUX|^(?=.*1080p)(?=.*HEVC)|[xh][-_. ]?26[45]|German.*DL|((?<=\\d{4}).*German.*(DL)?)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2)\\b))\\b)(((?=.*\\b(Blu[-_. ]?ray|BD|HD[-_. ]?DVD)\\b)(?=.*\\b(AVC|HEVC|VC[-_. ]?1|MVC|MPEG[-_. ]?2|BDMV|ISO)\\b))|^((?=.*\\b(^((?=.*\\b((.*_)?COMPLETE.*|Dis[ck])\\b)(?=.*(Blu[-_. ]?ray|HD[-_. ]?DVD)))|3D[-_. ]?BD|BR[-_. ]?DISK|Full[-_. ]?Blu[-_. ]?ray|^((?=.*((BD|UHD)[-_. ]?(25|50|66|100|ISO)))))))).*|(?i)(DVD9|DVD5|NTSC|PAL|VOB IFO|VC-1|AVC|MPEG-2|\\bCOMPLETE[-.\\s]?(?:UHD[-.\\s])?BLU[-.\\s]?RAY\\b|\\bCOMPLETE BLURAY\\b|\\bBR-Disk\\b)"
      }
    },
    {
      "name": "Remux",
      "implementation": "ReleaseTitleSpecification",
      "negate": true,
      "required": true,
      "fields": {
        "value": "(?i)(REMUX|DVDRip)"
      }
    }
  ]
}
```


## Xvid

```json
{
  "name": "Xvid",
  "includeCustomFormatWhenRenaming": false,
  "specifications": [
    {
      "name": "Xvid",
      "implementation": "ReleaseTitleSpecification",
      "negate": false,
      "required": true,
      "fields": {
        "value": "(?i)[-. ]Xvid"
      }
    }
  ]
}
```



