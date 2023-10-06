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

